#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

#include "phylib.h" //header

/* Harkirat Soomal A1 Code */

/* A1 Part 1 Code*/

/**
 * Allocates memory for a new phylib_object, sets its type to PHYLIB_STILL_BALL,
 * and transfers the information provided in the function parameters into the structure.
 *
 * @param number The number assigned to the ball.
 * @param pos The position of the ball.
 * @return A pointer to the phylib_object if successful, otherwise NULL.
 */

phylib_object *phylib_new_still_ball(unsigned char number, phylib_coord *pos) {

    // Allocate memory for a new phylib_object
    phylib_object * new_ball = (phylib_object *)malloc(sizeof(phylib_object));

    // Check if memory allocation was successful
    if (new_ball == NULL) {
        return NULL;
    }

    // Set the type of the object to PHYLIB_STILL_BALL
    new_ball->type = PHYLIB_STILL_BALL;

    // Set the ball's number
    new_ball->obj.still_ball.number = number;

    // Set the ball's position
    new_ball->obj.still_ball.pos.x = pos->x;
    new_ball->obj.still_ball.pos.y = pos->y;

    // Return the pointer to the created phylib_object
    return new_ball;
}



/**
 * Allocates memory for a new phylib_object, sets its type to PHYLIB_ROLLING_BALL,
 * and transfers the information provided in the function parameters into the structure.
 *
 * @param number The number assigned to the ball.
 * @param pos The position of the ball.
 * @param vel The velocity of the ball.
 * @param acc The acceleration of the ball.
 * @return A pointer to the phylib_object if successful, otherwise NULL.
 */
phylib_object *phylib_new_rolling_ball(unsigned char number, phylib_coord *pos, phylib_coord *vel, phylib_coord *acc) {
   
   // Check if any of the pointers are NULL
    if (pos == NULL || vel == NULL || acc == NULL) {
        return NULL;
    }
    
    // Allocate memory for a new phylib_object
    phylib_object *new_ball = (phylib_object *)malloc(sizeof(phylib_object));

    // Check if memory allocation was successful
    if (new_ball == NULL) {
        return NULL;
    }

    // Set the type of the object to PHYLIB_ROLLING_BALL
    new_ball->type = PHYLIB_ROLLING_BALL;
    // Set the ball's number
    new_ball->obj.rolling_ball.number = number;
    // Set the ball's position
    new_ball->obj.rolling_ball.pos.x = pos->x;
    new_ball->obj.rolling_ball.pos.y = pos->y;
    // Set the ball's velocity
    new_ball->obj.rolling_ball.vel.x = vel->x;
    new_ball->obj.rolling_ball.vel.y = vel->y;
    // Set the ball's acceleration
    new_ball->obj.rolling_ball.acc.x = acc->x;
    new_ball->obj.rolling_ball.acc.y = acc->y;

    // Return the pointer to the created phylib_object
    return new_ball;
}


/**
 * Allocates memory for a new phylib_object, sets its type to PHYLIB_HOLE,
 * and transfers the information provided in the function parameters into the structure.
 *
 * @param pos The position of the hole.
 * @return A pointer to the phylib_object if successful, otherwise NULL.
 */
phylib_object *phylib_new_hole(phylib_coord *pos) {

    // Check if any of the pointers are NULL
    if (pos == NULL) {
        return NULL;
    }
    // Allocate memory for a new phylib_object
    phylib_object *new_hole = (phylib_object *)malloc(sizeof(phylib_object));

    // Check if memory allocation was successful
    if (new_hole == NULL) {
        return NULL;
    }

    // Set the type of the object to PHYLIB_HOLE
    new_hole->type = PHYLIB_HOLE;
    // Set the hole's position
    new_hole->obj.hole.pos.x = pos->x;
    new_hole->obj.hole.pos.y = pos->y;
    // Return the pointer to the created phylib_object
    return new_hole;
}


/**
 * Allocates memory for a new phylib_object, sets its type to PHYLIB_HCUSHION or PHYLIB_VCUSHION,
 * and transfers the information provided in the function parameters into the structure.
 * Returns a pointer to the phylib_object. If the malloc function fails, it returns NULL.
 */
phylib_object *phylib_new_hcushion(double y) {
    // Allocate memory for a new phylib_object
    phylib_object *new_hcushion = (phylib_object *)malloc(sizeof(phylib_object));

    // Check if memory allocation was successful
    if (new_hcushion == NULL) {
        return NULL;
    }

    // Set the type of the object to PHYLIB_HCUSHION
    new_hcushion->type = PHYLIB_HCUSHION;
    // Set the y-coordinate of the horizontal cushion
    new_hcushion->obj.hcushion.y = y;

    // Return the pointer to the created phylib_object
    return new_hcushion;
}


phylib_object *phylib_new_vcushion(double x) {
    // Allocate memory for a new phylib_object
    phylib_object *new_vcushion = (phylib_object *)malloc(sizeof(phylib_object));

    // Check if memory allocation was successful
    if (new_vcushion == NULL) {
        return NULL;
    }

    // Set the type of the object to PHYLIB_VCUSHION
    new_vcushion->type = PHYLIB_VCUSHION;
    // Set the x-coordinate of the vertical cushion
    new_vcushion->obj.vcushion.x = x;

    // Return the pointer to the created phylib_object
    return new_vcushion;
}  


/**
 * Allocates memory for a table structure and initializes it.
 * Sets the member variable, time, to 0.0, and assigns the values of its array elements to
 * pointers to new objects created by the phylib_new_* functions provided above.
 *
 * @return A pointer to the phylib_table if successful, otherwise NULL.
 */
phylib_table *phylib_new_table(void) {
    // Allocate memory for a new phylib_table
    phylib_table *new_table = (phylib_table *)malloc(sizeof(phylib_table));

    // Check if memory allocation was successful
    if (new_table == NULL) {
        return NULL;
    }

    // Set the member variable time to 0.0
    new_table->time = 0.0;

    // Initialize array elements with pointers to new objects created by phylib_new_* functions
    new_table->object[0] = phylib_new_hcushion(0.0);
    new_table->object[1] = phylib_new_hcushion(PHYLIB_TABLE_LENGTH);
    new_table->object[2] = phylib_new_vcushion(0.0);
    new_table->object[3] = phylib_new_vcushion(PHYLIB_TABLE_WIDTH);

    // Add 6 holes using phylib_new_hole
    phylib_coord hole_positions[6] = {
        {0.0, 0.0},
        {0.0, PHYLIB_TABLE_LENGTH / 2},
        {0.0, PHYLIB_TABLE_LENGTH},
        {PHYLIB_TABLE_WIDTH, 0.0},
        {PHYLIB_TABLE_WIDTH, PHYLIB_TABLE_LENGTH / 2},
        {PHYLIB_TABLE_WIDTH, PHYLIB_TABLE_LENGTH}
    };
    for (int i = 0; i < 6; ++i) {
        new_table->object[i + 4] = phylib_new_hole(&hole_positions[i]);
    }

    // Set the remaining pointers to NULL
    for (int i = 10; i < PHYLIB_MAX_OBJECTS; ++i) {
        new_table->object[i] = NULL;
    }

    // Return the pointer to the created phylib_table
    return new_table;   
}



/******************/
/*A1 Part 2 Code*/



/**
 * Allocates memory for a new phylib_object, copies its contents from src to dest.
 * If src points to a location containing a NULL pointer, dest is assigned the value of NULL.
 *
 * @param dest  Pointer to the destination phylib_object pointer.
 * @param src   Pointer to the source phylib_object pointer.
 */
void phylib_copy_object(phylib_object **dest, phylib_object **src) {
    if (*src == NULL) {
        *dest = NULL;
    } else {
        *dest = malloc(sizeof(phylib_object));
        if (*dest != NULL) {
            // Copy the entire object
            memcpy(*dest, *src, sizeof(phylib_object));
        }
    }
}


/**
 * Allocates memory for a new phylib_table, copies its contents from the given table.
 * Returns the address of the new phylib_table. If malloc fails, returns NULL.
 *
 * @param table  Pointer to the phylib_table to be copied.
 * @return       Pointer to the new phylib_table.
 */
phylib_table *phylib_copy_table(phylib_table *table) {
    if (table == NULL) {
        return NULL;
    }
    // Allocate memory for a new phylib_table
    phylib_table *new_table = malloc(sizeof(phylib_table));
    // Check if malloc was successful
    if (new_table == NULL) {
        return NULL;
    }
    // Copy the entire table
    memcpy(new_table, table, sizeof(phylib_table));
    // Copy each object
    for (int i = 0; i < PHYLIB_MAX_OBJECTS; i++) {
        if (table->object[i] != NULL) {
            phylib_copy_object(&(new_table->object[i]), &(table->object[i]));
        } else {
            new_table->object[i] = NULL;
        }
    }
    // Return the address of the new phylib_table
    return new_table;
}


/**
 * Adds a phylib_object to the phylib_table. Finds the first NULL pointer in the object array
 * of the table and assigns it the address of the given object. If no NULL pointers are found,
 * the function does nothing.
 *
 * @param table   Pointer to the phylib_table to which the object will be added.
 * @param object  Pointer to the phylib_object to be added.
 */
void phylib_add_object(phylib_table *table, phylib_object *object) {
   
    // Iterate over the object array to find the first NULL pointer
    for (int i = 0; i < PHYLIB_MAX_OBJECTS; ++i) {
        if (table->object[i] == NULL) {
            // Assign the address of the given object to the NULL pointer
            table->object[i] = object;
            return;  // Object added successfully, exit the function
        }
    }
    // If no NULL pointers are found, do nothing
}


/**
 * Frees memory allocated for the phylib_table and its associated phylib_objects.
 * @param table  Pointer to the phylib_table to be freed.
 */
void phylib_free_table(phylib_table *table) {
    // Check if table is NULL
    if (table == NULL) {
        return;  // Do nothing if table is NULL
    }
    // Iterate over the object array to free non-NULL pointers
    for (int i = 0; i < PHYLIB_MAX_OBJECTS; i++) {
        if (table->object[i] != NULL) {
            free(table->object[i]);  // Free the memory associated with the object
            table->object[i] = NULL;  // Set the pointer to NULL after freeing
        }
    }
    // Free memory allocated for the table itself
    free(table);
}


/**
 * Returns the difference between two phylib_coord structures.
 *
 * @param c1  The first phylib_coord structure.
 * @param c2  The second phylib_coord structure.
 * @return    The resulting phylib_coord structure (c1 - c2).
 */
phylib_coord phylib_sub(phylib_coord c1, phylib_coord c2) {
    phylib_coord result;

    // Calculate the difference for both x and y values
    result.x = c1.x - c2.x;
    result.y = c1.y - c2.y;

    return result;
}


/**
 * Calculates the length of the vector/coordinate c using the Pythagorean theorem.
 * Avoids using the exp function for squaring values.
 *
 * @param c  The phylib_coord structure representing the vector/coordinate.
 * @return   The length of the vector/coordinate.
 */
double phylib_length(phylib_coord c) {
    // Calculate the square of the length using the Pythagorean theorem (avoiding exp function)
    double length = sqrt((c.x * c.x) + (c.y * c.y));
    return length;
}


/**
 * Calculates the dot product between two vectors.
 *
 * @param a Vector a represented by a phylib_coord structure.
 * @param b Vector b represented by a phylib_coord structure.
 * @return The dot product of vectors a and b.
 */
double phylib_dot_product(phylib_coord a, phylib_coord b) {
    // Calculate the dot product as the sum of the product of corresponding components
    double dotProduct = ((a.x * b.x) + (a.y * b.y));
    return dotProduct;
  
}


/**
 * Calculates the distance between two objects.
 *
 * @param obj1 Pointer to the first phylib_object (must be PHYLIB_ROLLING_BALL).
 * @param obj2 Pointer to the second phylib_object.
 * @return The distance between obj1 and obj2, considering their types and positions.
 *         Returns -1.0 if obj1 is not a PHYLIB_ROLLING_BALL or if obj2 isn't a valid type.
 */
double phylib_distance(phylib_object *obj1, phylib_object *obj2) {
    // Check if obj1 and obj2 are NULL
    if (obj1 == NULL || obj2 == NULL) {
        return -1.0;
    }
    // Check if obj1 is a PHYLIB_ROLLING_BALL
    if(obj1->type != PHYLIB_ROLLING_BALL) {
        return -1.0;
    }
    double distance = 0.0; // Initialize distance to zero

    // Calculate distance based on the type of obj2
    switch (obj2->type) {
        // Calculate distance based on the type of obj2
        case PHYLIB_STILL_BALL:
        case PHYLIB_ROLLING_BALL: {
            distance = phylib_length(phylib_sub(obj1->obj.rolling_ball.pos, obj2->obj.rolling_ball.pos)) - PHYLIB_BALL_DIAMETER;
            break;
        }
        // Calculate distance based on the type of obj2
        case PHYLIB_HOLE: {
            distance = phylib_length(phylib_sub(obj1->obj.rolling_ball.pos, obj2->obj.hole.pos)) - PHYLIB_HOLE_RADIUS;
            break;
        }
        // Calculate distance based on the type of obj2
        case PHYLIB_VCUSHION: {
            distance = fabs(obj1->obj.rolling_ball.pos.x - obj2->obj.vcushion.x) - PHYLIB_BALL_RADIUS;
            break;
        }
        // Calculate distance based on the type of obj2
        case PHYLIB_HCUSHION: {
            distance = fabs(obj1->obj.rolling_ball.pos.y - obj2->obj.hcushion.y) - PHYLIB_BALL_RADIUS;
            break;
        }
        // Return -1.0 if obj2 is not a valid type
        default:
            return -1.0; // Invalid type
    }
    return distance; // Return calculated distance
}


/******************/
/*A1 Part 3 Code */


/**
 * Updates the position and velocity of a PHYLIB_ROLLING_BALL object after rolling for a specified period of time.
 *
 * @param new   Pointer to the new PHYLIB_ROLLING_BALL object to be updated.
 * @param old   Pointer to the old PHYLIB_ROLLING_BALL object representing the initial state.
 * @param time  Time period for which the rolling occurs.
 */
void phylib_roll(phylib_object *new, phylib_object *old, double time) 
{
    //Check if new and old are NULL
    if (new == NULL || old == NULL) {
        return;
    }
    // Check if new and old are PHYLIB_ROLLING_BALLs
    if (new->type != PHYLIB_ROLLING_BALL || old->type != PHYLIB_ROLLING_BALL) {
        return;  // Do nothing if not PHYLIB_ROLLING_BALLs
    }
    //Check if time is negative
    if (time < 0.0) {
        return;
    }
    // Calculate the new positions using the physics formula
    new->obj.rolling_ball.pos.x = old->obj.rolling_ball.pos.x +
                                  (old->obj.rolling_ball.vel.x * time) +
                                  (0.5 * old->obj.rolling_ball.acc.x * (time * time));

    new->obj.rolling_ball.pos.y = old->obj.rolling_ball.pos.y +
                                  (old->obj.rolling_ball.vel.y * time) +
                                  (0.5 * old->obj.rolling_ball.acc.y * (time * time));

    // Calculate new velocity
    new->obj.rolling_ball.vel.x = old->obj.rolling_ball.vel.x + (old->obj.rolling_ball.acc.x * time);
    new->obj.rolling_ball.vel.y = old->obj.rolling_ball.vel.y + (old->obj.rolling_ball.acc.y * time);
    

    // Check if velocities change sign, and set corresponding accelerations to zero
    if (old->obj.rolling_ball.vel.x * new->obj.rolling_ball.vel.x < 0.0) {
        new->obj.rolling_ball.vel.x = 0.0;
        new->obj.rolling_ball.acc.x = 0.0;
    }
    if (old->obj.rolling_ball.vel.y * new->obj.rolling_ball.vel.y < 0.0) {
        new->obj.rolling_ball.vel.y = 0.0;
        new->obj.rolling_ball.acc.y = 0.0;
    }
}





/**
 * Checks whether a ROLLING_BALL has stopped. If it has, converts it to a STILL_BALL.
 *
 * @param object Pointer to the PHYLIB_ROLLING_BALL object to be checked and possibly converted.
 * @return 1 if the ball is converted to STILL_BALL, 0 if it has not stopped or is not a ROLLING_BALL.
 */
unsigned char phylib_stopped(phylib_object *object) {
    // Calculate the length of the velocity vector
    double velocity_length = phylib_length(object->obj.rolling_ball.vel);

    // Check if the object is a ROLLING_BALL and has stopped
    if (velocity_length < PHYLIB_VEL_EPSILON) {
        // Convert to STILL_BALL
        object->type = PHYLIB_STILL_BALL;

        // Copy the ball number and coordinates
        object->obj.still_ball.number = object->obj.rolling_ball.number;
        object->obj.still_ball.pos.x = object->obj.rolling_ball.pos.x;
        object->obj.still_ball.pos.y = object->obj.rolling_ball.pos.y;

        // Return 1 to indicate that the ball has been converted to STILL_BALL
        return 1;
    }

    // Return 0 to indicate that the ball has not stopped or is not a ROLLING_BALL
    return 0;
}


/**
 * Implements the collision behavior between two phylib_objects.
 * 
 * If b is a HCUSHION, negates y velocity and acceleration of a.
 * If b is a VCUSHION, negates x velocity and acceleration of a.
 * If b is a HOLE, frees memory of a.
 * If b is a STILL_BALL, upgrades it to a ROLLING_BALL.
 * If b is a ROLLING_BALL, computes collision behavior between a and b.
 * 
 * @param a Pointer to the first phylib_object.
 * @param b Pointer to the second phylib_object.
 */
void phylib_bounce(phylib_object **a, phylib_object **b) {
    switch ((*b)->type) {
        case PHYLIB_HCUSHION:
            // Case 1: b is a HCUSHION
            // Negate y velocity and y acceleration of a
            (*a)->obj.rolling_ball.vel.y = -((*a)->obj.rolling_ball.vel.y);
            (*a)->obj.rolling_ball.acc.y = -((*a)->obj.rolling_ball.acc.y);
            break;
        case PHYLIB_VCUSHION:
            // Case 2: b is a VCUSHION
            // Negate x velocity and x acceleration of a
            (*a)->obj.rolling_ball.vel.x = -((*a)->obj.rolling_ball.vel.x);
            (*a)->obj.rolling_ball.acc.x = -((*a)->obj.rolling_ball.acc.x);
            break;
        case PHYLIB_HOLE:
            // Case 3: b is a HOLE
            // Free the memory of a and set it to NULL
            free(*a);
            *a = NULL;
            break;
            //break statement is needed here
        case PHYLIB_STILL_BALL:
            // Case 4: b is a STILL_BALL
            // "Upgrade" STILL_BALL to ROLLING_BALL
            (*b)->type = PHYLIB_ROLLING_BALL;
            // Fall through intentionally
        case PHYLIB_ROLLING_BALL: {
            // Compute r_ab (position of a with respect to b)
            phylib_coord r_ab = phylib_sub((*b)->obj.rolling_ball.pos, (*a)->obj.rolling_ball.pos);
            // Compute the normal vector, n
            double length_r_ab = phylib_length(r_ab);
            phylib_coord n;
            if (length_r_ab != 0) {
                n.x = r_ab.x / length_r_ab;
                n.y = r_ab.y / length_r_ab;
            } else {
                n.x = 0.0;
                n.y = 0.0;
            }
            // Compute v_rel (relative velocity of a with respect to b)
            phylib_coord v_rel;
            v_rel.x = (*a)->obj.rolling_ball.vel.x - (*b)->obj.rolling_ball.vel.x;
            v_rel.y = (*a)->obj.rolling_ball.vel.y - (*b)->obj.rolling_ball.vel.y;
            // Calculate v_rel_n (relative velocity in the direction of ball a)
            double v_rel_n = phylib_dot_product(v_rel, n);
            // Update velocities
            (*a)->obj.rolling_ball.vel.x = (*a)->obj.rolling_ball.vel.x - v_rel_n * n.x;
            (*a)->obj.rolling_ball.vel.y = (*a)->obj.rolling_ball.vel.y - v_rel_n * n.y;
            (*b)->obj.rolling_ball.vel.x = (*b)->obj.rolling_ball.vel.x + v_rel_n * n.x;
            (*b)->obj.rolling_ball.vel.y = (*b)->obj.rolling_ball.vel.y + v_rel_n * n.y;
            // Update the table to reflect the changes
            // Compute speeds
            double speed_a = phylib_length((*a)->obj.rolling_ball.vel);
            double speed_b = phylib_length((*b)->obj.rolling_ball.vel);
            if (speed_a > PHYLIB_VEL_EPSILON) {
                // Set acceleration of a to the negative velocity divided by the speed multiplied by PHYLIB_DRAG
                (*a)->obj.rolling_ball.acc.x = -((*a)->obj.rolling_ball.vel.x) / speed_a * PHYLIB_DRAG;
                (*a)->obj.rolling_ball.acc.y = -((*a)->obj.rolling_ball.vel.y) / speed_a * PHYLIB_DRAG;
            }
            if (speed_b > PHYLIB_VEL_EPSILON) {
                // Set acceleration of b to the negative velocity divided by the speed multiplied by PHYLIB_DRAG
                (*b)->obj.rolling_ball.acc.x = -((*b)->obj.rolling_ball.vel.x) / speed_b * PHYLIB_DRAG;
                (*b)->obj.rolling_ball.acc.y = -((*b)->obj.rolling_ball.vel.y) / speed_b * PHYLIB_DRAG;
            }
            break;
        }
    }
}




/**
 * Returns the number of ROLLING_BALLs on the table.
 *
 * Iterates through the objects in the table and counts the ROLLING_BALLs.
 *
 * @param t Pointer to the phylib_table structure.
 * @return Number of ROLLING_BALLs on the table.
 */
unsigned char phylib_rolling(phylib_table *t) {
    // Initialize the count of ROLLING_BALLS to zero
    unsigned char rolling_count = 0;

    // Iterate through the objects in the table
    for (int i = 0; i < PHYLIB_MAX_OBJECTS; ++i) {
        // Check if the current object is not NULL and of type ROLLING_BALL
        if (t->object[i] && t->object[i]->type == PHYLIB_ROLLING_BALL) {
            // Increment the count of ROLLING_BALLS
            rolling_count++;
        }
    }
    // Return the count of ROLLING_BALLS
    return rolling_count;
}


/**
 * Returns a segment of a pool shot.
 *
 * If there are no ROLLING_BALLs on the table, returns NULL.
 * Otherwise, returns a copy of the table with updated ROLLING_BALL positions.
 * Time increments from PHYLIB_SIM_RATE until PHYLIB_MAX_TIME or conditions are met.
 *
 * @param table Pointer to the phylib_table structure.
 * @return Pointer to the modified phylib_table if successful, else NULL.
 */
phylib_table *phylib_segment( phylib_table *table) {

    // Maximum value for the time
    double maximumValue =(PHYLIB_MAX_TIME) /PHYLIB_SIM_RATE;

    // Check if there are no ROLLING_BALLs on the table
    if (phylib_rolling(table)==0){ return NULL; }

    // Create a new table to store the updated table
    phylib_table* new =phylib_copy_table(table); //updated table to be returned (i.e. table after the "segment")

    
    // Roll the balls and check for stops and collisions
    for (double current=1; 
    current<=maximumValue; 
    current++) {//roll balls

        // Roll the balls
        for (int i=0; 
        i<PHYLIB_MAX_OBJECTS; 
        i++) { //loop until max time is reached

            // Check if the object is a ROLLING_BALL
            if (table->object[i]!= NULL && 
            table->object[i]->type ==PHYLIB_ROLLING_BALL) {
                phylib_roll(new->object[i], table->object[i],
                current* PHYLIB_SIM_RATE); // roll the ball
            }
        }

        // Update the time
        new->time =table->time +(current*PHYLIB_SIM_RATE); //update time

        // Check for stops and collisions
        for (int i = 0; i <PHYLIB_MAX_OBJECTS; i++) 
        { //after rolling all balls, check for stops and collisions
            if (table->object[i]!=NULL && 
            table->object[i]->type==PHYLIB_ROLLING_BALL ) 

            {//checking for stopped balls
                if ( phylib_stopped(new->object [i] ) ) 
                {
                    // this is a stopped ball
                    return new;
                }

                for (int j=0; 
                j<PHYLIB_MAX_OBJECTS;j++){ //checking for collisions
                    // If there is a collision, update the table
                    if (j!=i && new->object [j]!=NULL && 
                    phylib_distance(new->object[i],new->object[j]) <0.0) {
                        // If there is a collision, update the table
                        phylib_bounce(&new->object[i],&new->object[j]); return new;
                    }
                }
            }
        }
    }

    // Return the updated table
    return new;
}



/* NEW function for A2 */

/**
 * Converts a phylib_object into a string representation.
 *
 * @param object A pointer to a phylib_object.
 *
 * @return A string that describes the object. The string includes the type of the object and its properties.
 *         For example, for a STILL_BALL object, the string includes the number and position of the ball.
 *         For a ROLLING_BALL object, the string includes the number, position, velocity, and acceleration of the ball.
 *         For a HOLE object, the string includes the position of the hole.
 *         For a HCUSHION object, the string includes the y-coordinate of the cushion.
 *         For a VCUSHION object, the string includes the x-coordinate of the cushion.
 */
char *phylib_object_string( phylib_object *object )
{
    static char string[80];
    if (object==NULL)
    {
        snprintf( string, 80, "NULL;" );
        return string;
    }
    switch (object->type)
    {
        case PHYLIB_STILL_BALL:
            snprintf( string, 80,
            "STILL_BALL (%d,%6.1lf,%6.1lf)",
            object->obj.still_ball.number,
            object->obj.still_ball.pos.x,
            object->obj.still_ball.pos.y );
            break;
        case PHYLIB_ROLLING_BALL:
            snprintf( string, 80,
            "ROLLING_BALL (%d,%6.1lf,%6.1lf,%6.1lf,%6.1lf,%6.1lf,%6.1lf)",
            object->obj.rolling_ball.number,
            object->obj.rolling_ball.pos.x,
            object->obj.rolling_ball.pos.y,
            object->obj.rolling_ball.vel.x,
            object->obj.rolling_ball.vel.y,
            object->obj.rolling_ball.acc.x,
            object->obj.rolling_ball.acc.y );
            break;
        case PHYLIB_HOLE:
            snprintf( string, 80,
            "HOLE (%6.1lf,%6.1lf)",
            object->obj.hole.pos.x,
            object->obj.hole.pos.y );
            break;
        case PHYLIB_HCUSHION:
            snprintf( string, 80,
            "HCUSHION (%6.1lf)",
            object->obj.hcushion.y );
            break;
        case PHYLIB_VCUSHION:
            snprintf( string, 80,
            "VCUSHION (%6.1lf)",
            object->obj.vcushion.x );
            break;
    }
    return string;
}



function startGame(event) {
    event.preventDefault(); // Prevent the default form submission

    // Extract form data
    var player1 = document.getElementById('player1').value;
    var player2 = document.getElementById('player2').value;
    var gameNumber = document.getElementById('gameNumber').value;
    
    // Create the SVG element for the pool table
    var svg = document.createElementNS("http://www.w3.org/2000/svg", "svg");
    svg.setAttribute("width", "700");
    svg.setAttribute("height", "1375");
    svg.setAttribute("viewBox", "-25 -25 1400 2750");
    svg.setAttribute("xmlns", "http://www.w3.org/2000/svg");
    svg.setAttribute("xmlns:xlink", "http://www.w3.org/1999/xlink");
    svg.setAttribute("id", "poolTable");

    // Create and append SVG elements for the pool table components (balls, cushions, etc.)
    // You can add code here to dynamically generate SVG elements for all the components of the pool table

    // For demonstration purposes, let's add a circle element representing the cue ball
    var cueBall = document.createElementNS("http://www.w3.org/2000/svg", "circle");
    cueBall.setAttribute("cx", "100");
    cueBall.setAttribute("cy", "100");
    cueBall.setAttribute("r", "15");
    cueBall.setAttribute("fill", "white");
    svg.appendChild(cueBall);

    // Append the SVG element to the game content container
    var gameContent = document.getElementById('gameContent');
    gameContent.appendChild(svg);

    // Hide the form container and display the game content
    document.getElementById('startGameForm').style.display = 'none';
    document.getElementById('gameContent').style.display = 'block';
}


document.addEventListener("DOMContentLoaded", function() {
    var cueBall = document.getElementById("cueBall");
    var isDragging = false;
    var initialPosition = { x: 0, y: 0 };

    // Function to handle mouse down event on the cue ball
    cueBall.addEventListener("mousedown", function(event) {
        isDragging = true;
        initialPosition.x = event.clientX;
        initialPosition.y = event.clientY;
    });

    // Function to handle mouse move event while dragging the cue ball
    document.addEventListener("mousemove", function(event) {
        if (isDragging) {
            // Calculate the new position of the cue ball
            var dx = event.clientX - initialPosition.x;
            var dy = event.clientY - initialPosition.y;
            var newX = cueBall.getAttribute("cx") - 0 + dx;
            var newY = cueBall.getAttribute("cy") - 0 + dy;
            cueBall.setAttribute("cx", newX);
            cueBall.setAttribute("cy", newY);
            // Update the initial position for the next move
            initialPosition.x = event.clientX;
            initialPosition.y = event.clientY;
        }
    });

    // Function to handle mouse up event, i.e., releasing the cue ball
    document.addEventListener("mouseup", function(event) {
        if (isDragging) {
            isDragging = false;
            // Calculate the difference between release position and initial position
            var releaseX = event.clientX;
            var releaseY = event.clientY;
            var diffX = releaseX - initialPosition.x;
            var diffY = releaseY - initialPosition.y;
            // Compute the initial velocity of the cue ball (you need to implement this logic)
            var initialVelocity = computeInitialVelocity(diffX, diffY);
            // Generate a POST request to the shoot() function on the server
            var xhr = new XMLHttpRequest();
            xhr.open("POST", "/shoot", true);
            xhr.setRequestHeader("Content-Type", "application/json");
            xhr.onreadystatechange = function() {
                if (xhr.readyState === XMLHttpRequest.DONE) {
                    if (xhr.status === 200) {
                        // Handle successful response from the server
                        console.log("Shot successful");
                    } else {
                        // Handle error response from the server
                        console.error("Error:", xhr.status);
                    }
                }
            };
            // Send the initial velocity as JSON to the server
            xhr.send(JSON.stringify({ velocity: initialVelocity }));
        }
    });
});

// Function to compute the initial velocity of the cue ball based on the difference in positions
function computeInitialVelocity(diffX, diffY) {
    // Implement your logic to compute the initial velocity
    // This is just a placeholder, replace it with your actual calculation
    return { vx: diffX, vy: diffY };
}

# Billiards Physics Visualizer

A full-stack, multi-threaded billiards game GUI that simulates realistic billiards physics in real-time. This project integrates optimized server-side algorithms, efficient memory allocation in C, and advanced database management in MySQL, applying OOP principles to enhance performance and realism.

## Features

- **Real-Time Physics Modeling:** Simulates realistic billiards physics, including collision detection, friction, and momentum transfer.
- **Full-Stack Architecture:** Backend implemented in C with efficient memory management and server-side processing.
- **Advanced Database Management:** Uses MySQL for managing game data, player scores, and statistics.
- **Multi-Threading:** Enhances game performance by handling multiple simultaneous tasks, such as physics calculations and user interactions.
- **Cross-Platform GUI:** Built using HTML, CSS, JavaScript, and jQuery for a responsive and interactive user interface.
- **API Integration:** Allows for communication between the front-end and back-end for real-time updates and data management.

## Technologies Used

- **C:** Core game logic and physics simulation.
- **Python:** Scripting for data processing and server management.
- **Node.js:** Server-side logic and API handling.
- **MySQL:** Database management for storing and retrieving game-related data.
- **JavaScript & jQuery:** Front-end scripting for dynamic content and user interactions.
- **HTML & CSS:** Structure and styling of the game interface.

## Usage

To use the Billiards Physics Visualizer:

1. Clone the repository.
2. Install dependencies using `npm install`.
3. Set up the MySQL database.
4. Compile the C code for the game logic.
5. Run the application via `node server.js` and execute the game binary.
6. Open your browser and navigate to `http://localhost:3000` to start playing.

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/billiards-physics-visualizer.git
   cd billiards-physics-visualizer

npm install
gcc -o billiards_game main.c -pthread
node server.js
./billiards_game


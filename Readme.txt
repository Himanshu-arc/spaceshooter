=====================================
        SPACE HERO SHOOTER
=====================================

A simple 2D space shooter game built using Python and the Arcade library.

-------------------------------------
1. PROJECT OVERVIEW
-------------------------------------
Space Hero Shooter is a beginner-friendly arcade-style game where the player
controls a spaceship and shoots incoming enemies. The game increases in
difficulty over time and keeps track of the player's score and high score.

-------------------------------------
2. FEATURES
-------------------------------------
- Player-controlled spaceship
- Left and right movement using keyboard
- Bullet shooting system
- Enemy spawning with zig-zag movement
- Collision detection (bullet vs enemy, enemy vs player)
- Score system
- High score saving (persistent across game runs)
- Pause and resume functionality
- Increasing difficulty as score increases
- Game Over screen
- Restart option

-------------------------------------
3. CONTROLS
-------------------------------------
LEFT ARROW   -> Move spaceship left
RIGHT ARROW  -> Move spaceship right
SPACEBAR     -> Shoot bullets
P            -> Pause / Resume game
R            -> Restart game after Game Over

-------------------------------------
4. HOW TO RUN THE GAME
-------------------------------------
1. Make sure Python 3.8 or above is installed.
2. Install the Arcade library:
   
   pip install arcade

3. Run the main game file:

   python main.py

(Replace 'main.py' with the actual filename if different.)

-------------------------------------
5. GAME RULES
-------------------------------------
- Each enemy destroyed increases the score.
- Enemies move faster as the score increases.
- The player starts with limited lives.
- Collision with an enemy reduces one life.
- When all lives are lost, the game ends.

-------------------------------------
6. FILES USED
-------------------------------------
- main.py           : Main game file
- high_score.json   : Stores the highest score
- README.txt        : Project description

-------------------------------------
7. CONCEPTS USED
-------------------------------------
- Python Object-Oriented Programming
- Game loop and real-time updates
- Sprite-based collision detection
- File handling (JSON)
- Keyboard event handling
- Basic mathematics for movement

-------------------------------------
8. FUTURE IMPROVEMENTS
-------------------------------------
- Power-ups
- Boss enemies
- Enemy shooting
- Health bar system
- Game menu and settings
- Sound effects and background music

-------------------------------------
9. AUTHOR
-------------------------------------
Developed as a learning project to understand Python game development
using the Arcade library.

=====================================

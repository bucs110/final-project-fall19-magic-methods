# 110 Go!
## CS 110 Final Project
### Fall Semester, 2019
### [Assignment Description](https://drive.google.com/open?id=1HLIk-539N9KiAAG1224NWpFyEl4RsPVBwtBZ9KbjicE)

<< [https://github.com/bucs110/final-project-fall19-magic-methods](#) >>

<< [link to demo presentation slides](#) >>

### Team: Magic Methods
#### Ethan Huang, Jiahao Pan, Anthony Tom

## Project Description
Our project is a runner type game based loosely on the mechanics of Kiloo's Subway Surfers and Halfbrick Studio's
Jetpack Joyride. The game centers around a nightmare in which the player is running to class, but never gets there.
As the player runs to class, various obstacles and powerups (TBD) will appear. The game's design will be based on the
school's campus itself.

***    

## User Interface Design
* ![UI Sketch](/assets/UI_Drawing.jpg)
    * For example, if your program has a start screen, game screen, and game over screen, you should include a wireframe / screenshot / drawing of each one and a short description of the components
     *Start Screen - game title and play button
     *Game Screen - character and game setting
     *End Screen - displays score and includes option to play again or end
* << You should also have a screenshot of each screen for your final GUI >>

***        

## Program Design
* Non-Standard libraries
    * [Pyganim](https://pyganim.readthedocs.io/en/latest/index.html)
        * Pyganim is a module that works in conjunction with Pygame to create animated images that can easily be played, paused, and stopped.
* Class Interface Design
    * ![Class diagram](/assets/Temp_Class_Diagram.png)
* Classes
    * Controller class - takes user input and updates the game
    * Character class - includes varbiables and methods for the character used by the player
    * Background class - includes variables and methods for the background to be drawn to the screen
    * AnimatedSprite class - creates an animated sprite that can be used for animations with the pyganimation library
    * Tile class - creates a tile from a section grabbed from a sprite sheet

***

## Tasks and Responsibilities
* You must outline the team member roles and who was responsible for each class/method, both individual and collaborative.

### Software Lead - Ethan Huang

The Software Lead will be overseeing the code written by both the Front End Specialist and the Back End Specialist
and making sure that the team has a schedule for features that need to be implemented. He will also be responsible
for ensuring that the logic written by Back End Specialist is correct.

### Front End Specialist - Jiahao Pan

The Front End Specialist will be writing the code that depicts the game's assets and designs on the screen.

### Back End Specialist - Anthony

The Back End Specialist will be writing the necessary classes and drawing diagrams showing the relationships between
each of the classes. He will also be responsible for writing the code that performs the game's mechanics.

## Testing
* Testing for our program will be sequential. After clicking through the start screen, the user should immediately enter the game screen. By using the up and down keys, the user will be able to change lanes in the game. When colliding with a goblin, the user should take damage. After losing all of his or her health, the user should be taken to an end screen that includes the options to play again or return to the start screen.

| Step                  | Procedure     | Expected Results  | Actual Results |
| ----------------------|:-------------:| -----------------:| -------------- |
|  1  | Click the "play" button  | Screen switches from start to game  |          |
|  2  | Press the w or s keys  | The player changes lanes in the screen |                 |
|  3  | Collide with an obstacle  |  The player's health should decrease by 1  |               |
|  4  | Lose all health  |  Screen switches from game to end  |               |
|  5  | Click the "play" button  |  Screen switches from end to game with variables reset  |               |
|  6  |  Repeat steps and click the "exit" button  |  Screen switches from end to start |                 |
|  7  |  Click the "x" button  |  Game quits itself  |                    |

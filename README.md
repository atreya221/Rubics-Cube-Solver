# Rubics-Cube-Solver

## Description

This repository contains the code for a program for solving an unsolved Rubik's Cube by following step-by-step insructions on the screen. This program is compatible with both `Windows` and `Linux` operating systems. On running the program, a webcam window opens. Then the user holds an unsolved Rubik's cube in front of it. The program automatically scans and detects the faces of the cube using `OpenCV`. It generates the solution of the cube using `Kociemba` module and stores it as a list of moves to be made by the user. After this, instructions are displayed on the screen in the form of augmented arrows and text. By following the instructions, the Rubik's Cube gets solved in less than 30 moves.


## Installation

In order to install and use the app, you need too have `python3` already installed on your system.

1.  Clone the repository on your local system:
    ```
    git clone https://github.com/atreya221/Rubics-Cube-Solver.git
    ```

2.  The required dependencies listed in `requirements.txt` will be automatically installed in a fresh virtual environment `.env`:
    ```
    $ python3 setup.py
    ```
3.  Activate the virtual environment to run the app:
    ```
    $ . ./.env/bin/activate
    ```
    
## User Guide
    
   You need to follow the instructions given below in order to solve the cube.
   
   1. Decide one of the faces of your cube as a front face, and then mark the top, down, left, right, and back face accordingly.
   2. Webcam window will first ask you to show the front face. As soon as you show the front face, squares will start getting marked, and when all the 9 squares are marked it         will ask you to show the top face.
   3. Following similar steps will scan the top, down, right, left, and back face.
   4. After scanning all the faces correctly, the screen will display the instruction in the form of an arrow and text. 
   5. Follow the instruction shown on the screen and then show the front face to the screen.
   6. Keep following the instructions shown on the screen until you see the text "Cube is solved".

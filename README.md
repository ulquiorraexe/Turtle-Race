# Etch A Sketch vs Turtle Race

## Overview

This is a simple **Turtle Race** and **Etch A Sketch** game created using Python's `turtle` module.

## Code Comparison: Etch A Sketch vs Turtle Race

### Etch A Sketch (Commented Code)

This section is a simple **Etch A Sketch** program, where the user controls a turtle to draw on the screen using keyboard keys.

#### Explanation:

1. **Turtle and Screen**: The `turtle` module in Python is used to create graphical drawings, and the `Screen` represents the window.
2. **Functions**:
   - `forwards()`: Moves the turtle forward by 10 units.
   - `backwards()`: Moves the turtle backward by 10 units.
   - `to_right()`: Turns the turtle to the right by 10 degrees.
   - `to_left()`: Turns the turtle to the left by 10 degrees.
   - `clear()`: Resets the turtle, clearing the screen and erasing the drawing.
3. **Screen Events**: `screen.listen()` allows the screen to listen for keypresses. When the user presses a specific key, the corresponding function is called using `screen.onkey`.

This code essentially allows the user to use the keyboard to move the turtle and draw, with the option to clear the screen.

### Turtle Race (Active Code)

This section is a **Turtle Race** program, where the user bets on which turtle will win a race. The turtles move randomly until one of them crosses the finish line.

#### Explanation:

1. **Turtles and Race Setup**:
   - The `Screen` setup configures the screen size for the race.
   - The user is prompted to bet on which turtle (by color) they think will win using `screen.textinput()`.
   - A list of `colors` and `positions` defines the turtles' starting positions and colors.
   - 6 turtles are created, each assigned a color and an initial position.

2. **Race Start**:
   - If the user makes a bet, the race begins (`race = True`).
   
3. **Race Loop**:
   - Inside a `while race` loop, each turtle moves a random distance (between 0 and 10).
   - If a turtle's `xcor()` exceeds 230, the race ends, and the winner is declared.
   - The program checks if the user's bet matches the winning turtle's color and prints the result (win/lose).

4. **Outcome**: Once the race finishes, the program informs the user whether they won or lost based on their bet.

### Summary:

- **Etch A Sketch** allows the user to draw using the arrow keys, simulating a simple drawing program.
- **Turtle Race** allows the user to bet on which turtle will win the race, with turtles moving randomly to the finish line.

Both codes use the `turtle` module, but one focuses on drawing while the other simulates a race.

## Requirements

- Python 3.x
- `turtle` module (which is included in standard Python installations)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/ulquiorraexe/turtle-race.git

2. Navigate to the project directory:
   ```bash
   cd turtle-race

3. Run the program:
   ```bash
   python main.py

## License

This project does not have a license.

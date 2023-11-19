# Travelling-Salesman

## Setup
pip install -r requirements.txt

## Run
python main.py

## Use
Left Click to add points\
Right Click to remove points\
Space to find the path\
Backspace to clear the canvas

## Introduction

Upon initiation, the code opens a Pygame window, allowing users the ability to intuitively introduce and remove cities via left and right mouse clicks, respectively. 
The program allows users to interactively add and remove cities on a 2D plane and observes the real-time application of a greedy algorithm to optimize the salesman's path.


### Point Class

The Point class represents each city in the TSP simulation. It contains attributes for the city's coordinates (x and y), a reference to the next city in the path (next), a flag indicating if the city is visited (done), and a dictionary (values) to store distances to other cities.

- The `_sub_` method calculates the absolute distance between two points, aiding in determining proximity for point addition or removal.
- The `getTuple` method returns the coordinates of the point as a tuple.
- The `distance` method computes the Euclidean distance between two points.

### add_point Function

The `add_point` function adds a new city to the simulation. It creates a Point object at the specified coordinates unless the point is too close to an existing city (within `circleRadius`), preventing overlap.

### remove_point Function

The `remove_point` function deletes a city from the simulation. It identifies the closest city within `circleRadius` of the specified coordinates and removes it from the list of cities.

### all_done Function

The `all_done` function checks whether all cities have been visited. It returns `True` if all cities are marked as visited (`done`), indicating the completion of the TSP path.

### set_points Function

The `set_points` function updates and displays the current cost of the TSP path on the Pygame window. It uses the Pygame font module to render the cost as text at a specified position.

### Main Loop

The main loop captures user input events using Pygame. It handles mouse clicks for adding and removing points and key presses for starting and resetting the TSP simulation.

The simulation dynamically calculates and updates the cost of the path as the algorithm attempts to connect cities.

The loop draws lines between connected cities, circles representing cities (green for visited, red for unvisited), and updates the display. The simulation continues until the user exits the window.


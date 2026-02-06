from random import randint
import numpy as np

cube = np.array([ 
    np.full((4, 4), "w"), # Green front, white top
    np.full((4, 4), "g"),
    np.full((4, 4), "y"),
    np.full((4, 4), "b"),
    np.full((4, 4), "o"),
    np.full((4, 4), "r")
])

def rotate_X(cube): # Clockwise from right
    return np.array([
        cube[1],
        cube[2],
        cube[3],
        cube[0],
        cube[4],
        cube[5],
    ])

def rotate_Y(cube): # Clockwise from top
    return np.array([
        cube[0],
        cube[5],
        cube[2],
        cube[4],
        cube[1],
        cube[3],
    ])

def rotate_Z(cube): # Clockwise from front
    return np.array([
        cube[4],
        cube[1],
        cube[5],
        cube[3],
        cube[2],
        cube[0],
    ])

def outer_turn(cube, turn, direction): # turns along the U-face, but rotates before and after
    if turn == "R":
        cube = rotate_Z(rotate_Z(rotate_Z(cube)))

    if direction == "":
        temp = cube[1][0]
        cube[1][0] = cube[5][0]
        cube[5][0] = cube[3][0]
        cube[3][0] = cube[4][0]
        cube[4][0] = temp

    if turn == "R":
        cube = rotate_Z(cube)
    return cube


print(outer_turn(cube,"U",""))
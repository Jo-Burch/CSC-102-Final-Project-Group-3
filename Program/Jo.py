# Jo — Puzzle Developer (Quadrants 1–4)
#	Core Responsibilities
#		Build all four quadrant puzzles
#		Ensure each puzzle follows the same interface
#		Implement puzzle logic and state tracking
#	Create logic for:
#		Quadrant 1 puzzle
#		Quadrant 2 puzzle
#		Quadrant 3 puzzle
#		Quadrant 4 puzzle
#		Maintain puzzle state dictionaries
#		Ensure each puzzle returns True when solved
#		Balance difficulty across puzzles

#---# Will need to Change to fit our Bomb (from bomb_phases from prof)#---#
from bomb_configs import *
from tkinter import *
import tkinter
from threading import Thread
from time import sleep
import os
import sys

class Puzzle:
    def __init__(self, puzzle_id):
        self.puzzle_id = puzzle_id
        
        self.completed = False
        self.progress = 0
    def start(self):
        self.completed = False
        self.progress = 0
    def check_solution(self):
        pass
    def update_progress(self, value):
        self.progress += value
        self.check_solution()
    def reset(self):
        self.completed = False
        self.progress = 0
        
class Q1_Puzzle(Puzzle):
    def __init__(self):
        super.__init__()
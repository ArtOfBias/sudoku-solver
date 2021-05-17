import suduko_solver
import random
import pygame
import time
from typing import List, NoReturn

EMPTY_BOARD = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

pygame.font.init()

width, height = 600, 600

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Suduko Solver")

font = pygame.font.SysFont("helvetica", 40)

x, y = 0, 0
edge = 500 / 9

def draw_box() -> NoReturn:
    """highlights selected square"""
    for i in range(2):
        pygame.draw.line(screen, (255, 0, 0), (x * edge-3, (y + i) *edge), (x * edge + edge + 3, (y + i) * edge), 7)
        pygame.draw.line(screen, (255, 0, 0), ( (x + i) * edge, y * edge ), ((x + i) * edge, y * edge + edge), 7)

suduko_solver.solve()


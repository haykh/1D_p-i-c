from parameters import *
import numpy as np

class Particle:
    def __init__(self, pos, vel, charge, move):
        self.x = pos
        self.v = vel
        self.q = charge
        self.mv = move

def twoStream1 ():
    sep = 1.0 * SIZE / (NP / 2)
    PARTS = []
    for i in range(NP / 2):
        # unperturbed position
        x0 = (i + 0.5) * sep

        # perturbation
        theta = 2 * np.pi * MODE * x0 / SIZE
        dx = AMPL * np.cos(theta)
        x1 = x0 + dx
        x2 = x0 - dx

        # periodic boundaries
        if x1 < 0:
            x1 += SIZE
        if x2 < 0:
            x2 += SIZE
        if x1 >= SIZE:
            x1 -= SIZE
        if x2 >= SIZE:
            x2 -= SIZE

        # add to PARTS
        PARTS.append(Particle (x1, -1.0, Q, True))
        PARTS.append(Particle (x2, 1.0, Q, True))

    sep = SIZE / NP
    for i in range (NP):
        x0 = (i + 0.5) * sep
        PARTS.append(Particle (x0, 0.0, -Q, False))

    return PARTS

def twoStream2 ():
    PARTS = []
    # specie 1
    for i in range(NP / 2):
        x = np.random.uniform(0, SIZE)
        PARTS.append(Particle (x, 1.0, Q, True))
        x = np.random.uniform(0, SIZE)
        PARTS.append(Particle (x, -1.0, Q, True))
    for i in range(NP):
        x = np.random.uniform(0, SIZE)
        PARTS.append(Particle (x, 0.0, -Q, False))
    return PARTS

def fourStream ():
    PARTS = []
    for i in range(NP / 4):
        x = np.random.uniform(0, SIZE)
        PARTS.append(Particle (x, 0.5, Q, True))
        x = np.random.uniform(0, SIZE)
        PARTS.append(Particle (x, -0.5, Q, True))
        x = np.random.uniform(0, SIZE)
        PARTS.append(Particle (x, -1.5, Q, True))
        x = np.random.uniform(0, SIZE)
        PARTS.append(Particle (x, 1.5, Q, True))
    for i in range(NP):
        x = np.random.uniform(0, SIZE)
        PARTS.append(Particle (x, 0.0, -Q, False))
    return PARTS

def plasmaFluc ():
    sep = 1.0 * SIZE / NP
    PARTS = []
    for i in range(NP):
        # unperturbed position
        x0 = (i + 0.5) * sep
        x0 += np.random.uniform(-dX, dX)
        # perturbation
        if (x0 < SIZE / 2 + 5 * dX) and (x0 >= SIZE / 2):
            x0 -= np.abs(x0 - SIZE / 2) * np.sqrt(2.0)

        if x0 < 0:
            x0 += SIZE
        if x0 >= SIZE:
            x0 -= SIZE
        PARTS.append(Particle (x0, 0.0, Q, True))

    for i in range(NP):
        x0 = (i + 0.5) * sep
        PARTS.append(Particle (x0, 0.0, -Q, False))
    return PARTS

def ionScreen ():
    PARTS = []
    for i in range(NP + 100):
        x = np.random.uniform(0, SIZE)
        PARTS.append(Particle (x, 0.0, Q, True))
    sep = 1.0 * SIZE / NP
    for i in range(NP):
        x0 = np.random.uniform(0, SIZE)
        PARTS.append(Particle (x0, 0.0, -Q, False))
    PARTS.append(Particle (SIZE / 2.0, 0.0, -100 * Q, False))
    return PARTS

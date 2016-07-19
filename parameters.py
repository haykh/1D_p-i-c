# NODES
CELLS = 100             # number of cells
NODES = CELLS + 1       # number of node points

SIZE = 20.0             # size of the system

STEPS = 1000
NAME = 'four-stream'
dX = SIZE / CELLS       # distance between nodes (spatial step)
dT = 0.1                # timestep (should be: omegaP * dt < 0.3)

# PLASMA PARAMETERS
omegaP = 1.0            # normalized plasma frequency
eps0 = 1.0              # normalized vacuum permittivity

# SOR ERROR
ERROR = 1e-5

# PARTICLES single
NPpC = 50               # number of particles per species per cell
NP = NPpC * CELLS       # number of particles
QoverM = -1.0           # normalized q/m factor for moving particles
# particle charges determined by plasma frequency
Q = omegaP**2 * (1 / QoverM) * eps0 * (SIZE / NP)
# PERTURBATION
MODE = 1
AMPL = 1e-1

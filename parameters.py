# NODES
CELLS = 50              # number of cells
NODES = CELLS + 1       # number of node points

SIZE = 20.0             # size of the system

STEPS = 100

# This NAME determines what primary configuration is used
#   'plasma_fluc' - simple plasma fluctuations
#   'two-stream' - two-stream instability (uniform distribution)
#   'two-stream_r' - two-stream instability (random distribution)
#   'four-stream' - "four-stream" instability (kind of)
# feel free to create your own & add case in `main.py`
NAME = 'plasma_fluc'
dX = SIZE / CELLS       # distance between nodes (spatial step)
dT = 0.1                # timestep (should be: omegaP * dt < 0.3)

# PLASMA PARAMETERS
omegaP = 1.0            # normalized plasma frequency
eps0 = 1.0              # normalized vacuum permittivity

# SOR ERROR
ERROR = 1e-5

# PARTICLES single
NPpC = 50               # number of particles per species per cell
NP = NPpC * CELLS       # number of particles (of particular specie) (used to determine charge!)

# PERTURBATION
MODE = 1
AMPL = 1e-1

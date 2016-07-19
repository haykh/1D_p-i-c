import numpy as np
from parameters import *

# Weighting density on nodes from particles' position data
#   ACCEPTS particles array
#   RETURNS density [on nodes] array
def density (parts):
    rho = [0.0 for i in range(NODES)]
    NPart = len(parts)
    # first-order CIC weighting
    for k in range(NPart):
        coord = (parts[k].x / dX)
        i = np.floor(parts[k].x / dX)
        d = coord - i

        cur = int(i)
        nxt = (cur + 1)

        rho[cur] += parts[k].q * (1.0 - d)
        rho[nxt] += parts[k].q * d

    # ions
    # for i in range(NODES - 1):
    #     rho[i] += Qi * (NP - 50) / CELLS
    #
    # rho[int(CELLS / 2)] += Qi * 50

    rho[NODES - 1] += rho[0]
    rho[0] = rho[NODES - 1]

    rho = np.array(rho)

    rho /= dX

    return rho

# import generation as gen
# particles1 = gen.fourStream()
# # particles2 = gen.twoStream1()
# print np.sum(density(particles1)[:-1])

# Successive over-relaxation method for potential
#   ACCEPTS density [on nodes] array
#   RETURNS potential [on nodes] array
def SOR (rho):
    # SOR parameter
    omega = 2.0 / (1 + 2 * np.pi / NODES)
    # omega = 1.4

    # initial phi values
    phi = np.array([0.0 for i in range(NODES)])

    # right hand side
    rhs = -np.copy(rho) * dX**2 / eps0

    # solver
    for k in range(10000):
        phinew = np.copy(phi)
        for i in range(NODES - 1):
            nxt = (i + 1) if (i < NODES - 2) else 0
            prv = (i - 1) if (i > 0) else (NODES - 2)

            phinew[i] = (1 - omega) * phi[i] + (omega / -2.0) * (rhs[i] - phinew[prv] - phi[nxt])

        # checking convergence
        if k % 25 == 0:
            if np.max(np.abs(phinew - phi)) < ERROR:
                phi = phinew
                # print "SOR steps: ", k
                break
        phi = np.copy(phinew)

    phi[NODES - 1] = phi[0]
    return phi

# Calculating field from potential on nodes
#   ACCEPTS potential [on nodes] array
#   RETURNS field [on nodes] array
def fieldOnNodes (phi):
    efield = np.array([0.0 for i in range(NODES)])
    for i in range(NODES):
        nxt = (i + 1) if (i < NODES - 1) else 0
        prv = (i - 1) if (i > 0) else (NODES - 1)

        efield[i] = (phi[prv] - phi[nxt]) / (2 * dX)

    return efield

# Interpolating field from nodes to particles
#   ACCEPTS field [on nodes] array & particles
#   RETURNS field [on particles] array
def fieldOnParticles (field, parts):
    NPart = len(parts)
    efield = np.array([0.0 for i in range(NPart)])
    # first-order CIC backwards-weighting
    for k in range(NPart):
        if parts[k].mv:
            xp = (parts[k].x / dX)
            j = np.floor(parts[k].x / dX)

            nxt = (j + 1) if (j + 1) < NODES else 0

            efield[k] = (nxt - xp) * field[j] + (xp - j) * field[nxt]
    return efield

# First time rewind velocity by dT/2 forward or backward
#   ACCEPT rewind direction & field [on particles] array & particles
#       direction forward: +1
#       direction backward: -1
#   RETURNS particles [new velocities] array
def rewind (direction, field, parts):
    NPart = len(parts)
    for k in range(NPart):
        # updating velocity
        if parts[k].mv:
            parts[k].v += direction * field[k] * QoverM * dT / 2.0
    return parts

# Interpolating field from nodes to particles
#   ACCEPTS field [on particles] array & particles
#   RETURNS particles [new positions and velocities] array
def moveParticles (field, parts):
    NPart = len(parts)
    for k in range(NP):
        if parts[k].mv:
            # updating velocity
            parts[k].v += field[k] * QoverM * dT

            # updating position
            parts[k].x += parts[k].v * dT

            while parts[k].x < 0:
                parts[k].x += SIZE
            while parts[k].x >= SIZE:
                parts[k].x -= SIZE
    return parts

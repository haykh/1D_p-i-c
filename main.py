import numpy as np
import matplotlib.pyplot as plt

import generation as gen
from cycle import *
import helpers as hlp

particles = gen.fourStream()

# PROGRESS BAR
stp = 0
hlp.printProgress(stp, STEPS, prefix = 'Progress:', suffix = 'Complete', barLength = 50)

for step in range(STEPS):
    rho = density(particles)
    PHI = SOR(rho)
    EFIELDn = fieldOnNodes(PHI)
    EFIELD = fieldOnParticles(EFIELDn, particles)

    if step == 0:
        particles = rewind(-1, EFIELD, particles)

    particles = moveParticles(EFIELD, particles)

    # write to file
    if step % 1 == 0:
        # print "step: ", step
        output = open('dats/' + NAME + '/step_' + str(step) + '.dat', 'w')
        newparts = rewind(1, EFIELD, particles)
        NPart = len(particles)
        for i in range(NPart):
            if newparts[i].mv:
                print >>output, newparts[i].x, ' ', newparts[i].v
        output.close()

    # PROGRESS BAR
    stp += 1
    hlp.printProgress(stp, STEPS, prefix = 'Progress:', suffix = 'Complete', barLength = 50)

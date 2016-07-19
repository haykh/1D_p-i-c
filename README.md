# 1 dimensional particle-in-cell code

## Files description
- `parameters.py` - simulation & plasma parameters
- `generation.py` - various function to generate plasma
- `cycle.py` - basic [backwards]weighting and solution functions
- `main.py` - the main part containing the whole p-i-c cycle and data export

- `plotter.py` - for creating animation from data exported to `.dat` files

- `helpers.py` - progress-bar and timing functions

## Simulation
The program can be started by calling `python main.py`. Make sure to modify paths and plasma generation function:
```python
particles = gen.NAME_FROM_GENERATION_PY()
```

## Plotting
To simply view the animation comment out `anim.save(…)` leaving `plt.show()`. To save the animation, make sure to put `ffmpeg` codecs from [here](http://www.ffmpegmac.net/) to your `/usr/local/bin/` directory (necessary for OS X).

## Experimenting with various inputs
Feel free to create your own plasma generation functions. The only thing you need to keep in mind, is to keep the overall number density 0. You can check that by doing
```python
numpy.sum(density(particles)[:-1])
```
`[:-1]` here is because of the periodic boundary conditions and `density[NODES - 1]` equals to `density[0]`.

Particles can be movable, i.e., `particle.mv = True`, or permanently nailed in place, `particle.mv = False`. 

## Further reading
[Plasma physics via computer simulation](https://www.amazon.com/Plasma-Physics-via-Computer-Simulation/dp/0750310251) by C.K. Birdsall and A.B Langdon

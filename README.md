# 1 dimensional particle-in-cell code

## Files description
- `parameters.py` - simulation & plasma parameters
- `generation.py` - various function to generate plasma
- `cycle.py` - basic [backwards]weighting and solution functions
- `main.py` - the main part containing the whole p-i-c cycle and data export

- `plotter.py` - for creating animation from data exported to `.dat` files

- `helpers.py` - progress-bar and timing functions

## Simulation
The program can be started by calling `python main.py`. Make sure to modify output paths in `main.py` and input in `parameters.py`:
```python
NAME = ‘input_value_name’
```

This `NAME` determines what primary configuration is used:
- `’plasma_fluc’` - simple plasma fluctuations (see [video](https://www.youtube.com/watch?v=CRl_Q-YGAiU))
- `’two-stream’` - two-stream instability (uniform distribution) (see [video](https://www.youtube.com/watch?v=HylkN0Ygl1E))
- `’two-stream_r’` - two-stream instability (random distribution) (see [video](https://www.youtube.com/watch?v=C5kP_TZ3IHY))
- `’four-stream’` - "four-stream" instability (kind of) (see [video](https://www.youtube.com/watch?v=xZGo-IZY8LU))

## Plotting
To simply view the animation comment out `anim.save(…)` leaving `plt.show()`. To save the animation, make sure to put `ffmpeg` codecs from [here](http://www.ffmpegmac.net/) to your `/usr/local/bin/` directory (necessary for OS X).

## Experimenting with various inputs
Feel free to create your own plasma generation functions. Add the `NAME` parameter for it in `parameters.py` and add the `elif` case in `main.py`. 

The only thing you need to keep in mind, is to keep the overall charge density neutral. You can check that by doing
```python
numpy.sum(density(particles)[:-1])
```
`[:-1]` here is because of the periodic boundary conditions and `density[NODES - 1]` equals to `density[0]`.

Particles can be movable, i.e., `particle.mv = True`, or permanently nailed in place, `particle.mv = False`. 

## Further reading
[Plasma physics via computer simulation](https://www.amazon.com/Plasma-Physics-via-Computer-Simulation/dp/0750310251) by C.K. Birdsall and A.B Langdon

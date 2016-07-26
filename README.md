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
- `’beam_instability’` - beam instability (see [video](https://youtu.be/omAHGhcDOwI))

## Plotting
Plotter works distinctly by calling `python plotter.py`. To simply view the animation comment out `anim.save(…)` leaving `plt.show()`. To save the animation, make sure to put `ffmpeg` codecs from [here](http://www.ffmpegmac.net/) to your `/usr/local/bin/` directory (necessary for OS X).

## Experimenting with various inputs
Feel free to create your own plasma generation functions. Add the `NAME` parameter for it in `parameters.py` and add the `elif` case in `main.py`. 

The only thing you need to keep in mind, is to keep the overall charge density neutral. You can check that by doing
```python
numpy.sum(density(particles)[:-1])
```
`[:-1]` here is because of the periodic boundary conditions and `density[NODES - 1]` equals to `density[0]`.

Particles can be movable, i.e., `particle.mv = True`, or permanently nailed in place, `particle.mv = False`. 

### `Particle` class
This class contains the info about particles. 

It accepts: 
- `pos`: position
- `vel`: velocity
- `omegaP`: plasma frequency
- `QoverM`: charge-to-mass ratio
- `move`: `True` if particle is movable, `False` if it’s not

It contains:
- `particle.x` and `particle.v`: [accepts `float`] logical position and velocity of the particle
- `particle.qm`: [accepts `float`] charge/mass ratio for the particle
- `particle.q`: particle charge determined by the equation 
    
    ```python
    self.q = omega_p**2 * (1 / qm) * eps_0 * (L / N)
    ```
    - `omega_p` is the given plasma frequency
    - `eps_0` is the vacuum permittivity (set to be 1)
    - `L / N` is the number density of particle specie
- `particle.mv`: [accepts `bool`] the particle is either movable or not

## Further reading
- Birdsall, C. K., & Langdon, A. B., **1991**, *Plasma Physics via Computer Simulation*, The Adam Hilger Series on Plasma Physics, edited by C. Birdsall & A. Langdon. Adam Hilger, Bristol, England [(ISBN: 0-07-005371-5)](https://www.amazon.com/Plasma-Physics-via-Computer-Simulation/dp/0750310251)
- Hockney, R. W., & Eastwood, J. W., **1988**, *Computer Simulation Using Particles*, Bristol: Hilger [(ISBN: 978-0852743928)](https://www.amazon.com/Computer-Simulation-Using-Particles-Hockney/dp/0852743920)

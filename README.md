# Simulating a Quantum Network with Satellite Repeaters

## Plan
- Create code class
- Set variables for distances

### Variables
- LEO: < 2000km (where satellite should be); lowest satellite altitude is 167,4km
- Num repeaters: 1-3 (?)
- Distance between A and B: > 2000km (hard max for establishing quantum link)
- China's satellite distance between repeater and ground station: 1200km

### Considerations
- Distance A to R and R to B: equidistent? would make sense to have the strongest link between all ground stations and satellite
- Noise: weather, solar radiation


### Values
- Ground-ground: 0.18dB/km
- best-case silica optical fibres: 0.095-0.13 dB/km (https://arxiv.org/pdf/1707.01339)
- Satellite-ground (free-space): 30-50 at 500km, 0.014-0.023dB/km
- Satellite-satellite: 0.001-0.002dB/km (hypothetical, very little noise); 0.07 free space in atmosphere
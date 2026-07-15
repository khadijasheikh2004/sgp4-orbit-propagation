# SGP4 Satellite Orbit Propagation

A Python implementation of satellite orbit propagation using the **SGP4 (Simplified General Perturbations 4)** orbital model. The program reads Two-Line Element (TLE) data for multiple satellites, propagates each satellite through one complete orbital revolution, generates 3D orbit visualizations, and exports the predicted state vectors to a CSV file.

## Features

- Reads TLE data for multiple satellites
- Creates `Satrec` objects using the SGP4 library
- Computes one complete orbital revolution from the TLE epoch
- Samples the orbit at configurable intervals
- Predicts:
  - Position (x, y, z) in kilometers
  - Velocity (vx, vy, vz) in km/s
- Generates a 3D orbit plot for every satellite
- Saves all propagated state vectors into a single CSV file

---

## Satellites Included

The repository contains TLE data for the following 11 satellites:

- STELLA
- LARETS
- BLITS
- AJISAI (EGS)
- LARES
- EXPLORER 27 (BEACON-C)
- STARLETTE
- LAGEOS 1
- LAGEOS 2
- COSMOS 1989 (ETALON 1)
- COSMOS 2024 (ETALON 2)

These satellites are commonly used in geodetic and laser ranging studies.

---

## Project Structure

```
project/
│
├── src/
│   ├── main.py
│   ├── read_tle.py
│   ├── propagate.py
│   ├── plot_orbit.py
│   └── save_predictions.py
│
├── tle/
│   └── satellites.tle
│
├── output/
│   ├── *.png
│   └── sgp4_predictions.csv
│
└── README.md
```

---

## Workflow

1. Read the TLE file containing multiple satellites.
2. Parse each satellite into an SGP4 `Satrec` object.
3. Compute the orbital period from the mean motion.
4. Propagate one complete orbit beginning at the TLE epoch.
5. Record timestamp, position, and velocity for each sampled point.
6. Plot the 3D orbit.
7. Save all predictions into a combined CSV file.

---

## Output

### Orbit Plots

A PNG image is generated for every satellite showing its propagated orbit around Earth.

Example:

```
output/
    STELLA_orbit.png
    LARES_orbit.png
    BLITS_orbit.png
    ...
```

### CSV File

All propagated state vectors are stored in:

```
output/sgp4_predictions.csv
```

The CSV contains the following columns:

| Column | Description |
|---------|-------------|
| satellite | Satellite name |
| timestamp | Propagation time |
| x | X position (km) |
| y | Y position (km) |
| z | Z position (km) |
| vx | Velocity X (km/s) |
| vy | Velocity Y (km/s) |
| vz | Velocity Z (km/s) |

---

## Installation

Clone the repository:

```bash
git clone https://github.com/khadijasheikh2004/sgp4-orbit-propagation.git

cd SGP4-Orbit-Propagation
```

Install the required packages:

```bash
pip install sgp4 pandas matplotlib numpy
```

---

## Usage

From the `src` directory, run:

```bash
python main.py
```

The program will:

- Load all satellites from the TLE file
- Propagate one orbital revolution for each satellite
- Display the orbit plots
- Save orbit images in the `output` folder
- Export all propagated state vectors to a CSV file

---

## Main Modules

### `read_tle.py`

Reads a TLE file and creates SGP4 `Satrec` objects for each satellite.

### `propagate.py`

Computes one complete orbital revolution using the SGP4 propagator and returns the predicted position and velocity vectors.

### `plot_orbit.py`

Generates a 3D visualization of the propagated orbit and saves it as a PNG image.

### `save_predictions.py`

Exports the propagated satellite state vectors into a CSV file.

### `main.py`

Coordinates the complete pipeline from reading TLEs to generating plots and exporting predictions.

---

## Dependencies

- Python 3.x
- sgp4
- pandas
- numpy
- matplotlib

Install all dependencies with:

```bash
pip install sgp4 pandas numpy matplotlib
```

---

## License

This project is intended for educational and research purposes.

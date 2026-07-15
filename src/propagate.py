import math
from datetime import timedelta

from sgp4.api import jday
from sgp4.conveniences import sat_epoch_datetime


def propagate_satellite(satellite, samples=360):
    """
    Propagate one complete orbit from the TLE epoch.

    Parameters
    ----------
    satellite : Satrec
        SGP4 satellite object.

    samples : int
        Number of points sampled over one orbital revolution.

    Returns
    -------
    predictions : list
        List of dictionaries containing timestamp,
        position (km), and velocity (km/s).
    """

    # Start propagation from the TLE epoch
    start_time = sat_epoch_datetime(satellite)

    # Mean motion (radians/minute)
    mean_motion = satellite.no_kozai

    # Orbital period (minutes) time to complete one full orbit
    period_minutes = (2 * math.pi) / mean_motion

    print(f"Orbital Period : {period_minutes:.2f} minutes")

    # Time between samples (seconds)
    dt = (period_minutes * 60) / samples

    predictions = []

    for i in range(samples + 1):

        current_time = start_time + timedelta(seconds=i * dt)

        jd, fr = jday( # converts calendar date t julian date
            current_time.year, # sgp4 only accepts julian dates
            current_time.month,
            current_time.day,
            current_time.hour,
            current_time.minute,
            current_time.second + current_time.microsecond / 1e6,
        )

        error, position, velocity = satellite.sgp4(jd, fr)

        if error != 0:
            continue

        predictions.append(
            {
                "timestamp": current_time,
                "x": position[0],
                "y": position[1],
                "z": position[2],
                "vx": velocity[0],
                "vy": velocity[1],
                "vz": velocity[2],
            }
        )

    return predictions
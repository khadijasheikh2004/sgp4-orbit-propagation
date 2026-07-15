import matplotlib.pyplot as plt
import numpy as np


def plot_orbit(df, satellite_name, save_path=None):

    fig = plt.figure(figsize=(8, 8)) # creates the window

    ax = fig.add_subplot(111, projection="3d") # creates 3d plotting acis

    ax.plot( # draws the orbit as a connected line
        df["x"],
        df["y"],
        df["z"],
        linewidth=2,
        label=satellite_name,
    )

    ax.scatter( # places earth at the origin
        0,
        0,
        0,
        s=120,
        label="Earth",
    )

    # Equal axis scaling
    max_range = np.array([ # calculates the largest axis length
        df["x"].max() - df["x"].min(),
        df["y"].max() - df["y"].min(),
        df["z"].max() - df["z"].min(),
    ]).max() / 2

    # finds the center of the orbit
    mid_x = (df["x"].max() + df["x"].min()) / 2
    mid_y = (df["y"].max() + df["y"].min()) / 2
    mid_z = (df["z"].max() + df["z"].min()) / 2

    # makes every axis the same length
    ax.set_xlim(mid_x - max_range, mid_x + max_range)
    ax.set_ylim(mid_y - max_range, mid_y + max_range)
    ax.set_zlim(mid_z - max_range, mid_z + max_range)

    # labels the axes in kilometers
    ax.set_xlabel("X (km)")
    ax.set_ylabel("Y (km)")
    ax.set_zlabel("Z (km)")

    ax.set_title(f"{satellite_name} - SGP4 Prediction")

    ax.legend()

    if save_path:
        plt.savefig(save_path, dpi=300)

    plt.show()
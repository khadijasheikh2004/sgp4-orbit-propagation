import os # used for creating folders, joining file paths, checking directories
import pandas as pd # pandas is used for tables

from read_tle import read_tle
from propagate import propagate_satellite
from save_predictions import save_predictions
from plot_orbit import plot_orbit


TLE_FILE = "../tle/satellites.tle"

OUTPUT_FOLDER = "../output"

os.makedirs(OUTPUT_FOLDER, exist_ok=True)


def main():

    print("=" * 60)
    print("Residual Learning Physics Pipeline")
    print("=" * 60)

    satellites = read_tle(TLE_FILE)

    print(f"\nLoaded {len(satellites)} satellites.\n")

    all_predictions = []

    for sat in satellites:

        name = sat["name"]

        print("=" * 60)
        print(name)
        print("=" * 60)

        predictions = propagate_satellite(
            sat["satellite"]
        )

        # Add satellite name to every prediction
        for row in predictions:
            row["satellite"] = name

        all_predictions.extend(predictions)

        # Individual orbit plots
        df = pd.DataFrame(predictions)

        safe_name = (
            name.replace(" ", "_")
            .replace("(", "")
            .replace(")", "")
            .replace("-", "_")
        )

        plot_orbit(
            df,
            name,
            os.path.join(
                OUTPUT_FOLDER,
                f"{safe_name}_orbit.png",
            ),
        )

    # Create one combined dataframe
    combined_df = pd.DataFrame(all_predictions)

    # Reorder columns
    combined_df = combined_df[
        [
            "satellite",
            "timestamp",
            "x",
            "y",
            "z",
            "vx",
            "vy",
            "vz",
        ]
    ]

    save_predictions(
        combined_df,
        os.path.join(
            OUTPUT_FOLDER,
            "sgp4_predictions.csv",
        ),
    )

    print("\nFinished successfully.")


if __name__ == "__main__":
    main()
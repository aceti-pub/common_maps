import numpy as np
import os
def map_importer(map_name: str):
    """
    Import a map from a file and return the base matrix and lat/lon map.

    Args:
        map_name (str): The name of the map to import.

    Returns:
        tuple: A tuple containing the base matrix and lat/lon map.
    """
    # Load the base matrix
    base_matrix = np.load(os.path.join("maps", f"{map_name}.npy"))

    # Load the lat/lon map
    lat_lon_map = np.load(os.path.join("maps", f"lat_lon_{map_name}.npy"))

    return base_matrix, lat_lon_map
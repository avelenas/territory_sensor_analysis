import numpy as np

def clean_sector(sector:np.ndarray) -> None:
    median = np.nanmedian(sector)

    low = sector < median -10
    high = sector > median + 10

    sector[low] = median
    sector[high] = median
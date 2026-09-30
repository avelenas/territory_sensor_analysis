import numpy as np

from cleaner import clean_all_sectors

def analyze_sector(sector: np.ndarray, sector_number: int) -> dict:
    if np.isnan(sector).any():
        return None

    min_temp = np.min(sector)
    max_temp = np.max(sector)
    mean_temp = np.mean(sector)
    median_temp = np.median(sector)
    temp_range = max_temp - min_temp

    return {"sector_index": sector_number,
            "min_temp": min_temp,
            "max_temp": max_temp,
            "mean_temp": mean_temp,
            "median_temp": median_temp,
            "temp_range": temp_range,
    }

def process_data_sectors(all_sectors: np.ndarray) -> None:
    results = []
    sector_number = 1

    for row in all_sectors:
        for sector in row:
            result = analyze_sector(sector, sector_number)
            if result is not None:
                results.append(result)
            sector_number += 1

    with open("results/sectors_analysis.csv", "w", encoding="utf-8") as file:
        file.write("sector_index,"
                   "min_temp,"
                   "max_temp,"
                   "mean_temp,"
                   "median_temp,"
                   "temp_range\n")

        for result in results:
            file.write(
                f"{result['sector_index']},"
                f"{result['min_temp']:.2f},"
                f"{result['max_temp']:.2f},"
                f"{result['mean_temp']:.2f},"
                f"{result['median_temp']:.2f},"
                f"{result['temp_range']:.2f}\n"
            )

if __name__ == "__main__":
    from data_service import data, sectors

    clean_all_sectors(sectors)
    process_data_sectors(sectors)
import numpy as np

def analyze_problems(sectors: np.ndarray) -> None:
    with open("results/sensors_problems.csv", "w", encoding="utf-8") as file:
        file.write("sector_index,nan_count,too_low_count,too_high_count,invalid_count\n")

        number = 0

        for row in sectors:
            for sector in row:
                median = np.nanmedian(sector)

                nan = np.isnan(sector).sum()
                low =(sector < median -10).sum()
                high = (sector > median + 10).sum()

                invalid = nan + low + high

                file.write(f"{number},{nan},{low},{high},{invalid}\n")
                number += 1
    file.close()


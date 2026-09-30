import numpy as np

data = np.genfromtxt("results/sectors_analysis.csv", delimiter=",", names=True)

sector_index = data["sector_index"]
mean_temperature = data["mean_temp"]
average_temperature = np.mean(mean_temperature)
coldest_indexes = np.argsort(mean_temperature)[:10]
warmest_indexes = np.argsort(mean_temperature)[-10:][::-1]
difference = np.abs(mean_temperature - average_temperature)
closest_indexes = np.argsort(difference)[:30]

with open("results/all_sectors.csv", "w", encoding="utf-8") as file:
    file.write("sector_index,category\n")

    for index in coldest_indexes:
        file.write(f"{int(sector_index[index])},coldest\n")

    for index in warmest_indexes:
        file.write(f"{int(sector_index[index])},warmest\n")

    for index in closest_indexes:
        file.write(f"{int(sector_index[index])},closest_to_average\n")
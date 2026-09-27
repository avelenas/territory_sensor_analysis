from pathlib import Path
import numpy as np

folder = Path("data_files/sensors.csv")

data = np.loadtxt(folder, delimiter=",")

print(data)
print("\n", data.shape)
print("\n", type(data))

sectors = data.reshape(12, 10, 14, 10).transpose(0, 2, 1, 3)
print()
print(sectors)
print("\n", sectors.shape)
print("\n", type(sectors))

print("cеверо-запад", sectors[0][0])
print("\n", "cеверо-восток", sectors[0][-1])
print("\n", "юго-запад", (sectors[-1][0]))
print("\n", "юго-восток", sectors[-1][-1])


# sectors[0][0][0][0] = 4648.21
# print(data[0][0])
# print("cеверо-запад", sectors[0][0])
from pathlib import Path
import numpy as np

folder = Path("data_files/sensors.csv")

data = np.loadtxt(folder, delimiter=",")

print(data)
print("\n", data.shape)
print("\n", type(data))
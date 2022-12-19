import os
import pandas as pd
import numpy as np
from io import StringIO
import scipy
import matplotlib.pyplot as plt


def read_files(folder):
    files = []
    for file in os.listdir(folder):
        if file.endswith(".dat"):
            files.append(file)
    return files


def read_file(file):
    with open(file, "r") as f:
        lines = f.readlines()
        level_count = 0
        sub_level_count = 0
        levels = dict()
        for line in lines:
            if level_count == 0 and sub_level_count == 0:
                pos = [(0, 5), (6, 10), (11, 15), (16, 20), (21, -1)]
                df = pd.read_fwf(StringIO(line), header=None, colspecs=pos, encoding='utf8',
                                 names=["element", "A", "Z", "n", "rest"])
                z = int(df["Z"][0])
                a = int(df["A"][0])
                level_count = int(df["n"][0])
                sub_level_count = 0
                levels[f"Z{z:03}A{a:03}"] = list()
            elif level_count > 0 and sub_level_count == 0:
                pos = [(0, 3), (4, 14), (15, 20), (20, 23), (23, 34), (34, 37), (37, -1)]
                df = pd.read_fwf(StringIO(line), header=None, colspecs=pos, encoding='utf8',
                                 names=["level_i", "energy", "spin", "parity", "life_time", "n_sub_levels", "rest"])
                sub_level_count = int(df["n_sub_levels"][0])
                energy = float(df["energy"][0])
                levels[f"Z{z:03}A{a:03}"].append(energy)
                level_count -= 1
            elif sub_level_count > 0:
                sub_level_count -= 1
    return levels


def suggested_function(energy, a, b, c):
    return a + b * energy + c * energy ** 2


def main():
    levels = dict()
    folder = "./levels"
    files_in_folder = read_files(folder)
    for file in files_in_folder:
        levels |= read_file(f"{folder}/{file}")
    for key, value in levels.items():
        if len(value) > 10:
            xs = np.array(value)
            ys = np.array([value.index(x) for x in value])
            p0 = [1, 1, 1]
            params = scipy.optimize.curve_fit(suggested_function, xs, ys, p0)
            a, b, c = params[0]
            squared_diffs = np.square(ys - suggested_function(xs, a, b, c))
            squared_diffs_from_mean = np.square(ys - np.mean(ys))
            r_squared = 1 - np.sum(squared_diffs) / np.sum(squared_diffs_from_mean)
            print(f"{key}: R² = {r_squared:.2f} with {a:8.2f}, {b:8.2f}, {c:8.2f}")
            plt.figure()
            plt.plot(xs, ys, "o")
            plt.plot(xs, suggested_function(xs, a, b, c))
            plt.title(f"{key} R² = {r_squared:.2f} with {a:.2f}, {b:.2f}, {c:.2f}")
            plt.savefig(f"./plots/{key}.png")
            plt.close()


if __name__ == '__main__':
    main()

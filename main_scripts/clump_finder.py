import sys
import os
#from raise_error import *
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from implementation.finding_patterns import find_clumps


def main():

    data_path = os.path.join(os.path.dirname(__file__), "..", "data", "e_coli.txt")
    data_path = os.path.join(os.path.dirname(__file__), "..", "data", "find_clumps_data.txt")

    with open(data_path, "r") as file:
        lines = file.readlines()

    genome = lines[0].strip()
    k_mer_size, window_size, threshold_count = map(int, lines[1].strip().split())

    clumps = find_clumps(genome, k_mer_size, window_size, threshold_count)
    print(clumps)
    #print(int((len(clumps) + 1)/(k_mer_size + 1)))

if __name__ == "__main__":
    main()

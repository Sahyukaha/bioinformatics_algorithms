import sys
import os
#from raise_error import *
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from implementation.finding_patterns import generate_neighborhood

def main():

    data_path = os.path.join(os.path.dirname(__file__), "..", "data", "generate_string_neighbors_data.txt")

    with open(data_path, "r") as file:
        lines = file.readlines()

    string = lines[0].strip()
    num_mismatch = int(lines[1])

    neighbors = generate_neighborhood(string, num_mismatch)
    print(' '.join(neighbors))
    #print(int((len(clumps) + 1)/(k_mer_size + 1)))

if __name__ == "__main__":
    main()

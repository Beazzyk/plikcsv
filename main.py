import csv
import sys


def read_csv(file_path):
    plik = []
    with open(file_path, mode='r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for line in reader:
            plik.append(line)
        return plik


def change_data(data, new_data):
    data_to_change = new_data.split(",")
    x_value = int(data_to_change[1])
    y_value = int(data_to_change[0])
    new_value = data_to_change[2]
    if 0 <= x_value < len(data) and 0 <= y_value < len(data[x_value]):
        data[x_value][y_value] = new_value
    else:
        print(f"Index {x_value},{y_value} is out of range.")


def write_data(file_path, data_to_write):
    with open(file_path, mode="w", newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(data_to_write)

if __name__ == "__main__":
    if len(sys.argv) > 3:
        input_csv = sys.argv[1]
        output_csv = sys.argv[2]
        data = read_csv(input_csv)
        for argument in sys.argv[3:]:
            change_data(data, argument)
        print(data)
        write_data(output_csv, data)
    else:
        print("Not enough arguments.")
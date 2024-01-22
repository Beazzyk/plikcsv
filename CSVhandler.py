import csv
import os


class CSVHandler:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = []

    def read_csv(self):
        if not os.path.exists(self.file_path):
            print(f"Plik nie istnieje: {self.file_path}")
            return

        with open(self.file_path, mode='r', newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            for line in reader:
                self.data.append(line)

    def change_data(self, new_data):
        data_to_change = new_data.split(",")
        if len(data_to_change) == 3:
            x_value = data_to_change[1]
            y_value = data_to_change[0]
            new_value = data_to_change[2]

            if x_value.isnumeric() and y_value.isnumeric():
                x_index = int(x_value)
                y_index = int(y_value)
                if 0 <= x_index < len(self.data) and 0 <= y_index < len(self.data[x_index]):
                    self.data[x_index][y_index] = new_value
                else:
                    print(f"Indeks {x_value},{y_value} jest poza zakresem.")
            else:
                print("Wartości indeksów muszą być numerami.")
        else:
            print("Nieprawidłowy format danych wejściowych. Proszę podać trzy wartości oddzielone przecinkami.")

    def write_data(self, output_path):
        if not os.path.exists(output_path):
            print(f"Plik nie istnieje: {output_path}")
            return

        with open(output_path, mode="w", newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(self.data)


import sys
from CSVhandler import CSVHandler


def main():
    if len(sys.argv) > 3:
        input_csv = sys.argv[1]
        output_csv = sys.argv[2]
        csv_handler = CSVHandler(input_csv)
        csv_handler.read_csv()

        for argument in sys.argv[3:]:
            csv_handler.change_data(argument)

        print(csv_handler.data)
        csv_handler.write_data(output_csv)
    else:
        print("Nie wystarczajacy argument.")


if __name__ == "__main__":
    main()

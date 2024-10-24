import re
import csv
import argparse
import os


def main():
    parser = argparse.ArgumentParser(description="Searches a csv for numbers scientific notation and converts them to a float.")
    parser.add_argument("Input_CSV", help="The path of the CSV to edit.")
    parser.add_argument("Output_CSV", help="The path where the generated CSV is saved.")
    args = parser.parse_args()

    csv_sci_to_float(args.Input_CSV, args.Output_CSV)


def csv_sci_to_float(input_path: str, output_path: str):
    if os.path.exists(output_path):
        if os.path.samefile(input_path, output_path):
            raise Exception("Input and output paths cannot be the same.")
    
    with open(input_path, 'r', encoding='utf-8') as input_csv, open(output_path, 'w', newline='', encoding='utf-8') as output_csv:
        r = csv.reader(input_csv)
        w = csv.writer(output_csv)
        for row in r:
            new_row = [sci_to_float(i) for i in row]
            w.writerow(new_row)


# Uses regex to determine if a value is in exponential notation and if so, uses string manipulation to conver it to a float.
# WARNING: This function takes and returns strings as it's reliant on string manipulation.
def sci_to_float(val: str) -> str:
    if re.match(r'[-+?[0-9]*\.?[0-9]+[Ee][-+]?[0-9]+', val):
        try:
            precision = get_precision(val)
            return f"{float(val):.{precision}f}"
        except ValueError:
            pass
    return val


# Finds the exponent in the notated number
def get_precision(sci_num: str) -> int:
    sci_num = ''.join(char.lower() if char == 'E' else char for char in sci_num)
    base, exp = sci_num.split('e')
    exp = int(exp)
    if exp < 0:
        base_dec = len(base.split(".")[1]) if "." in base else 0
        return int(abs(exp) + base_dec)
    else:
        return 0
    

if __name__ == "__main__":
    main()

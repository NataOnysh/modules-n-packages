import csv
from converter.temperature import celsius_to_fahrenheit as to_f, fahrenheit_to_celsius as to_c
from converter.distance import m_to_ft as to_ft, ft_to_m as to_m


def convert_temp(database_name: str, target_temp: str):
    input_file = f'{database_name}.csv'
    output_file = f'{database_name}_updated.csv'
    with open(input_file, mode='r', encoding='utf-8') as file, open(output_file, mode='w', newline='', encoding='utf-8') as output:
        reader = csv.DictReader(file)
        writer = csv.DictWriter(output, fieldnames=reader.fieldnames)
        writer.writeheader()
        for row in reader:
            reading = row['Reading'].split('°')
            temp = int(reading[0])
            temp_scale = str(reading[1])
            if temp_scale == target_temp:
                writer.writerow(row)
            else:
                if target_temp == 'F':
                    reading = to_f(temp)
                elif target_temp == 'C':
                    reading = to_c(temp)
                row['Reading'] = reading
            writer.writerow(row)
    return output_file


convert_temp('temp_database', 'F')

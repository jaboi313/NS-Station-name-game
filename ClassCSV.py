import csv

class CSV:
    def __init__(self, file_path: str = 'Stations_info.csv'):
        self.__file_path = file_path

    def get_colum_names(self) -> list:
        """Reads the CSV file colum name(s)."""
        with open(self.__file_path, 'r', newline='', encoding='utf-8') as infile:
            reader = csv.DictReader(infile)
            return reader.fieldnames

    def read_whole_file(self) -> list[list]:
        """Reads the CSV file and returns its content as a list of lists."""
        with open(self.__file_path, 'r', newline='', encoding='utf-8') as infile:
            info = csv.reader(infile, delimiter=',')
            return list(info)
        
    def read_whole_column(self, column_name: str) -> list[str]:
        """Reads a specific column from the CSV file and returns it as a list.
            Possible colums:    get_colum_names()
        """
        with open(self.__file_path, 'r', newline='', encoding='utf-8') as infile:
            reader = csv.DictReader(infile)
            column_data = []

            for row in reader:
                if column_name in row:
                    column_data.append(row[column_name])

        return column_data
    
    def get_row_from_value(self, value: list, value_column: str) -> list[str]:
        """Searches for the value in the CSV file and returns its row"""
        normalized_values = {v.lower().replace(" ", "").replace("-", "") for v in value if isinstance(v, str)}

        with open(self.__file_path, 'r', newline='', encoding='utf-8') as infile:
            reader = csv.DictReader(infile)

            # Loop door alle rijen en zoek naar een match
            for row in reader:
                cell_value = row[value_column].lower().replace(" ", "").replace("-", "")
                if cell_value in normalized_values:
                    return row  # Geef de eerste gevonden rij terug

        return None  # Geen match gevonden
    
    def get_row_from_value_one_colum(self, value: list, value_column: str, return_column: str) -> str:
        """Searches for the value in the CSV file and returns a colum value in the same row"""
        normalized_values = {v.lower().replace(" ", "").replace("-", "") for v in value if isinstance(v, str)}

        with open(self.__file_path, 'r', newline='', encoding='utf-8') as infile:
            reader = csv.DictReader(infile)

            # Loop door alle rijen en zoek naar een match
            for row in reader:
                cell_value = row[value_column].lower().replace(" ", "").replace("-", "")
                if cell_value in normalized_values:
                    return row  [return_column]

        return None
    

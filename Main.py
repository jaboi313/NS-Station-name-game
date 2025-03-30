from ClassCSV import CSV
from ClassAnagram import Anagram

csv = CSV()
anagram = Anagram("Lengte mijnen", csv.read_whole_column('Station'))

if __name__ == "__main__":
    print(anagram.solve_fast())
    print(anagram.get_combinations_made("fast"))
    print(csv.get_row_from_value(anagram.solve_fast(), 'Station'))
    print(csv.get_row_from_value_one_colum(anagram.solve_fast(), 'Station', 'Code'))

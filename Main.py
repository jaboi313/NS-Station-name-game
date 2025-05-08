from ClassCSV import CSV
from ClassAnagram import Anagram

csv = CSV()
anagram = Anagram(input("Puzzelwoord: "), csv.read_whole_column('Station'))

if __name__ == "__main__":
    solve = anagram.solve_fast()
    print(solve)
    print(anagram.get_combinations_made("fast"))
    print(csv.get_row_from_value(solve, 'Station'))
    print(csv.get_row_from_value_one_colum(solve, 'Station', 'Code'))

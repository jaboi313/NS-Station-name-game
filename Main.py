from ClassCSV import CSV
from ClassAnagram import Anagram

csv = CSV()
anagram = Anagram("Lengte mijnen", csv.read_whole_column('Station'))

print(anagram.anagram())
print(anagram.get_combinations_made())
print(csv.get_row_from_value(anagram.anagram(), 'Station'))
print(csv.get_row_from_value_one_colum(anagram.anagram(), 'Station', 'Code'))

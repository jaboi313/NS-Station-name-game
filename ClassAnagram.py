from itertools import permutations

class Anagram:
    def __init__(self, word:str, word_list:list[str] = None):
        self.__word = word
        self.__word_list = word_list
        self.__combinations_made = 0

    def get_combinations_made(self):
        return self.__combinations_made

    def is_word_in_list(self, word) -> bool:
        """Checks if the given word (case-insensitive) is in the list."""
        return any(item.lower().replace(" ", "").replace("-", "") == word for item in self.__word_list)

    def anagram(self):
        letters = [chr for chr in self.__word.replace(" ", "").lower()]
        repeat_check = []

        for current in permutations(letters):
            current_word = ''.join(current)
            self.__combinations_made += 1
            if self.__word_list is not None:
                if self.is_word_in_list(current_word) and current_word not in repeat_check:
                    repeat_check.append(current_word)
            else:
                if current_word not in repeat_check:
                    repeat_check.append(current_word)
        
        return repeat_check
from itertools import permutations
from collections import Counter

class Anagram:
    def __init__(self, word: str, word_list: list[str] = None):
        self.__word = word.replace(" ", "").lower()
        self.__word_counter = Counter(self.__word)
        self.__word_list_fast = set(map(lambda w: w.lower().replace(" ", "").replace("-", ""), word_list)) if word_list else set()
        self.__word_list_medium = set(map(lambda w: w.lower().replace(" ", "").replace("-", ""), word_list)) if word_list else None
        self.__word_list_slow = word_list
        self.__combinations_fast_made = 0
        self.__combinations_medium_made = 0
        self.__combinations_slow_made = 0

    def is_word_in_list(self, word) -> bool:
        """Checks if the given word (case-insensitive) is in the list."""
        return any(item.lower().replace(" ", "").replace("-", "") == word for item in self.__word_list_fast)

    def get_combinations_made(self, type:str = "fast"):
        """type can be: 'fast', 'medium' or 'slow'"""
        if type == "fast":
            return self.__combinations_fast_made
        if type == "medium":
            return self.__combinations_medium_made
        if type == "slow":
            return self.__combinations_slow_made
        else:
            raise ValueError("type must be: 'fast', 'medium' or 'slow'")
    
    def solve_fast(self):
        """Generates anagrams and returns only the valid ones from the word list."""
        valid_anagrams = set()

        possible_words = {word for word in self.__word_list_fast if Counter(word) == self.__word_counter}

        for word in possible_words:
            self.__combinations_fast_made += 1
            valid_anagrams.add(word)

        return list(valid_anagrams)


    def solve_medium(self):
        """Generates anagrams and returns only the valid ones from the word list."""
        letters = tuple(self.__word)
        seen_words = set()
        valid_anagrams = set()

        for current in permutations(letters):
            current_word = ''.join(current)
            print(current_word)
            # Avoid redundant checks
            if current_word in seen_words:
                continue
            seen_words.add(current_word)
            self.__combinations_medium_made += 1

            if self.__word_list_medium and current_word in self.__word_list_medium:
                valid_anagrams.add(current_word)

        return list(valid_anagrams)
    

    def solve_slow(self):
        letters = [chr for chr in self.__word]
        repeat_check = []

        for current in permutations(letters):
            current_word = ''.join(current)
            self.__combinations_slow_made += 1
            if self.__word_list_slow is not None:
                if self.is_word_in_list(current_word) and current_word not in repeat_check:
                    repeat_check.append(current_word)
            else:
                if current_word not in repeat_check:
                    repeat_check.append(current_word)
        
        return repeat_check
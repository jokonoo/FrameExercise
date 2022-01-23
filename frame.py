from math import ceil


class CharLengthError(Exception):
    pass


class NotEvenOrOddNumberOfCharacters(Exception):
    pass


class Frame:
    def __init__(self, text, char, number_of_spaces=1, centre=False):
        self.text = text
        if len(char) > 1:
            raise CharLengthError('Must be only one character')
        self.char = char
        self.number_of_spaces = ceil(abs(number_of_spaces))
        if centre:
            if all([True if len(word) % 2 == 0 else False for word in text]):
                self.centre = centre
            elif all([True if len(word) % 2 != 0 else False for word in text]):
                self.centre = centre
            else:
                raise NotEvenOrOddNumberOfCharacters('Must be only even or odd number of characters in words to center')
        self.centre = centre

    def build_frame(self):
        n_of_spaces = ceil(abs(self.number_of_spaces))  # making sure that number is both positive and not int
        longest_word = len(max(self.text, key=len))  # finding length of the longest word
        floor = (longest_word + 2 + (
                2 * n_of_spaces)) * self.char  # building floor based on len of longest word and character each side
        if self.centre:
            wall = [
                f'{self.char}{word.center(len(floor) - 2 * len(self.char))}{self.char}'
                for word in self.text]  # if center is set to True, then words are centered
        else:
            wall = [
                f'{self.char}{word.rjust(len(word) + n_of_spaces)}{self.char.rjust(len(floor) - (len(self.char)) - n_of_spaces - len(word))}'
                for word in self.text]  # building walls based on length of longest word and number of spaces
        wall = '\n'.join(wall)  # joining all words with newline character
        return f'{floor}\n{wall}\n{floor}'  # finally returning whole frame together


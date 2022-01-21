def frame(text, char, number_of_spaces=1, center=False):
    longest_word = len(max(text, key=len))  # finding length of the longest word
    floor = (longest_word + 2 + (
                2 * number_of_spaces)) * char  # building floor based on length of longest word and character each side
    if center:
        wall = [
            f'{char}{word.center(len(floor)-2*len(char))}{char}'
            for word in text]  # if center is set to True, then words are centered
    else:
        wall = [
            f'{char}{word.rjust(len(word) + number_of_spaces)}{char.rjust(len(floor)-(len(char))-number_of_spaces-len(word))}'
            for word in text]  # building walls based on length of longest word, number of spaces, and character/s
    wall = '\n'.join(wall)  # joining all words with newline character
    return f'{floor}\n{wall}\n{floor}'  # finally returning whole frame together

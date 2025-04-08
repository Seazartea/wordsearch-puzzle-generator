import random
import sys
from pdf_generator import pdf_maker
from get_words_from_txtfile import get_input


def main():
    word_list_for_grid, pdf_title = get_input()
    grid, wordsearch_words = create_wordsearch_grid(word_list_for_grid)
    pdf_maker(pdf_title, grid, wordsearch_words)



#takes selected words and arranges them on an empty wordsearch grid, making sure they fit, before then filling the rest of the grid with random letters
def create_wordsearch_grid(word_list):
    grid, width, height = make_empty_grid()
    directions = ["N", "NE", "E", "SE", "S", "SW", "W", "NW"]
    wordsearch_words = []

    while len(wordsearch_words) < 24:
        n = 0
        keep_looping = "yes"
        #exits program if tried every word in chosen word list
        if len(word_list) <= 0:
            sys.exit("Program failed to make wordsearch puzzle, ran out of words to choose from.")

        word = random.choice(word_list)
        word_list.remove(word)
        #remove any spaces in word for putting into grid
        word_without_space = word.replace(" ", "")
        while n <= (2 * width * height):
            x = random.randint(0, (width - 1))
            y = random.randint(0, (height - 1))
            d = 0
            while d <= 16:
                direction = random.choice(directions)
                if will_the_word_fit(grid, word_without_space, x, y, direction, width, height):
                    grid = insert_word(grid, word_without_space, x, y, direction)
                    wordsearch_words.append(word)
                    keep_looping = "no"
                    break
                d += 1
            if keep_looping == "no":
                break
            n += 1


    finished_grid = random_letter_filler(grid)
    return finished_grid, wordsearch_words



#creates nested lists of set dimensions that will act as the basis for the wordsearch grid and returns a made grid of 0's
#the 0's are used to denote an empty space in the grid for when words are added and later any remaining 0's will be replaced with random letters
def make_empty_grid():
    #set dimensions here
    width = 22
    height = 24
    grid = []
    for i in range(height):
        line = []
        for k in range(width):
            line.append("0")
        grid.append(line)

    return grid, width, height



#fills any remaining 0's with random letters
def random_letter_filler(grid):
    alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    for i in range(len(grid)):
        for k in range(len(grid[i])):
            if grid[i][k] == "0":
                grid[i][k] = random.choice(alphabet)

    return grid



#Takes the grid, starting point, a word and direction to go in and sees if the word can fit or if those spaces are already filled or if the word would go beyond the size of the grid
def will_the_word_fit(grid, word, x, y, direction, width, height):
    for letter in word:
        if x < 0 or y < 0:
            return False
        if x >= width or y >= height:
            return False
        if grid[y][x] != "0":
            if grid [y][x] != letter:
                return False
        x, y = increment_coords(x, y, direction)

    return True



#Having confirmed the word can fit, iterates over letter in word and inserts into grid in given direction from a starting position
def insert_word(grid, word, x, y, direction):
    for letter in word:
        grid[y][x] = letter
        x, y = increment_coords(x, y, direction)

    return grid



#changes input coords depending on which direction word is oriented
def increment_coords(x, y, direction):
    if direction == "N":
        y -= 1
    elif direction == "NE":
        y -= 1
        x += 1
    elif direction == "E":
        x += 1
    elif direction == "SE":
        y += 1
        x += 1
    elif direction == "S":
        y += 1
    elif direction == "SW":
        y += 1
        x -= 1
    elif direction == "W":
        x -= 1
    elif direction == "NW":
        y -= 1
        x -= 1

    return x, y



if __name__ == "__main__":
    main()

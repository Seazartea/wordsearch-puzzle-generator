import sys


def get_input():
    print("Choose a theme for the wordsearch words to be. Random includes words from the other themes and more.")
    print("1. Christmas, 2. Colours, 3. Countries & Capitals, 4. Food, 5. Halloween")
    print("6. Musical Instruments, 7. Plants & Animals, 8. School Subjects, 9. Sports, 10. Periodic Elements")
    print("11. Random")
    choice = input("Enter the number for the theme you want for the wordsearch puzzle: ")
    if choice.isnumeric():
        word_list_for_grid, pdf_title = get_words(choice)
    else:
        sys.exit("Input must be a number to be valid")

    return word_list_for_grid, pdf_title



#takes user input, reads in associated txt file, and returns list of words and title.
#Title is for the header/title of the generated pdf
def get_words(choice):
    if choice == "1":
        title = "Christmas"
        try:
            with open("word_lists/christmas.txt", "r") as file:
                input_list = file.read().splitlines()
        except FileNotFoundError:
            sys.exit("Input file 'christmas.txt' does not exist")

    elif choice == "2":
        title = "Colours"
        try:
            with open("word_lists/colours.txt", "r") as file:
                input_list = file.read().splitlines()
        except FileNotFoundError:
            sys.exit("Input file 'colours.txt.' does not exist")

    elif choice == "3":
        title = "Countries & Capitals"
        try:
            with open("word_lists/countries_capitals.txt", "r") as file:
                input_list = file.read().splitlines()
        except FileNotFoundError:
            sys.exit("Input file 'countries_capitals.txt' does not exist")

    elif choice == "4":
        title = "Food"
        try:
            with open("word_lists/food.txt", "r") as file:
                input_list = file.read().splitlines()
        except FileNotFoundError:
            sys.exit("Input file 'food.txt' does not exist")

    elif choice == "5":
        title = "Halloween"
        try:
            with open("word_lists/halloween.txt", "r") as file:
                input_list = file.read().splitlines()
        except FileNotFoundError:
            sys.exit("Input file 'halloween.txt' does not exist")

    elif choice == "6":
        title = "Musical Instruments"
        try:
            with open("word_lists/musical_instruments.txt", "r") as file:
                input_list = file.read().splitlines()
        except FileNotFoundError:
            sys.exit("Input file 'musical_instruments.txt' does not exist")

    elif choice == "7":
        title = "Plants & Animals"
        try:
            with open("word_lists/plants_animals.txt", "r") as file:
                input_list = file.read().splitlines()
        except FileNotFoundError:
            sys.exit("Input file 'plants_animals.txt' does not exist")

    elif choice == "8":
        title = "School Subjects"
        try:
            with open("word_lists/school_subjects.txt", "r") as file:
                input_list = file.read().splitlines()
        except FileNotFoundError:
            sys.exit("Input file 'school_subjects.txt' does not exist")

    elif choice == "9":
        title = "Sports"
        try:
            with open("word_lists/sports.txt", "r") as file:
                input_list = file.read().splitlines()
        except FileNotFoundError:
            sys.exit("Input file 'sports.txt' does not exist")

    elif choice == "10":
        title = "Periodic Elements"
        try:
            with open("word_lists/periodic_elements.txt", "r") as file:
                input_list = file.read().splitlines()
        except FileNotFoundError:
            sys.exit("Input file 'periodic_elements.txt' does not exist")
            
    else:
        title = "Word Search"
        try:
            with open("word_lists/all.txt", "r") as file:
                input_list = file.read().splitlines()
        except FileNotFoundError:
            sys.exit("Input file 'all.txt' does not exist")

    #convert all words into uppercase versions
    output_list = []
    for i in input_list:
        x = i.upper()
        output_list.append(x)

    return output_list, title

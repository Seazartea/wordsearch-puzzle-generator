from fpdf import FPDF


#function that takes the wordsearch grid and words to find, and makes a .pdf file in the standard wordsearch style
def pdf_maker(title, grid, wordsearch_words):
    #defaults to an A4 page in portrait orientation
    pdf = FPDF()
    pdf.add_page()


    #Dealing with header, title should be the theme of the wordsearch puzzle
    pdf.set_font("Helvetica", "B", 34)
    pdf.cell(0, 25, title, align = "C")
    pdf.ln()


    #Placing the wordsearch grid on the pdf, does it letter by letter
    #Currently set up for 22 wide, if change needs realigning of the pdf.set(x) x value, use the food title to line up centre between the two O's
    pdf.set_font("Helvetica", "", 15)
    for row in grid:
        pdf.set_x(17)
        for letter in row:
            pdf.cell(8, 8, letter, align = "C")
        pdf.ln()


    #Placing the words to find in the grid
    #If either more words are added or more rows of grid added, will cause last row of words to be put on a new page
    pdf.ln(5)
    words_to_find_distance_from_left = 17
    pdf.set_x(words_to_find_distance_from_left)
    pdf.set_font("Helvetica", "B", 11)
    n = 0
    for word in wordsearch_words:
        pdf.cell(63, 5, word, align = "L")
        n += 1
        #splits words into three columns
        if n % 3 == 0:
            pdf.ln()
            pdf.set_x(words_to_find_distance_from_left)


    pdf.output("word_search_puzzle.pdf")

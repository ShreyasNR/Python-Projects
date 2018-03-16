__author__ = 'jc451634'

# Initialize the constants

FILE = "books.csv"


def main():
    print("Reading List 1.0 - by Shreyas Bharadwaj N R")
    book_list = []
    load_books(book_list)
    print(book_list)
    display_menu()
    choice = input(">>>")
    while choice.lower() != 'q':
        if choice.lower() == 'r':
            required_books(book_list)
        elif choice.lower() == 'c':
            completed_books(book_list)
        elif choice.lower() == 'a':
            book_list = add_books()
        elif choice.lower() == 'm':
            complete_a_book(book_list)
        else:
            print("Invald menu choice")
        display_menu()
        choice = input(">>>")
    print("{} books have been saved to {}".format(len(book_list), FILE))
    print("Have a nice day :)")


def display_menu():
    """
    This function is used to display the options Menu
"""
    MENU = "Menu: \nR - List required books\nC - List completed books\nA - Add new book\nM - Mark a book as " \
           "completed\nQ - Quit"
    print(MENU)


# After the display_menu function

def load_books(book_list):
    """
     This will load books from file to List
"""
    book_file = open(FILE, 'r')
    for line in book_file:
        book_list.append(line.strip().split(','))
    book_file.close()


# After the load_books()

def complete_a_book(book_list):
    """
    This Function will complete a book into a file
"""
    required_books(book_list)
    print("Enter the number of a book to mark as completed")
    try:
        num_of_book = int(input(">>>"))
        if book_list[num_of_book][3] == 'c':
            print("That book is already completed")
        else:
            book_list[num_of_book][3] = 'c'
            books_file = open(FILE, 'w')
            for i in book_list:
                for j in i:
                    if j == "r" or j == "c":
                        print(j, end='', file=books_file)
                    else:
                        print(j, end=',', file=books_file)
                print(file=books_file)
            books_file.close()
            print("{} by {} is completed".format(book_list[num_of_book][0], book_list[num_of_book][1]))
    except ValueError:
        print("Invalid input; enter a valid number")
        complete_a_book(book_list)


# After the complete function

def required_books(book_list):
    """
    This function displays the list of books which need to be read
"""
    total_pages = 0
    print("Required Books:")
    count = 0
    count2 = 0
    for i in book_list:
        if 'r' in book_list[count][3]:
            print("{}. {:<50s} by {:<20s} {:>15s} pages".format(count, book_list[count][0], book_list[count][1],
                                                                book_list[count][2]))
            total_pages += int(book_list[count][2])
            count2 = count2 + 1
        count += 1
    if count != 0:
        print("Total pages for {} books: {}".format(count2, total_pages))
    else:
        print("No books")


# end of required_books function

def completed_books(book_list):
    """
    This function is used to print all the completed books
"""
    total_pages = 0
    print("Completed Books:")
    count = 0
    count2 = 0
    for i in book_list:
        if 'c' in book_list[count][3]:
            print("{}. {:<50s} by {:<20s} {:>15s} pages".format(count, book_list[count][0], book_list[count][1],
                                                                book_list[count][2]))
            total_pages += int(book_list[count][2])
            count2 = count2 + 1
        count += 1
    print("Total pages for {} books: {}".format(count2, total_pages))


# end of completed_books function

def add_books():
    """
    This function will help us to add books to the file books.csv
"""
    title = input("Title:")
    while title == "":
        print("Input can not be blank")
        title = input("Title:")
    author = input("Author:")
    while author == "":
        print("Input can not be blank")
        author = input("Author:")
    flag = 0
    pages = 0
    while flag == 0:
        try:
            pages = int(input("Pages: "))
            while pages <= 0:
                print("Number must be >= 0")
                pages = int(input("Pages: "))
            flag = 1
        except ValueError:
            print("Invalid input; enter a valid number")
    print("{} by {}, ({} pages) added to reading list".format(title, author, pages))
    book = [title, author, str(pages), 'r']
    book_list = []
    load_books(book_list)
    book_list.append(book)
    print(book_list)
    books_file = open(FILE, 'w')
    for i in book_list:
        for j in i:
            if j == "r" or j == "c":
                print(j, end='', file=books_file)
            else:
                print(j, end=',', file=books_file)
        print(file=books_file)
    books_file.close()
    return book_list


# end of add_books function

def save_books(books):
    """
    This function will help the program to update data into file books.csv
"""


# end of save book function
main()

'''
'''
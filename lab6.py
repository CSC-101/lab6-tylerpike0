import data
from typing import Optional

# Write your functions for each part in the space below.

# Part 0

# Finds the index of the smallest value in the list, if there are values,
#     starting from the provided index (if in bounds).
# input: a list of integers
# input: a starting index
# returns: index of smallest value as an int or None if no value is found
def index_smallest_from(values:list[int], start:int) -> Optional[int]:
    if start >= len(values) or start < 0:
        return None

    mindex = start
    for idx in range(start + 1, len(values)):
        if values[idx] < values[mindex]:
            mindex = idx

    return mindex


# Sorts, in place, the elements of a list using the selection sort algorithm.
# input: a list of integers
# returns: nothing is returned; the list is sorted in place
#    <This function modifies/mutates the input list. Though a traditional
#     approach, cloning the list sorting the clone is potentially less
#     surprising. Or even using a different sorting algorithm.>
def selection_sort(values:list[int]) -> None:
    for idx in range(len(values) - 1):
        mindex = index_smallest_from(values, idx)
        tmp = values[mindex]
        values[mindex] = values[idx]
        values[idx] = tmp


# Part 1
from data import Book

# takes in a list of books and two bounding indexes, and returns the first alphabetical
# number from that range
# input: list[Book]
# input: int
# input: int
# output: None
def index_alphabetical_first_from(books:list[Book], start:int) -> Optional[int]:
    if start >= len(books) or start < 0:
        return None

    first_index = start
    for idx in range(start + 1, len(books)):
        if books[idx].title < books[first_index].title:
            first_index = idx
    return first_index

# takes in two books, and returns true if the first comes first alphabetically
# input: Book
# input: Book
# output: bool
def alphabetical_ascending(book1: Book, book2: Book) -> bool:
    return book1.title.lower() < book2.title.upper()

# takes in a list of books and sorts it alphabetically by their titles
# input: list[Book]
# output: None
def selection_sort_books(books:list[Book]) -> None:
    for index in range(len(books) - 1):
        alphabetical_first_index = index_alphabetical_first_from(books, index)
        tmp = books[alphabetical_first_index]
        books[alphabetical_first_index] = books[index]
        books[index] = tmp


# Part 2

# takes in a string and returns a string that has the characters, but letters have
# swapped case
# input: str
# output: str
def swap_case(input_string: str) -> str:
    swapped_string = ""
    for character in input_string:
        if character.isalpha():
            if character.islower():
                swapped_string += character.upper()
            else:
                swapped_string += character.lower()
        else:
            swapped_string += character
    return swapped_string


# Part 3

# takes in a string and two characters, and returns a string with all the character of
# the second input, replaced with those of the third
# input = str
# input = str
# input = str
# output = str
def str_translate(input_string: str, old: str, new:str) -> str:
    translated_string = ""
    for character in input_string:
        if character == old:
            translated_string += new
        else:
            translated_string += character

    return translated_string


# Part 4

# takes in a string, and returns a dictionary where each key is a word, with the value being
# the number of times that word appears in the str
# input: str
# output: dict[str: int]
def histogram(input_string:str) -> dict[str: int]:
    word_counts = {}
    for word in input_string.split():
        if word in word_counts.keys():
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    return word_counts

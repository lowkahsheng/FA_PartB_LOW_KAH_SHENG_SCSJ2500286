from library_module import Book

books = {
    "Python 101","Philip Robbins" ,
    "Data Science","Jannah Mohd"
}

#Add a new book from user input
title = input ("Enter book title: ")
author = input ("Enter book author: ")
books=[title,author]

#Save to file
with open("books.txt" , "w") as f:
    for t,a in books.items():
        f.write (f"{t}:{a}\n")

#Read back from file
with open ("books,txt" , "r") as file:
    lines = file.readlines()

print("\nBook List from File:")
for line in lines:
    t, a = line.strip().split(":")
    b= books (t,a)
    b.display_info()
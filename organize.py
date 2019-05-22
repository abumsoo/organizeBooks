#!/usr/bin/env python

import json
import requests

apiSearch = "http://openlibrary.org/search.json?title="

def searchBook(title):
    search = apiSearch + title.replace(' ', '+')
    response = requests.get(search)
    data = response.json()
    docs = data["docs"]

    print(json.dumps(data, indent=4, sort_keys=True))
    latestPub = ''
    for doc in docs:
        # check title matches and there exists a publish year
        titleCurrent = doc["title"].lower()
        if "publish_year" in doc and title.lower() in titleCurrent:
            if latestPub == '':
                latestPub = doc
            elif latestPub["publish_year"] < doc["publish_year"]:
                latestPub = doc

    print()
    print("Title: " + latestPub["title"])
    print("Author: " + latestPub["author_name"][0])
    print("Publication year: " + str(latestPub["publish_year"][0]))
    print()
            
        
def enterBook():
    with open('books', 'a') as f:
        title = input("Enter the title of the book: ")
        f.write(title + '\n')

def delBook():
    with open('books', 'w') as f:
        title = input("Enter the title of the book: ")

def readList():
    with open('books') as f:
        for line in f:
            print(line, end = '')

def main():
    choice = None
    while choice != 'q':
        print("(e)nter a book")
        print("show book (l)ist")
        print("(s)earch for a title")
        print("(q)uit")
        choice = input()
        if choice == 'q':
            break
        elif choice == 'e':
            enterBook()
        elif choice == 'l':
            readList()
        elif choice == 's':
            title = input("Enter a title: ")
            searchBook(title)
        else:
            print("Not a valid option.")


if __name__ == "__main__":
    main()

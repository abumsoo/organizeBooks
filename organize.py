#!/usr/bin/env python

import csv
import json
import requests

apiSearch = "http://openlibrary.org/search.json?title="

def searchBook(title):
    search = apiSearch + title.replace(' ', '+')
    response = requests.get(search)
    data = response.json()
    docs = data["docs"]

    # print(json.dumps(data, indent=4, sort_keys=True))
    latestPub = ''
    for doc in docs:
        # check title matches and there exists a publish year
        titleCurrent = doc["title"].lower()
        if "publish_year" in doc and title.lower() == titleCurrent:
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

def delBook(title):
    current = []
    with open('books') as f:
        for book in f:
            if title not in book:
                current.append([book])
    with open('books', 'w') as f:
        writer = csv.writer(f)
        writer.writerows(current)

def readList():
    with open('books') as f:
        for line in f:
            print(line, end = '')

def main():
    choice = None
    while choice != 'q':
        print("(e)nter a book into your list")
        print("(p)rint your book list")
        print("(s)earch for a title")
        print("(d)elete a title from your list")
        print("(q)uit")
        choice = input()
        if choice == 'q':
            break
        elif choice == 'e':
            enterBook()
        elif choice == 'p':
            readList()
        elif choice == 's':
            title = input("Enter a title: ")
            searchBook(title)
        elif choice == 'd':
            title = input("Enter a title: ")
            delBook(title)
        else:
            print("Not a valid option.")


if __name__ == "__main__":
    main()

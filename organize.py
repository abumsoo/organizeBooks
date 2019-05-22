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
        writer = csv.writer(f)
        title = input("Enter the title of the book: ")
        page = input("Enter the page you are on (optional): ")
        if page != '':
            writer.writerow([title, page])
        else:
            writer.writerow([title, 0])



def delBook(title):
    current = []
    # read in csv into a list excluding the sought title
    with open('books') as f:
        reader = csv.reader(f)
        for line in reader:
            if title != line[0]:
                current.append(line)
    # write the list
    with open('books', 'w') as f:
        writer = csv.writer(f)
        writer.writerows(current)


def readList():
    with open('books') as f:
        reader = csv.reader(f)
        for line in reader:
            print(line[0] + ' - ' + line[1])


def main():
    choice = None
    while choice != 'q':
        print()
        print("(e)nter a book into your list")
        print("(p)rint your book list")
        print("(s)earch for a title")
        print("(d)elete a title from your list")
        print("(q)uit")
        choice = input("> ")
        print()
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

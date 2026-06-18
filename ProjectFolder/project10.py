books=[]
def load_books():
    with open("books.txt","r") as file:
        for line in file:
            line=line.strip()
            data=line.split(",")
            available=data[2]
            available=(available=="True")
            books.append({"title":data[0],"author":data[1],"available":available})
def save_book():
    with open("books.txt","w") as file:
        for book in books:
            title=book["title"]
            author=book["author"]
            available=book["available"]
            file.write(f'{title},{author},{available}\n')
def add_book():
    book_title=input("Enter title: ")
    author=input("Enter author: ")
    available=True
    for book in books:
        if book["title"].title()==book_title.title():
            print("Book already exist in the library!")
            available=False
            break
    else:
        books.append({"title":book_title.title(),"author":author,"available":available})
        print("Book added successfully!\n")
def view_book():
    if not books:
        print("No record found")
    else:
        for book in books:
            title=book["title"]
            author=book["author"]
            if book["available"]==True:
                available="Yes"
            else:
                available="No"
            print(f'{title}\nAuthor:{author}\nAvailable:{available}\n')
def search_book():
    if not books:
        print("No record found")
        return
    else:
        book_title=input("Enter title: ")
        for book in books:
            if book["title"].lower()==book_title.lower():
                title=book["title"]
                author=book["author"]
                if book["available"]==True:
                    available="Yes"
                else:
                    available="No"
                print(f'\nTitle:{title}\nAuthor:{author}\nAvailable:{available}\n')
                break
        else:
            print("Book not available!")
def borrow_book():
    book_name=input("Enter title: ")
    flag=False
    for book in books:
        if book_name.lower() in book["title"].lower():
            flag=True
            if book["available"]==True:
                book["available"]=False
                print("Book borrowed successfully")
                break
            else:
                print("Book is already borrowed")
    if not flag:
        print("Book not available!")
def return_book():
    title=input("Enter title: ")
    flag=False
    for book in books:
        if book["title"].lower()==title.lower():
            flag=True
            if book["available"]==False:
                book["available"]=True
                print("Book returned successfully!")
                break
            else:
                print("Book was never borrowed")
    if not flag:
        print("Book not available!")
def delete_book():
    if not books:
        print("No record found")
    else:
        for i in range(len(books)):
            title=books[i]["title"]
            print(f'{i+1}. {title}')
        number=int(input("Enter number: "))
        for i in range(len(books)):
            if number==i+1:
                del books[i]
                print("Book deleted successfully")
                break
def statistics():
    if not books:
        print("No record found")
        return
    else:
        available_count=0
        borrowed_count=0
        for i in range(len(books)):
            if books[i]["available"]==True:
                available_count+=1
            else:
                borrowed_count+=1
        print(f'Total Books: {len(books)}\nAvailable Books: {available_count}\nBorrowed Books: {borrowed_count}\n')
def show_available_books():
    if not books:
        print("No records found")
        return
    else:
        for book in books:
            if book["available"]==True:
                print(book["title"])
def sort_books():
    if not books:
        print("No record found")
        return
    else:
        sorted_book=sorted(books,key=lambda x:x["title"])
        for book in sorted_book:
            if book["available"]==True:
                available="Yes"
            else:
                available="No"
            print(f'\nTitle: {book["title"]}\nAuthor: {book["author"]}\nAvailable: {available}\n')
menu="\t\t=====Library Management=====\n1. Add Book\n2. View Books\n3. Search Book\n4. Borrow Book\n5. Return Book\n6. Delete Book\n7. Statistics\n8. Show only Available Books\n9. Sort books by Title(A-Z)\n10. Exit\n"
load_books()
while True:
    print(menu)
    choice=input("Enter your choice: ")
    if choice.isdigit():
        if choice=="1":
            add_book()
            save_book()
        elif choice=="2":
            view_book()
        elif choice=="3":
            search_book()
        elif choice=="4":
            borrow_book()
            save_book()
        elif choice=="5":
            return_book()
            save_book()
        elif choice=="6":
            delete_book()
            save_book()
        elif choice=="7":
            statistics()
        elif choice=="8":
            show_available_books()
        elif choice=="9":
            sort_books()
        elif choice=="10":
            break
        else:
            print("Invalid choice")
    else:
        print("The choice must be a digit!")

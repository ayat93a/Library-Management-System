
from datetime import date
import json
import sys


class LMS:
    "doc string"
    lended = 'lended_books.txt'


    def __init__(self , books_list , library_name ):
        self.books_list = 'books_list.txt'
        self.library_name = library_name
        self.books_dict = {}
        self.ID = 101
        # i give the id as agrument and dive it a defult value 
        with open(self.books_list, 'r') as books:
            for _ in self.books_list:
                lines = books.readline().strip()
                # skip the empty line -->
                if not lines.strip():
                    continue
                self.books_dict.update({self.ID: {'book_name' : lines , "lender_name" : ' ' , "issue_date" : ' ' , 'status': 'Available'}})
                self.ID += 1
                with open ('lended_books.txt' , 'w') as lended:
                    lended.write(json.dumps(self.books_dict))

            # print(self.books_dict)
        return 
        
   
    def Display_book(self):
        # i want from yjis fuction --> ID and Book name
        print('**Book ID********************Book Title**********************************Status*************')
        print('                                                                                      ')
        for key in self.books_dict:
                print(key , '>>>>>>>>' ,  self.books_dict[key]['book_name'] , '>>>' , [self.books_dict[key]['status']]) 
                print('______________________________________________________________________________')
                print('                                                                 ')
                # '\t\t' --> space between the strings
        # for key , value in self.books_dict.items():
        #         print (key , value.get('book_name'), "- [", value.get("status"),"]")
                #  ----> get method to access the value 
        
        return  

    def choice(self):
        print('choose another one ?')
        choice = input('y/n  >>>   ')
        if choice == 'y' :
            ll = LMS('books_list.txt' , 'python')
            ll.Issue_books()
        else:
            print(self.books_dict)
            sys.exit() 


    def Issue_books(self):
        book_id = input('Enter the id of the book you want to lend  >>>   ')
        self.issue_date = date.today()
        # how can i add the clock?
        # user input is str , key int --> i cant compare them without convert the user input to int
        for key in self.books_dict:
            if int(book_id) == key and [self.books_dict[key]['status'] == 'Available'] :
                with open ('lended_books.txt' , 'w') as lended_dict :
                    self.books_dict[key]['status'] = 'Unavailable'
                    lended_dict.write(json.dumps(self.books_dict))
                    print(self.books_dict)
                    print('hi')

                        #  i cant use update method in nested loop 'in this case'
            elif book_id == key and [self.books_dict[key]['status'] == 'Unavailable'] :      
                    print (f'sorry this book was lended form {book_id}, you can pick another one')
                    book_id = int(input ('Enter the id of the book you want to lend  >>>   '))
            ll = LMS('books_list.txt' , 'python')
            ll.choice()
        # print(self.books_dict)
        
           
lms = LMS('books_list.txt' , 'python')
lms.Display_book()
lms.Issue_books()
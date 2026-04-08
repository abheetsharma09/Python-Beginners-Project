import json
#LIBRARY SYSTEM
class book_add: #Books class to assing values and add books to the json file
    def __init__(self, book_name , book_author , book_isbn , book_status = "Available") -> None:
        self.book_name = book_name
        self.book_isbn = book_isbn
        self.book_author = book_author
        self.book_status = book_status

    def book_add_to_dic(self): #Add books data to the Dictionary and then to json
        books_dic = {}
        books_dic["Name"] = self.book_name
        books_dic["ISBN."] = self.book_isbn
        books_dic["Author"] = self.book_author
        books_dic["Status"] = self.book_status

        print(books_dic)
        with open("random.json" , "a") as books_data_to_write:
            books_data_to_write.write("\n") #Here it add gaping b/w two dictionaries data
            json.dump(books_dic , books_data_to_write )
            print(f'Books Sucessfully Added to the Library')


#Takes the User Input and Start to call all the function
def user_input_func(user_input):
    if user_input == 0:
        print("Welcome to the Library")
        user_input_book = input("Enter Book Name : ")
        user_input_author = input("Enter Author Name : ")
        user_input_isbn = input("Enter the ISBN Number : ")
        book_add(user_input_book , user_input_author , user_input_isbn).book_add_to_dic()
    elif user_input == 1:
        #Calls the Book issue class and the search method inside it(filtrs the data)
        book_issue().book_issue_search()
    else:
        print("Choose b/w 0 or 1 to continue")

#Books issue search and Update
class book_issue(book_add): #Search the the books from the json file using name and isbn number
    #(Here using inheritence)
    def __init__(self , empty_list = []) -> None:
        self.empty_list = empty_list
        with open("random.json" , "r")as book_data_to_read:
            for data in book_data_to_read:#loops the whole json file 1 by 1
                if data.strip():#ignores line gaps
                    book_data_to_read_dic = json.loads(data) #here it returns data in adictionary formated
                    empty_list.append(book_data_to_read_dic)
                else:
                    pass
    def book_issue_search(self):
        print("Search Book Here")
        user_inp_gate = int(input("Search by Name(0) or ISBN(1) : "))
        if user_inp_gate == 0:
            user_inp_gate_name = input("Enter the Book Name : ")
            for data_empty_list in self.empty_list:
                if data_empty_list["Name"] == user_inp_gate_name:
                    print("------------------------------------")
                    print(f'Book Name : {data_empty_list["Name"]}')
                    print(f'Book ISBN : {data_empty_list["ISBN."]}')
                    print(f'Book Author : {data_empty_list["Author"]}')
                    print(f'Book Status : {data_empty_list["Status"]}')
                    print("------------------------------------")
                    user_inp_gate_A = int(input("Do you want to issue the book?[Yes(0) - No(1)] "))
                    if user_inp_gate_A == 0:
                        if data_empty_list["Status"] == "Available":
                            print("Book now Issued to you")
                            data_empty_list["Status"] = "Issued"
                            print(data_empty_list)
                        else:
                            print("Sorry!! Book not Available")
                    elif user_inp_gate_A == 1:
                        pass
                    else:
                        pass

                else:
                    pass

        elif user_inp_gate == 1:
            user_inp_gate_isbn = input("Enter the ISBN : ")
            for data_empty_list in self.empty_list:
                if data_empty_list["ISBN."] == user_inp_gate_isbn:
                    print("------------------------------------")
                    print(f'Book Name : {data_empty_list["Name"]}')
                    print(f'Book ISBN : {data_empty_list["ISBN."]}')
                    print(f'Book Author : {data_empty_list["Author"]}')
                    print(f'Book Status : {data_empty_list["Status"]}')
                    print("------------------------------------")
                    user_inp_gate_B = int(input("Do you want to issue the book?[Yes(0) - No(1)] "))
                    if user_inp_gate_B == 0:
                        if data_empty_list["Status"] == "Available":
                            print("Book now Issued to you")
                            data_empty_list["Status"] = "Issued"
                            print(data_empty_list)
                        else:
                            print("Sorry!! Book not Available")
                    elif user_inp_gate_B == 1:
                        pass
                    else:
                        pass
                else:
                    pass
        else:
            print("Choose a Valid Operator")


        
user_input = int(input("What you want to Perform - Add Books(0) or Issue Books(1)? ") ) #Main Gate to the System
user_input_func(user_input)#Main functions which control all the Classes 

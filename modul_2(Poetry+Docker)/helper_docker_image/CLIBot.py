from AddressBook import *
from BotInterface import ABCInterface

class CLIBot(ABCInterface):
    def __init__(self):
        self.book = AddressBook()

    
    def input_error(func):
        def inner(*args):
            try:
                return func(*args)
            except (KeyError, ValueError, IndexError, TypeError, FileNotFoundError) as err:
                print( f'Error: {err}')
        return inner
    
    @input_error
    def add(self):
        name = Name(input("Name: ")).value.strip()
        phones = Phone().value
        birth = Birthday().value
        email = Email().value.strip()
        status = Status().value.strip()
        note = Note(input("Note: ")).value
        record = Record(name, phones, birth, email, status, note)
        return self.book.add(record)
    
    @input_error
    def search(self):
        print("There are following categories: \nName \nPhones \nBirthday \nEmail \nStatus \nNote")
        category = input('Search category: ')
        pattern = input('Search pattern: ')
        result = (self.book.search(pattern, category))
        for account in result:
            if account['birthday']:
                birth = account['birthday'].strftime("%d/%m/%Y")
                result = "_" * 50 + "\n" + f"Name: {account['name']} \nPhones: {', '.join(account['phones'])} \nBirthday: {birth} \nEmail: {account['email']} \nStatus: {account['status']} \nNote: {account['note']}\n" + "_" * 50
                print(result)

    @input_error
    def edit(self):
        contact_name = input('Contact name: ')
        parameter = input('Which parameter to edit(name, phones, birthday, status, email, note): ').strip()
        new_value = input("New Value: ")
        return self.book.edit(contact_name, parameter, new_value)

    @input_error
    def remove(self):
        pattern = input("Remove (contact name or phone): ")
        return self.book.remove(pattern)

    @input_error
    def save(self):
        file_name = input("File name: ")
        return self.book.save(file_name)

    @input_error
    def load(self):
        file_name = input("File name: ")
        return self.book.load(file_name)
    
    @input_error
    def congratulate(self):
        print(self.book.congratulate())
    
    @input_error
    def view(self):
        print(self.book)

    
    @input_error
    def exit(self):
        exit()

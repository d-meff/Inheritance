class Person:
    def __init__(self, name, address, telephone_num):
        self.__name = name
        self.__address = address
        self.__telephone_num = telephone_num

    def print_person(self):
        print("Name: " + self.__name)
        print("Addy: " + self.__address)
        print("Phone Number: " + self.__telephone_num)

    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_telephone_number(self):
        return self.__telephone_num

class Customer(Person):
    def __init__(self, customer_number, name, address, telephone_num, mailing_list):

        Person.__init__(self, name, address, telephone_num)

        self.__customer_number = customer_number
        self.__mailing_list = mailing_list

    def print_person(self):
        print(f'''Name: {Person.get_name(self)}
        Address: {Person.get_address(self)}
        Phone Num: {Person.get_telephone_number(self)}
        Mailing List: {self.__mailing_list}
        Customer Number: {self.__customer_number}''')

        print()

        Person.print_person(self)

    
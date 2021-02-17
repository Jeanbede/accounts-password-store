import random
import string


users = list()
credentials = list()

"""
declared two empty lists to store data
"""

class Credentials:
    
    def __init__(self, account_name, username, password):
        self.account_name = account_name
        self.username = username
        self.password = password

        """
        Created the class credential-details and initialized using the self keyword
        """
    def my_credentials():
        print("Choose among the  options below to continue")
        print("\n1. Create new credential-details \n2. Store credential-details of existing accounts \n3. View existing credential-details \n4. Logout")
        credentials_option = input()
        if credentials_option == "1":
            print("Do you want system generated password?")
            option = input("\n1. Yes \n2. No")
            if option == "1":
                pwd =Users.random_password(10)
                acc
        
            elif option == "2":
                account1 = Credentials(account_name = input("Account Name (e.g. facebook): "), username = input("Username: "), password = input("Password: "))
                credentials.append(account1)
               
                Users.view_credentials()
                Users.delete()
            else:
                print("Invalid input")
                Credentials.my_credentials()

        elif credentials_option == "2":
            account1 = Credentials(account_name = input("Account Name (e.g. Twitter): "), username = input("Username: "), password = input("Password: "))
            credentials.append(account1)
            Users.view_credentials()
            Users.delete()                  
            
        elif credentials_option == "3":
            Users.view_credentials()


class Users:

    def __init__(self, username, password):

        self.username = username
        self.password = password

        """
        Created class users and initialized using the self keyword
        """

    def login():
        print("Put your credential-details to login")
        username = input("Username: ")
        password = input("Password: ")

        for x in users:
            if x.username == username and x.password == password:
                print("Login successful")
                Credentials.my_credentials()
            else:
                pass    

    def view_credentials():
        print("choose among of the options below to view your credential-details:")
        print("\n1. Yes \n2. No")
        viewers_choice = input()
        if viewers_choice == "1":
            for x in credentials:
                print("Account: " + x.account_name,"Username: " + x.username,"Password: " + x.password)
        elif viewers_choice == "2":
            print("Thanks for check in!")
            Users.login()
        else:
            print("invalid choice")

    def delete():
        print("Do you want to delete credential-details?")
        print("\n1. Yes \n2. No")
        delete_option = input()
        if delete_option == "1":
            credentials.clear()
            print("You have deleted credential-details from the list")
        elif delete_option == "2":
            print("your credential-details are stored in the application")
        else:
            print("Invalid input.")
            delete() 

    def passwordGenerate(stringLength=8):
        """
        method that generate a random password
        """
        password = string.ascii_lowercase + string.ascii_uppercase + "~!@#$%;:^&*"
        return ''.join(random.choice(password) for i in range(int(stringLength)))  



class Main:

    user1 = Users("user", "1234")
    users.append(user1)
    def create_account():
        print("Kindly input your username and password to proceed")
        user1 = Users(input("Username: "), input("Password: "))
        users.append(user1)
        print("Account has been created successfully.")
        print("select 1 to login and 2 to exit")
        option = input()
        if option == "1":
            Users.login()
        else:
            Main.create_account ()  

    """
    Created a create account method that calls the login functiong
    """

    def main():

        print("Hello, welcome to Password Store Account.Choose one of the below options to proceed:")
        print("\n1. Login \n2. Create new account \n3. Exit")
        user_option = input()

        if user_option == "1":
            Users.login()
        elif user_option == "2":
            Main.create_account()
        elif user_option == "3":
            exit()
        else:
            print("Invalid option")

if __name__ == '__main__':
    Main.main()            
                    
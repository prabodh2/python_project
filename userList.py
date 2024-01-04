from  packages.userSchema import User

class UserList:

    users = []

    def signup(self):
        name = input("Enter your name : ")
        Email = input("Enter your Email : ")
        password = input("Enter a password : ")
        isAdmin = int(input("Are you 1.admin or 2.user : "))
        uid = len(UserList.users) + 1

        TempUser=User(uid,name,isAdmin, Email, password)
        UserList.users.append(TempUser)
        print("User created successfully!!!")
        return 1

    def signin(self):
        name=input("Enter your name : ")
        password=input("Enter your password : ")
        # print(UserList.users)
        for i in UserList.users:
            # print(i)
            print(i.name, i.getPassword())
            if i.name == name and i.getPassword() == password:
                print("Welcome!!!")
                return i
        else:
            print("Incorrect Username and Password, Sign Up if you dont have an account")
            return 0
    
    def displayUsers(self):
        if len(UserList.users):
            for i in UserList.users:
                i.display()
        else:
            print("No Users to display")
from packages.userList import UserList
from packages.productList import ProductList

users = UserList()
products = ProductList()

user = ""

def logout():
    global user
    user = None

def login():
    user = UserList.signin()
    return user if user else None

def authUser():
    print("1- Login")
    print("2- Sigup")
    print("0- exit")
    choice = int(input("Select: "))
    if (choice == 0):
        print("Exiting...")
        return 0
    elif (choice == 1):
        print("Login")
        user = users.signin()
        print(user)
        return user if user else None
    elif (choice == 2):
        users.signup()
        return users.signin()
    else:
        print("Invalid Reponse!!!")
        return None

def adminPanal():
    print("Admin Panal")
    print("1- Create a new Product")
    print("2- Update a Product")
    print("3- Display All Products")
    print("4- Log Out")
    print("0- Exit")
    choice = int(input("Select: "))
    if (choice == 0):
        print("Exiting...")
        return 0
    elif (choice == 1):
        print("Create a new Product")
        products.createProduct(user.isAdmin)
    elif (choice == 2):
        print("Update a Product")
        pid = int(input("Enter the Product ID: "))
        response = products.updateProduct(user.isAdmin, pid)
        while (not response):
            response = products.updateProduct(user.isAdmin)
    elif (choice == 3):
        products.displayProducts()
    elif (choice == 4):
        logout()
    else:
        print("Invalid Reponse!!!")
        return None
    return 1

def userPanal():
    print("User Panal")
    print("1- Display All Products")
    print("2- Log out")
    print("0- Exit")
    choice = int(input("Select: "))
    if (choice == 0):
        print("Exiting...")
        return 0
    elif (choice == 1):
        products.displayProducts()
    elif (choice == 4):
        logout()
    else:
        print("Invalid Reponse!!!")
        return None

def main():
    toggle = 1
    global user
    user = None

    while (toggle):
        print("Select an option...")
        if (not user):
            response = authUser()
            if (response == 0):
                toggle = 0
                break
            elif (response == None):
                user = None
                toggle = 1
                continue
            user = response
            print("Used Login Sucessfully!!!")
        else:
            print(f"Hello {user.name}")
            
            response = adminPanal() if user.isAdmin else userPanal()
            if (response == 0):
                toggle = 0
                break
            elif (response == None):
                toggle = 1
                continue

if __name__ == "__main__":
    main()

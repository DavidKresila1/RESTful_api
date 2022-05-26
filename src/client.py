import requests

baseUrl = "http://127.0.0.1:5000/"

print("_________________Client side for API________________________")

def help():
    print("______________________Help___________________")
    print("Commands:")
    print("Search user by id:   id user search")
    print("Search user by userId:   user search by userid")
    print("Search post by id:   post search by id")
    print("Post search by userId:   post search by userid")
    print("Add new post:   add")
    print("Delete post:   delete")
    print("End client app:   exit")
    onStart()

def postSearchByUserId():
    print("Please enter userId value")
    userId = input("Enter userId: ")
    response = requests.get(baseUrl + f"/searchPostByUserId/{userId}")
    print(response.json())
    print("\nDo you want to continue to search?\n If not enter no\n if yes enter yes.")
    cont = input("Input answser: ")
    if cont == "yes":
        searchById()
    elif cont == "no":
        onStart()
    else:
        print("Invalid input")
        postSearchByUserId()


def postSearchById():
    print("Please enter id value")
    postId = input("Enter id: ")
    response = requests.get(baseUrl + f"/searchPostById/{postId}")
    print(response.json())
    print("\nDo you want to continue to search?\n If not enter no\n if yes enter yes.")
    cont = input("Input answser: ")
    if cont == "yes":
        searchById()
    elif cont == "no":
        onStart()
    else:
        print("Invalid input")
        postSearchById()


def searchById():
    print("Please enter id value")
    id = input("Enter id: ")
    response = requests.get(baseUrl + f"/idSearch/{id}")
    print(response.json())
    print("\nDo you want to continue to search?\n If not enter no\n if yes enter yes.")
    cont = input("Input answser: ")
    if cont == "yes":
        searchById()
    elif cont == "no":
        onStart()
    else:
        print("Invalid input")
        searchById()


def searchByUserId():
    print("Please enter userId value")
    userId = input("Enter id: ")
    response = requests.get(baseUrl + f"//userIdSearch/?={userId}")
    print(response.json())
    print("\nDo you want to continue to search?\n If not enter no\n if yes enter yes.")
    cont = input("Input answser: ")
    if cont == "yes":
        searchByUserId()
    elif cont == "no":
        onStart()
    else:
        print("Invalid input")
        searchByUserId()


def addToJson():
    global userId
    print("Please enter value")
    userId = int(input("Enter userid: "))
    title = input("Enter title: ")
    body = input("Enter body: ")
    response = requests.patch(baseUrl + f"/update/user/{userId}/{title}/{body}")
    print(response.json())
    print("\nDo you want to continue to search?\n If not enter no\n if yes enter yes.")
    cont = input("Input answser: ")
    if cont == "yes":
        addToJson()
    elif cont == "no":
        onStart()
    else:
        print("Invalid input")
        searchByUserId()

def delete():
    print("Please enter postId value")
    id = input("Enter id: ")
    response = requests.delete(baseUrl + f"//userIdSearch/?={id}")
    print(response.json())
    print("\nDo you want to continue to search?\n If not enter no\n if yes enter yes.")
    cont = input("Input answser: ")
    if cont == "yes":
        searchByUserId()
    elif cont == "no":
        onStart()
    else:
        print("Invalid input")
        searchByUserId()


def onStart():
    print("Enter command, if you need help type --help or read manual")
    command = input("Enter command: ")
    if command == "id user search":
        searchById()
    elif command == "user search by userid":
        searchByUserId()
    elif command == "post search by id":
        postSearchById()
    elif command == "add":
        addToJson()
    elif command == "post search by userid":
        postSearchByUserId()
    elif command == "delete":
        delete()
    elif command == "exit":
        exit()
    elif command == "--help":
        help()
    else:
        onStart()


onStart()

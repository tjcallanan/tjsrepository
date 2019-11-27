def main():
    loop()
#here i set the range of attempts
def loop():
    username = "bank_admin"
    password = "Hytu76E"

    for i in range (3, 0, -1):
        attempt = input("Username: ")
        attempt_password = input("Password: ")
        if attempt == username and attempt_password == password:
            break
        else:
            if(i >1):
                print("Incorrect username and/or password. Please try again.")

                


    #these are the two possible final outcomes
    if(i ==1):
        print("You have been denied access. SECURITY ALERT: 0 ATTEMPS REMAINING.")
    else:
        print("Access granted.")
main()


while True:
    password = "1234"
    guess = input("Enter a 4-digit password: ")
    
    if guess == password:
        print("Congratulations, you guessed the password correctly!")
        break
    else:
        print("Incorrect password. Please try again.")

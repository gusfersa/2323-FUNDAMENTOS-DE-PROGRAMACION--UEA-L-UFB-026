# Example: Password Verification using a do-while loop
correct_password = "mysecretpassword"
entered_password = ""
attempts = 0

print("Welcome to the Password Verification Program!")

while True:
    entered_password = input("Enter your password: ")
    attempts += 1
    if entered_password == correct_password:
        print(f"Password verified in {attempts} attemtps. Access granted!")
        break
    else:
        print("Incorrect password. Please try again.")

print("Program ended.")
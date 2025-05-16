# Get the student's age
age = int(input("Enter the student's age: "))

# Outer condition to check minimum age
if age >= 10:
    # Nested condition to check maximum age
    if age <= 20:
        print("You are eligible to enroll in Raj's class.")
    else:
        print("You are too old to enroll in Raj's class.")
else:
    print("You are too young to enroll in Raj's class.")

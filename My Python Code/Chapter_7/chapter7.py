full_name = input("What is your name? ")

print(f"Hello {full_name}")

full_name += input("What is your last name?")

print(f"Hello {full_name}")

age = input("How old are you? ")

if int(age) < 18:
    print("have a beer")
elif int(age) < 18:
    print("Not today")
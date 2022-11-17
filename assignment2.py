def blank_check(check):
    while check == '':
        check = input("Please enter the required information: ")
    else:
        return check



name = input("what is your name?: ")
name = blank_check(name)
print(f"Ok, {name}! Let's gather a few more details about your stay: ")
conf_id = input("what is your conference ID?: ")
conf_id = blank_check(conf_id)
org = input("what organization do you represent?: ")
org = blank_check(org)
email = input("what is your email address?: ")
email = blank_check(email)
food = input("any food preferences?: ")
food = blank_check(food)

classes = ("Python for beginners", "Database development with Python",
           "Python for data science", "Advanced Python for application developers")
answers = []
for x in classes:
    print(f"{name},Would you like to attend", x, "Y/N?")
    response = input()
    while response.lower() not in ('y', 'n'):
        response = input("please only enter a Y for yes of a N for no: ")
    answers.append(response)
    if response.lower() == 'y':
        print("ok, i've reserved you a seat!")
    else:
        print("ok, maybe some other time!")
print(f"ok {name}, we have your responses listed as follows:")
for i, j in zip(classes, answers):
    print(i, j)
count = 0
for i in answers:
    if i.lower() == 'y':
        break
    elif i.lower() == 'n':
        count += 1
if count == len(answers):
    print("you're going to be bored!")

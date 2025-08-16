# for loop არის ციკლი, რომელიც გამოიყენება რაღაც ციკლური ოპერაციების გასაკეთებლად


number = int(input("enter number:"))
if number > 0: 
    print("number is positive")
elif number < 0:
    print("number is negative")
else:
    print("number is zero")


number1 = int(input("enter number:"))
if number1 % 2 == 0:
    print("რიცხვი არის ლუწი")
else:
    print("რიცხვი არის კენტი")


score = int(input("enter score of exam:"))
if score == 100:
    print("მალადეს")
elif score < 50:
    print("ვერ ჩააბარე")
else:
    print("შემოიტანეთ სწორი ქულა")
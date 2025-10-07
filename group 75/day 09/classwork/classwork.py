money = 10
payment = input("დაწერე რამდენის გადახდა გსურს: ")
if payment == "5":
    print("შენ იყიდე ვაშლი")
elif payment == "2":
    print("შენ იყიდე მსხალი")
elif int(payment) > money:
    print("შენ არ გაქვს საკმარისი თანხა ანგარიშზე!")
else:
    print("შენ იყიდე რაღაც")
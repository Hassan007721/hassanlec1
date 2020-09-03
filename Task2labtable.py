# printing table using while loop
print("--------------------------------------")
print("table using while loop")
print("------------------------------------------")
table = 8
i = 1
while i <=10:
    x = table * i
    print(table, " * " ,i, " = ",x,)
    i +=1
print("-----------------------------------\n")
print("table using for loop")

# table with for loop
table = 5
for i in range (1,11):
    x=table*i
    print(table, "*" ,i, "=" ,x,)
    i+=1

account = { "moni123" : "moni180505" , "sanjay123" : "Sanjay@123" , "vishal234" : "Vishal#1234"}

print("Welcome to The page !!!!")

attempts =  3 

# for...else loop
#The else block executes only when the loop finishes normally without executing break

for i in range(attempts,0,-1):

   
    username = input("Enter the username : ")
    password =input ("Enter the passowrd : ")

    if username in account and  account[username] == password :
        print("Successfully Loggged in")
        break;

    else :
        print(f"There is only {i-1} attemps left ")
else:
    print("You have exceeded all the attempts")
    print("Account is loccked")




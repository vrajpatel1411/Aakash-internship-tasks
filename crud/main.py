def password():
    MAX_LEN = 10
    DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] 
    LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                     'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                     'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                     'z']
 
    UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                     'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q',
                     'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                     'Z']
 
    

    COMBINED_LIST = DIGITS + UPCASE_CHARACTERS + LOCASE_CHARACTERS 
 

    rand_digit = random.choice(DIGITS)
    rand_upper = random.choice(UPCASE_CHARACTERS)
    rand_lower = random.choice(LOCASE_CHARACTERS)

 
    temp_pass = rand_digit + rand_upper + rand_lower
 
 
    for x in range(MAX_LEN - 4):
        temp_pass = temp_pass + random.choice(COMBINED_LIST)
        temp_pass_list = array.array('u', temp_pass)
        random.shuffle(temp_pass_list)
 
    password = ""
    for x in temp_pass_list:
        password = password + x
    return password





def create(option,mydb):
    mycursor=mydb.cursor()

    print("Welcome to Vraj Patel Bank")
    print("Please fill up your details to create your account in our bank and pls provide ")
    name=input("Enter your name=>")
    mobile_number=int(input("enter your mobile number=>"))
    email=input("enter your email address=>")
    address=input("enter your home address=>")
    user_id=random.randint(0000000000,9999999999)
    login_id=input("Create your login id=>")

    user_sql="insert into users (user_id,user_name,mobile_number,email,address) values (%s,%s,%s,%s,%s)"
    user_var=(user_id,name,mobile_number,email,address)
    mycursor.execute(user_sql,user_var)
    mydb.commit()
    user_password=password()

    banking_sql="insert into banking1(user_id,user_name,mobile_number,login_id,password) values(%s,%s,%s,%s,%s)"
   
    banking_var=(user_id,name,mobile_number,login_id,user_password)
    mycursor.execute(banking_sql,banking_var)
    mydb.commit()
    
    print("To open account your account you have to deposit money")
    user_balance=int(input("enter minimum balance=>"))
    balance_sql="insert into balance_details(user_id,login_id,balance) values (%s,%s,%s)"
    balance_var=(user_id,login_id,user_balance)
    mycursor.execute(balance_sql,balance_var)
    mydb.commit()
    
    print("Your account is created successfully")
    sql="SELECT user_id,user_name,login_id,password FROM banking1 where user_id={}".format(user_id)

    
    mycursor.execute(sql)
    myresult = mycursor.fetchone()
    print("User id=>",myresult[0])
    print("USer name=>",myresult[1])
    print("Login_id=>",myresult[2])
    print("Password=>",myresult[3])
       



def check_balance(mydb):
    
    print("Welcome to Vraj Patel Bank")
    login_id=input("Enter your login id=>")
    password=input("Enter your password=>")
    mycursor=mydb.cursor()
    sql="select balance from balance_details inner join banking1 on balance_details.login_id=banking1.login_id where balance_details.login_id=%s and banking1.password=%s" 
    mycursor.execute(sql,(login_id,password,))
    myresult = mycursor.fetchone()
    if myresult is None:
        print("you have enter wrong Id and Password")
    else:
        for x in myresult:
            print(x) 
 
def Deposit_money(mydb):
    print("Welcome to Vraj Patel Bank")
    login_id=input("Enter your login id=>")
    password=input("Enter your password=>")
    mycursor=mydb.cursor()
    sql="select balance from balance_details inner join banking1 on balance_details.login_id=banking1.login_id where balance_details.login_id=%s and banking1.password=%s" 
    mycursor.execute(sql,(login_id,password,))
    myresult = mycursor.fetchone()
    if myresult is None:
        print("you have enter wrong Id and Password")
    else:
        amount=int(input("Enter the amount you want to deposit=>"))
        sql="select balance from balance_details inner join banking1 on balance_details.login_id=banking1.login_id where balance_details.login_id=%s and banking1.password=%s" 
        mycursor.execute(sql,(login_id,password,))
        myresult = mycursor.fetchone()
        for x in myresult:
            amount=amount+x     
        sql="update balance_details set balance=%s where login_id=%s"
        var=(amount,login_id)
        mycursor.execute(sql,var)
        mydb.commit()
        print(mycursor.rowcount, "record(s) affected")








import mysql.connector
import random
import array

mydb=mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="vraj1411",
    database="Banking"
    )
        
print("1. Create account")
print("2. Check balance")
print("3. Deposit Money")
print("4. Send money")
print("5. Show Transcation")
print("6. Withdraws")


option=int(input())


if option==1:
    create(option,mydb)

elif option==2:
    check_balance(mydb)
    
elif option==3:
    Deposit_money(mydb)
    

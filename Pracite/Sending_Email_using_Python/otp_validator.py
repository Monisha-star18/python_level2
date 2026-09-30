import secrets
import smtplib
import re
from email.message import EmailMessage


from config import get_password

is_ValidEmail = False

#the regex for the email
email_pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"

#input from user 
receivers_email_id :str  = input("Enter the Email id to get otp : ")

if re.match(email_pattern , receivers_email_id) :
    is_ValidEmail = True

if is_ValidEmail : 
    
    # Python's secrets module is specifically designed for cryptographically secure random values.
    # the randombelow is a function pick a random value as mentioned and also it dont include the mention value 

    def generate_otp() -> str:
        return f"{secrets.randbelow(1_000_000):06d}" # either 10**6 or 1_000_000 both are same 


    SENDERS_EMAIL_ID = "monisha.r180505@gmail.com"
    SENDERS_APP_PASSWORD = get_password()

    #create the server 
    with smtplib.SMTP("smtp.gmail.com",587) as server:

        #the server is been created with the tls 
        server.starttls()

        #set the server by login by the sender email and app passowrd 
        if not SENDERS_EMAIL_ID and SENDERS_APP_PASSWORD :
            print("The senders email or the app password is missing")
            
        else :
            server.login(SENDERS_EMAIL_ID,SENDERS_APP_PASSWORD)

            #the mail formate 
            email_message  = EmailMessage()

            email_message['Subject'] = "OTP verification code for Login "
            email_message['From'] = SENDERS_EMAIL_ID
            email_message['To'] = receivers_email_id
            email_message.set_content("Your Otp is : " + generate_otp())

            #send the mail
            server.send_message(email_message)

            print("Email is sent")




        


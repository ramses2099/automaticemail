import os
from dotenv import load_dotenv
import csv
from email.message import EmailMessage
import ssl
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
load_dotenv()

#load environment variables
ENV_PASSWORD = os.getenv('ENV_PASSWORD') 
ENV_SENDER = os.getenv('ENV_SENDER')

BODY ="""
Dear [Hiring Manager],

I hope this message finds you well. I am reaching out to express my interest in potential job opportunities as fullstack development. 
With my skills and experience, I am excited to explore how I might contribute to Companies innovative projects.

Please find my CV attached for your review. I would be grateful for the chance. I am available at your convenience and can be reached via email at ramses2099@gmail.com or by phone at (519) 590-8503.

Thank you very much for considering my CV. 

Warm regards,
Jose Encarnacion

"""


def sendemail(arr:list)->None:    
    # Subject and body of the email
    subject = "Cv-Jose Encarnacion"
    dear = f"{arr[1]} - {arr[2]} - {arr[3]}"
    body = BODY.replace("[Hiring Manager]" , dear),  
    
    # Set up the MIME
    message = MIMEMultipart()
  
    message["From"] = ENV_SENDER
    message["To"] = arr[5]
    message["Subject"] = subject
    message.attach(MIMEText(body[0], "plain"))
           
    # File to be attached
    filename = "CV-Jose_Encarnacion.pdf"  # Name of the file with extension
    filepath = "CV-Jose_Encarnacion.pdf"

    # Open the file in binary mode
    part = MIMEBase("application", "octet-stream")
    
    with open(filepath, "rb") as attachment:
        # MIMEBase is used to encapsulate the file data
        part.set_payload(attachment.read())

    # Encode file to ASCII characters for email transfer
    encoders.encode_base64(part)

    # Add header to the attachment part
    part.add_header("Content-Disposition", f"attachment; filename= {filename}")

    # Attach the file to the email message
    message.attach(part)
    
    context = ssl.create_default_context()
    # Connect to the Gmail server (you can replace it with your SMTP server)
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(ENV_SENDER, ENV_PASSWORD)  # Login to the email server
            print("Connected to the email server!")  # Confirm connection
            print(f"Sending email to {arr[5]}" ) # Send
            server.sendmail(ENV_SENDER, arr[5], message.as_string())  # Send the email
            print("Email sent successfully!")
    except Exception as e:
        print(f"Error: {e}")
      
def main() -> None:
    os.system("cls")
        
    arr =[1,'Ahmad Olia','Founder- Technical Recruitment','MeshGrid HR','https://www.linkedin.com/in/ahmad-olia/',
          'glenis.jerez17@gmail.com','(647) 949-4762','Toronto, ON']
    
    sendemail(arr)
    
    # with open('data.csv', mode ='r')as file:
    #     csvFile = csv.reader(file)
    #     for lines in csvFile:
    #         print(lines)
            




if __name__ == "__main__":
    main()
    
    
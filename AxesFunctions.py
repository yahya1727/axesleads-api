import smtplib
import re
from email.message import EmailMessage

axes_info = {
    "email":"axesleads@gmail.com",
    "password":"djubcqjjxrzpxykm"
}

customer_info = {
      "email":"axesfeedbackcustomer@gmail.com",
      "password":"vxghinsgbjsfciss"
}

regex = "^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"
 
def EmailVaildOrNotValid(email):
    if(re.search(regex, email)):
        return True
    else:
        return False

def validateForm(data:dict):
    name = len(data["uname"])
    email = len(data["uemail"])
    subject = len(data["usubject"])
    body = len(data["body"])

    if name == 0 or email == 0 or subject == 0 or body == 0:
        return False
    else:
        return True



def SendMailToAxes(userdetails:dict):
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(str(customer_info["email"]), str(customer_info["password"]))
        email = EmailMessage()
        email["From"] = str(customer_info["email"])
        email["To"] = str(axes_info["email"])
        email["Subject"] = "{}'s Customer Feedback".format(str(userdetails["uname"]))
        msg = '''
        Dear AxesLeads,

        Subject: {}
        
        Message: {}

        Regards,
        {}
        Customer
        {}
        '''.format(str(userdetails["usubject"]), str(userdetails["body"]), str(userdetails["uname"]), str(userdetails["uemail"]))
        email.set_content(msg)
        server.send_message(email)
    except Exception as e:
         print(e)
         return False
    finally:
        server.quit()
        return True

def SendMailToCustomer(userdata:dict):
    try:
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            validation = validateForm(userdata)
            if validation == True:
                email_valid = EmailVaildOrNotValid(str(userdata["uemail"]))
                if email_valid == True:
                    customer = userdata
                    sendmailto_axes = SendMailToAxes(customer)
                    if sendmailto_axes == True:
                        server.login(str(axes_info["email"]), str(axes_info["password"]))
                        from_addr = str(axes_info["email"])
                        to_addr = str(userdata["uemail"])
                        subject = "Grateful for Your Inquiry & Exclusive Offer Inside!"
                        msg = '''
                    Dear {},

                    I hope this email finds you well! I wanted to take a moment to express my sincerest gratitude for reaching out to us at AxesLeads. Your interest and trust in our services mean a great deal to us.

                    At AxesLeads, we understand the importance of reliable and accurate data to drive your business forward. With our extensive expertise and cutting-edge technology, we have helped countless businesses like yours unlock their full potential by providing high-quality B2B data solutions. We are thrilled that you have chosen to explore how we can assist you in achieving your goals.

                    To show our appreciation and to help you experience the exceptional value of our services, we would like to extend an exclusive offer to you. We are offering 6 free data solutions every first-time of a client's service.

                    What specific industries and the approximate amount of data are typically required for your business? This information will help us determine the scope and discuss further details.

                    Don't miss out on this exclusive offer! 
                    
                    Wishing you continued success in your endeavors.

                    We are excited to hear from you soon.

                    Warm regards,

                    Mohammad Faiz
                    Business Development Executive(BDE)
                    AxesLeads
                        '''.format(str(customer["uname"]))
                        email = EmailMessage()
                        email["From"] = from_addr
                        email["To"] = to_addr
                        email["Subject"] = subject
                        email.set_content(msg)
                        server.send_message(email)
                        return "Your Message Has Been Sent Successfully. You Will Be Notified Via Mail By Our Team. Have A Great Day!"
                    else:
                        print(sendmailto_axes)
                        return "Oops, Server Down! Try Again Later..."
                else:
                    return "Please Enter A Valid Email!"
            else:
                 return "Please Fill All The Fields!"
    except Exception as e:
          print(e)
          return "Oops, Server Error!"
    finally:
         server.quit()
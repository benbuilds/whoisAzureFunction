import datetime
import logging
import smtplib
import whois

import azure.functions as func

#declare variables
lastUpdateDate = '2020-04-07T10:55:06.807Z'

def getDomainInfo():
    print('Collecting whois info...')
    w = whois.whois("google.com") #TODO change 'google.com' to the domain name you want to check
    w.expiration_date  # dates converted to datetime object
    datetime.datetime(2013, 6, 26, 0, 0)
    w.text  # the content downloaded from whois server
    return w

def sendUpdateEmail(w):
    FROM = 'fromaddress' #TODO which address to send updates from
    TO = 'toaddress' #TODO which address to send updates to
    SUBJECT = "Update on domain availability"

    USERNAME= 'youremail@youremail.com' #TODO login/email info for 'from' address
    PASSWORD = 'youemailpassword' #TODO login password for 'from' address

    print("Preparing message...\n")
    msg = "\r\n".join([
    "From: " + FROM,
    "To: " + TO,
    "Subject: " + SUBJECT,
    "",
    "\n*****Domain Update: *****\n\n" + w.text
    ])

    print("Sending message... \n" + msg)
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(USERNAME, PASSWORD)
    server.sendmail(FROM, TO, msg)
    server.quit()
    print('SUCCESS: Message Sent...')

def main(mytimer: func.TimerRequest) -> None:
    utc_timestamp = datetime.datetime.utcnow().replace(
        tzinfo=datetime.timezone.utc).isoformat()

    if mytimer.past_due:
        logging.info('The timer is past due!')

    #get the Domain info from the DNS Server
    w = getDomainInfo()

    #check if there has been an update in the Domain record
    if lastUpdateDate not in w.text:
        print("Update found! Sending notification...")
        sendUpdateEmail(w)
    else:
        print('No Update. Last Status... \n\n' + w.text)

    logging.info('Python timer trigger function ran at %s', utc_timestamp)

import smtplib
from email.mime.text import MIMEText


def send_mail(customer, service, rating, comments):
    port = 2525
    smtp_server = 'smtp.mailtrap.io'
    login = 'Insert your username'
    password = 'Insert your password'
    message = f"<h3>New Feedback Submission</h3><ul><li>Customer: {customer}</li><li>Service: {service}</li><li>Rating: {rating}</li><li>Comments: {comments}</li></ul>"

    sender_email = 'Insert your email 1'
    receiver_email = 'Insert your email 2'
    msg = MIMEText(message, 'html')
    msg['Subject'] = 'Feedback'
    msg['From'] = sender_email
    msg['To'] = receiver_email

    # Send email
    with smtplib.SMTP(smtp_server, port) as server:
        server.login(login, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
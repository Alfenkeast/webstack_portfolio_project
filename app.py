from flask import Flask, request, render_template
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

app = Flask(__name__)
app = Flask(__name__, static_url_path='/static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_email', methods=['POST'])
def send_email():
    location = request.form.get('location')
    date = request.form.get('date')

    # Gmail configuration
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    sender_email = 'g44892950@gmail.com'  
    sender_password = 'aykx uhmk ytji fjuo'  
    receiver_email = 'alfenkeast@gmail.com'  

    try:
        # Creating a connection to the SMTP server
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)

        # Compose the email
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = 'Booking Information'

        # Email body
        body = f'Location: {location}\nDate: {date}'
        msg.attach(MIMEText(body, 'plain'))

        # Send the email
        server.sendmail(sender_email, receiver_email, msg.as_string())

        # Close the server
        server.quit()

        return 'Email sent successfully!'
    except Exception as e:
        return f'Error: {str(e)}'
    

if __name__ == '__main__':
    app.run(debug=True)

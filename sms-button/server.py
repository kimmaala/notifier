import smtplib
from email.message import EmailMessage
from flask import Flask
from flask_cors import CORS

GMAIL_ADDRESS = "pixiee1dust@gmail.com"
APP_PASSWORD = "uwhxrzncjjwbvqvk"
SEND_TO = "kimverlynmaala@gmail.com"

app = Flask(__name__)
CORS(app)

@app.route("/send", methods=["POST"])
def send():
    try:
        msg = EmailMessage()
        msg["Subject"] = "Button Alert"
        msg["From"] = GMAIL_ADDRESS
        msg["To"] = SEND_TO
        msg.set_content("The button was clicked!")

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(GMAIL_ADDRESS, APP_PASSWORD.replace(" ", ""))
            smtp.send_message(msg)
        return {"ok": True}
    except Exception as e:
        return {"ok": False, "error": str(e)}, 500

app.run(port=5000)
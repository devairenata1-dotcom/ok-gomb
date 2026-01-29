import smtplib
from email.message import EmailMessage
import os
from flask import Flask, render_template, request


def send_email():
    msg = EmailMessage()
    msg["Subject"] = "OK gomb megnyomva 👀"
    msg["From"] = os.environ.get("EMAIL_FROM")
    msg["To"] = os.environ.get("EMAIL_TO")
    msg.set_content("Valaki megnyomta az OK gombot az oldalon.")

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(
            os.environ.get("EMAIL_FROM"),
            os.environ.get("EMAIL_PASSWORD")
        )
        server.send_message(msg)


app = Flask(__name__)

# ⬇️ 3. ROUTE
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if request.form.get("confirmed") == "yes":
            send_email()
            print("Email elküldve")
    return render_template("index.html")


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
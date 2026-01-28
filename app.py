from flask import Flask, render_template, request
import smtplib
from email.message import EmailMessage
from datetime import datetime

app = Flask(__name__)

def send_email():
    msg = EmailMessage()
    msg["Subject"] = "OK gomb megnyomva"
    msg["From"] = "devairenata1@gmail.com"
    msg["To"] = "devairenata1@gmail.com"

    msg.set_content(
        f"Az OK gombot megnyomták.\nIdőpont: {datetime.now()}"
    )

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login("devairenata1@gmail.com", "bvwu hocd fcsr zxfe")
        server.send_message(msg)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        send_email()
        return "<h2>Köszi! Email elküldve 🙂</h2>"
    return render_template("index.html")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
app.run(host="0.0.0.0", port=port)
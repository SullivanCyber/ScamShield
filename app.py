from flask import Flask, render_template, request, redirect, session
import random
import time
from risk_engine import calculate_risk

app = Flask(__name__)
app.secret_key = "scamshield_secret"

# Demo user
USER = {
    "username": "demo",
    "password": "password123"
}

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if username == USER["username"] and password == USER["password"]:
            risk_score, reasons = calculate_risk(request)

            session["risk"] = risk_score
            session["reasons"] = reasons
            session["otp"] = str(random.randint(100000, 999999))
            session["otp_time"] = time.time()

            if risk_score > 60:
                return render_template("blocked.html", risk=risk_score, reasons=reasons)

            return redirect("/mfa")

        return render_template("login.html", error="Invalid credentials")

    return render_template("login.html")

@app.route("/mfa", methods=["GET", "POST"])
def mfa():
    if request.method == "POST":
        otp_input = request.form["otp"]
        otp_real = session.get("otp")
        otp_time = session.get("otp_time")

        if time.time() - otp_time > 30:
            return render_template("mfa.html", error="OTP expired")

        if otp_input == otp_real:
            return redirect("/dashboard")

        return render_template("mfa.html", error="Invalid OTP")

    return render_template("mfa.html", otp=session.get("otp"))

@app.route("/dashboard")
def dashboard():
    return render_template(
        "dashboard.html",
        risk=session.get("risk"),
        reasons=session.get("reasons")
    )

if __name__ == "__main__":
    app.run(debug=True)































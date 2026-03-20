from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        # Simple login logic
        if username == "admin" and password == "password123":
            return "<h2>Access Granted - Welcome to ScamShield Dashboard</h2>"
        else:
            return "<h2>Access Denied - High Risk Login</h2>"

    return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=False)































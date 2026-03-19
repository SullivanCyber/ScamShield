ScamShield – MFA & Behavioral Risk Demonstration

Description:
ScamShield is an entry-level cybersecurity project designed to demonstrate how Multi-Factor Authentication (MFA) and basic behavioral risk analysis can help prevent account takeover attacks, which are frequently used in scams and phishing schemes.

Key Features:
• Secure password-based login
• Simulated Time-based One-Time Password (TOTP) MFA
• Behavioral risk scoring for user actions
• Adaptive authentication based on risk assessment

Demonstrated Security Concepts:
• Multi-Factor Authentication (MFA)
• Risk-Based Authentication
• Account Takeover Prevention
• Behavioral Analytics

Project Importance:
Many scams are successful because attackers steal user credentials. This project demonstrates how implementing multiple layers of identity verification significantly reduces the risk of unauthorized account access.

 What the App Does

* Simulates a login system with risk evaluation
* Calculates risk based on:
  * Failed login attempts
  * Unknown devices
  * Suspicious IP behavior
* Dynamically routes users to:
  * ✅ Dashboard (low risk)
  * ❌ Blocked page (high risk)
* Demonstrates adaptive authentication and access control logic

---

 How It Works

1. User attempts to log in
2. The system analyzes behavioral risk factors
3. A risk score is calculated
4. Based on the score:
  * Low risk → Access granted
  * High risk → Access denied

---

 Technologies Used

* Python
* Flask
* HTML/CSS (if applicable)
* Git/GitHub

---

 How to Run the Project

1. Clone the repository

git clone https://github.com/SullivanCyber/ScamShield.git
cd ScamShield

2. Install dependencies

pip install flask

3. Run the application

python app.py

4. Open in browser

http://127.0.0.1:5000/

---

📸 Screenshots

✅ Successful Login (Low Risk)

Successful Login

❌ Blocked Login (High Risk)

Blocked Login

---

  Key Concepts Demonstrated

* Risk-Based Authentication (RBA)
* Identity & Access Management (IAM)
* Behavioral Analysis
* Access Control Logic
* Security Decision-Making

---

 Purpose

This project was built to simulate how modern systems evaluate login risk and enforce security policies in real-world environments.

---

 Author

Blake Sullivan
GitHub: https://github.com/SullivanCyber

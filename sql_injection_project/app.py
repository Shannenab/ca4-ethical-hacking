from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__)

# -----------------------------
# 1. SQL INJECTION (Login Page)
# -----------------------------
@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()

        # ❌ SQL Injection vulnerability (INTENTIONAL)
        query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
        cursor.execute(query)

        result = cursor.fetchone()
        conn.close()

        if result:
            return "✅ Login Successful (Vulnerable App)"
        else:
            return "❌ Login Failed"

    return render_template("login.html")


# -----------------------------
# 2. XSS (Comment Page)
# -----------------------------
@app.route("/comment", methods=["GET", "POST"])
def comment():
    user_comment = ""
    if request.method == "POST":
        user_comment = request.form["comment"]
    return render_template("comment.html", comment=user_comment)


# -----------------------------
# 3. BROKEN AUTHENTICATION
# -----------------------------
@app.route("/admin")
def admin():
    return "🚨 Welcome Admin! (No Authentication Check)"


# -----------------------------
# 4. SENSITIVE DATA EXPOSURE
# -----------------------------
@app.route("/users")
def users():
    conn = sqlite3.connect("databasee.db")

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    data = cursor.fetchall()
    conn.close()

    return f"⚠️ Users Table (Plain Text Passwords): {data}"


# -----------------------------
# MAIN (SECURITY MISCONFIGURATION)
# -----------------------------
if __name__ == "__main__":
    # ❌ Debug mode ON (Security Misconfiguration)
    app.run(debug=True)

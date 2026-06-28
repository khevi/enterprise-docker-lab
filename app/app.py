from flask import Flask
import mysql.connector
import os

app = Flask(__name__)

DB_HOST = os.getenv("DB_HOST", "mysql-db")
DB_USER = os.getenv("DB_USER", "appuser")
DB_PASSWORD = os.getenv("DB_PASSWORD", "AppPass123")
DB_NAME = os.getenv("DB_NAME", "devopsdb")

@app.route("/")
def home():
    conn = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )
    cursor = conn.cursor()
    cursor.execute("SELECT id, message, created_at FROM visits ORDER BY id DESC LIMIT 5")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()

    html = "<h1>Enterprise Flask + MySQL App</h1>"
    html += "<p>Application connected successfully to MySQL container.</p>"
    html += "<ul>"
    for row in rows:
        html += f"<li>{row[0]} - {row[1]} - {row[2]}</li>"
    html += "</ul>"
    return html

@app.route("/health")
def health():
    return "OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

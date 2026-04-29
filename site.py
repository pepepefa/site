from flask import Flask
import sqlite3

app = Flask(__name__)

@app.route("/")
def home():
    conn = sqlite3.connect("refs.db")
    cursor = conn.cursor()

    cursor.execute("""
    SELECT ref, COUNT(*) 
    FROM users 
    WHERE ref IS NOT NULL
    GROUP BY ref
    ORDER BY COUNT(*) DESC
    """)

    data = cursor.fetchall()

    html = "<h1>📊 Статистика рефералов</h1><br>"

    for ref, count in data:
        html += f"<p>{ref} → {count} человек</p>"

    return html

app.run(host="0.0.0.0", port=3000)

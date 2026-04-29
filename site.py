from flask import Flask
import sqlite3

app = Flask(__name__)

@app.route("/")
def home():
    with sqlite3.connect("refs.db") as conn:
        cursor = conn.cursor()
        cursor.execute("""
        SELECT ref, COUNT(*) 
        FROM users 
        WHERE ref IS NOT NULL
        GROUP BY ref
        ORDER BY COUNT(*) DESC
        """)
        data = cursor.fetchall()

    html = "<h1>📊 Статистика рефералів</h1><br>"

    for ref, count in data:
        html += f"<p>{ref} → {count} людей</p>"

    return html

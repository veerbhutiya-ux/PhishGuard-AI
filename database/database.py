import sqlite3

def create_database():
    conn = sqlite3.connect("database/phishguard.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS scan_history (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT,
        url TEXT,
        score INTEGER,
        risk TEXT,
        scan_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    conn.commit()
    conn.close()


def save_scan(email, url, score, risk):
    conn = sqlite3.connect("database/phishguard.db")
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO scan_history(email, url, score, risk)
    VALUES (?, ?, ?, ?)
    """, (email, url, score, risk))

    conn.commit()
    conn.close()

def get_all_scans():

    conn = sqlite3.connect("database/phishguard.db")
    cursor = conn.cursor()

    cursor.execute("""
    SELECT id, email, score, risk, scan_time
FROM scan_history
ORDER BY id DESC
    """)

    scans = cursor.fetchall()

    conn.close()

    return scans
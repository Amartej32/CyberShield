import sqlite3

DATABASE = "cybershield.db"


def get_connection():
    connection = sqlite3.connect(DATABASE)
    connection.row_factory = sqlite3.Row
    return connection


def init_database():

    connection = get_connection()

    connection.execute("""
        CREATE TABLE IF NOT EXISTS security_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            event TEXT NOT NULL,
            ip_address TEXT NOT NULL,
            severity TEXT NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)

    # Add investigation_status column if it does not already exist
    columns = connection.execute(
        "PRAGMA table_info(security_logs)"
    ).fetchall()

    column_names = [column["name"] for column in columns]

    if "investigation_status" not in column_names:

        connection.execute("""
            ALTER TABLE security_logs
            ADD COLUMN investigation_status TEXT DEFAULT 'Open'
        """)

    connection.commit()
    connection.close()


def add_sample_logs():

    connection = get_connection()

    count = connection.execute(
        "SELECT COUNT(*) FROM security_logs"
    ).fetchone()[0]

    if count == 0:

        sample_logs = [

            (
                "Multiple Login Attempts",
                "192.168.1.25",
                "Medium"
            ),

            (
                "Successful Login",
                "192.168.1.18",
                "Low"
            ),

            (
                "Port Scan Detected",
                "192.168.1.45",
                "Critical"
            ),

            (
                "Failed Login Attempt",
                "192.168.1.32",
                "Medium"
            ),

            (
                "Normal Network Activity",
                "192.168.1.12",
                "Low"
            )

        ]

        connection.executemany("""
            INSERT INTO security_logs
            (event, ip_address, severity)
            VALUES (?, ?, ?)
        """, sample_logs)

        connection.commit()

    connection.close()
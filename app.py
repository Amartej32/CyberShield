from flask import Flask, render_template, request, redirect
from database import init_database, add_sample_logs, get_connection

app = Flask(__name__, static_folder="static")

# Create database and sample data
init_database()
add_sample_logs()


# =========================
# Dashboard
# =========================

@app.route("/")
def home():

    connection = get_connection()

    total_events = connection.execute(
        "SELECT COUNT(*) FROM security_logs"
    ).fetchone()[0]

    threats = connection.execute(
        """
        SELECT COUNT(*)
        FROM security_logs
        WHERE severity IN ('Medium', 'Critical')
        """
    ).fetchone()[0]

    critical = connection.execute(
        """
        SELECT COUNT(*)
        FROM security_logs
        WHERE severity = 'Critical'
        """
    ).fetchone()[0]

    logs = connection.execute(
        """
        SELECT *
        FROM security_logs
        ORDER BY id DESC
        LIMIT 5
        """
    ).fetchall()

    connection.close()

    return render_template(
        "index.html",
        total_events=total_events,
        threats=threats,
        critical=critical,
        logs=logs
    )


# =========================
# Security Logs
# =========================

@app.route("/logs")
def security_logs():

    connection = get_connection()

    logs = connection.execute(
        """
        SELECT *
        FROM security_logs
        ORDER BY id DESC
        """
    ).fetchall()

    connection.close()

    return render_template(
        "logs.html",
        logs=logs
    )


# =========================
# Add Security Event
# =========================

@app.route("/add-log", methods=["GET", "POST"])
def add_log():

    if request.method == "POST":

        event = request.form["event"]
        ip_address = request.form["ip_address"]
        severity = request.form["severity"]

        connection = get_connection()

        connection.execute(
            """
            INSERT INTO security_logs
            (event, ip_address, severity, investigation_status)
            VALUES (?, ?, ?, ?)
            """,
            (
                event,
                ip_address,
                severity,
                "Open"
            )
        )

        connection.commit()
        connection.close()

        return redirect("/logs")

    return render_template("add_log.html")


# =========================
# Threats
# =========================

@app.route("/threats")
def threats_page():

    connection = get_connection()

    threats = connection.execute(
        """
        SELECT *
        FROM security_logs
        WHERE severity IN ('Medium', 'Critical')
        ORDER BY id DESC
        """
    ).fetchall()

    critical_count = connection.execute(
        """
        SELECT COUNT(*)
        FROM security_logs
        WHERE severity = 'Critical'
        """
    ).fetchone()[0]

    connection.close()

    return render_template(
        "threats.html",
        threats=threats,
        critical_count=critical_count
    )


# =========================
# Investigations
# =========================

@app.route("/investigations")
def investigations():

    connection = get_connection()

    investigation_list = connection.execute(
        """
        SELECT *
        FROM security_logs
        WHERE severity IN ('Medium', 'Critical')
        ORDER BY id DESC
        """
    ).fetchall()

    critical_count = connection.execute(
        """
        SELECT COUNT(*)
        FROM security_logs
        WHERE severity = 'Critical'
        """
    ).fetchone()[0]

    connection.close()

    return render_template(
        "investigations.html",
        investigations=investigation_list,
        critical_count=critical_count
    )


# =========================
# Individual Investigation
# =========================

@app.route("/investigate/<int:log_id>")
def investigate(log_id):

    connection = get_connection()

    investigation = connection.execute(
        """
        SELECT *
        FROM security_logs
        WHERE id = ?
        """,
        (log_id,)
    ).fetchone()

    connection.close()

    if investigation is None:
        return "Security event not found", 404

    return render_template(
        "investigate.html",
        investigation=investigation
    )


# =========================
# Update Investigation Status
# =========================

@app.route(
    "/investigate/<int:log_id>/status",
    methods=["POST"]
)
def update_investigation_status(log_id):

    status = request.form["status"]

    allowed_statuses = [
        "Open",
        "Investigating",
        "Resolved"
    ]

    if status not in allowed_statuses:
        return "Invalid investigation status", 400

    connection = get_connection()

    connection.execute(
        """
        UPDATE security_logs
        SET investigation_status = ?
        WHERE id = ?
        """,
        (status, log_id)
    )

    connection.commit()
    connection.close()

    return redirect(
        f"/investigate/{log_id}"
    )


# =========================
# Reports & Analytics
# =========================

@app.route("/reports")
def reports():

    connection = get_connection()


    # Total events

    total_events = connection.execute(
        """
        SELECT COUNT(*)
        FROM security_logs
        """
    ).fetchone()[0]


    # Low severity

    low_count = connection.execute(
        """
        SELECT COUNT(*)
        FROM security_logs
        WHERE severity = 'Low'
        """
    ).fetchone()[0]


    # Medium severity

    medium_count = connection.execute(
        """
        SELECT COUNT(*)
        FROM security_logs
        WHERE severity = 'Medium'
        """
    ).fetchone()[0]


    # Critical severity

    critical_count = connection.execute(
        """
        SELECT COUNT(*)
        FROM security_logs
        WHERE severity = 'Critical'
        """
    ).fetchone()[0]


    # Event distribution

    event_data = connection.execute(
        """
        SELECT event, COUNT(*) AS total
        FROM security_logs
        GROUP BY event
        ORDER BY total DESC
        """
    ).fetchall()


    # Recent logs

    recent_logs = connection.execute(
        """
        SELECT *
        FROM security_logs
        ORDER BY id DESC
        LIMIT 10
        """
    ).fetchall()


    connection.close()


    # Prepare chart data

    event_labels = [
        row["event"]
        for row in event_data
    ]

    event_counts = [
        row["total"]
        for row in event_data
    ]


    return render_template(
        "reports.html",

        total_events=total_events,

        low_count=low_count,

        medium_count=medium_count,

        critical_count=critical_count,

        event_labels=event_labels,

        event_counts=event_counts,

        recent_logs=recent_logs
    )


# =========================
# Run CyberShield
# =========================

if __name__ == "__main__":
    app.run(debug=True)

# CyberShield - Mini SIEM

CyberShield is a beginner-friendly Security Information and Event Management (SIEM) web application built with Python, Flask, and SQLite.

It provides a simple environment for monitoring security events, identifying potential threats, investigating suspicious activity, tracking investigation status, and viewing security analytics.

## Live Demo

[Open CyberShield Live Demo](https://cybershield-0f0u.onrender.com/)

## Project Highlights

* Security monitoring dashboard
* Security event logging
* Threat detection based on severity
* Investigation workflow for suspicious events
* Investigation status tracking
* Reports and security analytics
* Recent security event monitoring
* Source IP tracking
* Dark cybersecurity-themed interface
* Public cloud deployment

## Dashboard Preview

A dashboard screenshot can be added here:

```text
screenshots/dashboard.png
```

## Security Workflow

```text
Security Event
      |
      v
Event Logging
      |
      v
Severity Classification
      |
      v
Threat Detection
      |
      v
Security Investigation
      |
      v
Status Tracking
      |
      v
Reports & Analytics
```

## Technologies Used

| Technology | Purpose                   |
| ---------- | ------------------------- |
| Python     | Backend programming       |
| Flask      | Web application framework |
| SQLite     | Security event database   |
| HTML       | Page structure            |
| CSS        | User interface styling    |
| JavaScript | Interactive functionality |
| Chart.js   | Analytics visualization   |
| Git        | Version control           |
| GitHub     | Source code hosting       |
| Render     | Cloud deployment          |

## Project Structure

```text
CyberShield/
|
+-- static/
|   +-- style.css
|
+-- templates/
|   +-- index.html
|   +-- logs.html
|   +-- add_log.html
|   +-- threats.html
|   +-- investigations.html
|   +-- investigate.html
|   +-- reports.html
|
+-- app.py
+-- database.py
+-- requirements.txt
+-- .gitignore
+-- README.md
```

## Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/Amartej32/CyberShield.git
```

### 2. Open the project

```bash
cd CyberShield
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

Windows:

```powershell
venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the application

```bash
python app.py
```

### 7. Open in your browser

```text
http://127.0.0.1:5000
```

## Security Features

CyberShield allows users to:

* Record suspicious security events
* Track source IP addresses
* Categorize events by severity
* Identify medium and critical events
* Investigate suspicious activity
* Track investigation progress
* Review security activity through reports and analytics

## Project Goal

The goal of CyberShield is to provide a practical learning environment for understanding the basic workflow of a Security Information and Event Management system.

The project demonstrates how security events can be collected, categorized, investigated, and presented through a web-based security dashboard.

## Future Improvements

* User authentication
* Real-time security monitoring
* IP reputation checking
* Automated threat detection
* Email alerts
* Persistent production database
* Advanced analytics
* Role-based access control
* Security event filtering
* Exportable security reports

## Author

**Amar Sai Teja**

GitHub:
https://github.com/Amartej32

---

Built as a cybersecurity learning and portfolio project.

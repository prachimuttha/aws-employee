# AWS Employee Management System

A Flask-based web application deployed on AWS that manages employee records and profile images.

## What This Project Does
- Provides a web interface (`templates/AddEmp.html` and `templates/AddEmpOutput.html`) to submit employee details and upload profile images.
- Stores structured employee data in an Amazon RDS (MySQL) database (`employee`).
- Stores uploaded employee images in an Amazon S3 bucket (`add-employee-bucket14`).

## AWS Services & Tech Stack
- **Compute:** Amazon EC2
- **Database:** Amazon RDS (MySQL)
- **Storage:** Amazon S3
- **Application:** Python, Flask (`EmpApp.py`)
- **Version Control:** Git & GitHub

## How to Configure `config.py`
Sensitive credentials (`config.py`) are excluded from the repository using `.gitignore`. To run the project:

1. Copy `config.sample.py` to a new file named `config.py`:
   ```bash
   cp config.sample.py config.py

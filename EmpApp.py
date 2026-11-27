from flask import Flask, render_template, request
import pymysql
import boto3
from config import *

app = Flask(__name__)

bucket = custombucket
region = customregion

db_conn = pymysql.connect(
    host=customhost,
    port=3306,
    user=customuser,
    password=custompass,
    db=customdb
)

@app.route("/", methods=['GET', 'POST'])
def home():
    return render_template('AddEmp.html')

@app.route("/addemp", methods=['POST'])
def AddEmp():
    emp_id = request.form['emp_id']
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    primary_skill = request.form['primary_skill']
    location = request.form['location']
    emp_image_file = request.files['emp_image_file']

    insert_sql = "INSERT INTO emp VALUES (%s, %s, %s, %s, %s)"
    cursor = db_conn.cursor()

    if emp_image_file.filename == "":
        return "Please select a file"

    try:
        cursor.execute(insert_sql, (emp_id, first_name, last_name, primary_skill, location))
        db_conn.commit()

        emp_image_file_name_in_s3 = "emp-id-" + str(emp_id) + "_image_file"
        s3 = boto3.client('s3', region_name=region)
        s3.upload_fileobj(emp_image_file, bucket, emp_image_file_name_in_s3)

        emp_name = f"{first_name} {last_name}"
        return render_template('AddEmpOutput.html', name=emp_name)
    except Exception as e:
        return str(e)
    finally:
        cursor.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)

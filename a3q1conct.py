import psycopg2

# Function that is used to connect to the database with psycopg2
def connect():
    return psycopg2.connect(
        dbname="a3demo",
        user="postgres",
        password="postgres",
        host="localhost",
        port="5432"
    )

# Function is used for retrieving and displaying all the records for the table
def getAllStudents():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    conn.close()

# Function that is used for inserting new students into our table
def addStudent(first_name, last_name, email, enrollment_date):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s)",
                   (first_name, last_name, email, enrollment_date))
    conn.commit()
    print("You have added a student.")
    cursor.close()
    conn.close()

# Function that is used for updating the student email by replacing it with a new one
def updateStudentEmail(student_id, new_email):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("UPDATE students SET email = %s WHERE student_id = %s", (new_email, student_id))
    conn.commit()
    print("You have updated the email.")
    cursor.close()
    conn.close()

# Function for deleting a student
def deleteStudent(student_id):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE student_id = %s", (student_id,))
    conn.commit()
    print("You have deleted the student.")
    cursor.close()
    conn.close()

# This is what I will use for testing the CRUD operations
# First Test 
#getAllStudents()
    
# Second Test
#addStudent("Arkan", "Slabi", "arkanemail@outlook.com", "2023-08-01")

# Third Test
#updateStudentEmail(1, "newemail@outlook.com")
    
# Fourth Test
#deleteStudent(1)

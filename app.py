from flask import Flask, render_template, request
from flask_mail import Mail, Message
import psycopg2

app = Flask(__name__)


# --- PostgreSQL connection ---
def get_db_connection():
    return psycopg2.connect(
        host="localhost",
        database="smart_tech_db",  # Change if needed
        user="postgres",  # Your DB username
        password="emmanuel"  # Your DB password
    )


# --- Email Configuration (FIXED) ---
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['kingsleyuzokwe0@gmail.com'] = 'your_admin_email@gmail.com'  # Replace with your email
app.config['txmr edhi xvgi kvoy'] = 'your_app_password'  # Gmail app password
mail = Mail(app)


# --- Static Pages ---
@app.route('/')
def home():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/services')
def services():
    return render_template('services.html')


@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        # Save feedback to database
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO feedbacks (name, email, message)
            VALUES (%s, %s, %s)
        """, (name, email, message))
        conn.commit()
        cur.close()
        conn.close()

        # Send email to admin
        msg = Message(
            subject=f"New Feedback from {name}",
            sender=email,
            recipients=[app.config['MAIL_USERNAME']],
            body=f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"
        )
        mail.send(msg)

        return f"✅ Thank you {name}, your feedback has been submitted!"

    return render_template('feedback.html')


@app.route('/pricing')
def pricing():
    return render_template('pricing.html')


@app.route('/ebooks')
def ebooks():
    return render_template('ebooks.html')


# --- User Registration ---
@app.route('/register', methods=['POST'])
def register():
    data = request.form
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO users (fullname, email, password, dob, phone, course)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (
        data['fullname'], data['email'], data['password'],
        data['dob'], data['phone'], data['courses']
    ))
    conn.commit()
    cur.close()
    conn.close()
    return f"✅ Thanks {data['fullname']}, you're registered for {data['courses']}!"


# --- Course Enrollment ---
@app.route('/enroll', methods=['POST'])
def enroll():
    email = request.form['email']
    course = request.form['course']

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO enrollments (user_email, course_name)
        VALUES (%s, %s)
    """, (email, course))
    conn.commit()
    cur.close()
    conn.close()

    return f"🎓 {email} has successfully enrolled in {course}!"

from flask import Flask, render_template, request, redirect
import psycopg2

app = Flask(__name__)

# Connect to PostgreSQL
conn = psycopg2.connect(
    dbname='your_db',
    user='your_user',
    password='your_pass',
    host='localhost',
    port='5432'
)
cur = conn.cursor()

@app.route('/enroll', methods=['POST'])
def enroll():
    full_name = request.form['full_name']
    email = request.form['email']
    course = request.form['course']

    cur.execute("INSERT INTO enrollments (full_name, email, course) VALUES (%s, %s, %s)",
                (full_name, email, course))
    conn.commit()

    return f"<h2>Thanks {full_name}, you’ve enrolled in {course}!</h2><a href='/'>Back Home</a>"

# Your existing routes (home, about, etc.)
@app.route('/')
def home():
    return render_template('index.html')

# You can add route for courses.html if not done yet
@app.route('/courses')
def courses():
    return render_template('courses.html')

if __name__ == '__main__':
    app.run(debug=True)



# --- Login (Basic placeholder) ---
@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']
    # TODO: Add real login validation
    return f"🔐 Login received from {email}"


# --- Run the app ---
if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, request, jsonify, redirect, url_for, session
import os
import shutil

app = Flask(__name__)
app.secret_key = "radhika_academy_premium_key"

# Copy generated images to static/assets if they exist
ASSETS_DIR = os.path.join(os.path.dirname(__file__), 'static', 'assets')
os.makedirs(ASSETS_DIR, exist_ok=True)
BRAIN_DIR = r"C:\Users\James\.gemini\antigravity\brain\057ffe71-23e2-4005-97c9-89dcca84e0f2"
try:
    for filename in os.listdir(BRAIN_DIR):
        if filename.endswith(".png"):
            shutil.copy(os.path.join(BRAIN_DIR, filename), os.path.join(ASSETS_DIR, filename))
except Exception as e:
    print("Could not copy images:", e)

# Dummy database
users = {
    "student@radhika.com": {"password": "123", "name": "Priya", "role": "student", "paid": True, "fees_due": 0},
    "new_student@radhika.com": {"password": "123", "name": "Kavya", "role": "student", "paid": False, "fees_due": 5000},
    "staff@radhika.com": {"password": "123", "name": "Radhika Admin", "role": "staff", "paid": True}
}

videos = [
    {"id": 1, "title": "Bridal Makeup Masterclass", "description": "Learn the secrets of flawless bridal makeup.", "url": "https://www.w3schools.com/html/mov_bbb.mp4", "thumbnail": "makeup_class_1777374949875.png"},
    {"id": 2, "title": "Advanced Fashion Design", "description": "Creating stunning modern garments.", "url": "https://www.w3schools.com/html/mov_bbb.mp4", "thumbnail": "fashion_design_1777375076281.png"}
]

orders = []

@app.route('/')
def home():
    # Pass the image filenames to the template so they can be rendered correctly
    return render_template('index.html', 
                           hero_bg="hero_bg_1777374993169.png", 
                           makeup="makeup_class_1777374949875.png",
                           fashion="fashion_design_1777375076281.png")

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/expertise')
def expertise():
    return render_template('expertise.html')

@app.route('/courses')
def courses():
    return render_template('courses.html', 
                           makeup="makeup_class_1777374949875.png",
                           fashion="fashion_design_1777375076281.png")

@app.route('/upcoming-courses')
def upcoming_courses():
    return render_template('upcoming-courses.html')

@app.route('/achievers')
def achievers():
    return render_template('achievers.html')

@app.route('/feedback')
def feedback():
    return render_template('feedback.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/dashboard')
def dashboard():
    if 'user' not in session:
        return redirect(url_for('login'))
    user = users.get(session['user'])
    return render_template('dashboard.html', user=user, videos=videos, orders=orders, users=users)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        if email in users and users[email]['password'] == password:
            session['user'] = email
            return redirect(url_for('dashboard'))
        return render_template('login.html', error="Invalid credentials")
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('home'))

@app.route('/upload', methods=['POST'])
def upload_video():
    if 'user' in session and users[session['user']]['role'] == 'staff':
        title = request.form.get('title')
        description = request.form.get('description')
        videos.append({
            "id": len(videos)+1, 
            "title": title, 
            "description": description, 
            "url": "https://www.w3schools.com/html/mov_bbb.mp4",
            "thumbnail": "makeup_class_1777374949875.png"
        })
        return redirect(url_for('dashboard'))
    return "Unauthorized", 403

@app.route('/pay_fees', methods=['POST'])
def pay_fees():
    if 'user' in session:
        email = session['user']
        if users[email]['role'] == 'student':
            users[email]['paid'] = True
            users[email]['fees_due'] = 0
            orders.append({"user": email, "type": "Fees Payment", "amount": 5000})
            return redirect(url_for('dashboard'))
    return "Unauthorized", 403

if __name__ == '__main__':
    app.run(debug=True, port=5000)

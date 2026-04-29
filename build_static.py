import os
import re
import shutil

templates_dir = "templates"
root_dir = "."

replacements = {
    r"\{\{\s*url_for\('static',\s*filename='(.*?)'\)\s*\}\}": r"static/\1",
    r"\{\{\s*url_for\('home'\)\s*\}\}": "index.html",
    r"\{\{\s*url_for\('about'\)\s*\}\}": "about.html",
    r"\{\{\s*url_for\('expertise'\)\s*\}\}": "expertise.html",
    r"\{\{\s*url_for\('courses'\)\s*\}\}": "courses.html",
    r"\{\{\s*url_for\('upcoming_courses'\)\s*\}\}": "upcoming-courses.html",
    r"\{\{\s*url_for\('achievers'\)\s*\}\}": "achievers.html",
    r"\{\{\s*url_for\('feedback'\)\s*\}\}": "feedback.html",
    r"\{\{\s*url_for\('contact'\)\s*\}\}": "contact.html",
    r"\{\{\s*url_for\('login'\)\s*\}\}": "login.html",
    r"\{\{\s*url_for\('logout'\)\s*\}\}": "index.html",
    r"\{\{\s*url_for\('dashboard'\)\s*\}\}": "dashboard.html",
    r"\{\{\s*url_for\('pay_fees'\)\s*\}\}": "#",
    r"\{\{\s*url_for\('upload_video'\)\s*\}\}": "#",
    r"\{\{\s*url_for\('static',\s*filename='assets/'\s*\+\s*hero_bg\)\s*\}\}": "static/assets/hero_bg_1777374993169.png",
    r"\{\{\s*url_for\('static',\s*filename='assets/'\s*\+\s*makeup\)\s*\}\}": "static/assets/makeup_class_1777374949875.png",
    r"\{\{\s*url_for\('static',\s*filename='assets/'\s*\+\s*fashion\)\s*\}\}": "static/assets/fashion_design_1777375076281.png",
    r"\{\{\s*url_for\('static',\s*filename='assets/'\s*~\s*video\.thumbnail\)\s*if\s*video\.thumbnail\s*else\s*'[^']*'\s*\}\}": "static/assets/makeup_class_1777374949875.png",
    r"\{\{\s*user\.name\s*\}\}": "Student",
    r"\{\{\s*'Staff'\s*if\s*user\.role\s*==\s*'staff'\s*else\s*'Student'\s*\}\}": "Student",
    r"\{\{\s*user\.fees_due\s*\}\}": "5000",
    r"\{\{\s*'green'\s*if\s*user\.paid\s*else\s*'red'\s*\}\}": "red",
    r"\{\{\s*'Paid'\s*if\s*user\.paid\s*else\s*'Pending\s*\(₹'\s*~\s*user\.fees_due\s*~\s*'\)'\s*\}\}": "Pending (₹5000)",
    r"\{\{\s*video\.title\s*\}\}": "Bridal Makeup Masterclass",
    r"\{\{\s*video\.description\s*\}\}": "Learn the secrets of flawless bridal makeup.",
    r"\{\{\s*users\|length\s*-\s*1\s*\}\}": "24",
    r"\{\{\s*orders\|length\s*\*\s*5000\s*\}\}": "120000",
}

for filename in os.listdir(templates_dir):
    if filename.endswith(".html"):
        filepath = os.path.join(templates_dir, filename)
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
            
        for pattern, replacement in replacements.items():
            content = re.sub(pattern, replacement, content)
            
        # Clean up remaining Jinja conditionals and loops
        content = re.sub(r"\{%\s*if.*?%\}", "", content)
        content = re.sub(r"\{%\s*elif.*?%\}", "", content)
        content = re.sub(r"\{%\s*else.*?%\}", "", content)
        content = re.sub(r"\{%\s*endif.*?%\}", "", content)
        content = re.sub(r"\{%\s*for.*?%\}", "", content)
        content = re.sub(r"\{%\s*endfor.*?%\}", "", content)
        
        with open(os.path.join(root_dir, filename), "w", encoding="utf-8") as f:
            f.write(content)

print("Static HTML files generated in root directory.")

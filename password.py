from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)

def generate_password(length):
    if length < 12:
        return "Password must be at least 12 characters!"

    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    all_chars = lowercase + uppercase + digits + symbols
    password = random.choices(all_chars, k=length)
    return ''.join(password)

@app.route("/", methods=["GET", "POST"])
def index():
    password = ""
    if request.method == "POST":
        length = int(request.form.get("length", 12))
        password = generate_password(length)
    return render_template("index.html", password=password)

if __name__ == "__main__":
    app.run(debug=True)

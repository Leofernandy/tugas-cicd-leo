from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to Leo's CI/CD Pipeline! and Thankyou"

@app.route("/status")
def status():
    return "OK - System is running smoothly"

if __name__ == "__main__":
    app.run()

# trigger vercel update
import app

def test_home():
    assert app.home() == "Welcome to Leo's CI/CD Pipeline! and Thankyou! Bye"

def test_status():
    assert app.status() == "OK - System is running smoothly"
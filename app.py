from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Вітаю на моєму простому сайті!"

if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask

app = Flask(__name__)

@app.route("/")
def homepage():
    return "FakePinterest - Meu primeiro site"

if __name__ == "__main__":
    app.run(debug=True


# teste de alteração
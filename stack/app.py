from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from chatbot import get_response

app = Flask(__name__)
CORS(app)

# 🏠 Frontend
@app.route("/")
def home():
    return render_template("index.html")

# 🤖 Chat API (FIXED)
@app.route("/chat", methods=["POST"])
def chat():
    print("CHAT HIT")   # debug

    data = request.get_json()
    print(data)         # debug

    msg = data.get("message", "")
    reply = get_response(msg)

    return jsonify({"reply": reply})


# 🚀 RUN SERVER (LAST LINE ONLY)
if __name__ == "__main__":
    app.run(debug=True)
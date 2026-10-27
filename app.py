from flask import Flask, request, jsonify
from cipher import encrypt, decrypt

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "name": "TES-1 Cipher API",
        "author": "YOUR NAME — CYS 415",
        "endpoints": {
            "POST /encrypt": {"body": {"text": "...", "key": "..."}},
            "POST /decrypt": {"body": {"cipher": "...", "key": "..."}}
        }
    })

@app.post("/encrypt")
def do_encrypt():
    d = request.get_json(force=True)
    try:
        return jsonify({"cipher": encrypt(d["text"], d["key"])})
    except KeyError:
        return jsonify({"error": "need 'text' and 'key'"}), 400

@app.post("/decrypt")
def do_decrypt():
    d = request.get_json(force=True)
    try:
        return jsonify({"text": decrypt(d["cipher"], d["key"])})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
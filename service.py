from flask import Flask, jsonify
import json
app = Flask(__name__)

# Open the JSON file
with open('data.json') as f:
    # Load the data from the file
    data = json.load(f)

# Bir route tanımlayalım
@app.route("/api")
def api():
    # Sözlüğü JSON formatında döndürelim
    return jsonify(data)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
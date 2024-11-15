from flask import Flask, render_template, jsonify
from scraper import fetch_all_items

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/api/items')
def get_items():
    items = fetch_all_items()
    return jsonify(items)

if __name__ == "__main__":
    app.run(debug=True)

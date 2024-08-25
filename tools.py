from flask import Flask, request, jsonify, send_from_directory, render_template, redirect, url_for
from langchain_cohere.llms import Cohere
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Use correct environment variable key
# cohere_api_key = os.environ.get('COHERE_API_KEY')

@app.route("/" , methods =['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route("/generate_code", methods=['GET', 'POST'])
def generate_suggestions():
    if request.content_type != 'application/json':
        return jsonify({"error": "Unsupported Media Type, expected 'application/json'"}), 415
    try:
        data = request.json
        user_input = data.get("input1")
        if not user_input:
            return jsonify({"error": "No input provided"}), 400
        prompt = f"Give me the code of {user_input}"
        llm = Cohere(cohere_api_key="key")
        completion = llm.invoke(input=prompt)
        return jsonify({"suggestion": completion})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True)

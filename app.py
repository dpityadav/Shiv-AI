from flask import Flask, render_template, request, jsonify
import openai
import os

app = Flask(_name_)

# Load API key from environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')

    try:
        # Call OpenAI API
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are SHIV AI, a smart assistant."},
                {"role": "user", "content": user_message}
            ]
        )

        bot_reply = response['choices'][0]['message']['content']
        return jsonify({'reply': bot_reply})

    except Exception as e:
        return jsonify({'reply': f"Error: {str(e)}"})

if _name_ == '_main_':
    app.run(host='0.0.0.0', port=5000)

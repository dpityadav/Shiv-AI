
from flask import Flask, render_template_string, request, jsonify

app = Flask(__name__)

dashboard_html = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SHIV Dashboard</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="dashboard-container">
        <h1>Welcome to SHIV AI</h1>
        <div class="chat-box" id="chat-box"></div>
        <input type="text" id="user-input" placeholder="Type your message...">
        <button onclick="sendMessage()">Send</button>
    </div>
    <script src="script.js"></script>
</body>
</html>
'''

@app.route('/')
def login():
    return '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SHIV Login</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="login-container">
        <h1>SHIV AI Login</h1>
        <form action="/login" method="post">
            <input type="text" name="username" placeholder="Username" required>
            <input type="password" name="password" placeholder="Password" required>
            <button type="submit">Login</button>
        </form>
    </div>
</body>
</html>
'''

@app.route('/login', methods=['POST'])
def do_login():
    return dashboard_html

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    response = f"I received your message: {user_message}"
    return jsonify({'reply': response})

if __name__ == '__main__':
    app.run(debug=True)

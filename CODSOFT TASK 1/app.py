from flask import Flask, request, jsonify, render_template_string
from chatbot import get_response

app = Flask(__name__)

PAGE = """
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width,initial-scale=1" />
    <title>Simple Chatbot</title>
    <style>
      body { font-family: Arial, sans-serif; margin: 2rem; }
      #chat { border: 1px solid #ddd; padding: 1rem; height: 300px; overflow:auto; }
      .user { color: #003366; margin: .5rem 0 }
      .bot { color: #006600; margin: .5rem 0 }
      #input { width: 80%; padding: .5rem }
      #send { padding: .5rem .75rem }
    </style>
  </head>
  <body>
    <h2>Simple Chatbot (Web)</h2>
    <div id="chat">
      <div class="bot">Chatbot: Hello — type below to start the chat.</div>
    </div>
    <div style="margin-top:1rem">
      <input id="input" placeholder="Say something..." />
      <button id="send">Send</button>
    </div>

    <script>
      const chat = document.getElementById('chat');
      const input = document.getElementById('input');
      const send = document.getElementById('send');

      function append(role, text){
        const d = document.createElement('div');
        d.className = role === 'user' ? 'user' : 'bot';
        d.textContent = (role === 'user' ? 'You: ' : 'Chatbot: ') + text;
        chat.appendChild(d);
        chat.scrollTop = chat.scrollHeight;
      }

      async function sendMessage(){
        const text = input.value.trim();
        if(!text) return;
        append('user', text);
        input.value = '';

        const res = await fetch('/chat', {
          method: 'POST', headers: {'Content-Type':'application/json'},
          body: JSON.stringify({message: text})
        });
        const data = await res.json();
        append('bot', data.reply);
      }

      send.addEventListener('click', sendMessage);
      input.addEventListener('keydown', (e)=>{ if(e.key === 'Enter') sendMessage(); });
    </script>
  </body>
</html>
"""


@app.route('/')
def index():
    return render_template_string(PAGE)


@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json() or {}
    message = (data.get('message') or '').lower().strip()
    reply = get_response(message)
    if reply == '__EXIT__':
        return jsonify({'reply': 'Goodbye! (chat ended)'}), 200
    return jsonify({'reply': reply}), 200


if __name__ == '__main__':
    # Run on localhost:5000
    app.run(host='127.0.0.1', port=5000)

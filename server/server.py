from flask import Flask, request, render_template
app = Flask(__name__)

entries = []

@app.route('/')
def index():
    print(entries)
    return render_template('index.html', entries=entries)

@app.route('/write', methods=['POST'])
def write():
    data = request.get_json()['entry_data']
    entries.append(data)
    print(data)
    return 'OK'


if __name__ == '__main__':
    app.run(debug=True, port=8080)
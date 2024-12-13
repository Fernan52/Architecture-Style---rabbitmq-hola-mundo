from flask import Flask
import pika

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '¡Hola Mundo con RabbitMQ!'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

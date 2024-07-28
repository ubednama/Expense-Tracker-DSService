from flask import Flask
from flask import request,jsonify
from .service.messageService import MessageService
from kafka import KafkaProducer
import json
import os

app = Flask(__name__)
app.config.from_pyfile('config.py')

messageService = MessageService()
kafka_host = os.getenv('KAFKA_HOST', 'localhost')
kafka_port = os.getenv('KAFKA_PORT', '9092')
kafka_bootstrap_servers = f'{kafka_host}:{kafka_port}'

print("Kafka server is "+kafka_bootstrap_servers)
print("\n")

producer = KafkaProducer(bootstrap_servers=kafka_bootstrap_servers,
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'))

@app.route('/v1/ds/message', methods=['POST'])
def handle_message():
    message = request.json.get('message')
    result = messageService.process_message(message)

    if result is not None:
        serialized_result = result.serialize()
        producer.send('expense_service', serialized_result)
        return jsonify(serialized_result), 200
    else:
        return jsonify({"error": "Invalid message format"}), 400
    
@app.route('/v1/ds/api', methods=['GET'])
def handle_api():
    return jsonify({"message": "API is live"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
from flask import Flask, request, jsonify
import os
import logging

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)

@app.route('/open_file', methods=['POST'])
def open_file():
    try:
        data = request.json
        logging.debug(f"Received data: {data}")
        file_path = data.get('file_path')
        
        if file_path and os.path.exists(file_path):
            if os.name == 'nt':  # Windowsの場合
                os.startfile(file_path)
            elif os.name == 'posix':  # macOSの場合
                subprocess.run(['open', file_path])
            elif os.name == 'posix':  # Linuxの場合
                subprocess.run(['xdg-open', file_path])
            else:
                return jsonify({"error": "Unsupported OS"}), 500
            
            logging.debug(f"Opened file: {file_path}")
            return jsonify({"message": "File opened successfully!"}), 200
        else:
            logging.error("File not found")
            return jsonify({"error": "File not found"}), 404
    except Exception as e:
        logging.error(f"Error occurred: {e}")
        return jsonify({"error": "Internal Server Error"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=60000)

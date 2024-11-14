from flask import Flask, request, jsonify
import requests
import os

def checkurl():
    url = request.args.get('url')
    
    # Check if the URL uses the file scheme
    if url.startswith("file:///"):
        # Strip "file://" and attempt to read the local file
        file_path = url[7:]  # Removes 'file://'
        
        # Prevent accessing files outside of specific directories for safety
        if not os.path.exists(file_path):
            return jsonify({"error": "URL Not Found"}), 404
        
        try:
            with open(file_path, 'r') as file:
                file_content = file.read()
            return file_content
        except Exception as e:
            return jsonify({"error": "URL Not Found"}), 404

    # For regular URLs, use requests to fetch the content
    try:
        response = requests.get(url)
        return response.text
    except Exception as e:
        return jsonify({"error": "URL Not Found"}), 404
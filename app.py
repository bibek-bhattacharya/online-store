from flask import Flask, request, jsonify
from app import create_app

app = create_app()



# @app.route('/', methods=['GET'])
# def get():
#     return jsonify({ 'msg' : 'Hello World'})


if __name__ == "__main__":
    app.run(debug=True)

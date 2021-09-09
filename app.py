from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=['POST', 'GET'])
def index():
    value = request.json['input']

    if (value == "hotdog"):
        return "yes, i am a hotdog"

    else:
        return "hello!"

    # return jsonify({"key": [0,1,2,3,4,5]})

if __name__=="__main__":
    app.run(debug=True)
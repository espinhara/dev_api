from flask import Flask, jsonify, request
import json

developers = [
    {"name": "Gabriel", "hard_skills": ["JavaScript", "Python", "NodeJS", "VueJS", "React", "Flutter", "Vue Native"]},
    {"name": "Ricardo",
     "hard_skills": ["JavaScript", ".NET", "NodeJS", "VueJS", "React", "Flutter", "Asp.Net", "jQuery", "React Native"]},
    {"name": "Eduardo", "hard_skills": ["JavaScript", "C#", "NodeJS", "React", "React Native", ".NET"]},
    {"name": "Lucas", "hard_skills": ["JavaScript", ".NET", "NodeJS", "VueJS", "React", "C#", "SQL Server"]},
    {"name": "Leandro", "hard_skills": ["JavaScript", "Python", "NodeJS", "MongoDB"]},
    {"name": "Gustavo", "hard_skills": ["JavaScript", "NodeJS", "React"]},
    {"name": "Allan", "hard_skills": ["Drawing", "Speak in Japanese", "Design"]},
    {"name": "Guilherme", "hard_skills": [".NET", "C#", "SQL Server"]}
]

app = Flask(__name__)


@app.route("/dev/<int:id>", methods=['GET', 'PUT', 'DELETE'])
def developer(id):
    if request.method == 'GET':
        try:
            response = developers[id]
        except IndexError:
            message = "Cannot find developer ID {} ".format(id)
            response = {"status": "error", "message": message}
        return jsonify(response)
    elif request.method == 'PUT':
        model = json.loads(request.data)
        developers[id] = model
        return jsonify({'status': 'ok', "model": model})
    elif request.method == 'DELETE':
        developers.pop(id)
        return jsonify({"status": "ok"})


@app.route("/dev", methods=['GET', 'POST'])
def develop():
    if request.method == 'GET':
        return jsonify(developers)
    elif request.method == 'POST':
        model = json.loads(request.data)
        developers.append(model)
        index = len(developers)
        return jsonify({"status": "ok", "message": "Added new Developer", "model": developers[index-1]})


if __name__ == '__main__':
    app.run(debug=True)

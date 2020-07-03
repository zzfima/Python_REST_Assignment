from flask import Flask, jsonify, abort, request

app = Flask(__name__)

all_personnel = [
    {
        'address': 'Shlomi, hertsel 14/14, 577688',
        'name': 'Avi Shalom',
        'salary': 12500,
        'devision': 'Software',
        'birthday': '1970-04-23'
    },
    {
        'address': 'Haifa, magenim 5, 654667',
        'name': 'Moshe Cohen',
        'salary': 7000,
        'devision': 'Software',
        'birthday': '1980-05-13'
    }
]


@app.route('/')
def index():
    """Get Welcome message
    Returns:
        string: start message"""
    return "Its simple Organization Personnel Managing system"


@app.route('/personnelmanaging/api/v1.0/get_all_personnel', methods=['GET'])
def get_all_personnel():
    """GET All Personnel

    Returns:
        JSON: all Personnel"""
    return jsonify({'all_personnel': all_personnel})


@app.route('/personnelmanaging/api/v1.0/get_personnel/<string:personnel_name>', methods=['GET'])
def get_personnel(personnel_name):
    """GET Personnel by name

    Args:
        personnel_name (string): personnel name
    Returns:
        JSON: concrete personnel"""
    personnel = [p for p in all_personnel if p['name'] == personnel_name]
    if len(personnel) == 0:
        abort(404)
    return jsonify({'personnel': personnel[0]})


@app.route('/personnelmanaging/api/v1.0/add_personnel', methods=['POST'])
def add_personnel():
    """Add personnel

    Args:
        personnel (personnel): object, describes personnel"""
    mandatory_fields = ['address', 'name', 'salary', 'devision', 'birthday']
    if not request.json or not any(f in request.json for f in mandatory_fields):
        abort(400)
    personnel = {
        'address': request.json['address'],
        'name': request.json['name'],
        'salary': request.json['salary'],
        'devision': request.json['devision'],
        'birthday': request.json['birthday']
    }
    all_personnel.append(personnel)
    return jsonify({'personnel': personnel}), 201


@app.route('/personnelmanaging/api/v1.0/remove_personnel/<string:personnel_name>', methods=['POST'])
def delete_task(personnel_name):
    personnel = [p for p in all_personnel if p['name'] == personnel_name]
    print(personnel)
    if len(personnel) == 0:
        abort(404)
    all_personnel.remove(personnel[0])
    return jsonify({'result': True})


if __name__ == '__main__':
    app.run()

# Run server by
# 1. In VSCode terminal: Server\python -m flask run
# 2. CMD: Server\python app.py
# Add personnel in GIT Bush:
# curl -i -H "Content-Type: application/json" -X POST -d '{"address":"Akko", "name":"Maya", "salary":3333, "devision":"other", "birthday":"1960-05-13"}' http://localhost:5000/personnelmanaging/api/v1.0/add_personnel
# remove personnel:
#

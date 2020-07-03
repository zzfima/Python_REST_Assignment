from flask import Flask, jsonify, abort

app = Flask(__name__)

all_personnel = [
    {
        'name': 'Avi Shalom',
        'address': 'Shlomi, hertsel 14/14, 577688',
        'salary': 12500,
        'devision': 'Software',
        'birthday': '1970-04-23'
    },
    {
        'name': 'Moshe Cohen',
        'address': 'Haifa, magenim 5, 654667',
        'salary': 7000,
        'devision': 'Software',
        'birthday': '1980-05-13'
    }
]

@app.route('/')
def index():
    """Get empty route
    Returns:
        string: start message"""
    return "Its simple Organization Personnel Managing system"


@app.route('/personnel/api/v1.0/all_personnel', methods=['GET'])
def get_all_personnel():
    """GET All Personnel
    Returns:
        [JSON]: all Personnel"""
    return jsonify({'all_personnel': all_personnel})


@app.route('/personnel/api/v1.0/personnel/<string:personnel_name>', methods=['GET'])
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


if __name__ == '__main__':
    app.run(debug=True)

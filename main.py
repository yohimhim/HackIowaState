from flask import *
import random, csv
app = Flask(__name__)

@app.route("/")
def home():
    f = open("index.html", "r")
    return f.read()
@app.route("/api", methods=["GET", "POST"])
def api():
    if request.method == 'GET':
        # If a GET request is made, check if 'data' parameter exists in the query string.
        user_data = request.args.get('data')
    elif request.method == 'POST':
        # If a POST request is made, check if 'data' is in the request form data.
        user_data = request.form.get('data')
    try:
        # Replace 'data.csv' with your CSV file's path.
        with open('MOCK_DATA.csv', 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            rows = list(csv_reader)

        if rows:
            # Choose a random row from the CSV data.
            random_row = random.choice(rows)
            return jsonify(random_row)
        else:
            return jsonify({'error': 'CSV file is empty'}), 500

    except FileNotFoundError:
        return jsonify({'error': 'CSV file not found'}), 404

    # if user_data:
    #     return jsonify({'user_data': user_data})
    # else:
    #     return jsonify({'error': 'Data not provided'}), 400
if __name__ == "__main__":
    app.run(debug=True)
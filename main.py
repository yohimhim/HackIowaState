from flask import *
from flask_cors import CORS
import random, csv
app = Flask(__name__)
CORS(app)
@app.route("/")
def home():
    f = open("index.html", "r")
    return f.read()
@app.route("/api", methods=["GET", "POST"])
# def api():
#     if request.method == 'GET':
#         # If a GET request is made, check if 'data' parameter exists in the query string.
#         row = request.form('row')
#     elif request.method == 'POST':
#         # If a POST request is made, check if 'data' is in the request form data.
#         row = request.form['row']
#     try:
#         # Replace 'data.csv' with your CSV file's path.
#         with open('MOCK_DATA.csv', 'r') as csv_file:
#             csv_reader = csv.DictReader(csv_file)
#             rows = list(csv_reader)

#         if rows:
#             # # Choose a random row from the CSV data.
#             # random_row = random.choice(rows)
#             return jsonify(int(row))
#         else:
#             return jsonify({'error': 'CSV file is empty'}), 500

#     except FileNotFoundError:
#         return jsonify({'error': 'CSV file not found'}), 404
def api():
    try:
        # Replace 'data.csv' with your CSV file's path.
        with open('MOCK_DATA.csv', 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            rows = list(csv_reader)

        if not rows:
            return jsonify({'error': 'CSV file is empty'}), 500

        # Get the last 4 rows from the CSV data.
        last_4_rows = rows[-4:]

        return jsonify(last_4_rows)

    except FileNotFoundError:
        return jsonify({'error': 'CSV file not found'}), 404
@app.route("/add", methods=["GET", "POST"])
def add():
        # if request.method == 'POST':
        # Get the form data from the request
        username = request.form.get('username')
        spots = request.form.get('spots')
        location = request.form.get('location')
        text = request.form.get('text')
        ip_addr = request.form.get('ip-addr')
        # Create a new row with the form data
        new_row = [username, location, spots, text, ip_addr]
        print(new_row)
        csv_file_path = 'MOCK_DATA.csv'
        # Open the CSV file in append mode and write the new row
        with open(csv_file_path, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(new_row)
    # if request.method == 'GET':
    #     # If a GET request is made, check if 'data' parameter exists in the query string.
    #     user_data = request.args.get('data')
    # elif request.method == 'POST':
    #     # If a POST request is made, check if 'data' is in the request form data.
    #     user_data = request.form.get('data')
    # try:
    #     # Replace 'data.csv' with your CSV file's path.
    #     with open('MOCK_DATA.csv', 'w') as csv_file:
    #         csv_reader = csv.DictReader(csv_file)
    #         rows = list(csv_reader)


    #     # Open the CSV file in append mode (if it exists) or create a new one
    #     with open("MOCK_DATA.csv", mode='a', newline='') as file:
    #         writer = csv.writer(file)

    #         # Write the new row to the CSV file
    #         writer.writerow(new_row)
    #     if rows:
    #         # Choose a random row from the CSV data.
    #         random_row = random.choice(rows)
    #         return jsonify(random_row)
    #     else:
    #         return jsonify({'error': 'CSV file is empty'}), 500

    # except FileNotFoundError:
    #     return jsonify({'error': 'CSV file not found'}), 404
        return "<script>window.location = 'http://127.0.0.1:9000';</script>"
if __name__ == "__main__":
    app.run(debug=True)
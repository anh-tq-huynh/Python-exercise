import json
from flask import Flask, Response, request
import mysql.connector

connection = mysql.connector.connect(
    host="127.0.0.1",
    port = 3306,
    database = 'flight_game',
    user='root',
    password='121100',
    autocommit = True,
    collation = 'utf8mb4_general_ci'
)


app = Flask(__name__)
@app.route("/airport/<icao>")
def airport(icao):
    try:
        icao_sql = f'SELECT NAME, MUNICIPALITY FROM AIRPORT WHERE IDENT = "{icao}"'
        icao_cursor = connection.cursor()
        icao_cursor.execute(icao_sql)
        result = icao_cursor.fetchall()
        if icao_cursor.rowcount >0:
            for row in result:
                response = {
                    "ICAO": icao,
                    "Name": row[0],
                    "Location": row[1]
                }
        response_json = json.dumps(response)
        http_response = Response(response_json, status=200, mimetype='application/json')
        return http_response
    except ValueError:
        response = {
            "message" : 'Invalid input',
            "status": 400
        }

@app.errorhandler(404)
def not_found(error):
    response = {
        "message": "Not Found",
        "status": 404
    }
    json_response = json.dumps(response)
    http_response = Response(json_response, status=404, mimetype='application/json')
    return http_response

if __name__ == "__main__":
    app.run(host = '127.0.0.1', port = 8000)
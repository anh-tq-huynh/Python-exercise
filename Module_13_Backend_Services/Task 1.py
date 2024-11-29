import json
from flask import Flask, Response

app = Flask(__name__)
@app.route("/prime-number/<number>")
def prime_number(number):
    try:
        count = 0
        for num in range(1,number+1):
            if number%num == 0:
                count += 1
        if count == 2:
            response = [
                {"Number": number,
                 "isPrime": "True"}
            ]
        else:
            response = [
                {"Number": number,
                 "isPrime": "False"}
            ]
        json_response= json.dumps(response)
        http_response = Response(response = json_response, status=200, mimetype='application/json')
        return http_response
    except ValueError:
        response = [
            {"message": "Invalid value input",
             "status":400}
        ]
@app.errorhandler(404)
def page_not_found(error_code):
    response = [
        {"message": "Not Found",
         "status":404}
    ]
    json_response = json.dumps(response)
    http_response = Response(response=json_response, status=200, mimetype='application/json')
    return http_response

if __name__ == "__main__":
    app.run(use_reLoader=True, host = '127.0.0.1', port = 5000)
from flask import Flask, jsonify, request

import random
from BackSolver import *
 

app = Flask(__name__)

difficult = 2
mynewgame, original = new_sudoku_board(difficult)


@app.route('/api/sudoku', methods=['GET'])
def get_sudoku():
    global mynewgame, original
    return jsonify({"board": mynewgame, "solution": original})

@app.route('/api/validate', methods=['POST'])
def validate_solution():
    user_solution = request.get_json()
    global original
    if test_if_equal(user_solution, original) == True:
        return jsonify({"valid": True})
    else:
        return jsonify({"valid": False})
    
    
if __name__ == '__main__':
    app.run(debug=True)
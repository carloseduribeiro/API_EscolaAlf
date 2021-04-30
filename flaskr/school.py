from datetime import date
from random import randint

from bson.json_util import dumps, loads
from flask import Flask, request

from db import Banco


# Generate a number registration and return:
def generate_registration() -> int:
    # Format: YYYY|Year period (10/20)|Random (4 digits)
    reg_result = date.today().strftime('%y')
    reg_result += str(10 if date.today().month <= 6 else 20)
    reg_result += f"{str(randint(1, 999)) + str(randint(1, 9)):0>4}"
    return int(reg_result)


# Convert a string date to iso format (YYYY-MM-DD):
def convert_str_to_iso_date(current: str) -> str:
    final = current.split('/') if '/' in current else current.split('-')
    if len(final[0]) == 2:
        final.reverse()
    return '-'.join(final)


# Checks whether the body request keys is as expected:
def body_request_is_valid(current_keys: list, expected: list) -> bool:
    expected.sort()
    current_keys.sort()
    return False if current_keys != expected else True


def exam_is_valid(body_request: dict) -> bool:
    exam = body_request.copy()
    # Remove other keys:
    exam.pop("name")
    exam.pop("access_token")

    # Checks the number of questions:
    if len(exam.keys()) > 20 or len(exam.keys()) == 20:
        return False

    total_weight = 0.0
    for num, quest in exam.items():
        # Checks if de number str have a integer:
        try:
            int(num)
        except ValueError:
            return False

        # Checks if the answer is in the list of alternatives:
        if quest['answer'] not in quest['alternatives']:
            return False

        total_weight += quest['weight']

    # Checks if total weight is 10:
    if total_weight != 10.0:
        return False
    return True


app = Flask("__name__")

# Create DB:
db = Banco()
access_token = "dc599a9972fde3045dab59dbd1ae170b"


# ---- ESCOLA ----:

# GET: /school/students: retorna todos os alunos matriculados.
@app.route("/school/students", methods=['GET'])
def get_students():
    # Get body request:
    raw_request = request.data.decode('utf-8')
    body_request = loads(raw_request)
    token = str(body_request['access_token'])

    # Check if access token was privded or valid:
    if not token:
        return "Error: access token was not provided!", 400
    elif token != access_token:
        return "Error: invalid access token!"

    result_data = dumps(db.student.find({}, {"_id": 0}))
    return result_data


# POST: /school/student: cadastra um novo aluno.
@app.route("/school/student", methods=['POST'])
def create_student():
    pass


# GET: /school/exams: retorna todos as provas cadastradas.
@app.route("/school/exams", methods=['GET'])
def get_school_exams():
    pass


# POST: /school/exam: cadastra uma nova prova.
@app.route("/school/exam", methods=['POST'])
def create_exam():
    pass


# ---- ALUNO: ----

# GET: /student/{matricula}/exams: retorna todas as provas do aluno.
@app.route("/student/<int:reg>/exams", methods=['GET'])
def get_student_exams(reg=None):
    pass


# GET: /student/{matricula}/exam/{id}: retorna todas as questões e alternativas da prova do aluno.
@app.route("/student/<int:reg>/exam/<int:id_exam>")
def get_student_exam(reg=None, id_exam=None):
    pass


# POST: /student/{matricula}/exam: cadastra as repostas do aluno (realiza a prova).
@app.route("/student/<int:reg>/exam")
def create_student_exam_answer(reg=None):
    pass


if __name__ == "__main__":
    app.run(debug=True)

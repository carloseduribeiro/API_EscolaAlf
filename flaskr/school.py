from datetime import date, time
from random import randint

from bson.json_util import dumps, loads
from flask import Flask, request

from db import Banco


def generate_registration() -> int:
    reg_result = date.today().strftime('%y')
    reg_result += str(10 if date.today().month <= 6 else 20)
    reg_result += str(randint(1, 9999))
    return int(reg_result)


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

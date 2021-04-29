from flask import Flask
from db import Banco

app = Flask("__name__")

# Create DB:
db = Banco()


# ---- ESCOLA ----:

# GET: /school/students: retorna todos os alunos matriculados.
@app.route("/school/students", methods=['GET'])
def get_students():
    pass


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

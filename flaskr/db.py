from pymongo import MongoClient


class Banco:

    def __init__(self):
        # Create a conection with mongodb:
        self.__conn = MongoClient(host="localhost", port=27017)
        self.__db = self.__conn.alf_db  # create db.

        # Creates collections for students and exams:
        self.student = self.__db.student
        self.exam_answers = self.__db.exam_answers
        self.exam = self.__db.exam

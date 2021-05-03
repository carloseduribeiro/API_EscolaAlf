from datetime import date
from random import randint


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


# Checks questions of exam:
def exam_is_valid(body_request: dict) -> tuple:
    exam = body_request.copy()
    # Remove other keys:
    exam.pop("name")
    exam.pop("access_token")

    # Checks the number of questions:
    if len(exam.keys()) > 20 or len(exam.keys()) == 20:
        return "Message: The number of questions is invalid.", False

    total_weight = 0.0
    for num, quest in exam.items():
        # Checks if the number str have a integer:
        try:
            int(num)
        except ValueError:
            return "Message: The question number must be numeric.", False

        # Checks if the answer is in the list of alternatives:
        if quest['answer'] not in quest['alternatives']:
            return f"Message: The answer of question '{num}' not exists in the alternatives.", False

        if quest['weight'] == 0:
            return f"Message: The weight of question '{num}' must be greater than 0.", False

        total_weight += quest['weight']

    # Checks if total weight is 10:
    if total_weight != 10.0:
        return f"Message: The sum of the weights must be equal to ten.", False
    return "", True


# Checks if answers of exam:
def answers_is_valid(body_request: dict) -> tuple:
    answers = body_request.copy()

    # Remove other keys:
    answers.pop("id_exam")
    answers.pop("registration")

    for num, answer in answers.items():
        # Checks if the number str have a integer:
        try:
            int(num)
        except ValueError:
            return "Message: The question number must be numeric.", False

        # Checks whether the answer is a one len string:
        try:
            if not isinstance(answer, str) or len(answer) != 1:
                raise Exception(f"Message: The answer of question {num} must be one letter.")
        except Exception as error:
            return error.args[0], False

    return "", True

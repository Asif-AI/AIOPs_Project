from setuptools import setup, find_packages

REQUIREMENT_FILE_NAME = "requirements.txt"
REMOVE_PACKAGE = "-e ."

def get_requirement_list(requirement_file_name = REQUIREMENT_FILE_NAME)->list:
    try:
        rerquirement_list = None
        with open(requirement_file_name, 'r') as requirement_file:
            requirement_list = [requirement.replace("\n", " ") for requirement in requirement_file.readlines()]
            requirement_list.remove(REMOVE_PACKAGE)
        return requirement_list
    except Exception as e:
        raise e


setup(
    name = "LSTM_TextClassification",
    version = "0.0.1",
    description = "LSTM Based Text Classification",
    author = "Asif Khan",
    packages = find_packages(),
    install_requires = get_requirement_list()

)

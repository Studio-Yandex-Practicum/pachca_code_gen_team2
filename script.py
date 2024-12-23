import ast
import os

from jinja2 import Environment, FileSystemLoader


def extract_functions_from_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        tree = ast.parse(file.read())

    functions = []
    for node in ast.walk(tree):
        if isinstance(node, ast.AsyncFunctionDef) or isinstance(node, ast.FunctionDef):
            functions.append(ast.unparse(node))
    return functions

def get_all_api_functions(api_dir):
    all_functions = []
    for root, _, files in os.walk(api_dir):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                functions = extract_functions_from_file(file_path)
                all_functions.extend(functions)
    return all_functions


api_dir = "./pachca-api-open-api-3-0-client/pachca_api_open_api_3_0_client/api"
endpoints = get_all_api_functions(api_dir)

env = Environment(
    loader=FileSystemLoader('templates')
)

client_template = env.get_template('client.py.jinja')

client_path = './pachca-api-open-api-3-0-client/pachca_api_open_api_3_0_client/client.py'

with open(client_path, mode='w') as file:
    file.write(client_template.render(endpoints=endpoints))

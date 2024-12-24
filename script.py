import ast
import os

from jinja2 import Environment, FileSystemLoader


def extract_functions_and_imports_from_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        tree = ast.parse(file.read())

    functions = []
    imports = []
    
    for node in ast.walk(tree):
        if isinstance(node, ast.AsyncFunctionDef) or isinstance(node, ast.FunctionDef):
            functions.append(ast.unparse(node))
        elif isinstance(node, ast.ImportFrom):
            # Убираем пробел после 'from' и обрабатываем импорты
            module = node.module if node.module else ''
            if module.startswith('.'):
                module = module[1:]  # Убираем точку в начале
            for alias in node.names:
                if module == 'typing' or module == 'http':
                    imports.append(f"from {module} import {alias.name}")
                else:
                    imports.append(f"from .{module} import {alias.name}")

    return functions, imports


def get_all_api_functions_and_imports(api_dir):
    all_functions = []
    all_imports = []
    for root, _, files in os.walk(api_dir):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                functions, imports = extract_functions_and_imports_from_file(file_path)
                all_functions.extend(functions)
                all_imports.extend(imports)
    return all_functions, all_imports


api_dir = "./pachca-api-open-api-3-0-client/pachca_api_open_api_3_0_client/api"
endpoints, imports = get_all_api_functions_and_imports(api_dir)

env = Environment(
    loader=FileSystemLoader('templates')
)

client_template = env.get_template('client.py.jinja')

client_path = './pachca-api-open-api-3-0-client/pachca_api_open_api_3_0_client/client.py'

with open(client_path, mode='w', encoding="utf-8") as file:
    # Объединяем импорты в одну строку
    unique_imports = list(set(imports))  # Убираем дубликаты
    file.write("\n".join(unique_imports) + "\n\n")  # Записываем импорты в файл
    file.write(client_template.render(endpoints=endpoints))

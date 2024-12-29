# import ast
# import os
# import subprocess

# import yaml
# from jinja2 import Environment, FileSystemLoader


# def extract_functions_and_imports_from_file(file_path) -> None:
#     with open(file_path, "r", encoding="utf-8") as file:
#         tree = ast.parse(file.read())

#     functions = []
#     imports = []

#     for node in ast.walk(tree):
#         if isinstance(node, ast.AsyncFunctionDef) or isinstance(node,
#                                                                 ast.FunctionDef):
#             functions.append(ast.unparse(node))
#         elif isinstance(node, ast.ImportFrom):
#             # Убираем пробел после 'from' и обрабатываем импорты
#             module = node.module if node.module else ''
#             if module.startswith('.'):
#                 module = module[1:]  # Убираем точку в начале
#             for alias in node.names:
#                 if module == 'typing' or module == 'http':
#                     imports.append(f"from {module} import {alias.name}")
#                 else:
#                     imports.append(f"from .{module} import {alias.name}")

#     return functions, imports


# def get_all_api_functions_and_imports(api_dir):
#     all_functions = []
#     all_imports = []
#     for root, _, files in os.walk(api_dir):
#         for file in files:
#             if file.endswith(".py"):
#                 file_path = os.path.join(root, file)
#                 functions, imports = extract_functions_and_imports_from_file(file_path)
#                 all_functions.extend(functions)
#                 all_imports.extend(imports)
#     return all_functions, all_imports


# def create_modified_openapi_yaml(input_path, output_path):
#     with open(input_path, "r", encoding="utf-8") as file:
#         openapi_data = yaml.safe_load(file)
#     base_url = openapi_data.get("servers", [{}])[0].get("url")
#     openapi_data["x-base-url"] = base_url

#     with open(output_path, "w", encoding="utf-8") as file:
#         yaml.dump(openapi_data, file)

#     return base_url


# def generate_client(openapi_path, templates_path):
#     command = [
#         "openapi-python-client",
#         "generate",
#         "--path", openapi_path,
#         "--custom-template-path", templates_path,
#         "--overwrite"
#     ]
#     subprocess.run(command, check=True)


# def process_generated_client(api_dir, client_template_path, client_output_path, base_url):
#     endpoints, imports = get_all_api_functions_and_imports(api_dir)

#     env = Environment(loader=FileSystemLoader('templates'))
#     client_template = env.get_template(client_template_path)

#     with open(client_output_path, mode='w', encoding="utf-8") as file:
#         # Объединяем импорты в одну строку
#         unique_imports = list(set(imports))  # Убираем дубликаты
#         file.write("\n".join(unique_imports) + "\n\n")  # Записываем импорты в файл
#         file.write(client_template.render(endpoints=endpoints, base_url=base_url))


# openapi_input_path = "openapi.yaml"
# openapi_modified_path = "openapi_modified.yaml"
# templates_path = "./templates"
# api_dir = "./pachca-api-open-api-3-0-client/pachca_api_open_api_3_0_client/api"
# client_template_name = "client.py.jinja"
# client_output_path = "./pachca-api-open-api-3-0-client/pachca_api_open_api_3_0_client/client.py"

# # Выполнение шагов
# base_url = create_modified_openapi_yaml(openapi_input_path, openapi_modified_path)
# generate_client(openapi_modified_path, templates_path)
# process_generated_client(api_dir, client_template_name, client_output_path, base_url)

import ast
import os

import yaml
from jinja2 import Environment, FileSystemLoader


def extract_functions_and_imports_from_file(file_path) -> None:
    with open(file_path, "r", encoding="utf-8") as file:
        tree = ast.parse(file.read())

    functions = []
    imports = []

    for node in ast.walk(tree):
        if isinstance(node, ast.AsyncFunctionDef) or isinstance(node,
                                                                ast.FunctionDef):
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


def get_base_url_from_yaml(openapi_yaml):
    with open(openapi_yaml, "r", encoding="utf-8") as file:
        data = yaml.safe_load(file)
    return data['servers'][0]['url']


api_dir = "./pachca-api-open-api-3-0-client/pachca_api_open_api_3_0_client/api"
openapi_yaml = "openapi.yaml"
endpoints, imports = get_all_api_functions_and_imports(api_dir)
base_url = get_base_url_from_yaml(openapi_yaml)

env = Environment(
    loader=FileSystemLoader('templates'),
)

client_template = env.get_template('client.py.jinja')

client_path = './pachca-api-open-api-3-0-client/pachca_api_open_api_3_0_client/client.py'

with open(client_path, mode='w', encoding="utf-8") as file:
    # Объединяем импорты в одну строку
    unique_imports = list(set(imports))  # Убираем дубликаты
    file.write("\n".join(unique_imports) + "\n\n")  # Записываем импорты в файл
    file.write(client_template.render(endpoints=endpoints, base_url=base_url))

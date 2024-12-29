# import ast
# import os

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


# api_dir = "./pachca-api-open-api-3-0-client/pachca_api_open_api_3_0_client/api"
# endpoints, imports = get_all_api_functions_and_imports(api_dir)

# env = Environment(
#     loader=FileSystemLoader('templates')
# )

# client_template = env.get_template('client.py.jinja')

# client_path = './pachca-api-open-api-3-0-client/pachca_api_open_api_3_0_client/client.py'

# with open(client_path, mode='w', encoding="utf-8") as file:
#     # Объединяем импорты в одну строку
#     unique_imports = list(set(imports))  # Убираем дубликаты
#     file.write("\n".join(unique_imports) + "\n\n")  # Записываем импорты в файл
#     file.write(client_template.render(endpoints=endpoints))



import ast
import os

from jinja2 import Environment, FileSystemLoader


def extract_functions_and_imports_from_file(file_path) -> None:
    with open(file_path, "r", encoding="utf-8") as file:
        tree = ast.parse(file.read())

    functions = []
    imports = []

    for node in ast.walk(tree):
        if isinstance(node, ast.AsyncFunctionDef) or isinstance(node, ast.FunctionDef):
            functions.append(ast.unparse(node))
        elif isinstance(node, ast.ImportFrom):
            module = node.module if node.module else '.'
            # if module.startswith('.'):
            #     module = module[1:]  # Убираем точку в начале
            for alias in node.names:
                if module == 'typing':
                    imports.append(f"from typing import {alias.name}")
                elif module.startswith('models'):
                    imports.append(f"from .models import {alias.name}")
                elif module == 'types':
                    imports.append(f"from .types import {alias.name}")
                else:
                    imports.append(f"from {module} import {alias.name}")

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


api_dir = "./pachca_servis/pachca_api_open_api_3_0_client/api"
endpoints, imports = get_all_api_functions_and_imports(api_dir)

env = Environment(
    loader=FileSystemLoader('templates')
)

client_template = env.get_template('client.py.jinja')

client_path = './pachca_servis/pachca_api_open_api_3_0_client/client.py'

with open(client_path, mode='w', encoding="utf-8") as file:
    unique_imports = list(set(imports))
    models_imports = sorted([model for model in unique_imports if model.startswith('from .models')])
    typing_imports = sorted([model for model in unique_imports if model.startswith('from typing import')])
    types_imports = sorted([model for model in unique_imports if model.startswith('from .types import')])
    other_imports = sorted(list(
        set(unique_imports) - set(typing_imports) - set(types_imports) - set(models_imports)))
    if models_imports:
        models_imports_str = "from .models import (\n    " + ",\n    ".join(
            [model.split('from .models import ')[-1] for model in models_imports]) + "\n)"
        file.write(models_imports_str + "\n\n")
    if typing_imports:
        typing_imports_str = "from typing import (\n    " + ",\n    ".join(
            [model.split('from typing import ')[-1] for model in typing_imports]) + "\n)"
        file.write(typing_imports_str + "\n\n")
    if types_imports:
        types_imports_str = "from .types import (\n    " + ",\n    ".join(
            [model.split('from .types import ')[-1] for model in types_imports]) + "\n)"
        file.write(types_imports_str + "\n\n")
    if other_imports:
        file.write("\n".join(other_imports) + "\n\n")
    file.write(client_template.render(endpoints=endpoints))

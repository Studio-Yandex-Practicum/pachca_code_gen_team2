from yaml_loader import YAML_DICT


def load_schema(path_to_schema: str):
    schema_name = path_to_schema.split('/')[-1]
    return YAML_DICT.get('components').get('schemas').get(schema_name)


def replace_ref_with_schema(schema: dict):
    schema_name = list(schema.keys())[0]
    if 'properties' in schema.get(schema_name):
        current_schema = schema.get(schema_name).get('properties')
    if 'items' in schema.get(schema_name):
        current_schema = schema.get(schema_name).get('items')
    for property in current_schema:
        if '$ref' in current_schema.get(property):
            current_schema[property] = load_schema(
                current_schema.get(property).get('$ref'))
    return schema


def simple_replace_ref_with_schema(schema):
    key = ''
    if 'properties' in schema:
        key = 'properties'
    elif 'items' in schema:
        key = 'items'
    else:
        return schema
    if '$ref' not in schema[key]:
        return schema
    schema[key] = load_schema(schema[key].get('$ref'))
    return schema

from yaml_loader import YAML_DICT


def load_schema(path_to_schema: str) -> dict:
    """Возвращает схему из ссылки."""
    schema_name = path_to_schema.split('/')[-1]
    return YAML_DICT.get('components').get('schemas').get(schema_name)


def replace_ref_with_schema(schema: dict) -> dict:
    # print(schema, '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
    """Заменяет ссылку на схему самой схемой."""
    schema_name = next(iter(schema.keys()))
    if 'allOf' in schema[schema_name]:
        all_inherits = [ingerit for ingerit in schema[schema_name]['allOf'] if '$ref' in ingerit]
        all_non_inherits = [ingerit for ingerit in schema[schema_name]['allOf'] if '$ref' not in ingerit]
        temp = {}
        for inherit in all_inherits:
            inheritable = load_schema(inherit['$ref'])
            if all_non_inherits: 
                all_non_inherits[0]['properties'] |= inheritable.get('properties') or inheritable.get('items')
            else:
                temp |= inheritable.get('properties') or inheritable.get('items')
        if all_non_inherits:
            schema[schema_name] = all_non_inherits[0]
        else:
            if 'items' in temp:
                schema[schema_name] = temp.get('items')
            elif 'properties' in temp:
                schema[schema_name] = temp
            else:
                schema[schema_name] = {'properties': temp}
            # schema[schema_name] = {'propertiess': schema[schema_name]}
        # print(schema, '---------------------------------------------------------------')
        return schema
    if 'properties' in schema.get(schema_name):
        current_schema = schema.get(schema_name).get('properties')
    if 'items' in schema.get(schema_name):
        current_schema = schema.get(schema_name).get('items')
    for property in current_schema:
        if '$ref' in current_schema.get(property):
            current_schema[property] = load_schema(
                current_schema.get(property).get('$ref'))

    # print(schema, '---------------------------------------------------------------')    
    return schema


def simple_replace_ref_with_schema(schema: dict) -> dict:
    """Заменяет ссылку на схему самой схемой."""
    key = ''
    if 'properties' in schema:
        key = 'properties'
    elif 'items' in schema:
        key = 'items'
    elif 'allOf' in schema:
        return load_schema(schema['allOf'][0]['$ref'])
    else:
        return schema
    if '$ref' not in schema[key]:
        return schema
    schema[key] = load_schema(schema[key].get('$ref'))
    return schema

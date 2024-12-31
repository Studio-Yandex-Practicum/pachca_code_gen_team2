from yaml_loader import YAML_DICT


def unite_schemas(schemas: list[dict], schema2: dict):
    for schema in schemas:
        schema2['type'] = schema2.get('type') or schema.get('type')
        required_proprties = schema2.get('required', [])
        required_proprties.extend(schema.get('required', []))
        schema2['required'] = list(set(required_proprties))
        if schema2['type'] == 'object':
            schema2['properties'] = (
                schema.get('properties', {}) | schema2.get('properties', {})
            )
        if schema2['type'] == 'array':
            if 'items' in schema2 and schema2['items'].get('properties'):
                required_proprties = schema2['items'].get('required', [])
                required_proprties.extend(schema['items'].get('required', []))
                schema2['required'] = list(set(required_proprties))
                print(schemas)
                print(schema2)
                schema2['items']['properties'] = (
                    schema.get('items').get('properties') | schema2.get('items').get('properties')
                )
            else:
                schema2['items'] = (
                    schema.get('items', {}) | schema2.get('items', {})
                )
    return schema2


def load_schema(path_to_schema: str) -> dict:
    """Возвращает схему из ссылки."""
    schema_name = path_to_schema.split('/')[-1]
    return YAML_DICT.get('components').get('schemas').get(schema_name)


def new_replace_ref_with_schema(schema: dict):
    if '$ref' in schema:
        return load_schema(schema['$ref'])

    if 'allOf' in schema:
        all_inherits = [new_replace_ref_with_schema(load_schema(ingerit['$ref'])) for ingerit in schema['allOf'] if '$ref' in ingerit]
        all_non_inherits = [ingerit for ingerit in schema['allOf'] if '$ref' not in ingerit]
        if not all_non_inherits:
            all_non_inherits = [{}]
        temp = all_non_inherits[0]
        temp = unite_schemas(all_inherits, temp)
        schema = temp
    schema_name = next(iter(schema.keys()))
    if 'allOf' in schema[schema_name]:
        schema[schema_name] = new_replace_ref_with_schema(schema[schema_name])
    return schema


def replace_ref_with_schema(schema: dict) -> dict:
    """OBSOLETE"""
    """Заменяет ссылку на схему самой схемой."""
    schema_name = next(iter(schema.keys()))
    final_result = {}
    if 'allOf' == schema_name:
        all_inherits = [ingerit for ingerit in schema[schema_name] if '$ref' in ingerit]
        # print(all_inherits)
        temp = {}
        for inherit in all_inherits:
            temp |= load_schema(inherit['$ref'])
        final_result = temp
    if 'allOf' in schema[schema_name]:
        if 'allOf' != schema_name:
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
        final_result = schema
    if 'allOf' in final_result:
        replace_ref_with_schema(final_result)
    if final_result:
        return final_result
    if 'properties' in schema.get(schema_name):
        current_schema = schema.get(schema_name).get('properties')
    elif 'items' in schema.get(schema_name):
        current_schema = schema.get(schema_name).get('items')
    else:
        return schema
    for property in current_schema:
        if '$ref' in current_schema.get(property):
            current_schema[property] = load_schema(
                current_schema.get(property).get('$ref'))
    return schema


def simple_replace_ref_with_schema(schema: dict) -> dict:
    """OBSOLETE"""
    """Заменяет ссылку на схему самой схемой."""
    key = ''
    if 'properties' in schema:
        key = 'properties'
    elif 'items' in schema:
        key = 'items'
    elif 'allOf' in schema:
        # print(schema['allOf'][0]['$ref'])
        # print(load_schema(schema['allOf'][0]['$ref']), '=========================')
        return load_schema(schema['allOf'][0]['$ref'])
    else:
        return schema
    if '$ref' not in schema[key]:
        return schema
    schema[key] = load_schema(schema[key].get('$ref'))
    return schema

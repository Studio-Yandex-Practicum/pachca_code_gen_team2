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
                schema2['items']['properties'] = (
                    schema.get('items').get('properties') | schema2.get('items').get('properties')
                )
            else:
                schema2['items'] = (
                    schema.get('items', {}) | schema2.get('items', {})
                )
    return schema2


def load_schema(path_to_schema: str, is_parameter: bool = False) -> dict:
    """Возвращает схему из ссылки."""
    schema_name = path_to_schema.split('/')[-1]
    if is_parameter:
        return YAML_DICT.get('components').get('parameters').get(schema_name)
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
        return load_schema(schema['allOf'][0]['$ref'])
    else:
        return schema
    if '$ref' not in schema[key]:
        return schema
    schema[key] = load_schema(schema[key].get('$ref'))
    return schema


def replace_refs_with_schemas(data):
    """
    Recursively walk through a dictionary and replace any value that is a dict with
    the structure {'$ref': 'string'} with the result of load_schema(value['$ref']).
    Additionally, for 'items' or 'properties' keys, process 'allOf' or single '$ref' when present.

    :param data: The dictionary to process.
    :param load_schema: A function that takes a reference string and returns the corresponding schema.
    :param unite_schemas: A function that takes a list of schemas from '$ref' and another object to unite them.
    :return: The processed dictionary with all necessary replacements.
    """
    if isinstance(data, dict):
        for key, value in list(data.items()):  # Use list to avoid runtime changes during iteration
            if isinstance(value, dict):
                if '$ref' in value and len(value) == 1:
                    # Replace the {'$ref': 'string'} structure with the loaded schema
                    ref_value = value['$ref']
                    data[key] = load_schema(ref_value)
                elif key in ['items', 'properties'] and isinstance(data[key], dict):
                    # Process 'allOf' or '$ref' when present
                    resolved_value = data[key]
                    if 'allOf' in resolved_value:
                        all_of = resolved_value['allOf']
                        if isinstance(all_of, list):
                            ref_schemas = [load_schema(ref['$ref']) for ref in all_of if '$ref' in ref]
                            other_schemas = [obj for obj in all_of if not '$ref' in obj]
                            if other_schemas:
                                united_schema = unite_schemas(ref_schemas, other_schemas[0])
                                data[key] = united_schema
                            else:
                                data[key] = unite_schemas(ref_schemas, {})
                    elif '$ref' in resolved_value and len(resolved_value) == 1:
                        # Process a single $ref in items or properties
                        ref_value = resolved_value['$ref']
                        data[key] = load_schema(ref_value)
                    else:
                        # Recursively process nested dictionaries
                        data[key] = replace_refs_with_schemas(resolved_value)
                else:
                    # Recursively process nested dictionaries
                    data[key] = replace_refs_with_schemas(value)
    elif isinstance(data, list):
        for i, item in enumerate(data):
            # Recursively process items in lists
            data[i] = replace_refs_with_schemas(item)
    return data


if __name__ == '__main__':
    d = {'ResponseEditmessagePut200': {'type': 'object', 'properties': {'data': {'type': 'array', 'description': 'Созданное сообщение', 'items': {'$ref': '#/components/schemas/Message'}}}}}
    print(replace_refs_with_schemas(d))

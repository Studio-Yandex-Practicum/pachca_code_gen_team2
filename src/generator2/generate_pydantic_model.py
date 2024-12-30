from constants import ENUM_TYPES, PYTHON_TYPES
from schema_link_processor import (
    new_replace_ref_with_schema,
)


def create_model(name: str, fields: list) -> str:
    """Генерирует код модели Pydantic."""
    model_code = f'class {name}(BaseModel):\n'
    for field in fields:
        if field[2]:
            model_code += (
                f'    {field[0]}: {field[1]} '
                f'= Field(..., description=\'{field[3]}\')\n'
            )
        else:
            model_code += (
                f'    {field[0]}: Optional[{field[1]}] '
                f'= Field(None, description=\'{field[3]}\')\n'
            )
    return model_code


def create_enum(name: str, enum_type: str, fields: list):
    enum_class_code = f'class enum_{name}({ENUM_TYPES.get(enum_type)}):\n'
    if enum_type == 'string':
        for field in fields:
            enum_class_code += f'    {field} = \'{field}\'\n'
    if enum_type == 'integer':
        for field in fields:
            enum_class_code += f'    {name}_{field} = {field}\n'
    return enum_class_code


def look_into_schema_new(schema: dict):
    schema = new_replace_ref_with_schema(schema)
    list_of_properties = []
    nested_properties = []
    enum_properties = []
    required_properties = []
    upper_schema_name = list(schema.keys())[0]
    inner_schema = (
        schema.get(upper_schema_name).get('properties')
        or schema.get(upper_schema_name).get('items',{}).get('properties')
        or schema.get(upper_schema_name).get('items',{}).get('items', {}).get('properties'))
    required_properties = schema.get(upper_schema_name).get('required', [])
    for property in inner_schema:
        inner_body = new_replace_ref_with_schema(inner_schema.get(property))
        if 'enum' in inner_body:
            enum_properties.append(
                (property, inner_body.get('type'),  inner_body['enum']),
            )
        inner_schema[property] = inner_body
        description = inner_body.get('description', 'No docstring provided')
        property_type = (
            PYTHON_TYPES.get(inner_body.get('type')) or inner_body.get('type'))
        if 'enum' in inner_body:
            property_type = f'enum_{property}'
        if property_type == 'object':
            property_type = property.capitalize()
        if property_type == 'array':
            list_type = inner_body.get("items").get("type")
            list_type = PYTHON_TYPES.get(list_type, list_type)
            if list_type == 'object' or list_type == 'array':
                list_type = property.capitalize()
            property_type = (f'List[{list_type}]')
        list_of_properties.append(
            (
                property,
                property_type,
                True if property in required_properties else False,
                description,
            ),
        )
        if ('allOf' in inner_body
           or inner_body.get('type') == 'object'
           or inner_body.get('type') == 'array'
           and inner_body.get('items', {}).get('properties')
           or inner_body.get('items', {}).get('items')):
            nested_properties.append(property)
    for nested in nested_properties:
        nested_obj = new_replace_ref_with_schema(inner_schema)
        if nested in nested_obj: 
            look_into_schema_new(
            {nested.capitalize(): nested_obj[nested]}
                )
        else:
            look_into_schema_new(nested_obj)
    for enum_class in enum_properties:
        print(create_enum(*enum_class))
    print(create_model(upper_schema_name, list_of_properties))


def look_into_schema(schema: dict) -> None:
    """Рекурсивно разбирает схемы.

    Генерирует модели pydantic для requestBody.
    """
    list_of_properties = []
    nested_properties = []
    enum_properties = []
    required_properties = []
    upper_schema_name = list(schema.keys())[0]
    inner_schema = schema.get(upper_schema_name).get('properties')
    required_properties = schema.get(upper_schema_name).get('required', [])
    for property in inner_schema:
        inner_body = new_replace_ref_with_schema(inner_schema.get(property))        
        # print(property, inner_body, '777777777777777777777777777777777777777777777777777777777777777777')
        if 'enum' in inner_body:
            enum_properties.append(
                (property, inner_body.get('type'),  inner_body['enum']),
            )
        description = inner_body.get('description', 'No docstring provided')
        property_type = (
            PYTHON_TYPES.get(inner_body.get('type')) or inner_body.get('type'))
        if 'enum' in inner_body:
            property_type = f'enum_{property}'
        if property_type == 'object':
            property_type = property.capitalize()
        # print(inner_body, '33333333333333333333333333333333333333333333333333333333333333')
        if property_type == 'array':
            list_type = inner_body.get("items").get("type")
            list_type = PYTHON_TYPES.get(list_type, list_type)
            if list_type == 'object' or list_type == 'array':
                list_type = property.capitalize()
            property_type = (f'List[{list_type}]')
        list_of_properties.append(
            (
                property,
                property_type,
                True if property in required_properties else False,
                description,
            ),
        )
        # print(property, inner_body, '=========================================================')
        if (inner_body.get('type') == 'object'
           or inner_body.get('type') == 'array'
           and inner_body.get('items', {}).get('properties')
           or inner_body.get('items', {}).get('items')):
            nested_properties.append(property)
    for nested in nested_properties:
        if ('items' in inner_schema.get(nested)
           and inner_schema.get(nested).get('items').get('properties')):
            look_into_schema(new_replace_ref_with_schema(
                {nested.capitalize(): inner_schema.get(nested).get('items')}),
            )
        elif ('items' in inner_schema.get(nested)
              and inner_schema.get(nested).get('items').get('items')):
            look_into_schema(new_replace_ref_with_schema(
                {
                    nested.capitalize():
                    inner_schema.get(nested).get('items').get('items'),
                }),
            )
        else:
            look_into_schema(new_replace_ref_with_schema(
                {nested.capitalize(): inner_schema.get(nested)}),
            )
    for enum_class in enum_properties:
        print(create_enum(*enum_class))
    print(create_model(upper_schema_name, list_of_properties))

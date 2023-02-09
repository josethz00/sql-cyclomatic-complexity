from os import path


def parse_schema(schema_string):
    table_count = 0
    in_table = False
    relation_count = 0
    for line in schema_string.splitlines():
        if line.startswith("CREATE TABLE"):
            in_table = True
            relation_count = 0
        elif in_table and "FOREIGN KEY" in line:
            relation_count += 1
        elif in_table and (line.startswith(");") or line.startswith(");\n")):
            in_table = False
            if relation_count == 1:
                table_count += 1
    return table_count

schema_string = open(path.join(path.dirname(__file__), "script.sql")).read()
print(parse_schema(schema_string))
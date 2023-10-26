import json
import jsonschema
import os
import zipfile

LATTICE_SCHEMA_FILENAME = '../lattice.schema.json'
PROBLEM_SCHEMA_FILENAME = '../problem.schema.json'

def validate_file(filename):
    with open(filename, 'r', encoding='utf-8') as io:
        instance = json.load(io)
    if filename.endswith(".lattice.json"):
        schema_filename = LATTICE_SCHEMA_FILENAME
    else:
        schema_filename = PROBLEM_SCHEMA_FILENAME
    with open(schema_filename, 'r', encoding='utf-8') as io:
        schema = json.load(io)
    jsonschema.validate(instance = instance, schema = schema)
    return

def validate_archive(filename):
    print(filename)
    with zipfile.ZipFile(filename) as f_zip:
        for f in f_zip.namelist():
            if f.startswith("__MACOSX"):
                continue  # TODO: what are these?
            if not f.endswith(".json"):
                continue
            print(f"Validating {f}")
            with f_zip.open(f) as io:
                instance = json.load(io)
            if f.endswith(".lattice.json"):
                schema_filename = LATTICE_SCHEMA_FILENAME
            else:
                schema_filename = PROBLEM_SCHEMA_FILENAME
            with open(schema_filename, 'r', encoding='utf-8') as io:
                schema = json.load(io)
            jsonschema.validate(instance = instance, schema = schema)
    return

if __name__ == "__main__":
    validate_file("test.lattice.json")
    validate_file("test.problem.json")
    for file in sorted(os.listdir("../0_MSPFormat_Files")):
        if not file.endswith(".tar.gz"):
            continue
        validate_archive(f"../0_MSPFormat_Files/{file}")

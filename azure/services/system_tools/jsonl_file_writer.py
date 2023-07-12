import json


def jsonl_file_writer(primers, primer_file_path):
    with open(primer_file_path, 'f') as file:
        for primer in primers:
            file.write(json.dumps({"primer": primer}) + '\n')

# The name of the file 'export.py' must match the 'entry_file' in the config.json
import os
import json

# READ TABLE ANNOTATED
file_path = f"{os.path.dirname(os.path.realpath(__file__))}/input.json"
file_open = open(file_path, encoding="utf-8")
table_annotated = json.load(file_open)

###
# HERE GOES YOUR CODE FOR EXPORT PLUGIN
###

# WRITE THE OUTPUT TO A FILE (The name of the file must match the 'output' in the 'config.json')
NAME_OF_THE_FILE_WITH_EXTENSION: str = ""
f"{os.path.dirname(os.path.realpath(__file__))}/output/{NAME_OF_THE_FILE_WITH_EXTENSION}"

# For example, if you want to serielize a graph using turtle format with 'rdflib' library, use:
# graph.serialize(destination=f"{os.path.dirname(os.path.realpath(__file__))}/output/kg.ttl", format="turtle")

import json
out=[]
with open('$PATH_TO/editsql/logs/logs_sparc_editsql/dev_use_predicted_queries_predictions.json') as f:
  for entry in f:
    data = json.loads(entry)
    out.append(data)

with open('readableJSON.txt', 'w') as json_file:
  for item in out:
    json.dump(item['input_seq'], json_file)
    json_file.write('\n')
    json.dump(item['prediction'], json_file)
    json_file.write('\n')
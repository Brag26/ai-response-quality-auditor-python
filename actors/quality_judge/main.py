import json
with open("outputs/pairs_loaded.json") as f:
    data=json.load(f)
for d in data:
    d["score"]=90
with open("outputs/pairs_scored.json","w") as f:
    json.dump(data,f,indent=2)
print("Scored pairs")

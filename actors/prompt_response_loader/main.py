import json, os
with open("sample_data/pairs.json","r") as f:
    data=json.load(f)
os.makedirs("outputs", exist_ok=True)
with open("outputs/pairs_loaded.json","w") as f:
    json.dump(data,f,indent=2)
print("Loaded pairs")

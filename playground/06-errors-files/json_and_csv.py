import json

with open("config.json", "w", encoding="utf-8") as f:
    json.dump({"debug": True}, f, indent=2)

with open("config.json", encoding="utf-8") as f:
    config = json.load(f)  # back to a dict

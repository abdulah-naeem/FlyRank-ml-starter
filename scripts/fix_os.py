import json

notebook_path = 'd:/Internships/Internship - FlyrankAI/Week 1/FlyRank-ml-starter/work/notebooks/w04_baseline_score.ipynb'
with open(notebook_path, 'r', encoding='utf-8') as f:
    nb = json.load(f)

# Insert import os into Cell 4
if "import os\n" not in nb['cells'][4]['source']:
    nb['cells'][4]['source'].insert(0, "import os\n")

with open(notebook_path, 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1)

print("Added import os to Cell 4")

import json
from jinja2 import Template

with open("outputs/pairs_scored.json") as f:
    data=json.load(f)

template=Template("<h1>Report</h1>{% for d in data %}<p>{{d.id}} - {{d.score}}</p>{% endfor %}")
html=template.render(data=data)

with open("outputs/report.html","w") as f:
    f.write(html)
print("Report generated")

# Из исходного текстового файла (pazzl.html) выбратьвсе html-коды изображений.
# Посчитать их количество.

import re
text = open("D:\manakova\pz\PZ-14\pazzl.html", "r+", encoding="utf-8").read()

ex = re.compile(r"<img\b[^>]*>", re.IGNORECASE)
print(ex.findall(text))
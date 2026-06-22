import re

st = "sun rises in east in"

k = re.match("s", st)
k = re.search("in", st)
k = re.findall("in", st)
k = re.finditer("in", st)

print(next(k).span())
print(next(k).span())

k = re.sub("in", "on", st)
print(k)

k = re.split(" ", st)
print(k)
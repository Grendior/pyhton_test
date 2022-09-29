import re

line = "123 i 34 witajcie"

m = re.findall("\d", line, re.IGNORECASE)

print(m)
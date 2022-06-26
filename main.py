import re
from zipfile import ZipFile
REGEX = r".*(23/Mar/2009:(09:(01:(0[4-9])|([1-5][0-9]))|((0[2-9])|([1-5][0-9]):[0-5][0-9]))|((1[0-9])|(2[0-3]):[0-5][0-9]:[0-5][0-9]))|" \
        r"|(2[4-7]/Mar/2009:([0-1][0-9])|(2[0-3]):[0-5][0-9]:[0-5][0-9])" \
        r"|(28/Mar/2009:(0[0-1]:[0-5][0-9]:[0-5][0-9])|(0[0-2]|[0-3][0-7]):([0-4][0-9]|5[0-4]))" \
        r".*\"GET .*\" 200"

with ZipFile("access.log.zip") as archive:
    archive.extractall()

log_file = open("access.log.txt")
count = 0
all_lines = log_file.readlines()
for line in all_lines:
    re.search(REGEX, line)
    count += 1

print(count)

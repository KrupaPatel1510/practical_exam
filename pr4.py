import os
import shutil

data_path = "exam_data"
logs_path = os.path.join(data_path, "logs")
archive_path = os.path.join(data_path, "archive")

os.makedirs(logs_path, exist_ok=True)
os.makedirs(logs_path, exist_ok=True)

with open(os.path.join(logs_path, "x.txt"), "w") as file:
	file.write("one\\ntwo\\n")
with open(os.path.join(logs_path, "y.txt"), "w") as file:
		file.write("three\\n")
with open(os.path.join(logs_path, "z.csv"), "w") as file:
	file.write("x,y\\n1,2\\n")

print(sorted(name for name in os.listdir(logs_path) if name.endswith(".txt")))

x_path = os.path.join(logs_path, "x.txt")
with open(x_path) as file:
	lines = file.readlines()
print(len(lines), lines[0].strip())

os.makedirs(archive_path)
shutil.move(x_path, os.path.join(archive_path, "x.txt"))
print(sorted(os.listdir(logs_path)), os.listdir(archive_path))

y_path = os.path.join(logs_path, "y.txt")
old_y_path = os.path.join(logs_path, "old_y.txt")
os.rename(y_path, old_y_path)
print(os.path.exists(y_path), os.path.isfile(old_y_path))

shutil.rmtree(data_path)
print(os.path.exists(data_path))
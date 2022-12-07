lines = None
with open("./input.txt") as f:
    lines = f.readlines()

"/a/b/asd.txt"
size = 3
# d = {"/a/b": 0}
d = {}

current_path = ""
for line in lines:
    if " cd " in line:
        if ".." in line:
            if len(current_path.split("/")) > 2:
                current_path = "/".join(current_path.split("/")[:-1])
            else:
                current_path = "/"
        else:
            if line.replace("$ cd ", "").strip() == "/":
                current_path = "/"
            else:
                if current_path == "/": 
                    current_path = current_path + line.replace("$ cd ", "").strip()
                else:
                    current_path = current_path + "/" + line.replace("$ cd ", "").strip()
        print(current_path)
        if current_path not in d:
            d[current_path] = 0
    elif "dir" in line or "ls" in line:
        pass
    else:
        size = int(line.split(" ")[0])
        path = current_path.split("/")
        for i in range(len(path)-1):
            if i == 0:
                current = "/".join(path[:])
            else:
                current = "/".join(path[:-i])
            print("{}) Adding to {}".format(i, current))
            d[current] += size
        d["/"] += size


sum = 0
for path in d:
    if d[path] <= 100000:
        sum += d[path]

print(sum)

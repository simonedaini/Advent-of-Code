line = None
with open("./input.txt") as f:
    line = f.read()


def find_marker(marker_length):
    for i in range(len(line)-marker_length):
        mark = line[i: i+marker_length]
        s = set(mark)
        if len(s) == marker_length:
            return i+marker_length

print(find_marker(4))
print(find_marker((14)))
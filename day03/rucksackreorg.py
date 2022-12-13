priority = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def get_input():
    lines = []
    with open("input.txt","r") as input_txt:
        lines = [line.strip() for line in input_txt.readlines()]
    return lines


def common_chars(s1,s2):
    common = ""
    return [ ch for ch in s1 if ch in s2 ]



total = 0 
for line in get_input():
    total = total + priority.index(common_chars(line[0:int(len(line)/2)],line[int(len(line)/2):len(line)])[0]) + 1

print(total)

lines = get_input()
total = 0
for i in range(0,len(lines),3):
    ln = lines[i:i+3]
    ch = set(ln[0]).intersection(*ln[1:]).pop()
    total = total + priority.index(ch) + 1

print(total)


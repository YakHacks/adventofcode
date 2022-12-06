import itertools
values = []
with open("input.txt","r") as input_txt:
    # Read values; "\n" maps to 0
    values=[int(line.strip()) if line != "\n" else 0 for line in input_txt.readlines()]

# Split list into groups delimited by elements with a value of zero
groups = [list(g) for k,g in itertools.groupby(values,lambda x: x!=0) if k]

# Print max group value
# print(sum(max(groups,key=sum)))

sums = sorted([sum(l) for l in groups], reverse=True)

# Print max group value
print(sums[0])
# Print sum of top three groups
print(sum(sums[0:3]))


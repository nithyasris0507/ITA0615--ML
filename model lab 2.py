# Find-S Algorithm (No libraries)

data = []
file = open("dataset.csv")
next(file)

for line in file:
    data.append(line.strip().split(","))

hypothesis = None

for row in data:
    if row[-1] == "Yes":
        if hypothesis is None:
            hypothesis = row[:-1]
        else:
            for i in range(len(hypothesis)):
                if hypothesis[i] != row[i]:
                    hypothesis[i] = "?"

print("Most Specific Hypothesis:")
print(hypothesis)

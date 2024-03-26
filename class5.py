ages = [15, 87, 65, 56, 32, 49, 37]

for age in ages:
  print(age)

for i in range(len(ages)):
  print(i, ages[i])

print(list(enumerate(ages)))

for idx, age in enumerate(ages):
  print(idx, age)

for _, age in enumerate(ages):
  print(age)
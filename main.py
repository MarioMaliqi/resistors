resistors = [100, 220, 323, 470, 1000, 10_000, 47_000, 63_000]
wanted_resistance = 810
pairs = []
results = []

def calculate_resistance(res1, res2, res3):
    return [res1, res2, res3, ((res1*res2) / (res1+res2)) + res3]

for i, res1 in enumerate(resistors):
    for j, res2 in enumerate(resistors):
        for k, res3 in enumerate(resistors):
            if (i == j or j == k or i == k):
                continue
            pairs.append({"res1": res1,
                            "res2": res2,
                            "res3": res3})

# for ress in results:
#     print()
#     for k, v in ress.items():
#         print(k, v)
#     print()

for ress in pairs:
    results.append(calculate_resistance(ress["res1"],
                                        ress["res2"],
                                        ress["res3"],
                                        ))

differences = []
for result in results:
    differences.append(abs(result[3] - wanted_resistance))

print(min(differences))
index_min = min(range(len(differences)), key=differences.__getitem__)
print(results[index_min])

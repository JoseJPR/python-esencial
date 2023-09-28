example = {
    "keyA": "valueA",
    "keyB": "valueB"
}

example["keyC"] = "valueC"
example["keyD"] = {
    "keyD_A": "valueD_A"
}

print(example["keyA"])
print(example["keyC"])
print(example["keyD"]["keyD_A"])
print(example.keys())
print(example.values())
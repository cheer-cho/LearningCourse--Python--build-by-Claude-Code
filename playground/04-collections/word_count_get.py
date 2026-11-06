text = "the cat saw the dog and the dog ran"

counts = {}
for word in text.split():
    before = counts.get(word, 0)
    counts[word] = before + 1
    print(f"{word!r:7} get -> {before}   now {counts}")

print("\nfinal:", counts)

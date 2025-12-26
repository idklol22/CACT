import json, random, os

src = "data/imdb_triplets.jsonl"
train_path = "data/imdb_triplets_train.jsonl"
val_path   = "data/imdb_triplets_val.jsonl"

random.seed(42)

rows = []
with open(src, "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if line:
            rows.append(json.loads(line))

random.shuffle(rows)
k = int(0.9 * len(rows))

os.makedirs("data", exist_ok=True)

with open(train_path, "w", encoding="utf-8") as f:
    for r in rows[:k]:
        f.write(json.dumps(r, ensure_ascii=False) + "\n")

with open(val_path, "w", encoding="utf-8") as f:
    for r in rows[k:]:
        f.write(json.dumps(r, ensure_ascii=False) + "\n")

print("Wrote:", train_path, "lines=", k)
print("Wrote:", val_path,   "lines=", len(rows)-k)
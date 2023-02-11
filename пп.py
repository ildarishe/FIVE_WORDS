with open("text\input.txt", encoding="utf-8") as f:
    for t in f.readlines():
        print(t.strip().split(" — ")[1][:-1])
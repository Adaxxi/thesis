pre = 0
count = 0
chinese = 0
with open("only_chinese.txt") as f, open("no_space.txt", "w") as w:
    for l in f:
        words = l.strip()
        for i in words:
            if i != ' ':
                count += 1
                w.write(i)
            else:
                chinese += 1

        if pre == count:
            w.write("\n")
        pre = count

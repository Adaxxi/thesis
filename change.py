# -*- coding: utf-8 -*-
pre = 0
count = 0
chinese = 0
with open("test.tex") as f, open("only_chinese.txt", "w") as w:
    for l in f:
        words = l.strip()
        for i in words:
            if i <= '~' and i >='!' :
                count += 1
            else:
                chinese += 1
                w.write(i)
        if pre == count:
            w.write("\n")
        pre = count

# with open("only_chinese.txt", "r") as f, open("final.txt", 'w') as w:
#     for l in f:
#         words = l.strip()
#         for i in words:
#             if i != '

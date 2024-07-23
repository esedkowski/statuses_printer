import re

f = open("nis_example.tex", "r")
f1 = open("new.tex", "w")

thisdict = {
    "model": "b737",
    "MSN": "123456",
    "REG": "AA-BBB",
    "org": "MyOrg",
    "DATE": "07.08.2024",
    "AP": "TESTTEST"
}

for line in f:
    txt = f.readline()
    test = re.findall("(@[a-zA-Z]+)", txt)
    for match in test:
        print(match[1:])
        txt = txt.replace(match, thisdict[match[1:]])
        print(txt)
    f1.write(txt)
f.close()
f1.close()

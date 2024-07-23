import re

f = open("nis_example.tex", "r")
f1 = open("new.tex", "w")

thisdict = {
    "model": "b737",
    "MSN": "123456",
    "REG": "AA-BBB",
    "org": "MyOrg",
    "DATE": "07.08.2024",
    "APNO": "TESTTEST",
    "ACPN": "B737",
    "ACSN": "123456",
    "ACTSN": "1000:14",
    "ACFC": "3535",
    "LHEPN": "AAAA",
    "LHESN": "BBBB",
    "LHETSN": "000:00",
    "LHEFC": "0000",
    "RHEPN": "AAAA",
    "RHESN": "BBBB",
    "RHETSN": "444:12",
    "RHEFC": "242424",
    "APUPN": "XXXXX",
    "APUSN": "ZZZZ",
    "APUTSN": "92024:12",
    "APUFC": "4242",
    "NLGPN": "VVVV",
    "NLGSN": "MMMMM",
    "NLGTSN": "92024:12",
    "NLGFC": "4242",
    "LLGPN": "VVVV",
    "LLGSN": "MMMMM",
    "LLGTSN": "92024:12",
    "LLGFC": "4242",
    "RLGPN": "VVVV",
    "RLGSN": "MMMMM",
    "RLGTSN": "92024:12",
    "RLGFC": "4242",
    "ORG": "Awasome Company",
    "AUTHOR": "John",
    "SIGNER": "Cooler John",
    "ORGFULLNAME": "Awasome Company Inc.",
    "ORGADDRESS": "IDK",
    "ORGLINK": "awasome.Company.org",
    "DocNo": "Test No. 1"
}


txt = f.read()
test = re.findall("(@[a-zA-Z_]+)", txt)
for match in test:
    #print(match)
    if match[1:] in thisdict:
        #print(match[1:], thisdict[match[1:]])
        txt = txt.replace(match, thisdict[match[1:]], 1)

f1.write(txt)
f.close()
f1.close()
#print(txt1)

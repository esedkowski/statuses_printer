source_file = open("source.tex", "w")

text = """
    \\newcommand{\\model}{b737}\n 
    \\newcommand{\\MSN}{0000}\n
    \\newcommand{\\registration}{AA-BBB}\n
    \\newcommand{\\dateSinceMenaged}{01.01.2000}
    \\newcommand{\\AircraftPN}{}\n
    \\newcommand{\\AircraftSN}{}\n
    \\newcommand{\\AircraftTFH}{}\n
    \\newcommand{\\AircraftTFC}{}\n
    \\newcommand{\\Eng1PN}{}\n
    \\newcommand{\\Eng1SN}{}\n
    \\newcommand{\\Eng1TFH}{}\n
    \\newcommand{\\Eng1TFC}{}\n
    \\newcommand{\\Eng2PN}{}\n
    \\newcommand{\\Eng2SN}{}\n
    \\newcommand{\\Eng2TFH}{}\n
    \\newcommand{\\Eng2TFC}{}\n
    \\newcommand{\\APUPN}{}\n
    \\newcommand{\\APUSN}{}\n
    \\newcommand{\\APUTFH}{}\n
    \\newcommand{\\APUTFC}{}\n
    \\newcommand{\\NoseLGPN}{}\n
    \\newcommand{\\NoseLGSN}{}\n
    \\newcommand{\\NoseLGTFH}{}\n
    \\newcommand{\\NoseLGTFC}{}\n
    \\newcommand{\\LeftLGPN}{}\n
    \\newcommand{\\LeftLGSN}{}\n
    \\newcommand{\\LeftLGTFH}{}\n
    \\newcommand{\\LeftLGTFC}{}\n
    \\newcommand{\\RightLGPN}{}\n
    \\newcommand{\\RightLGSN}{}\n
    \\newcommand{\\RightLGTFH}{}\n
    \\newcommand{\\RightLGTFC}{}\n
    \\newcommand{\\organization}{}\n
    \\newcommand{\\organizationFullName}{}\n
    \\newcommand{\\organizationApprovalNumber}{}\n
    \\newcommand{\\organizationAdress}\n
    \\newcommand{\\organizationLink}\n
    \\newcommand{\\Author}{}\n
    \\newcommand{\\Signer}{}\n
    \\newcommand{\\documentNumber}{}\n
    \\newcommand{\\date}{}\n
"""

source_file.write(text)
source_file.close()

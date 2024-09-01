from component import *

document = Document("Eryk", "Other Eryk", "0001", "01 JAN 2024")
engineLH = Component("0", "0", "XXX", "YYY")
engineRH = Component("0", "0", "XXX", "YYY")
apu = Component("0", "0", "XXX", "YYY")
lgNose = Component("0", "0", "XXX", "YYY")
lgLeft = Component("0", "0", "XXX", "YYY")
lgRight = Component("0", "0", "XXX", "YYY")
aircraft = Aircraft("0", "0", "01 JAN 2024", "B737", "00000", "AA-BBB", engineLH, engineRH, apu, lgNose, lgLeft, lgRight)
organization = Organization("Cool Company", "Cool Company XYZ", "QQQQ.9999", "Cool Street, Cool Town etc.", "company.cool")

text = (
    "\\newcommand{\\model}{" + aircraft.model + "}\n" +
    "\\newcommand{\\MSN}{" + aircraft.msn + "}\n" +
    "\\newcommand{\\registration}{" + aircraft.registration + "}\n" +
    "\\newcommand{\\dateSinceMenaged}{" + aircraft.dateSinceMenaged + "}\n" +
    "\\newcommand{\\AircraftTFH}{" + aircraft.totalFlightHours + "}\n" +
    "\\newcommand{\\AircraftTFC}{" + aircraft.totalFlightCycles + "}\n" +
    "\\newcommand{\\EngLHPN}{" + aircraft.engineLH.partNumber + "}\n" +
    "\\newcommand{\\EngLHSN}{" + aircraft.engineLH.serialNumber + "}\n" +
    "\\newcommand{\\EngLHTFH}{" + aircraft.engineLH.totalFlightHours + "}\n" +
    "\\newcommand{\\EngLHTFC}{" + aircraft.engineLH.totalFlightCycles + "}\n" +
    "\\newcommand{\\EngRHPN}{" + aircraft.engineRH.partNumber + "}\n" +
    "\\newcommand{\\EngRHSN}{" + aircraft.engineRH.serialNumber + "}\n" +
    "\\newcommand{\\EngRHTFH}{" + aircraft.engineRH.totalFlightHours + "}\n" +
    "\\newcommand{\\EngRHTFC}{" + aircraft.engineRH.totalFlightCycles + "}\n" +
    "\\newcommand{\\APUPN}{" + aircraft.apu.partNumber + "}\n" +
    "\\newcommand{\\APUSN}{" + aircraft.apu.serialNumber + "}\n" +
    "\\newcommand{\\APUTFH}{" + aircraft.apu.totalFlightHours + "}\n" +
    "\\newcommand{\\APUTFC}{" +  aircraft.apu.totalFlightCycles + "}\n" +
    "\\newcommand{\\NoseLGPN}{" + aircraft.lgNose.partNumber + "}\n" +
    "\\newcommand{\\NoseLGSN}{" + aircraft.lgNose.serialNumber + "}\n" +
    "\\newcommand{\\NoseLGTFH}{" + aircraft.lgNose.totalFlightHours + "}\n" +
    "\\newcommand{\\NoseLGTFC}{" + aircraft.lgNose.totalFlightCycles + "}\n" +
    "\\newcommand{\\LeftLGPN}{" + aircraft.lgLeft.partNumber + "}\n" +
    "\\newcommand{\\LeftLGSN}{" + aircraft.lgLeft.serialNumber + "}\n" +
    "\\newcommand{\\LeftLGTFH}{" + aircraft.lgLeft.totalFlightHours + "}\n" +
    "\\newcommand{\\LeftLGTFC}{" + aircraft.lgLeft.totalFlightCycles + "}\n" +
    "\\newcommand{\\RightLGPN}{" + aircraft.lgRight.partNumber + "}\n" +
    "\\newcommand{\\RightLGSN}{" + aircraft.lgRight.serialNumber + "}\n" +
    "\\newcommand{\\RightLGTFH}{" + aircraft.lgRight.totalFlightHours + "}\n" +
    "\\newcommand{\\RightLGTFC}{" + aircraft.lgRight.totalFlightCycles + "}\n" +
    "\\newcommand{\\organization}{" + organization.name + "}\n" +
    "\\newcommand{\\organizationFullName}{" + organization.fullName + "}\n" +
    "\\newcommand{\\organizationApprovalNumber}{" + organization.approvalNumber + "}\n" +
    "\\newcommand{\\organizationAddress}{" + organization.address + "}\n" +
    "\\newcommand{\\organizationLink}{" + organization.link + "}\n" +
    "\\newcommand{\\Author}{" + document.author + "}\n" +
    "\\newcommand{\\Signer}{" + document.signer + "}\n" +
    "\\newcommand{\\documentNumber}{" + document.number + "}\n" +
    "\\newcommand{\\documentDate}{" + document.date + "}\n"
)

source_file = open("source.tex", "w")
source_file.write(text)
source_file.close()

from component import *
from tools import newcommand

document = Document("Eryk", "Other Eryk", "0001", "01 JAN 2024")
engineLH = Component("0", "0", "XXX", "YYY")
engineRH = Component("0", "0", "XXX", "YYY")
apu = Component("0", "0", "XXX", "YYY")
lgNose = Component("0", "0", "XXX", "YYY")
lgLeft = Component("0", "0", "XXX", "YYY")
lgRight = Component("0", "0", "XXX", "YYY")
aircraft = Aircraft("0", "0", "01 JAN 2024", "B737", "00000", "AA-BBB", engineLH, engineRH, apu, lgNose, lgLeft, lgRight)
organization = Organization("Cool Company", "Cool Company XYZ", "QQQQ.9999", "Cool Street, Cool Town etc.", "company.cool")

text = ""

values = [aircraft.model, aircraft.msn, aircraft.registration, aircraft.dateSinceMenaged, aircraft.totalFlightHours, aircraft.totalFlightCycles, aircraft.engineLH.partNumber, aircraft.engineLH.serialNumber, aircraft.engineLH.totalFlightHours, aircraft.engineLH.totalFlightCycles, aircraft.engineRH.partNumber, aircraft.engineRH.serialNumber, aircraft.engineRH.totalFlightHours, aircraft.engineRH.totalFlightCycles, aircraft.apu.partNumber, aircraft.apu.serialNumber, aircraft.apu.totalFlightHours, aircraft.apu.totalFlightCycles, aircraft.lgNose.partNumber, aircraft.lgNose.serialNumber, aircraft.lgNose.totalFlightHours, aircraft.lgNose.totalFlightCycles, aircraft.lgLeft.partNumber, aircraft.lgLeft.serialNumber, aircraft.lgLeft.totalFlightHours, aircraft.lgLeft.totalFlightCycles, aircraft.lgRight.partNumber, aircraft.lgRight.serialNumber, aircraft.lgRight.totalFlightHours, aircraft.lgRight.totalFlightCycles, organization.name, organization.fullName, organization.approvalNumber, organization.address, organization.link, document.author, document.signer, document.number, document.date]

names = ["model", "MSN", "registration", "dateSinceMenaged", "AircraftTFH", "AircraftTFC", "EngLHPN", "EngLHSN", "EngLHTFH", "EngLHTFC", "EngRHPN", "EngRHSN", "EngRHTFH", "EngRHTFC", "APUPN", "APUSN", "APUTFH", "APUTFC", "NoseLGPN", "NoseLGSN", "NoseLGTFH", "NoseLGTFC", "LeftLGPN", "LeftLGSN", "LeftLGTFH", "LeftLGTFC", "RightLGPN", "RightLGSN", "RightLGTFH", "RightLGTFC", "organization", "organizationFullName", "organizationApprovalNumber", "organizationAddress", "organizationLink", "AuthorSigner", "documentNumber", "documentDate"]

for i in range(len(names)):
    text += newcommand(names[i], values[i])

source_file = open("source.tex", "w")
source_file.write(text)
source_file.close()

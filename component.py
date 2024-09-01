class Component:
    def  __init__(self, totalFlightHours, totalFlightCycles, partNumber, serialNumber):
        self.totalFlightHours =  totalFlightHours #pomyśleć nad formatem
        self.totalFlightCycles = totalFlightCycles #string, czy int?
        self.partNumber = partNumber 
        self.serialNumber = serialNumber 

class Aircraft:
    def __init__(self, totalFlightHours, totalFlightCycles, dateSinceMenaged, model, msn, registration, engineLH, engineRH, apu, lgNose, lgLeft, lgRight):
        self.totalFlightHours =  totalFlightHours #pomyśleć nad formatem
        self.totalFlightCycles = totalFlightCycles #string, czy int?
        self.dateSinceMenaged = dateSinceMenaged
        self.model = model
        self.msn = msn
        self.registration = registration
        self.engineLH = engineLH
        self.engineRH = engineRH 
        self.apu = apu
        self.lgNose = lgNose
        self.lgLeft = lgLeft
        self.lgRight = lgRight

class Organization:
    def __init__(self, name, fullName, approvalNumber, address, link):
        self.name = name
        self.fullName = fullName
        self.approvalNumber = approvalNumber
        self.address = address
        self.link = link

class Document:
    def __init__(self, author, signer, number, date):
        self.author = author
        self.signer = signer
        self.number = number
        self.date = date

document = Document("Eryk", "Other Eryk", "0001", "01.01.2024")
eng1 = Component("0", "0", "XXX", "YYY")
eng2 = Component("0", "0", "XXX", "YYY")
apu = Component("0", "0", "XXX", "YYY")
lgNose = Component("0", "0", "XXX", "YYY")
lgLeft = Component("0", "0", "XXX", "YYY")
lgRight = Component("0", "0", "XXX", "YYY")
aircraft = Aircraft("0", "0", "01.01.2024", "B737", "00000", "AA-BBB", eng1, eng2, apu, lgNose, lgLeft, lgRight)
blankComponent = Component("0:00", "0", "XXX", "YYY")

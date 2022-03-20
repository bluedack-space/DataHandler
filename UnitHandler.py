from EngUnitConversion import *

class UnitHandler():

    def __init__(self):
        self.initialization()

    def initialization(self):
        print("initialization() is called")

    @staticmethod
    def getUnit(unitName):
        unit = None
        if unitName=="K":
            unit = Temperature.Unit.K
        elif unitName=="C":
            unit = Temperature.Unit.C
        elif unitName=="F":
            unit = Temperature.Unit.F
        elif unitName=="km":
            unit = Length.Unit.km
        elif unitName=="m":
            unit = Length.Unit.m
        elif unitName=="cm":
            unit = Length.Unit.cm
        elif unitName=="mm":
            unit = Length.Unit.mm
        elif unitName=="kg":
            unit = Mass.Unit.kg
        elif unitName=="g":
            unit = Mass.Unit.g
        elif unitName=="Pa":
            unit = Pressure.Unit.Pa
        elif unitName=="MPa":
            unit = Pressure.Unit.MPa
        elif unitName=="atm":
            unit = Pressure.Unit.atm
        elif unitName=="N":
            unit = Force.Unit.N
        elif unitName=="kN":
            unit = Force.Unit.kN
        elif unitName=="kgf":
            unit = Force.Unit.kgf
        elif unitName=="A":
            unit = Current.Unit.A
        elif unitName=="mA":
            unit = Current.Unit.mA
        elif unitName=="W":
            unit = Power.Unit.W
        elif unitName=="kW":
            unit = Power.Unit.kW

        return unit

    @staticmethod
    def getUnitType(unitName):
        unitType = None
        if unitName=="DateTime":
            unitType = "DateTime"
        elif unitName=="K":
            unitType = "Temperature"
        elif unitName=="C":
            unitType = "Temperature"
        elif unitName=="F":
            unitType = "Temperature"
        elif unitName=="km":
            unitType = "Length"
        elif unitName=="m":
            unitType = "Length"
        elif unitName=="cm":
            unitType = "Length"
        elif unitName=="mm":
            unitType = "Length"
        elif unitName=="kg":
            unitType = "Mass"
        elif unitName=="g":
            unitType = "Mass"
        elif unitName=="Pa":
            unitType = "Pressure"
        elif unitName=="MPa":
            unitType = "Pressure"
        elif unitName=="atm":
            unitType = "Pressure"
        elif unitName=="N":
            unitType = "Force"
        elif unitName=="kN":
            unitType = "Force"
        elif unitName=="kgf":
            unitType = "Force"
        elif unitName=="A":
            unitType = "Current"
        elif unitName=="mA":
            unitType = "Current"
        elif unitName=="W":
            unitType = "Power"
        elif unitName=="kW":
            unitType = "Power"

        return unitType

    @staticmethod
    def convertUnit(value=None,unitNameIn=None,unitNameOut=None):
        unitType = UnitHandler.getUnitType(unitNameIn)
        unit     = UnitHandler.getUnit(unitNameIn)

        if unitType=="Force":
            V = Force(value, unit)
        elif unitType == "Temperature":
            V = Temperature(value, unit)
        elif unitType == "Length":
            V = Length(value, unit)
        elif unitType == "Mass":
            V = Mass(value, unit)
        elif unitType == "Pressure":
            V = Pressure(value, unit)
        elif unitType == "Force":
            V = Force(value, unit)
        elif unitType == "Current":
            V = Current(value, unit)
        elif unitType == "Power":
            V = Power(value, unit)

        V.changeUnit(unitNameOut)

        return V.value

if __name__ == '__main__':
    value = UnitHandler.convertUnit(value=10,unitNameIn="m",unitNameOut="km")
    print("value="+str(value))

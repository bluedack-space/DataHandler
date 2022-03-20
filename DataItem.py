from urllib.request import DataHandler
from EngUnitConversion import *
from UnitHandler import *

class DataItem():

    isPhysicalValue_   = None
    isDateTime_        = None
    hasConvertFormula_ = None
    unitName           = None
    unit               = None
    name               = None
    formula            = None
    dataList           = []

    def __init__(self):
        self.initialization()

    def __del__(self):
        self.dataList = None

    def initialization(self):
        self.setPhysicalValue(isPhysicalValue=True)
        self.setConvertFormula(hasConvertFormula=False)

    def isPhysicalValue(self):
        return self.isPhysicalValue_

    def setPhysicalValue(self, isPhysicalValue):
        self.isPhysicalValue_ = isPhysicalValue

    def isDateTime(self):
        return self.isDateTime_

    def setDateTime(self, isDateTime):
        self.isDateTime_ = isDateTime

    def hasConvertFormula(self):
        return self.hasConvertFormula_

    def setConvertFormula(self, hasConvertFormula):
        self.hasConvertFormula_ = hasConvertFormula

    def setName(self,name):
        self.name = name

    def getUnitName(self):
        return self.unitName

    def setUnit(self,unitName):
        self.unitName = unitName
        self.unit = UnitHandler.getUnit(unitName=self.unitName)
        if self.unit=="DateTime":
            self.setDateTime(isDateTime=True)
        else:
            self.setDateTime(isDateTime=False)

    def changeUnit(self,unitNameNew,withDataListConversion=True):
        if withDataListConversion and self.isPhysicalValue():
            for i in range(len(self.dataList)):
                self.dataList[i] = UnitHandler.convertUnit(value=self.getValue(i),unitNameIn=self.getUnitName(),unitNameOut=unitNameNew)
        self.setUnit(unitName=unitNameNew)

    def setDataList(self,dataList):
        self.dataList = dataList

    def getDataList(self):
        if self.isPhysicalValue():
            return self.dataList
        else:
            dataList = []
            for i in range(len(self.dataList)):
                dataList.append(self.getValueWithConvertByFormula(i))
            return dataList

    def setFormula(self,formula):
        if str(formula)!="nan":
            self.formula = str(formula)
        else:
            self.formula = None

    def getValue(self, i):
        if self.isPhysicalValue():
            return self.getValue_Raw(i)
        else:
            return self.getValueWithConvertByFormula(i)

    def getValue_Raw(self, i):
        return self.dataList[i]

    def getValueWithConvertByFormula(self, i):
        return self.getValueWithConvertByFormulaForSpecifiedValue(V=self.dataList[i])

    def getValueWithConvertByFormulaForSpecifiedValue(self, V):
            return eval(str(self.formula))

    def displayData(self):
        print("Data Name:"+str(self.name))
        print("Unit     :"+str(self.unit))
        print("Formula  :"+str(self.formula))
        if len(self.dataList)!=0:
            for i in range(len(self.dataList)):
                print(str(self.getValue(i)))

from DataItemList import *

if __name__ == '__main__':

    #-----------------------------------------------------
    # [01] Read DataItemList Setting from Excel file
    itemList = DataItemList()
    itemList.reader(fnameConfig="DataConfig.xlsx")

    #-----------------------------------------------------
    # [02] Read DataItem Contents from Excel file
    import pandas as pd

    df = pd.read_excel("DataContents.xlsx")
    for nv in range(itemList.getTotalItemNumbers()):
        item     = itemList.getItem(nv)
        itemName = item.name
        itemList.getItem(nv).setDataList(dataList=df[itemName])

    #itemList.displayData()

    #-----------------------------------------------------
    # [03] Convert Unit (if needed)
    for nv in range(itemList.getTotalItemNumbers()):
        item     = itemList.getItem(nv)
        if nv==2:
            item.changeUnit(unitNameNew="C",withDataListConversion=True)
        elif nv==3:
            item.changeUnit(unitNameNew="MPa",withDataListConversion=True)

    #itemList.displayData()

    #-----------------------------------------------------
    # [04] Obtain Pandas DataFrame Vars which is specified 
    # in DAtaItemList Setting Excel File
    df = itemList.getDataAsPandasDataFrame()
    print(df)

    varNameX     = "Time[DateTime]"
    varNameYList = ["VAR1[km]","VAR2[C]"]

    from DataHandlerBase import *

    x  = DataHandlerBase.getTimeInSeconds(df,labelTime=varNameX)
    y1 = df[varNameYList[0]]
    y2 = df[varNameYList[1]]

    import plotly.graph_objects as go

    fig = go.Figure(data=[
        go.Scatter(x=x, y=y1, name=varNameYList[0]),
        go.Scatter(x=x, y=y2, name=varNameYList[1]),
    ])
    
    fig.show()

import os

from DataItem import *
import pandas as pd

class DataItemList():

    itemList  = None

    def __init__(self):
        self.initialization()

    def initialization(self):
        self.itemList = []
    
    def appendDataItem(self,dataItem):
        self.itemList.append(dataItem)

    def reader(self,fnameConfig=None):
        import pandas as pd
        if os.path.splitext(fnameConfig)[1]=='.xlsx':
            df = pd.read_excel(fnameConfig,header=None)
            numVars    = df.shape[1]
            for nv in range(numVars):
                name     = str(df.iloc[0,nv])
                unitName = str(df.iloc[1,nv])
                formula  = str(df.iloc[2,nv])
                
                item = DataItem()
                item.setUnit(unitName=unitName)
                item.setName(name=name)

                if formula=="nan":
                    item.setPhysicalValue(isPhysicalValue=True)
                    item.setConvertFormula(hasConvertFormula=False)
                else:
                    item.setPhysicalValue(isPhysicalValue=False)
                    item.setConvertFormula(hasConvertFormula=True)
                    item.setFormula(formula=formula)

                self.appendDataItem(item)

            #self.displayData()

    def displayData(self):
        numVars = len(self.itemList)
        for nv in range(numVars):
            item = self.itemList[nv]
            print("------------------------------")
            item.displayData()

    def getTotalItemNumbers(self):
        return len(self.itemList)

    def getItem(self,index=None):
        return self.itemList[index]

    def getIndexByName(self,name=None):
        numVars = len(self.itemList)
        for nv in range(numVars):
            item = self.itemList[nv]
            if item.name==name:
                return nv
        return None

    def getDataAsPandasDataFrame(self,withUnitName=True):

        numVars = len(self.itemList)
        for nv in range(numVars):
            item     = self.itemList[nv]
            dataList = item.getDataList()
            dataList = dataList.copy()

            if nv==0:
                df  = pd.DataFrame(dataList,columns=[item.name])
            else:
                df  = pd.concat([df,pd.DataFrame(dataList,columns=[item.name])], axis=1)

            if withUnitName:
                varName = item.name + "[" + item.unitName + "]"
            else:
                varName = item.name

            #print("-------------------------------")
            #print(df)
            #print("item.name :"+str(item.name))
            #print("varName :"+str(varName))

            df = df.rename(columns={item.name: varName})

        return df

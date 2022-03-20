import numpy as np
import pandas as pd

class TableHandler():
    
    def __init__(self):
        print("This is constructor of ConvertTable")
        
    @staticmethod
    def getInitializedNumpyTable( numColumn, numRow, colNames=None ):
        if colNames==None:
            tab_np = np.zeros(numRow, dtype=[('V'+str(icol),'f8') for icol in range(numColumn)])
        else:
            tab_np = np.zeros(numRow, dtype=[(colNames[icol],'f8') for icol in range(numColumn)])
        return tab_np
    
    @staticmethod
    def getNumpyTable(tab):
        if type(tab) is np.ndarray:
            tab_np = tab
        elif type(tab) is pd.core.frame.DataFrame:
            tab_np = np.zeros(tab.shape[0], dtype=[(tab.columns[i],'f8') for i in range(tab.shape[1])])
            for irow in range(tab.shape[0]):
                for icol in range(tab.shape[1]):
                    tab_np[irow][icol] = tab.values[irow][icol]
        else:
            tab_np = None
        return tab_np
    
    @staticmethod
    def getPandasTable(tab):
        if type(tab) is np.ndarray:
            tab_pd = pd.DataFrame(tab)
        elif type(tab) is pd.core.frame.DataFrame:
            tab_pd = tab
        else:
            tab_pd = None
        return tab_pd
    
if __name__ == '__main__':
    #_/_/_/_/ Initialize Numpy Array with Column Name
    # (1) Initialize Matrix
    tab = TableHandler.getInitializedNumpyTable( numColumn=3, numRow=3, colNames=['V1','V2','V3'] )
    # (2) Read from file
    #tab = np.genfromtxt( "test.csv", skip_header=1, delimiter=",", dtype=[('V1', 'f8'), ('V2', 'f8'), ('V3', 'f8')] )
    
    tab[0][0] = 1.0
    tab[1][1] = 2.0
    tab[2][2] = 3.0
    
    # Access column data
    colData = tab['V1']
    print(colData)
    
    # Display Table Contents
    print(tab)
    # Display Table Column Names
    print(tab.dtype.names)
    
    #_/_/_/_/ Convert to Pandas DataFrame
    import pandas as pd
    # Convet to pandas table
    df = pd.DataFrame(tab)
    # Display Pandas Dataframe
    print(df)
    
    #_/_/_/_/ Convert Pandas DataFrame to Numpy Table
    tab_np = TableHandler.getNumpyTable(df)
    print("\n >>Converted to Numpy Table:\n")
    print(tab_np)
    print(tab_np.dtype.names)
    
    #_/_/_/_/ Convert Numpy Table to Pandas DataFrame
    tab_pd = TableHandler.getPandasTable(tab)
    print("\n >>Converted to Pandas Dataframe:\n")
    print(tab_pd)

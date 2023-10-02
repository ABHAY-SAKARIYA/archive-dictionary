import pandas as pd
import json

class File:
    
    class Json:
        def write(filename : str,
                  data : str=None) -> None:
            with open(filename,"a+") as writeJson:
                writeJson.write(json.dumps(data,indent=4))
        def read(filename : str) -> str:
            with open(filename,"r") as readJson:
                Jsondata = json.load(readJson)
            return Jsondata
        
    class Html:
        def write(filename : str,
                  data : str = None) -> None:
            with open(filename,"a+") as writehtml:
                writehtml.write(data)
        def read(filename : str) -> str:
            with open(filename,"r") as readhtml:
                Htmldata = readhtml.read()
            return Htmldata
        
    class Csv:
        def write(filename : str,
                  data : dict = None) -> None:
            dataFrame = pd.DataFrame(data)
            dataFrame.to_csv(filename)
        def read(filename : str) -> any:
            datacsv = pd.read_csv(filename)
            return datacsv
    
    class Excel:
        def write(filename : str,
                  data : dict = None) -> None:
            dataFrame = pd.DataFrame(data)
            dataFrame.to_excel(filename)
        def read(filename : str) -> dict:
            dataexcel = pd.read_excel(filename)
            return dataexcel
        

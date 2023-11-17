from filemanager import File

def getexcel():
    xdata = {"PDFName":[],"Language":[],"title":[]}
    data = File.Csv.read(filename="searchwithdictionary.csv")
    for _,row in data.iterrows():
        if "dictionary" in str(row["title"]).lower():
            if str(row["language"]).lower() == "english" or str(row["language"]).lower() == "hindi" or str(row["language"]).lower() == "gujarati" or str(row["language"]).lower() == "sanskrit" or str(row['language']).lower() == "eng" or str(row['language']).lower() == "guj" or str(row['language']).lower() == "hin" or str(row['language']).lower() == "san":
                if row["mediatype"] == "texts":
                    xdata["Language"].append(row["language"])
                    xdata["PDFName"].append(f"{row['identifier']}.pdf")
                    xdata["title"].append(row["title"])
# "collection","contributor","creator","identifier","language","mediatype","publisher","subject","title"
    return xdata


d = getexcel()

# File.Json.write(filename="Archive-dictionary-English-Excel-list.json",data=d)
# print(len(d["PDFName"]))


import requests 

lookup = "lookup/id"

def query_ensembl(variantID,method):
    URL = f"https://rest.ensembl.org/{method}/{variantID}?"
    response = requests.get(URL, headers={"Content-Type" : "application/json"})



    if response.status_code == 200:
        print(f"Succesfully retrieved data |--Code:{response.status_code}--|")
        result_data = response.json()
        
        for k,v in result_data.items():
            print(f"{k}:{v}")
    else:
        print(f"Failed to retrive data. |--Code:{response.status_code}--|")
    
query_ensembl("ENST00000357654",lookup)
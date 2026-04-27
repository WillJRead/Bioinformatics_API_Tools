import requests, sys
from pprint import pprint


lookup = "lookup/id/"
phenotype = "/phenotype/gene/human/"
VEP = "vep/human/hgvs/"


def query_ensembl(ext,on):
    server = "http://rest.ensembl.org/"
    URL = f"{server}{ext}{on}?"
    
    if ext == "vep/human/hgvs/":
        new_URL = f"{URL}AlphaMissense=1&CADD=1&Conservation=1&REVEL=1&canonical=1&mane=1"
        r2 = requests.get(new_URL, headers={"Content-Type":"application/json"})
        if r2.status_code == 200:
            print(f"---Request Successful---")
        elif r2.status_code != 200:
            print(f"---Request Failed---")
            print(f"---Error {r.status_code}---")
        response = r2.json()
        print("---Filter by canonical transcript?---")
        print("---y/n---")
        answer = input()
        filtered =[]
        if answer == "y":
            for i in response:
                t = i.get("transcript_consequences")
                for x in t:
                    if x.get("canonical") == 1:
                        filt = {k: v for k, v in i.items() if k !="transcript_consequences"}
                        filtered.append(filt)
                        filtered.append(x)
            return filtered

        else:
             return response
    else:
        r = requests.get(URL, headers={"Content-type":"application/json"})
        if r.status_code == 200:
            print(f"---Request Successful---")
        elif r.status_code != 200:
            print(f"---Request Failed---")
            print(f"---Error {r.status_code}---")
    
        response = r.json()
        if ext == "/phenotype/gene/human/":
            print("---Search via disease description?---")
            print("---y/n---")
            answer = input()
            filtered =[]
            if answer == "y":
                    print("---Enter keyword---")
                    keyword = input()
                    for i in response:
                        if keyword.upper() in i.get("description","").upper():
                                filtered.append(i)
                    return filtered
            else: 
                return response
 


 
#gene = query_ensembl(lookup,"ENSG00000135100")
#HPO = query_ensembl(phenotype,"ENSG00000135100")
#protein = query_ensembl(VEP,"ENST00000257555:c.544C>T")

from fastapi import FastAPI
import uvicorn
import Abas_V2
import json

app = FastAPI()

@app.get("/Comercio")
def comercio():
    valores = open('Repository_JSON/Comercio.json')
    data = json.load(valores)
    return data

@app.get("/Exportação/Espumantes")
def ExpEspumantes():
    valores = open('Repository_JSON/ExpEspumantes.json')
    data = json.load(valores)
    return data

@app.get("/Exportação/Suco")
def ExpSuco():
    valores = open('Repository_JSON/ExpSuco.json')
    data = json.load(valores)
    return data

@app.get("/Exportação/Uva")
def ExpUva():
    valores = open('Repository_JSON/ExpUva.json')
    data = json.load(valores)
    return data

@app.get("/Exportação/Vinho")
def ExpVinho():
    valores = open('Repository_JSON/ExpVinho.json')
    data = json.load(valores)
    return data

@app.get("/Importação/Espumantes")
def ImpEspumantes():
    valores = open('Repository_JSON/ImpEspumantes.json')
    data = json.load(valores)
    return data

@app.get("/Importação/Frescas")
def ImpEspumantes():
    valores = open('Repository_JSON/ImpEspumantes.json')
    data = json.load(valores)
    return data

@app.get("/Importação/Passas")
def ImpPassas():
    valores = open('Repository_JSON/ImpPassas.json')
    data = json.load(valores)
    return data

@app.get("/Importação/Suco")
def ImpSuco():
    valores = open('Repository_JSON/ImpSuco.json')
    data = json.load(valores)
    return data

@app.get("/Importação/Vinhos")
def ImpVinhos():
    valores = open('Repository_JSON/ImpVinhos.json')
    data = json.load(valores)
    return data

@app.get("/Processa/Americanas")
def ProcAmericanas():
    valores = open('Repository_JSON/ProcessaAmericanas.json')
    data = json.load(valores)
    return data

@app.get("/Processa/Mesa")
def ProcMesa():
    valores = open('Repository_JSON/ProcessaMesa.json')
    data = json.load(valores)
    return data

@app.get("/Processa/Semclass")
def ProcSemclass():
    valores = open('Repository_JSON/ProcessaSemclass.json')
    data = json.load(valores)
    return data

@app.get("/Processa/Viniferas")
def ProcViniferas():
    valores = open('Repository_JSON/PRocessaViniferas.json')
    data = json.load(valores)
    return data

@app.get("/Producao")
def Producao():
    valores = open('Repository_JSON/Producao.json')
    data = json.load(valores)
    return data

if __name__ =='__main__':
    uvicorn.run(app, host="localhost", port=8001)    
    Abas_V2.inicio()
    

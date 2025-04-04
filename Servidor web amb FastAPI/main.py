### Imports ##################################################
from fastapi import FastAPI
from pydantic import BaseModel
import json
import os

# Creació de l'aplicació FastAPI
app = FastAPI()

# Model de dades Pydantic
class Data(BaseModel):
    dia: int
    mes: int
    any: int

class Alumne(BaseModel):
    nom: str
    cognom: str
    data: Data
    email: str
    feina: bool
    curs: str

# Variables globals
nom_fitxer = "alumnes.json"
alumnes = []

### Funcions auxiliars #######################################
def carregar_alumnes():
    if os.path.exists(nom_fitxer):
        with open(nom_fitxer, 'r') as f:
            return json.load(f)
    return []

def desar_alumnes():
    with open(nom_fitxer, 'w') as f:
        json.dump(alumnes, f, indent=4)

def obtenir_id():
    if not alumnes:
        return 1
    return max(alumne['id'] for alumne in alumnes) + 1

# Carregar dades inicials
alumnes = carregar_alumnes()

### Endpoints ################################################
@app.get("/")
def principal():
    return "Institut TIC de Barcelona"

@app.get("/alumnes")
def total_alumnes():
    return {"total_alumnes": len(alumnes)}

@app.get("/alumnes/{id}")
def mostra_alumne(id: int):
    for alumne in alumnes:
        if alumne["id"] == id:
            return alumne
    return {"error": "L'alumne no existeix"}

@app.delete("/alumnes/{id}")
def elimina_alumne(id: int):
    for alumne in alumnes:
        if alumne["id"] == id:
            alumnes.remove(alumne)
            desar_alumnes()
            return {"missatge": "L'alumne s'ha esborrat correctament"}
    return {"error": "L'alumne no existeix"}

@app.post("/alumnes/")
def afegir_alumne(nou: Alumne):
    nou_id = obtenir_id()
    
    nou_alumne = {
        "id": nou_id,
        "nom": nou.nom,
        "cognom": nou.cognom,
        "data": {
            "dia": nou.data.dia,
            "mes": nou.data.mes,
            "any": nou.data.any
        },
        "email": nou.email,
        "feina": nou.feina,
        "curs": nou.curs
    }
    
    alumnes.append(nou_alumne)
    desar_alumnes()
    return {"missatge": "L'alumne s'ha afegit correctament"}
#Este Proyecto se trata sobre un ChatBot que te resueva dudas sobre ahorro enegético
#Autores: Daniel Pulgarin Bedoya, Luisa Fernanda Rios Arias y German Buritica
#Fecha: 2025-02-26
#importamos la clase FastAPI del framework FastAPI
from fastapi import FastAPI, HTTPException#hhtp exceptions maneja errores
from fastapi.responses import HTMLResponse, JSONResponse #Importamos la clase HTMLResponse de la libreria fastapi.responses
import pandas as pd #Nops ayuda a manejar dataframes con tablas dinámicas 
import nltk #Nltk es una libreria para procesar textos y analizarlos
from nltk.tokenize import word_tokenize #Se usa para dividir el texto en palabras
from nltk.corpus import wordnet #Se usa para obtener sinonimos de las palabras
from fastapi.templating import Jinja2Templates #Se usa para renderizar templates
from starlette.requests import Request #Se usa para manejar solicitudes HTTP
from fastapi.staticfiles import StaticFiles #Se usa para servir archivos estáticos

#-------------------Librerias para entrenar el ChatBot-------------------   
#Librerias para procesar textos y analizarlos
from sentence_transformers import SentenceTransformer #Se usa para obtener embeddings de las preguntas
import numpy as np #Se usa para manejar matrices numéricas
from sklearn.metrics.pairwise import cosine_similarity #Se usa para calcular la similaridad entre embeddings

nltk.download('averaged_perceptron_tagger')# Esta función obliga a que la libreria nltk se descargue en el la carpeta predeterminada
#Indicamos donde encontrar el archivo csv
#descargamos las herramientas necesarias de nltk para procesar textos y analizarlos
nltk.download('punkt') #paquete para dividir el texto en palabras
nltk.download('wordnet') #paquete para obtener sinonimos de las palabras en inglés
nltk.download('punkt_tab') #consejo para error interno del servidor error 500
nltk.download('omw-1.4')  # Mejor paquete para wordnet en varios idiomas

# Cargar modelo de embeddings
model = SentenceTransformer("paraphrase-multilingual-MiniLM-L12-v2")


def load_questions():
    try:
        df = pd.read_csv("DataSet/energia.csv", encoding='utf-8')[['version', 'name', 'applied_at']]
        df.columns = ["id", "pregunta", "respuesta"]
        # Convertir preguntas a embeddings
        preguntas = df['pregunta'].tolist()
        respuestas = df['respuesta'].tolist()
        embeddings = model.encode(preguntas)
        """df.fillna('').to_dict(orient='records')"""
        return {
            "data": df.fillna('').to_dict(orient='records'),
            "preguntas": preguntas,
            "respuestas": respuestas,
            "embeddings": embeddings
        }
    except Exception as e:
        print(f"\n❌ Error al cargar las preguntas: {e}\n")
        return {"data": [], "preguntas": [], "respuestas": [], "embeddings": None}

#Cargamos las preguntas al iniciar la aplicación para no leer el archivo csv en cada solicitud
preguntaDatos=load_questions()
pregunta_list = preguntaDatos["data"]
preguntas = preguntaDatos["preguntas"]
respuestas = preguntaDatos["respuestas"]
embeddings = preguntaDatos["embeddings"]

# Función para buscar respuesta
"""def responder(pregunta_usuario):
    embedding_usuario = model.encode([pregunta_usuario])
    similitudes = cosine_similarity(embedding_usuario, embeddings)
    indice_max = np.argmax(similitudes)
    return respuestas[indice_max]
"""

#función para obtener los sinonimos de una palabra
def get_synonyms(word):
    #Usamos wordnet para obtener los sinonimos de una palabra
    return{lemma.name().lower() for syn in wordnet.synsets(word) for lemma in syn.lemmas()}

#Creamos una instancia de la clase FastAPI que sea el motor de nuestra aplicación
#Esto inicializa la app con un titulo y una version
app=FastAPI(title="WattWise: ChatBot de Ahorro Energético", version="0.0.1")

app.mount("/templates/dist", StaticFiles(directory="templates/dist"), name="static")
# Configuramos la carpeta de templates local del proyecto

templates = Jinja2Templates(directory="../WhattWise-master")

# Ruta de inicio que devuelve el archivo HTML
@app.get("/", tags=["Inicio"])
def inicio(request: Request):
    #Cuando entremos en el navegador a http://127.0.0.1:8000 nos mostrara el siguiente mensaje
    return templates.TemplateResponse("index.html", {"request": request})

#Obteniendo la lista de preguntas
#Creamos una ruta que nos permita obtener la lista de preguntas y respuestas

#Ruta para obtener todas las preguntas
@app.get("/preguntas", tags=["Preguntas"])
def preguntas():
    if pregunta_list:
        return pregunta_list
    raise HTTPException(status_code=500, detail="❌ No hay preguntas disponibles.")#muestra un error en caso de que no haya preguntas

#Ruta para obtener una sola pregunta
@app.get("/preguntas/id/{id}", tags=["Preguntas"])# Se coloca /id para que la ruta no sea ambigua
def pregunta(id:int):
    #Buscamos la pregunta en la lista de preguntas la buscamos por su id
    pregunta = next((p for p in pregunta_list if p['id'] == id), None)
    if pregunta:
        return pregunta
    raise HTTPException(status_code=404, detail="⚠️ Pregunta no encontrada")


#Ruta del chatbot que responde a las preguntas con palabras clave de la categoria

@app.get('/chatbot', tags=["Chatbot"])
def chatbot(pregunta_usuario: str):
   
    if embeddings is None:
        raise HTTPException(status_code=500, detail="❌ No hay preguntas disponibles.")
    embedding_usuario = model.encode([pregunta_usuario])
    similitudes = cosine_similarity(embedding_usuario, embeddings)
    indice_max = np.argmax(similitudes)
    return {"Respuesta":respuestas[indice_max]}
    
    
# Ruta para buscar respuestas por palabra clave
@app.get("/preguntas/keyword/{keyword}", tags=["Preguntas"])
def buscar_pregunta(keyword: str):
    # Filtramos la lista de respuestas por palabra clave 
    resultados = [p for p in pregunta_list if keyword.lower() in p['pregunta'].lower()]
    if resultados:
        return resultados
    raise HTTPException(status_code=404, detail="⚠️ No se encontraron preguntas con esa palabra clave")
    
## Equipo 4

Daniel Pulgarin Bedoya
German Anibal Buritica Quimbayo
Luisa Fernanda Ríos Arias

Diseño y desarrollo de un chatbot con conocimientos relativo al ahorro energético



ProyectoTalento Tech

Bootcamp IA
Jheyson Eduardo Galvis Valencia
Ejecutor técnico

Juan Sebastian Robledo Giraldo
Mentor

Yerson Duvan Angúlo
Monitor

Febrero 28 2025

Introducción

La energía eléctrica ha aumentado con el paso de los años, tanto los costos como su impacto
ambiental son significativos. El desconocimiento de las personas sobre cómo reducir el consumo
energético, genera unos desperdicios de recursos que pueden optimizarse con estrategias sencillas.
Buscar soluciones tecnológicas y educativas que marquen la diferencia en la reducción del gasto
energético y promocionar las buenas prácticas sostenibles.
Las plataformas digitales actualmente demuestran ser herramientas importantes para cambiar
hábitos de consumo, para influenciar a las personas o difundir información, pero, su contenido no es
el más adecuado, o enfocado a la eficiencia energética. Incorporar la inteligencia artificial y el
análisis de datos permite una mayor personalización, esta se adapta a las necesidades de cada
persona y ofrece recomendaciones más efectivas.
Este proyecto permitirá de manera personalizada, aumentar conciencia a todos los usuarios que
usen el proyecto sobre el ahorro energético, automatizando la selección de información para ofrecer
una mejor recomendación, entre más uso le den los usuarios. A la fecha del documento, el consumo
de energía es un tema crítico y este tipo de herramientas pueden ser un apoyo clave para generar un
impacto social.
Desarrollo del Proyecto
Debido al tiempo y a la cantidad de personas que trabajan en el proyecto se decide solo
metodologías ágiles y de todas las ágiles se decide trabajar con una de las más importantes que es la
metodología Scrum.

Objetivos del Proyecto:

A. Objetivo General:

Diseñar y desarrollar un chatbot con conocimientos relativos al ahorro energético

B. Objetivos Específicos:

● Aumentar la conciencia sobre el ahorro energético de manera personalizada.
● Automatizar la selección de información para ofrecer recomendaciones relevantes.
● Implementar técnicas básicas de IA , accesibles para principiantes en programación.

1. Investigación y Análisis Inicial:

Se lleva una reunión inicial donde se hizo una lluvia de ideas, se tuvieron en cuenta ideas de
las áreas de gestión hospitalaria y ciencias farmacéuticas; de tránsito y urbanismo; de arte y
diseño digital; y de ciencias ambientales; después se debate sobre la opción más viable
considerando tanto los recursos, los conocimientos del grupo de desarrollo y el tiempo
establecido para el desarrollo del proyecto, se decide optar por ciencias ambientales.
Se realizará un análisis del consumo energético actual, identificando los principales
problemas relacionados con sistemas de iluminación ineficientes. Se tuvo en cuenta
principalmente papers o artículos científicos en el desarrollo del marco teórico.
Se plantea que para afrontar la problemática, además de aplicar las técnicas que conocen y
aprendieron los miembros del proyecto sobre inteligencia artificial, es a través de un
chatbot.

Con lo anterior llegan a la conclusión de que necesitan un dataset con las siguientes

características o categorías:

1.1.1. Identificador

1.1.2. Pregunta sobre el tema a trabajar

1.1.3. Respuesta correlacionada con la pregunta

Para el desarrollo del proyecto el sistema recomendado se basa en un archivo CSV el cual
contiene preguntas y respuestas informativas sobre ahorro de energía. Se realiza la
búsqueda en las páginas recomendadas de datasets. El grupo decide que a la fecha del
documento no hay un dataset que cumpla con las características previamente establecidas,
por lo tanto, se decide crear un dataset personalizado, por medio de la Creación de Dataset
en postgrest.new:

2. Diseño y Desarrollo del aplicativo

2.1. Estructura del archivo energía.csv :

id Pregunta Respuesta

1 ¿Cómo puedo reducir el
consumo de energía en mi
hogar?
Puedes reducir el consumo de energía apagando luces y
dispositivos cuando no los uses

2 ¿Qué tipo de bombillas son
más eficientes
energéticamente?
Las bombillas LED son las más eficientes energéticamente

3 ¿Cómo puedo mejorar la
eficiencia energética de mi
refrigerador?
Mantén el refrigerador lleno

4 ¿Cuáles son las ventajas de
usar paneles solares en casa?
Los paneles solares reducen la dependencia de la red
eléctrica

Figura 1.Fuente: Elaboración propia febrero 2025

2.2. Creamos una base de datos en formato SQL la cual se debe convertir el archivo
energia.csv y guardarlo en formato CSV (separado por comas).

2.3. La consulta SQL la subimos a una página en línea llamada tableconvert la cual se encarga de
insertar el SQL y realizar la conversión en formato CSV.

2.4. Código en Python:
Figura 2.Fuente: Programa visual studio UVS Code, Elaboración propia febrero 2025

2.5. Algoritmo de recomendación

Frameworks

● FastAPI
● Motor principal de la aplicación
Ejemplo :
app =FastAPI (.), rutas como @app.get(.)
Librerías
● Pandas
● Nltk (procesamiento de lenguaje natural):
● Center transformer
● Numpy
● Sklearn
Clases y funciones:
● Request
● Jinja2 Templates
● HTTPException
● HTMLResponse
● StaticFiles
● Word_tokenize
● JSONResponse
● Cosine_similarity
● Wordnet

3. Pruebas y resultados

Se realizaron pruebas con un archivo de 100 preguntas y respuestas sobre ahorro
energético.
Figura 3.Fuente:Chatbot. ejecutado. Elaboración propia febrero 2025

1. Diseño del Chatbot:

○ Se diseña un chatbot utilizando herramientas de inteligencia artificial (IA) y
procesamiento de lenguaje natural (NLP) para garantizar interacciones fluidas y
personalizadas.
○ Se agrega un dataset con preguntas y respuestas sobre sistemas eficientes sobre
ahorro de energía y sus beneficios.
○ El lenguaje de programación que se utiliza es Python, HTML y CSS

2. Desarrollo de Estrategias de Persuasión:

○ Se implementa técnicas de persuasión digital, como mensajes personalizados y
recomendaciones basadas en datos

3. Implementación y Pruebas:

○ El chatbot se integra en plataformas digitales accesibles para los usuarios, como
sitios web.

4. Recopilación de Datos y Evaluación:

○ Se realizará un seguimiento continuo para evaluar el progreso y optimizar las
respuestas del chatbot.
Marco Teórico

● Ahorro energético: El ahorro energético es el proceso de reducir el consumo de energía sin
comprometer las necesidades de los usuarios. Esta práctica es fundamental para enfrentar
desafíos globales como el cambio climático y la sostenibilidad. Según Goswami et al. (2019),
la eficiencia energética es crucial no sólo para reducir costos, sino también para disminuir el
impacto ambiental y la huella de carbono.

● Chatbots:Un chatbot es un software que utiliza IA para mantener conversaciones
interactivas con los usuarios, ya sea por texto o por voz. Los chatbots se entrenan para
interpretar el lenguaje humano a través de técnicas de NLP y generar respuestas apropiadas
según las solicitudes de los usuarios (Shawar & Atwell, 2007).

● Inteligencia Artificial: La Inteligencia Artificial (IA) se refiere al desarrollo de sistemas
computacionales capaces de realizar tareas que normalmente requieren inteligencia
humana, como el aprendizaje, la resolución de problemas y la toma de decisiones (Russell &
Norvig, 2016).
Resultados Esperados

● Permite que el usuario realice cualquier pregunta al chatbot y reciba siempre una respuesta,
sin importar la consulta.
Conclusión:

● Profundizar en el estudio del desarrollo de la inteligencia artificial.

● Analizar cómo se construye un chatbot, evaluando su funcionamiento en la práctica.

● Comprender las herramientas y metodologías que hay para el ML, además de apoyarse,
también, de cualquier tipo de herramientas de IA para el mejoramiento y optimización de
procesos.

Proyecto: Diseño y Desarrollo de un Chatbot
relativo al ahorro energético
https://github.com/GermanBuri/WhattWise-master
Bibliografía e infografía

● Abu Shawar, B., & Atwell, E. (2007). Chatbots: Are they really useful? LDV-Forum, 22, 29–49.

● DeepSeek. (2023). DeepSeek Chat [Modelo de lenguaje grande]. https://chat.deepseek.com

● Goswami, A., Kumar, P., & Rathi, R. (2019). Energy efficiency and conservation in buildings: A

review. Energy Reports, 5, 1256–1266. https://doi.org/10.1016/j.egyr.2019.09.010

● Martínez Moreno, A. G., & López-Espinoza, A. (2016). La transición del comportamiento

alimentario: una explicación desde la teoría de la conducta. Universitas Psychologica, 15(4).
https://doi.org/10.11144/Javeriana.upsy15-4.tcae

● OpenAI. (2023). ChatGPT (Versión 3.5) [Modelo de lenguaje grande]. https://chatgpt.com

● PostgREST. (s. f.). PostgREST (Versión 10.0) [Software]. https://postgrest.org

● Russell, S. J., & Norvig, P. (2016). Artificial intelligence: A modern approach. Pearson
Education Limited.

● TableConvert. (n. d.). TableConvert: Online table converter tool. https://tableconvert.com
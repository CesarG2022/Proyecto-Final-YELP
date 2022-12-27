<center> <h1>PROYECTO FINAL -PLUS YELP</h1> </center>
<center> “Connect and simplify big data to make the best investment decisions.”</center></br>

> **Note**<br>
> This README file is written in Spanish. To go to the English version [click here](README_EN.md).


**Tabla de Contenido:**
---
- [Descripción del proyecto](#descripcion-del-proyecto-)
proposito, breve descripción y alcances 
- [Equipo](#equipo-)
- [Archivos](#el-repositorio)
lista de archivos y descripcion de funcionalidad
- [Datos](#datos)
fuente y  link a diccionario  de datos de datos en bruto
transformación y validación de datos utilizados
- [Pipeline y Stack tecnológico](#pipeline)
descripcion de pipeline, der
- [Dashboard para toma de desiciones de inversión](#dashboard-para-toma-)

- [Sistema de recomendación de restaurantes](#sistema-de-recomendacion)

# Descripción del proyecto <a name="proyecto"></a>

Este proyecto se creó para que empresarios y emprendedores puedan identificar oportunidades de inversiones en el rubro del ocio(restaurantes, bares, hoteles, entre otros) utilizando información extraida de la opinión de clientes sobre los bienes o servicios prestados por decenas de miles de negocios ubicados en estados unidos y adicionalmente se aprovechó esta gran cantidad de datos para construir un sistema de recomendación de restaurantes para clientes que busquen nuevas experiencias de consumo. 

## Objetivos:
- Identificación de categorías y características de negocios con alto potencial de aceptación y por tanto de crecimiento y con bajo riesgo de cierre.
- Identificación de localizaciones convenientes para instalar un nuevo local.
- Diseño de un sistema de recomendaciones para usuarios sin y con historial de consumo y reseñas.

## Alcance:
- Extracción, transformación o limpieza, validación y almacenamiento estructurado de los datos.
- Creación y despliegue de un dashboard como web app como herramienta de visualización de la información extraida del análisis de los datos para la toma de desición de inversión e identificación de localización(a nivel estado) para asentar un nuevo local.
- Creación y despliegue como web app de un sistema de recomendación de restaurantes para consumidores.

# Equipo <a name="equipo"></a>
- Julio Gutierrez, [CesarG2022](https://github.com/CesarG2022)
- Erick Mamani [khorneflakes-dev](https://github.com/khorneflakes-dev)
- Jonathan Santacana [JCSR2022](https://github.com/JCSR2022)

# Archivos <a name="repo"></a>

- carpeta ETL
    - Creacion_archivos_carga_incremental.ipynb : notebook para hacer la división de los datasets iniciales en datasets para carga inicial, carga incremental e incremental para pruebas de validación.
    - ETL.ipynb : Notebook para la extracción, transformación, carga a base de datos SQL de los datos de los usuarios de yelp y para creación del modelo entidad relación.
    - Incremental_load.ipynb : notebook para la transformación, validación y carga incremental de los datos de nuevas reseñas y usuarios a la base de datos.
- carpeta Web_App:
    - requirements.txt : archivo para instalar en el ambiente virtual las librerías necesarias. 
    - app.py : script para hacer el despliegue de la web app que contiene la página del dashboard y la página del sistema de recomendación. 
    - Carpeta pages :
        - trending.py : script con el código de la pestaña de tendencias(Trends) del dashboard.
        - risk.py : script con el código de la pestaña de riesgos(risks) del dashboard.
        - opportunities.py : script con el código de la pestaña de oportunidades(opportunities) del dashboard.
        - users.py : script con el código de la página  del sistema de recomendación de restaurantes

# Datos<a name="datos"></a>

Los datos sobre reseñas, usuarios y empresas, fueron obtenidos de el [dataset abierto](https://www.yelp.com/dataset) para propósitos de aprendizaje de la app Yelp que cuenta con cerca de 7 millones de reseñas realizadas por aproximadamente 2 millones de usuarios sobre el servicio y/o producto ofrecido por un poco mas de 150 mil empresas de 13 estados de EEUU.

## Diccionario de datos (!!!!!!!SUPRIMIBLE!!!!!!!!)

users:
'n_user_id': integer user code,
'review_count': number of reviews written by the user, 
'yelping_since': user registration date, 
'useful': number of useful votes given by the users to other user's reviews,
'funny': number of funny votes given by the users to other user's reviews, 
'cool': number of cool votes given by the users to other user's reviews, 
'friends': comma separated str with friend's alphanumeric codes , 
'fans': number of fans, 
'average_stars': average reviews stars given by the user.

# Pipeline y Stack Tecnológico <a name="pipeline"></a>

## Alacenamiento en bruto y Division de los datos
En esta etapa se alamacenan los datasets de yelp en bruto en google drive en la carpeta "Dataset Yelp" y se dividen los archivos en bruto user.json, business.json y review.json en tres nuevos sets de archivos .json, esto se logra ejecutando el notebook "Creacion_archivos_carga_incremental.ipynb" el cual automáticamente crea la carpeta  pruebas_incremental con los siguientes archivos:
1) Archivos de carga inicial: user_inicial.json, business_inicial.json, review_inicial.json.
2) Archivos para carga incremental batch: user_incremental_#.json, donde # es un entero entre 0 y 7,
business_incremental.json y review_incremental#.json donde # es un entero entre 1 y 29.
3) Archivos para carga incremental con errores a creados a propósito para evaluar filtros de validación de formato y de datos duplicados: user_aleatorio.json, user_incremental_con_repeticiones#.json donde # es 8 o 9, business_aleatorio,json, business_incremental_con_repeticiones.json y review_aleatorio.json, review_incremental_con_repeticiones#.json donde #=[30,34]. 

## 

<p align="center">
  <img src="pipeline.png" />
</p>

## stack tecnológico
- Extraction and transformation:
- load and storage:
- analysis:
- incremental load or streaming
- Presentation: dash plotly


# Dashboard para toma de desiciones de inversión <a name="dashboard"></a>

## KPI’s (Key Performance Indicator)

Es una metrica **clave,** estas son solo unas cuantas respecto a las metricas pero tienen un alto impacto en el negocio, por lo que mejorarlas representara un inpacto positivo para la empresa,

entendemos asi que todos los KPI’s son metricas pero no todas las metricas son KPI’s

1) Variación porcentual del promedio de estrellas(calificación):
    PCC= (promedio estrellas año 2) - (promedio estrellas año 1) / ((promedio estrellas año 1) *100

2) Variación porcentual de reviews:
    PCR = (cantidad de reviews año 2) - (cantidad de reviews año 1) /((cantidad de reviews año 1))

3) popularidad: 
    PO = promedio(polaridad*(1-subjetividad))

4) porcentaje de sucursales cerradas por rubro
    CSC = (cantidad de sucursales cerradas) / (cantidad de sucursales totales por rubro) *100

# Sistema de recomendación de restaurantes <a name="sistema-de-recomendacion"></a>

### Users dataset:
- load: it was made in chunks of 400.000 rows to the dataframe called "users"
- drop columns: all the columns with amounts of compliments.
- change data type to use less memory: 'average_stars':np.float32 , 'fans':'uint16', 'review_count':'uint16', 'cool':'uint32', 'useful':'uint32', 'funny':'uint32', yelping_since:'%Y-%m-%d %H:%M:%S'
-  get integer index to replace alphanumeric index: to use less memory the alphanumerid user_id columns was replaced by the dataframe index(0 - 1987896)
-   No duplicated or null founded 



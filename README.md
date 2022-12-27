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
- carpeta con ETL
    - Creacion_archivos_carga_incremental.ipynb:
    - ETL.ipynb
    - Incremental_load.ipynb
- carpeta con despliegues
    - app.py
    - carpeta pages:
        - trending.py
        - risk.py
        - opportunities.py
        - users.py

# Datos<a name="datos"></a>

## Diccionario de datos

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

users_ids:
'n_user_id': integer user code,
'user_id': alphanumeric user code 

# Pipeline y Stack Tecnológico <a name="pipeline"></a>

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



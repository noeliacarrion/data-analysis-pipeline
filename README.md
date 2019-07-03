# La crisis migratoria y el clima
Pipelines Project - Bootcamp Data Analytics Ironhack

Este proyecto consiste en analizar la relación ente el clima y la crisis migratoria. A partir de un dataset de Kaggle elaborado por la Organización Nacional de Migraciones he relacionado el número de muertes de migrantes y sus rutas migratorias con el tiempo que hacía en esa localización exacta. Para ello he usado la API DarkSki. El archivo principal realiza el análisis consultando a la API y devuelve los gráficos con varios resultados.

EL proyecto cuenta con los siguientes archivos:

- main.py
- god.py
- acquisiion.py
- clean.py
- api.py
- analysis.py

# Limpieza:

Primero he limpiado el dataset, eliminando las columnas que no eran necesarias para el análisis, he recategorizado las condiciones de la muerte para evaluar si el tipo de muerte está influido por las condiciones climáticas y he renombrado los países para que estuvieran bien agrupados los lugares. Después me he quedado con las locaciones con al menos cinco muertes para reducir la muestra.

# API

He utilizado la API Darsky que me ofrece el tiempo en un momento determinado en un lugar específico. A partir de las coordenadas que me ofrecía el dataset, he solicitado a la api por cada coordenada los valores de "temperatureMax", "temperatureMin" y "uvIndex" (índice de radiación ultravioleta). Dado que tenía que llamar por cada valor que necesitaba, decidí coger los datos que van desde noviembre de 2018 a marzo de 2019.

# Análisis

Lo primero que he analizado es la relación entre la temperatura mínima el número de muertes y el mes, con la idea de comprobar si cuando la temperatura es más baja en los meses de invierno hay más muertes o no. Para ello había que tener en cuenta también la localización.

Con la media de temperaturas y las gráficas obtenidas, podemos comprobar que, excepto en un caso puntual, en el que hubo 70 muertes, se producen más muertes cuando la temperatura máxima es menor y cuando las temperaturas mínimas no son tan bajas. En este caso, los extremos no son determinantes para el número de muertes de migrantes.

Tambíen se ha llegado a la conclusión de que el número de causas de muerte "Unknown" es muy elevado, lo que demuestra que faltan datos para realizar un análisis más fiable. En el caso de la frontera americana con México, es más de la mitad, por ejemplo. Por localizaciones lo que sí se puede ver es que en Centro América las principales muertes se producen por accidentes (coche, tren y otros derivados de las condiciones de las rutas), seguido del asesinato.

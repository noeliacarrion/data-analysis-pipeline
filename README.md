# Proyecto Pipelines
Pipelines Project - Bootcamp Data Analytics Ironhack

Este proyecto consiste en analizar la relación ente el clima y la crisis migratoria. A partir de un dataset de Kaggle elaborado por la Organización Nacional de Migraciones he relacionado el número de muertes de migrantes y sus rutas migratorias con el tiempo que hacía en esa localización exacta. Para ello he usado la API DarkSki.

# Limpieza:

Primero he limpiado el dataset, eliminando las columnas que no eran necesarias para el análisis, he recategorizado las condiciones de la muerte para evaluar si el tipo de muerte está influido por las condiciones climáticas y he renombrado los países para que estuvieran bien agrupados los lugares. Después me he quedado con las locaciones con al menos cinco muertes para reducir la muestra.

# API

He utilizado la API Darsky que me ofrece el tiempo en un momento determinado en un lugar específico. A partir de las coordenadas que me ofrecía el dataset, he solicitado a la api por cada coordenada los valores de "temperatureMax", "temperatureMin" y "uvIndex" (índice de radiación ultravioleta). Dado que tenía que llamar por cada valor que necesitaba, decidí coger los datos que van desde noviembre de 2018 a marzo de 2019.

# Análisis

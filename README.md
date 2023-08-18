# Proyecto Final - Data Science
##  Transformando el Turismo y Ocio a través del Análisis de Datos

### Integrantes
- Ana Milena Alfaro
- Luis Romero
- Maximiliano Vaca Col
- Enzo Montinaro
- Carolina Guzmán Rodríguez

### Introducción

Somos una consultora de Analytics contratada por una cadena hotelera con el objetivo de mejorar la experiencia del usuario al proporcionar recomendaciones personalizadas de restaurantes, cafés y lugares para visitar cercanos al alojamiento. Nuestro análisis nos permitirá obtener insights que ayudarán a nuestro cliente a mejorar su posición en el competitivo sector de turismo y ocio en los Estados Unidos.

### Alcance

El análisis se centrará en la información de los estados de Florida, California y Nevada, considerados los puntos turísticos más relevantes para nuestro cliente en Estados Unidos. Nuestro enfoque inicial incluirá la recopilación y consolidación de datos relevantes para el análisis, abarcando información sobre restaurantes, cafés, lugares turísticos y preferencias de los huéspedes. A través de técnicas de análisis de datos y aprendizaje automático, identificaremos patrones y tendencias. Además, desarrollaremos e implementaremos un sistema de recomendación personalizado basado en los intereses y preferencias de los huéspedes. Para futuras versiones, este sistema se integrará con los sistemas de reservas y CRM de la cadena hotelera. También crearemos paneles interactivos y visualizaciones para que los directivos de la cadena hotelera puedan comprender fácilmente los insights y tomar decisiones informadas.

### Roles

- Data Engineering: Ana Milena Alfaro y Enzo Montinaro
- Data Science: Carolina Guzmán Rodríguez y Luis Romero
- Data Analytics: Maximiliano Vaca Col y Luis Romero

### Objetivos del Proyecto

1. Análisis de Sentimientos y Opiniones: Realizar un análisis de sentimientos utilizando técnicas de procesamiento de lenguaje natural (NLP) en las reseñas de Yelp y Google Maps para comprender la percepción de los usuarios sobre los negocios del sector de turismo y ocio en Estados Unidos.

2. Predicción de Crecimiento o Declive: Utilizar técnicas de machine learning supervisado para predecir cuáles serán los rubros de los negocios del sector que experimentarán un crecimiento o declive en el futuro, basándose en datos históricos de reseñas y puntuaciones.

3. Sistema de Recomendación de Negocios: Desarrollar un sistema de recomendación personalizado para los usuarios de Yelp y Google Maps, que sugiera comercios del sector de turismo y ocio basados en sus preferencias y experiencias previas.

4. Recomendación de Ubicación para Nuevos Locales: Mediante un modelo de machine learning, identificar las áreas geográficas más convenientes para emplazar nuevos locales de restaurantes y negocios afines al turismo, considerando la densidad de reseñas positivas, la competencia existente y otros factores relevantes (opcional, como insights de los resultados en un Dashboard).

### KPIs (Indicadores Clave de Rendimiento) con sus Métricas Asociadas

1. Índice de Satisfacción del Cliente:
   - Métrica: Porcentaje de reseñas positivas en relación con el total de reseñas analizadas.

2. Tasa de Crecimiento Estimada por Rubro:
   - Métrica: Porcentaje de crecimiento estimado en relación con el periodo de tiempo analizado.

3. Precisión del Modelo de Recomendación:
   - Métrica: Porcentaje de aciertos en las recomendaciones realizadas respecto a las elecciones reales de los usuarios.

4. Densidad de Reseñas Positivas por Área Geográfica:
   - Métrica: Número de reseñas positivas por kilómetro cuadrado.

5. Tasa de Interacción con Recomendaciones:
   - Métrica: Porcentaje de usuarios que interactúan con las recomendaciones proporcionadas por el sistema (indicador de relevancia y utilidad de la sugerencia).

### MVP: Sistema de Análisis y Recomendación de Negocios del Sector de Turismo y Ocio en Estados Unidos

El MVP (Producto Mínimo Viable) del proyecto se centrará en los siguientes aspectos:

1. Recopilación de datos y almacenamiento: Implementaremos un sistema de extracción y recolección de datos desde las API's de Yelp y Google Maps para obtener las reseñas, puntuaciones y detalles de los negocios. Además, crearemos una base de datos para almacenar y depurar los datos recopilados, incluyendo información relevante sobre los negocios y usuarios.

2. Análisis de sentimientos y opinión: Utilizaremos técnicas de procesamiento de lenguaje natural (NLP) para analizar las reseñas de los usuarios y asignar polaridades de sentimientos (positivas, neutras o negativas) a cada reseña. Así, calcularemos métricas de opinión, como el índice de satisfacción del cliente, basadas en la polaridad de las reseñas.

3. Predicción de crecimiento o declive: Emplearemos un modelo de machine learning supervisado, como Regresión Logística o Random Forest, para predecir el crecimiento o declive de los rubros de negocios basándose en datos históricos de reseñas y puntuaciones. Validaremos el modelo utilizando técnicas de evaluación adecuadas, como validación cruzada.

4. Sistema de recomendación de negocios: Implementaremos un sistema de recomendación basado en filtrado colaborativo o técnicas de recomendación híbridas, que sugiera negocios a los usuarios según sus preferencias y experiencias anteriores. Evaluaremos la efectividad del sistema de recomendación utilizando métricas como precisión y recall.

5. Recomendación de ubicación para nuevos locales: Como una mejora continua del sistema, utilizaremos técnicas de clustering o modelos de machine learning no supervisado, como K-Means, para agrupar áreas geográficas con características similares según las reseñas y puntuaciones de los negocios. De esta manera, identificaremos las zonas más prometedoras para emplazar nuevos locales según las agrupaciones resultantes.

Es importante considerar aspectos como la seguridad y la escalabilidad en el desarrollo del MVP. Además, hemos planteado como primera alternativa el uso de la plataforma Cloud Azure para alojar la base de datos y ejecutar los modelos de machine learning, de tal manera que se facilite la administración y el escalado del sistema.

Para el desarrollo, hemos adoptado la metodología SCRUM como metodología ágil, lo que nos permite iterar rápidamente y mejorar el MVP basándonos en la retroalimentación y los resultados obtenidos. También contamos con un equipo multidisciplinario que incluye expertos en ciencia de datos, desarrollo de software y marketing para abordar los diferentes aspectos del proyecto.

### Stack Tecnológico

![Stack Tecnologico propuesto](images/stack_tecnologico.jpeg)

### Workflow

Considerando la popularidad que posee Azure, y el acceso a documentación actualizada y precisa, así como la amplia gama de soluciones que ofrece en su plataforma, desde el almacenamiento y el procesamiento de datos hasta el análisis predictivo y la visualización, hemos decidido inclinarnos por su elección.

- Data Sources: Flat files + External API
- Integration: Logic Apps Azure
- Storage: Azure Data Lake Storage Gen2
- Data Warehouse: Azure Synapse Analytics
- Machine Learning: Azure Machine Learning
- Visualization: Power BI

### Arquitectura

![Arquitectura propuesta](images/flow_preliminar.png)

Cabe destacar que la implementación específica puede variar según los recursos disponibles y las preferencias del equipo, pero las tecnologías mencionadas proporcionan una base sólida para construir el MVP y demostrar la viabilidad del proyecto de Data Science.

## Diagrama de Entidad Relación (DER)

Un esquema Starflake es una combinación de un esquema en estrella y un esquema en copo de nieve. Los esquemas Starflake son esquemas en copo de nieve en los que solo algunas de las tablas de dimensiones han sido desnormalizadas. Los esquemas Starflake buscan aprovechar los beneficios tanto de los esquemas en estrella como de los esquemas en copo de nieve. Las jerarquías de los esquemas en estrella se desnormalizan, mientras que las jerarquías de los esquemas en copo de nieve se normalizan. Los esquemas Starflake se normalizan para eliminar redundancias en las dimensiones. Para normalizar el esquema, las jerarquías dimensionales compartidas se colocan en "outriggers" (extensiones).

![Diagrama ER](images/er.png)

El esquema starflake es una variante que busca encontrar un equilibrio entre la simplicidad de las consultas del esquema estrella y la normalización del esquema copo de nieve. En el esquema starflake, algunas tablas de dimensiones pueden tener atributos normalizados (como en el esquema copo de nieve) mientras que otras mantienen una estructura de esquema estrella, lo que ayuda a mejorar el rendimiento de las consultas. En resumen, el esquema starflake es un enfoque intermedio que busca combinar lo mejor de los dos mundos, es decir, la eficiencia de consultas del esquema estrella y la normalización del esquema copo de nieve. El enfoque específico de diseño puede variar según las necesidades y las características de los datos en un proyecto particular.

## Servicio de Azure Synapse Analytics

Azure ofrece un servicio llamado Azure Synapse Analytics, que nos permite crear un Data Warehouse escalable y de alto rendimiento. Este servicio integra almacenamiento y análisis, lo que lo convierte en una opción poderosa para empresas que buscan obtener información valiosa a partir de sus datos.

### Carga Inicial

Después de crear el Data Warehouse, el siguiente paso crucial es realizar la carga inicial de datos. Esto implica mover grandes volúmenes de información desde diferentes fuentes, como bases de datos transaccionales, archivos CSV o servicios en la nube, hacia el Data Warehouse. Durante esta etapa, es esencial diseñar cuidadosamente el proceso de extracción, transformación y carga (ETL) para garantizar la calidad y la integridad de los datos.

La carga inicial puede ser un proceso intensivo, ya que estamos transfiriendo una gran cantidad de datos en una sola vez. Sin embargo, establecer una base sólida es fundamental para asegurar que los análisis posteriores sean precisos y significativos.

### Carga Incremental

Una vez que hemos realizado la carga inicial, no detenemos ahí el proceso. Los datos cambian constantemente y es crucial mantener nuestro Data Warehouse actualizado para obtener insights en tiempo real. Aquí es donde entra en juego la carga incremental.

La carga incremental implica identificar y transferir solo los datos nuevos o modificados desde las fuentes de origen al Data Warehouse. Esto reduce el tiempo y los recursos necesarios para mantener los datos actualizados. En Azure, podemos aprovechar herramientas como Azure Data Factory para automatizar y programar esta carga incremental de manera eficiente.

### Beneficios de Azure para la Carga Incremental

Azure ofrece ventajas clave en el proceso de carga incremental. Primero, puede escalar automáticamente según las necesidades de sus datos, lo que garantiza un rendimiento óptimo incluso durante los períodos de mayor demanda. Además, las capacidades de seguridad y cumplimiento de Azure aseguran que sus datos estén protegidos en todo momento.


## Machine Learning

Nuestro sistema de recomendación combina tanto el sentimiento expresado en las reseñas como las calificaciones asignadas por los usuarios. Este enfoque se descompone en dos fases fundamentales: primero, estimamos los sentimientos de las reseñas (positivos o negativos) para crear calificaciones virtuales. Luego, aplicamos un modelo de regresión lineal a estas calificaciones virtuales.

## Análisis de Sentimientos

Optamos por desarrollar y evaluar un sistema de recomendación basado en el procesamiento del lenguaje natural, específicamente diseñado para el contexto de restaurantes.

Es relevante destacar que la mayoría de las reseñas otorgadas por los usuarios están en la categoría de 5 o 4 estrellas. Esto sugiere que la mayoría de las experiencias compartidas son positivas y satisfactorias. Además, observamos que los usuarios tienden a escribir reseñas especialmente cuando han tenido una experiencia positiva en un restaurante.

![Count Of Reviews](images/countorbs.jpg)

Durante nuestro análisis, evaluamos dos modelos de Análisis de Sentimientos: VADER y RoBERTa. Los resultados mostraron una relación sólida entre el tipo de sentimiento detectado en las reseñas y las calificaciones asignadas en forma de estrellas. Por ejemplo, notamos que la mayor cantidad de reseñas con sentimiento positivo están asociadas a una calificación de 5 estrellas, mientras que las reseñas con sentimiento negativo suelen tener calificaciones más bajas.

![stars](images/stars.jpg)

![dispersion](images/dispersion.jpg)

## Modelo VADER

VADER es un modelo que analiza cada palabra individualmente en una oración y asigna un puntaje de sentimiento a cada palabra. Este enfoque no considera el contexto más amplio de la reseña ni captura elementos sutiles como sarcasmo o ironía. Al evaluar las palabras de manera independiente, VADER no logra capturar las relaciones complejas entre las palabras y puede dar lugar a interpretaciones inexactas del sentimiento general de la reseña.

## Modelo RoBERTa

Por otro lado, optamos por utilizar el modelo RoBERTa, desarrollado por la compañía Hugging Face. RoBERTa es un modelo basado en transformers, que ha sido entrenado en una amplia variedad de datos textuales. A diferencia de VADER, RoBERTa no solo considera las palabras individuales, sino que también captura el contexto y las relaciones entre las palabras en una oración. Esto le permite comprender mejor el significado completo de la reseña y capturar elementos de lenguaje más complejos como el sarcasmo y la ironía.

Optamos por implementar RoBERTa como nuestro modelo de análisis de sentimientos, ya que este enfoque es capaz de capturar tanto las palabras como el contexto relacionado con otras palabras. A continuación, se presenta un ejemplo comparativo de ambos modelos:

## Ejemplo de Reseña:

“Gran bar Happy Hour 4-7 todos los días. Vinos y cervezas $3, pizza $5, aperitivos $4.50. Cenas y almuerzos para llevar son muy razonables y rápidos. El personal es amable.”

Valores del Modelo VADER:
{'neg': 0.0, 'neu': 0.711, 'pos': 0.289, 'compound': 0.9001}

Valores del Modelo RoBERTa:
{'roberta_neg': 0.0009888249, 'roberta_neu': 0.01591682, 'roberta_pos': 0.9830943}

## Regresión Lineal

Aplicamos una combinación lineal a las calificaciones predichas por cada matriz para obtener una calificación final. Esta calificación se utiliza para ordenar los resultados y generar las recomendaciones. Dado que un establecimiento puede tener varias reseñas o calificaciones, utilizamos la mediana como valor representativo. Esta elección se basa en su resistencia a valores atípicos y su capacidad para mantener la estabilidad en presencia de datos extremos.

![lineal](images/lineal.jpg)


El diagrama a continuación ilustra el flujo de datos en nuestro sistema de recomendación. Utiliza los requerimientos del usuario, como el tipo de local gastronómico y la ubicación, para filtrar y recomendar los establecimientos relevantes.

![Categorias](images/Categorias.jpg)

![Flujo](images/Flujo.jpg)


## Uso del Sistema de Recomendación

Nuestro sistema de recomendación combina el análisis de sentimientos y la calificación de las reseñas para ofrecer recomendaciones personalizadas a los usuarios. A continuación, se describe el proceso paso a paso:

    Entrada del Usuario: El sistema toma como entrada dos parámetros principales:
        Categoría: El usuario selecciona el tipo de local gastronómico de su interés a partir de un menú predeterminado que agrupa distintas categorías disponibles.
        Ubicación: Se utiliza un archivo .csv con información de hoteles de la cadena Hilton® en diferentes estados. Se eligieron 6 hoteles en cada estado como puntos de referencia para filtrar la zona de interés y realizar la búsqueda.

    Filtrado de Locales y Reseñas: Utilizando la categoría y la ubicación proporcionadas, el sistema filtra los locales que cumplen con esas condiciones. También se filtran las reseñas asociadas a estos locales.

    Análisis de Sentimientos: Se aplica el modelo de procesamiento de lenguaje natural RoBERTa para analizar el sentimiento de las reseñas. RoBERTa contextualiza las palabras y comprende el significado y el contexto de las reseñas, lo que permite una evaluación precisa del sentimiento expresado.

    Cálculo del Puntaje Ponderado: El sistema utiliza los valores de sentimiento (roberta_pos) obtenidos de RoBERTa, junto con las calificaciones (stars) asociadas a las reseñas, para calcular un puntaje ponderado para cada tienda. Este puntaje refleja tanto la calificación numérica como el sentimiento general de las reseñas.

    Modelo de Regresión Lineal: Se crea una matriz de características y un vector objetivo utilizando los puntajes ponderados calculados. Luego, se entrena un modelo de regresión lineal utilizando estos datos.

    Generación de Recomendaciones: Una vez entrenado el modelo, se utilizan los valores calculados y ponderados para realizar recomendaciones personalizadas. Los resultados se ordenan por el valor del puntaje, y las recomendaciones se presentan a los usuarios.

![Recomendacion](images/Recomendacion.jpg)

## Resultados y Conclusiones

Nuestro análisis y experimentos demuestran que los modelos basados en procesamiento de lenguaje natural, como RoBERTa, mejoran significativamente la calidad de las recomendaciones en comparación con los enfoques que solo consideran las calificaciones numéricas. La capacidad de comprender el contexto y las relaciones entre las palabras permite una interpretación más precisa de las reseñas, lo que se traduce en recomendaciones más acertadas.

Sin embargo, es importante destacar que la cantidad y calidad de los datos son factores cruciales para el éxito del sistema. Incluso con la inclusión de información textual, la falta de reseñas o la presencia de datos dispersos pueden limitar las mejoras en las recomendaciones. A pesar de esto, nuestro sistema ofrece una solución robusta y eficaz para brindar a los usuarios recomendaciones personalizadas basadas en sus preferencias y ubicación.


## Conclusión

En resumen, la creación de un Data Warehouse en Azure es un paso fundamental para desbloquear el potencial de sus datos. La carga inicial y la carga incremental son etapas cruciales para asegurar que los datos sean precisos, actualizados y listos para el análisis. Azure ofrece un conjunto de herramientas poderosas para llevar a cabo estas tareas de manera eficiente y confiable. Al invertir en la creación y el mantenimiento de su Data Warehouse en Azure, su organización estará en una posición sólida para tomar decisiones informadas y estratégicas basadas en datos precisos y oportunos.


### Entregables Sprint 1


- Diagrama de Gantt: Acceso desde el siguiente [Enlace](https://proyectofinalhenry.atlassian.net/jira/software/projects/PF/boards/1/timeline?shared=&atlOrigin=eyJpIjoiZjY1MWVjZDUyOGRiNDM0OThhYjgzNWMwMmZiYTFjOWEiLCJwIjoiaiJ9)
- Repositorio en GitHub: Acceso desde el siguiente [Enlace](https://github.com/shdata12/data12-pf-google-yelp)
- Drive de Google: Acceso desde el siguiente [Enlace](https://drive.google.com/drive/folders/1GDtpD1LJjT0tHUuSRr8Fp52LUsNWyMK0?usp=drive_link)


### Entregables Sprint 2


- Diccionario de datos: Acceso desde el siguiente [Enlace](src/dict_dw.md)
- Diagrama de Entidad Relación: Acceso desde el siguiente [Enlace](images/er.png)
- Diagrama de Arquitectura: Acceso desde el siguiente [Enlace](images/flow_preliminar.png)



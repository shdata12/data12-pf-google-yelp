
**Tabla: CATEGORY_SHOP**


| Campo           | Tipo de dato | Descripción                             |
|-----------------|--------------|-----------------------------------------|
| id_category_shop | int64        | ID único de la relación entre categoría y tienda |
| id_shop         | object       | ID de la tienda relacionada              |
| id_category     | int64        | ID de la categoría relacionada           |


**Tabla: CATEGORY**

| Campo        | Tipo de dato | Descripción                           |
|--------------|--------------|---------------------------------------|
| id_category  | int64        | ID único de la categoría              |
| category     | object       | Nombre de la categoría                |


**Tabla: REVIEWS**

| Campo       | Tipo de dato | Descripción                         |
|-------------|--------------|-------------------------------------|
| id_reviews  | object       | ID único de la reseña               |
| id_user     | object       | ID del usuario de la reseña         |
| id_source   | object       | ID de la fuente de la reseña        |
| stars       | int64        | Calificación de la reseña           |
| id_date     | int64        | ID de la fecha de la reseña         |
| review      | object       | Texto de la reseña                  |
| likes       | int64        | Número de "Me gusta" de la reseña   |
| source      | int64        | Fuente de los datos de la reseña    |


**Tabla: USERS**

| Campo       | Tipo de dato | Descripción                       |
|-------------|--------------|-----------------------------------|
| id_user     | object       | ID único del usuario              |
| user_name   | object       | Nombre del usuario                |
| useful      | int64        | Número de votos útiles del usuario|
| fans        | int64        | Número de seguidores del usuario  |


**Tabla: SHOPS**

| Campo       | Tipo de dato | Descripción                     |
|-------------|--------------|---------------------------------|
| id_shop     | object       | ID único de la tienda           |
| name        | object       | Nombre de la tienda             |
| stars       | float64      | Calificación promedio de la tienda |
| source      | int64        | Fuente de los datos |
| id_source   | object       | ID de la fuente  |


**Tabla: LOCATION**

| Campo        | Tipo de dato | Descripción                               |
|--------------|--------------|-------------------------------------------|
| id_shop      | int64        | ID único de la tienda                     |
| state        | object       | Estado donde se encuentra la tienda       |
| latitude     | float64      | Latitud de la ubicación de la tienda      |
| longitude    | float64      | Longitud de la ubicación de la tienda     |
| postal_code  | int64        | Código postal de la ubicación de la tienda |
| city         | object       | Ciudad donde se encuentra la tienda       |
| address      | object       | Dirección de la tienda                    |


**Tabla: DAY_TIME**

| Campo        | Tipo de dato | Descripción                               |
|--------------|--------------|-------------------------------------------|
| id_time      | int64        | ID único del intervalo de tiempo          |
| day_name     | object       | Nombre del día de la semana               |
| open_time    | object       | Hora de apertura                         |
| close_time   | object       | Hora de cierre                           |
| id_shop      | object       | ID de la tienda                          |


**Tabla: CHECKIN**

| Campo        | Tipo de dato | Descripción                               |
|--------------|--------------|-------------------------------------------|
| id_checkin   | int64        | ID único del check-in                     |
| id_source    | object       | ID de la fuente del check-in              |
| id_date      | int64        | ID de la fecha del check-in               |


**Tabla: CALENDAR**

| Campo        | Tipo de dato | Descripción                               |
|--------------|--------------|-------------------------------------------|
| id_date      | int64        | ID único de la fecha                      |
| day          | int64        | Día del mes                               |
| month        | int64        | Mes                                       |
| year         | int64        | Año                                       |
| time         | time         | Hora                                      |

# Proyecto de Análisis de Datos y Tablero Interactivo en Tableau

Este proyecto contiene el análisis de datos y un tablero interactivo en Tableau, estructurado en varias carpetas y archivos que responden a las preguntas planteadas en los ejercicios.

## Estructura del Proyecto


### `data/`
Esta carpeta contiene todos los archivos de datos requeridos para el análisis, como `Fuente para dashboard.xlsx`.

### `doc/`
Aquí se encuentra el cuestionario de las preguntas del ejercicio.

### `src/`
Esta carpeta contiene los archivos de código necesarios para responder a los ejercicios planteados:

- **`Ejercicio 1.sql`**: Contiene la consulta SQL necesaria para responder el ejercicio 1.
  
- **`Ejercicio 3/`**: 
  - **`Ejercicio 3.ipynb`**: Un Jupyter Notebook que responde a las preguntas 1, 2 y 3 del ejercicio 3.
  - **`pregunta4.py`**: Un script de Python que contiene la respuesta a la pregunta 4 del ejercicio 3.
 
  
- **`Ejercicio 4/`**: Esta subcarpeta contiene el script en python  que genera un streamlit para responder a las preguntas del ejercicio 4.
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
### Ejercicio 5
El tablero está disponible en el siguiente enlace público:
[Tablero en Tableau Public](https://public.tableau.com/shared/NWGPTRY4R?:display_count=n&:origin=viz_share_link)

##### 5.6: ¿Qué pasos recomendarías seguir para liberar el tablero para el uso en el día a día por parte del cliente?
- Revisión Interna y con el Cliente: Asegurar que el tablero cubra todas las necesidades del cliente y hacer ajustes si es necesario.
- Automatización de Datos: Cambiar la carga de datos de Excel a una base de datos SQL para que se actualice automáticamente día a día.
- Documentación: Proveer una guía rápida para que el cliente tenga un recurso de referencia.
- Capacitación: Instruir al cliente sobre el uso del tablero, enfocándose en navegación, filtros y extracción de datos.
- Periodo de Pruebas: Establecer un periodo de pruebas para recibir retroalimentación y hacer ajustes finales antes de su uso diario.

##### 5.7: ¿Cómo esperarías que fuera la interacción entre IBSO y el cliente durante los siguientes 12 meses?
- Soporte Técnico: Proporcionar soporte continuo al cliente para resolver cualquier problema téxnico.
- Actualización de Datos: Revisar los datos, así como los modelos de forecast. Si el modelo comineza a fallar mucho, tal vez reconsiderar un remodelo.
- Revisiones Periódicas: Programar revisiones periódicas para evaluar el uso del tablero.


## Examen Teorico.

##### Pregunta 1:
Lo que haría sería contactar al proveedor del ERP para identificar métodos de extracción de datos, ya sea mediante una API o archivos exportables. Utilizaría una herramienta en la nube para asegurar la seguridad de la información, y en ella implementaría el pipeline de datos para mantener la información protegida en todo momento.

##### Pregunta 2:
Primero, entendería las necesidades del cliente: cuáles son sus objetivos, planes y las herramients que piensa utilizar. Con esta información, desarrollaría un plan de costos e inversión. Existen opciones de pago por uso en la nube que permiten optimizar gastos y ajustar los recursos según el consumo real.
Segundo, evaluaría la escalabilidad del proyecto, consierando si se trata de una necesidad puntual o una solución a largo plazo. En función de esto, identificaría las herramientas y servicios que mejor se adapten al proyecto.

##### PRegunta 3:
Recomendaría hacer una cacrga de datos en horarios no laborales , así como tener un respaldo, no tan actualado.
En cuanto a tiempo, esto beneficiaria las operaciones ya que la carga de datos no interferiría ni retrasaría las actividades diarias.
En conocimientos, se requerirían expertos que aseguren el funcionamiento correcto del proceso y cuenten con un respaldo en caso de fallos.
Encostos, tener un servicio de respaldo implica un incremento en gastos.


### Pregunta 4:
Buscaría cómo optimizar este query. Dado que son pocas filas, algún proceso o la conexión podría estar afectando el rendimiento

## Pregunta 5:

Revisaría las tablas de origen para asegurarme de que la conexión esté activa y que los datos no presenten errores. También consideraría revisar ciertos cálculos que podrían tenr que ver con los problemas en el rendimiento.

### Pregunta 6 
Control de acceso y autenticacion, copia de seguridad, monitoreos continuos.

### PRegunta 7

La respuesta a esta pregunta se encuentra en el file Propuesta Examen 7.xlsx



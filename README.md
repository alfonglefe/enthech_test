# Prueba para Enthec
Mini proyecto realizado siguiendo las instrucciones descritas por los compañeros de Enthec.

## Objetivo
Mediante Python, acceder al buscador de Bing para buscar, por ejemplo, los resultados de "enthec", o buscar los archivos PDF del término "test" mediante dork.

### Proceso
Buscar información y documentación sobre "dork" ya que lo desconocía, y recordar los conocimientos de Python sobre web scrapping

Acceder al buscador de Bing para obtener la URL a modificar según los criterios de búsqueda.

Creación de métodos que realizan la búsqueda y guardado de la información, usando BeautifulSoup para obtener información adicional.

Refactorización para poder usar el método desde consola, pasando de 1 a 3 argumentos, donde el primer argumento es el término de búsqueda (siempre debe venir), el segundo el tipo de archivo, y el tercero el número de páginas de las que obtener los resultados. En caso de venir dos parámetros, el segundo puede ser el tipo de archivo o el número de páginas.

Creación de Dockerfile.

### Problemas encontrados
En la tarea se desrcibe que el programa recibirá una lista de términos, donde éstos pueden ser argumentos o un array. No sabía cómo interpretarlo, y terminé entendiendo que se podía referir a poder pasar más de un argumento a la función.

La información obtenida, al lanzar el programa en local, se guardan en la carpeta "outputs" los resultados obtenidos, en txt y en json. Pero desde la imagen de docker no he sido capaz de acceder para copiar esa información a mi local.

## Conclusión
Independientemente del feedback, he conseguido aprender sobre algo de lo que tenía conocimiento nulo.

Agradecer la oportunidad al equipo de Enthec, y más concretamente a María, con la que tuve la reunión.

# Curso_De_Eanx
## Google Colab: ciencia de datos

**Subir archivos y usarlos en bloques de código**

En Ciencias de Datos necesitamos datos. Para poder usar datos en Google Colab, en la barra izquierda en Archivos (ícono de carpeta), veremos que tenemos una carpeta *sample_data*, dentro de la cuál Colab ya nos provee de algunos datos de prueba.

Para subir archivos simplemente los arrastramos a este menú. Ten en cuenta que después de un tiempo que dejes de usar el Notebook estos archivos serán eliminados.

Dependiendo del tipo de archivo, Colab permitirá mostrarnos su contenido haciendo doble clic en el mismo. Por ejemplo, para archivos ***.csv*** se abrirá una vista de tabla.

Otra forma de subir archivos es haciendo clic en la primera opción (de las tres que se muestran arriba de las carpetas), y seleccionando el archivo a subir.

La tercera opción (la de la carpeta con el logo de Drive) sirve para activar la opción de usar archivos de Drive. Al hacer clic te pedirá que ejecutes un bloque de código (autogenerado) y que pegues un código de autorización, el cuál obtendrás a través de un link que el mismo bloque mostrará. Después de esto en los Archivos aparecerá la carpeta *drive*, donde se encuentran los archivos de tu Drive listos para usarse.

Recordemos que podemos usar comandos de terminal en un bloque de código. Para usar archivos en estos comandos, las rutas se forman de acuerdo al árbol de archivos que nos muestra el panel de Archivos. Por ejemplo, para usar un archivo de drive, su ruta sería `drive/MyDrive/<archivo>`. Sabrás si estas usando una ruta correcta si obtienes autocompletado al escribirla.

**Librerías de Google Colab**

Cuando creamos un Notebook en Colab, este ya tiene algunas librerías instaladas. Algunas de estas son:

- 📊 **matplotlib**: Generación de gráficos a partir de listas o arrays.
- 🧑‍💻 **numpy**: Cómputo científico para la manipulación de vectores.
- 🧑‍💻 **pandas**: Manipulación y análisis de datos de tablas y series temporales.
- 🧑‍💻 **scipy**: Herramientas y algoritmos matemáticos.
- 📊 **seaborn**: Visualización de datos estadísticos.

Algunas de estas librerías funcionan bien con Notebooks. Algunas proveen de métodos que al ejecutarlos nos muestran resultados gráficos, como gráficos estadísticos.

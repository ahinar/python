# Instrucciones de laboratorio: Funciones, bucles y estructuras de datos

En este laboratorio se le presentará un sistema de ordenación de menús que permitirá a los usuarios   
Ingrese tres opciones para un menú de selección. Usted tiene la tarea de completar el sistema de menús para que   
que devuelve y calcula la factura final para el usuario.
 <br><br>

> ### **Consejos: Antes de empezar**
> #### **Para ver el código y las instrucciones en paralelo**, seleccione lo siguiente en la barra de herramientas de VSCode:
> - Vista -> Diseño del editor -> dos columnas
> - Para ver este archivo en modo de vista previa, haga clic con el botón derecho en este archivo README.md y 'Abrir vista previa'
> - Seleccione su archivo de código en el árbol de código, que lo abrirá en una nueva pestaña de VSCode.
> - Arrastre los archivos de código de evaluación a la segunda columna. 
> - ¡Buen trabajo! Ahora puede ver las instrucciones y el código al mismo tiempo. 
> - ¿Tiene preguntas sobre el uso de VSCode? Consulte nuestros recursos de soporte [aquí](https://www.coursera.org/learn/programming-in-python/supplement/2IEyt/visual-studio-code-on-coursera).
> #### **Para correr
> #### **Para ejecutar tu código Python**
>: seleccione el archivo de Python en el árbol de archivos de Visual Studio Code 
> - Puede hacer clic con el botón derecho del ratón en el archivo y seleccionar "Ejecutar archivo de Python en la terminal" 
> o ejecute el archivo usando el archivo más pequeño   
    Botón de reproducción en la esquina superior derecha 
> de VSCode.  
    (Seleccione "Ejecutar archivo Python en la terminal" en el menú desplegable del botón provisto)
> - Alternativamente, puede seguir las instrucciones de laboratorio que usan comandos python3 para ejecutar su código en la terminal.
> 

<br> 

## Hay tres objetivos principales de esta actividad:
1. Crear nuevas funciones para resolver problemas específicos.
2. Adquirir experiencia en el uso de bucles for para iterar sobre diferentes colecciones de datos.
3. Crear y utilizar estructuras de datos para almacenar, recuperar y recorrer datos.

<br>

## Instrucciones de ejercicio

1. Abra el script ordering_system.py presente dentro de la carpeta del proyecto.

2. Ejecute el script y, cuando se le solicite, ingrese los tres productos de su elección según el menú: 1 = espresso, 2 = café, etc.


3. To run the script, open terminal and execute the following command. 

    ```
    python3 ordering_system.py
    ```

4. Extend the script to have a new function called `calculate_subtotal`.  
 It should accept one argument which is the order list and return the sum   
 of the prices of the items in the order list.

5. Implement `calculate_tax()` which calculates the tax of the subtotal.   
The tax percentage is 15% of overall bill.

6. Implement `summarize_order()` which returns a list of the names of the items   
that the customer ordered and the total amount (including tax) that they have to pay.  
 The orders should show the name and price.

<br>

## Final Step: Let's submit your code!
Nice work! To complete this assessment:
- Save your file through File -> Save 
- Select "Submit Assignment" in your Lab toolbar. 

Your code will be autograded and return feedback shortly on the "Grades" tab.  
You can also see your score in your Programming Assignment "My Submission" tab.
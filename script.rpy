# Coloca el código de tu juego en este archivo.

# Declara los personajes usados en el juego como en el ejemplo:

define e = Character("Eileen")

define x  = Character("Jesus")

define  y = Character("Jose Juan")

# El juego comienza aquí.

label start:

    # Muestra una imagen de fondo: Aquí se usa un marcador de posición por
    # defecto. Es posible añadir un archivo en el directorio 'images' con el
    # nombre "bg room.png" or "bg room.jpg" para que se muestre aquí.
    # Podemos obtener esta wea en https://opengameart.org/

    scene bg room

    # Muestra un personaje: Se usa un marcador de posición. Es posible
    # reemplazarlo añadiendo un archivo llamado "eileen happy.png" al directorio
    # 'images'.

    show eileen happy

    # Presenta las líneas del diálogo.         //gracias
    # "Jarsh best developer" los espacios necesitan estar todos a el mismo nivel. si no se rompe lol son 5 o 4 idk creo que 4
    e "¿hola, te gustaria que te hablara soibre el judaismo?"

    y "Odio a los judíos los considero una raza inferior."

    x "no puedo creer que la escoria se tome la libertad de insultar a una chica tan linda, pero dejando eso de lado el judaismo es una basura ya que ellos crearon el capitalismo"

    e "... pense que me ayudarias eres un sonso"
    x "jajajajajajaja, si que molestar a alguien hace el dia"
    y " * no puedo creer que ese tipo sea un cretino* "
    
    
    # la verdad ni yo me acuerdo
    #  
    e "Eres feo y te odio"

    # Finaliza el juego:

    return


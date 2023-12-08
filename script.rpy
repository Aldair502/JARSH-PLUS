# Coloca el código de tu juego en este archivo.
# Please don't nuke this thing we are at https://github.com/Aldair502/JARSH-PLUS
# Declara los personajes usados en el juego como en el ejemplo:

#colores para nombre de los personajes OMG
define e = Character("Eileen", who_color="#c8ffc8")

define x  = Character("Jesus", who_color="#804000")

define  y = Character("Jose Juan")

transform half_size:
    zoom 0.5 

transform big_size:
    zoom 1.5

transform sprite:
    yalign -0.2
    xalign 0.0

# El juego comienza aquí.

label start:
    #saca el archivo de music/ y lo pone como audio de fondo (si no tienes el juego completo esto crashea)
    #Music made by SpaghettiLord1010 https://spaghettilord1010.itch.io/mcp1
    play music "audio/bg1.ogg"
    # Muestra una imagen de fondo: Aquí se usa un marcador de posición por
    # defecto. Es posible añadir un archivo en el directorio 'images' con el
    # nombre "bg room.png" or "bg room.jpg" para que se muestre aquí.
    # Podemos obtener esta wea en https://opengameart.org/

    scene uni at big_size
    with fade

    # Muestra un personaje: Se usa un marcador de posición. Es posible
    # reemplazarlo añadiendo un archivo llamado "eileen happy.png" al directorio
    # 'images'.
    # Las imagenes de Eileen se robaron desde https://opengameart.org/content/doom-girl
    show 1 at sprite
    
    # Presenta las líneas del diálogo.        
    # "Jarsh best developer" los espacios necesitan estar todos a el mismo nivel. si no se rompe lol son 5 o 4 idk creo que 4
    e "Hola!, ¿te gustaria que te hablara sobre el judaismo?"
    menu:
        "No, odio a los judios. Los concidero una raza inferior.":        
            y "Odio a los judíos los considero una raza inferior."
            pause 1.0
            show 3 at sprite with dissolve
            e "Que wea te pasa"
            jump end
    x "no puedo creer que la escoria se tome la libertad de insultar a una chica tan linda, pero dejando eso de lado el judaismo es una basura ya que ellos crearon el capitalismo"

    e "... pense que me ayudarias eres un sonso"
    x "jajajajajajaja, si que molestar a alguien hace el dia"
    y " * no puedo creer que ese tipo sea un cretino* "
    y " (se escabulle)"
    hide 3 with dissolve
    # Eso esconde a la imagen eileen happy con el efecto de disolverse
    
    
    # la verdad ni yo me acuerdo
    #  when but pero XD
    # efecto dramatico donde la musica para
    label end:
    hide 3
    hide 1
    hide 2
    stop music fadeout 4
    e "..."
    e "Eres feo y te odio"

    # Finaliza el juego:

    return



$ nombre = ""

label start:

    $ nombre = renpy.input("Contraseña")

    "Incorrecto"

    call Reintentar

    jump Respuesta


label Reintentar:

    $ nombre = renpy.input("Contraseña")

    "Incorrecto"

return

label Respuesta:

    "Que tonta eres. Siempre olvidas lo importante :(" with fade

    jump introducción
   
return
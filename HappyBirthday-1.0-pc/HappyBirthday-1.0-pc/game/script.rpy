# Vous pouvez placer le script de votre jeu dans ce fichier.

# Déclarez sous cette ligne les images, avec l'instruction 'image'
# ex: image eileen heureuse = "eileen_heureuse.png"

# Déclarez les personnages utilisés dans le jeu.
define t = Character('Thomas', color="#c8ffc8")
define l = Character('Loreleï', color="#ffc8c8")
define n = Character(' ', color= "#ffc8c8")

# Le jeu commence ici
label start:
    play music "Free.mp3"
    t "Un après-midi de Juillet."

    scene jango2
    with dissolve

    t "Je dégustais une bonne bière en terasse quand soudain..."

    show main2 with dissolve

    t "le téléphone vibre"
    t " Vous avez reçu un message sur Tinder"

    menu:
        t " Est-ce que je dois y répondre ?"
        " Répondre ":
            jump scene2
        " ignorer ":
            jump sceneA

label scene2:

    scene atomic
    show lolo with dissolve

    t " Je crois que c'est elle ..."
    t "Lorelei et Thomas se commandent une bière"
    l " Tu t'y connais un peu en jeu vidéo ?"
    t " Carrément ! J'adore."
    l " Tu connais l'arcade ? Les PCB et système Jamma"
    t " Et toi tu connais Metal Gear Solid"
    n " Après 3 pintes de bières"
    l " Tu rentres comment ?"
    t " En trotinette"
    menu:
        l " Tu veux que je te dépose chez toi ?"
        " Oui, si ça te fais pas faire de détour ":
            jump scene3
        " Non, ça ira, je connais bien la route et les abris bus du coin ":
            jump sceneA

label scene3:

    scene sadi with dissolve
    show lolo  with dissolve

    t " Désolé, je viens de me séparer depuis peu la maison est en désordre"
    l " C'est pas grave je peux comprendre ( Heureusement qu'on est pas allé chez moi)"
    t " J'ai du rosé offert par les vieilles de Vallon si tu veux"
    l " Avec plaisir j'adore le rosé ( si il savait ...)"
    t " Ca te gène si je met un peu de musique ?"
    l " Vas-y! C'est le moment de voir ce que tu aimes comme musiques"
    t " Est-ce que tu connais Beirut ?"
    l " Pas du tout !"
    menu:
        " Lui proposer de mettre de la musique":
            jump scene4
        " Choisir la musique":
            jump sceneA

label scene4:
    play music "riptide.mp3"
    scene noir with dissolve

    n " La musique a fait basculer mon coeur" 

label sceneA:
    scene tempo

    n " Erreur de temporalité"
    n " Anomalie système"

    return

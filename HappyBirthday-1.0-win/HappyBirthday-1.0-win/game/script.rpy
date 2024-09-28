# Vous pouvez placer le script de votre jeu dans ce fichier.

# Déclarez sous cette ligne les images, avec l'instruction 'image'
# ex: image eileen heureuse = "eileen_heureuse.png"

# Déclarez les personnages utilisés dans le jeu.
define t = Character('Thomas', color="#c8ffc8")
define l = Character('Loreleï', color="#ffc8c8")
define n = Character(' ', color="#ffc8c8")
define b = Character('Boss', color="#ff0000")
define z = Character('Zekiel-San', color="#ffc8c8")

# préparation GIF

image fireworks:
    "1.gif"
    pause 0.125
    "2.gif"
    pause 0.125
    "3.gif"
    pause 0.125
    "4.gif"
    pause 0.125
    "5.gif"
    pause 0.125
    "6.gif"
    pause 0.125
    "7.gif"
    pause 0.125
    "8.gif"
    pause 0.125
    "9.gif"
    pause 0.125
    "10.gif"
    pause 0.125
    "11.gif"
    pause 0.125
    "12.gif"
    pause 0.125
    "13.gif"
    pause 0.125
    "14.gif"
    pause 0.125
    repeat


# Le jeu commence ici
label start:
    play music "Free.mp3"
    t "Un après-midi de Juillet."

    scene jango2
    with dissolve


    t "Je dégustais une bonne bière en terasse quand soudain..."

    show main2 with hpunch

    n "{i} Le téléphone vibre{/i}"
    n " Vous avez reçu un message sur Tinder"
    n " Une jeune femme super mimi vous propose un verre pour vous rencontrer"

    menu:
        t " Est-ce que je dois y répondre ?"
        " Répondre et y aller ":
            jump scene2
        " Ignorer ":
            jump sceneA

label scene2:

    scene atomic
    show lolo_wait with dissolve

    t " Je crois que c'est elle ..."
    n "{i}Lorelei et Thomas se commandent une bière{/i}"
    l " Tu t'y connais un peu en jeu vidéo ?"
    t " Carrément ! J'adore."
    l " Tu connais l'arcade ? Les PCB et système Jamma ?"
    t " Et toi tu connais Metal Gear Solid ?"
    n " {i}Après 3 pintes de bières{/i}"
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
    show lolo_idea  with dissolve

    t " Désolé, je viens de me séparer depuis peu et la maison est en désordre"
    l " C'est pas grave je peux comprendre {i} ( Heureusement qu'on est pas allé chez moi){/i}"
    t " J'ai du rosé offert par les vieilles de Vallon si tu veux"
    l " Avec plaisir j'adore le rosé {i} ( si il savait ...) {/i}"
    t " Ca ne te gêne pas si je met un peu de musique ?"
    l " Vas-y! C'est le moment de voir ce que tu aimes comme musiques"
    t " Est-ce que tu connais Beirut ?"
    l " Pas du tout !"
    menu:
        " La laisser choisir la musique ":
            jump scene4
        " Imposer la musique":
            jump sceneA

label scene4:
    play music "riptide.mp3"
    scene noir with dissolve

    n "{i} La musique a fait basculer mon coeur{/i}"

    play sound "kiss.mp3"
    show heart with pixellate

    n "{i}Une nuit pleine d'amour à alors débuté{/i}"

    scene cat


    n " {i}Sony a fait pipi sur ses chaussures{/i}"

    show lolo_angry with dissolve

    l " Je vais devoir rentrer me changer."
    l " Et jeter cette paire de chaussure."
    l " Je reviens plus tard, promis"

    menu:
        "Attendre son retour":
            jump scene5
        " Lui envoyer un message ''C'était sympa mais on ira pas plus loin'' ":
            jump sceneA

label scene5:
    play music "Nantes.mp3"
    scene apptlolo with dissolve
    show lolo_happy  with dissolve

    n " {i}Plusieurs mois plus tard ...{/i}"

    t " C'est assez fatiguant de faire une nuit chez toi, puis une nuit chez moi"
    l " Oui c'est vrai, et souvent j'oublie des affaires chez moi et puis les chats se retrouvent sans personnes parfois"

    menu:
        " Rompre, emmenager avec une meuf c'est que des emmerdes":
            jump sceneA
        " Lui proposer d'emmenager ensemble":
            jump scene6


label scene6:
    scene lille with dissolve
    show lolo_happy with dissolve

    n " {i}C'est l'approche de Noël{/i}"
    t " Ca fais un mois que nous vivons ensemble"
    l " Oui, c'est un vrai bonheur! "
    t " ... "
    l " Thomas ça va ?"
    t " ..."
    l " Thomas réponds moi ..."
    menu:
        " Et si on faisait un bébé et qu'on achetait une maison ensemble ? ":
            jump scene7
        " Je crois que nous deux ça le fais vraiment pas, on devrait s'arrêter là":
            jump sceneA

label scene7:
    scene nouvellemaison
    show lolo_idea  with dissolve

    n " {i}Nous avons acheté notre maison, et nous avons subit un second confinement du au Covid{/i}"
    n " {i}Loreleï est enceinte. Sa grossesse se passe bien.{/i}"
    n " {i}Il pleut dans la maison et de gros dégâts commencent à apparaitre{/i}"

    menu:
        " Annuler l'achat de la maison":
            jump sceneA
        " Rester confiné et se gaver de patisseries":
            jump scene8

label scene8:

    n " {i}La date fatidique est arrivé, Loreleï va bientôt accoucher{/i}"
    scene jdf
    n "{i} Le déclanchement est long et prends plusieurs jours...{/i}"
    t " {i}Je vais être papa ...{/i}"
    t " {i}Je ne vais plus pouvoir sortir tout les soirs{/i}"
    t " {i}Je ne vais plus pouvoir jouer aux jeux vidéos{/i}"
    t " {i}Je vais plus avoir de vie ...{/i}"

    menu:
        "Camper à la maternité":
            jump scene9
        " Fuir ses responsabilités":
            jump sceneA

label scene9:
    scene ezekielbedroom

    n " {i}Vous êtes de retour à la maison avec le petit bébé{/i}"
    n " {i}Votre vie vous reserve encore pas mal de surprises{/i}"
    n " {i}Se poser des questions constamment c'est le propre de l'être humain{/i}"
    n " {i}Mais le plus important, c'est qu'on s'aime, non ?{/i}"

    menu:
        " Annoncer à Loreleï que vous allez changer de carrière et vous lancer dans la vente de hotdog":
            jump sceneA
        " Annoncer à Loreleï que vous avez envie d'un deuxième enfant":
            jump sceneA

label sceneA:
    scene tempo
    play music "battle.mp3"

    n " Erreur de temporalité"
    n " Anomalie système"

    show boss  with dissolve

    b " AH AH AH AH AH AH AH"

    play sound "bowser.mp3"

    b " Jeune aventurier, tu as pris de mauvaises décisions dans ta vie"
    b " Cela m'a permis d'exister et de prendre contrôle de cette temporalité"
    b " J'ai capturé cette princesse et je vais contrôler le monde grâce à son pouvoir"

    show lolo_surprise with dissolve

    menu:
        " Sauver la princesse":
            jump sceneB
        " Abandonner la princesse":
            jump GameOver

label sceneB:
    hide lolo_surprise with dissolve
    show boss  with dissolve
    n " {i}Thomas fonce dans la bête{/i}"

    show boss with hpunch

    n " {i}La bête feroce, renvoie Thomas a des milliers de kilomètres{/i}"
    n " {i}Thomas est sonné{/i}"

    menu:
        " Abandonner la princesse et se soigner":
            jump GameOver
        " Partir dans un dojo et s'entrainer dur":
            jump sceneC

label sceneC:

    scene dbz

    play music "dbz.mp3"

    n "{i} Dans un dojo bien calme, vous rencontrez un petit maitre expert en arts martiaux{/i}"

    show zekielsan with dissolve

    t " Bonjour petit maître, une bête féroce a kidnappé une jeune femme en détresse"
    t " Pouvez-vous m'enseigner vos techniques pour en venir à bout ?"
    z " Viens par ici, je vais t'entrainer pour devenir plus fort"
    z " Il te faut te concentrer sur l'essentiel"
    z " La sagesse n'est pas celui qui sait choisir entre le croc monsieur et le fruit"
    z " Mais plutôt celui qui sait manger les deux"
    z " Penses-tu être capable de maîtriser mes techniques spéciales?"

    menu:
        " S'entrainer a l'artopique":
            jump sceneD
        " S'entrainer au lancer de toile":
            jump sceneD

label sceneD:
    n " {i}Vous vous sentez plus fort{/i}"
    menu:
        " S'entrainer encore":
            jump sceneD
        " Retourner combattre la bête":
            jump sceneE

label sceneE:

    hide zekielsan  with dissolve
    scene tempo
    show boss with pixellate
    play sound "bowser.mp3"


    n "{i} Thomas engage un long combat féroce contre la bête{/i}"
    t " Tu ne t'en sortira pas si facilement"
    t " J'ai été entrainé par maître ZEKIEL"
    b " Tu ne me battera jamais et la princesse m'offrira son plus beau pouvoir !"
    b " CELUI DE L AMOUUUUUUUUR"
    n " {i}Thomas prépare sa technique la plus efficace et terasse la bete{/i}"

    play sound "fart.mp3"

    hide boss with hpunch
    show lolo_happy with pixellate

    l " Oh merci Thomas, tu m'as sauvée. Qu'est-ce que je pourrais faire pour toi ?"

    menu:
        " J'aimerai une belle récompense s'il te plait":
            jump FINAL
        " Je vous aime princesse, c'est tout ce qui compte":
            jump FINAL

label FINAL:
    play music "ff.mp3"
    scene black
    with dissolve
    show fireworks:
        xalign 0.5
        yalign 0.5

    n " Félicitation"

    return

label GameOver:

    scene noir
    play music "gameover.mp3"

    n  " GAME OVER"

    return

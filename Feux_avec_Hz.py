# Code pour vérifier le fonctionnement du montage de la semaine #2
# @auteur   R. Cloutier
# @date     Janvier 2025
# @version  1.0

import board
import time
import neopixel
import digitalio

# Configuration des lignes de contrôle et du nombre de DEL pour les modules adressables
gCtrlLedInterne = neopixel.NeoPixel(board.NEOPIXEL, 1)  # Paramètres : DEL Interne : 1 seule DEL
gCtrlBarette8Dels = neopixel.NeoPixel(board.D5, 8)  	# Paramètres : ligne de contrôle : 8 DELs pour la barrette
gCtrlBarette8Dels.brightness = 0.1 						# Puissance à 10%... évite d'aveugler les gens!

# Configuration des lignes de contrôle pour les feux
gControleFeuRouge = digitalio.DigitalInOut(board.D10)
gControleFeuRouge.direction = digitalio.Direction.OUTPUT

gControleFeuJaune = digitalio.DigitalInOut(board.D9)
gControleFeuJaune.direction = digitalio.Direction.OUTPUT

gControleFeuVert = digitalio.DigitalInOut(board.D6)
gControleFeuVert.direction = digitalio.Direction.OUTPUT

gControleFeuJaune.value = False
gControleFeuVert.value = False
gControleFeuVert.value = False

Hz = 1
while(True): # boucle qui tourne toujours

        # Rouge seulement...
        print("Activation Rouge")
          
        gCtrlLedInterne.fill([255,0,0]) # affichage en rouge directement
        gCtrlBarette8Dels.fill([0,0,0]) # remise à 0 de l'ensemble des DELs
        gCtrlBarette8Dels[0] = (255,0,0) # DEL 0 rouge
        gCtrlBarette8Dels[1] = (255,0,0) # DEL 1 rouge
          
        gControleFeuRouge.value = True
        gControleFeuJaune.value = False
        gControleFeuVert.value = False
          
        time.sleep((1/Hz)/3)
          
          # Jaune seulement...
        print("Activation Jaune")
        gCtrlLedInterne.fill([255,255,0]) # affichage en jaune directement
        gCtrlBarette8Dels.fill([0,0,0]) # remise à 0 de l'ensemble des DELs
        gCtrlBarette8Dels[3] = (255,255,0) # DEL 3 jaune
        gCtrlBarette8Dels[4] = (255,255,0) # DEL 4 jaune
          
        gControleFeuRouge.value = False
        gControleFeuJaune.value = True
        gControleFeuVert.value = False
          
        time.sleep((1/Hz)/3)
          
          # Vert seulement...
        print("Activation Vert")
        gCtrlLedInterne.fill([0,255,0]) # affichage en vert directement
        gCtrlBarette8Dels.fill([0, 0, 0]) # remise à 0 de l'ensemble des DELs
        gCtrlBarette8Dels[6] = (0,255,0) # DEL 6 vert
        gCtrlBarette8Dels[7] = (0,255,0) # DEL 7 vert
          
        gControleFeuRouge.value = False
        gControleFeuJaune.value = False
        gControleFeuVert.value = True
        time.sleep((1/Hz)/3)
          



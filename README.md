# SAE_CRYPTO

Groupe  
TD2.1 : VALIN Ophélie  
TD2.2 : RANDRIANTSOA Nathan,BOCQUET Clémence, KESKIN YASIN

## Table des matieres
- Introduction
- Lancer les programmes
- Messages en clair et chiffrés
  * Message 1
  * Message 2
  * Message 3
- Methodes de chiffrement utilisees
  * Message 1
  * Message 2
  * Message 3
- Partie 2 
- Conclusion

---

### Introduction
 Dans le cadre de la SAé 3.04, nos enseignants nous ont demandé de réaliser plusieurs fonctions de déchiffrement de messages cryptés. Par groupe de 4, nous avons donc produit différentes méthodes afin de déchiffrer chacun des messages donnés. 


### Lancer les programmes
  Pour lancer les programmes, notamment la partie 2, vous devez créer un virtualenv (ou installer les librairies nécessaires).  
  Vous trouverez à la racine du projet **requirements.txt** avec l'ensemble des dépendances.

### Messages en clair et chiffrés
#### Message 1
 *Chiffré :*  
> OQ FQJFQ P'MBBMDQZOQ MZAPUZQ OAZFUQZF X'
> UZPUHGXSMNXQ EQODQF PQ OQFFQ
> ZAGHQXXQ QZUSYQ. EQDQL-HAGE OQXGU AG OQXXQ
> CGU FDAGHQDM XM OXQ?

*Déchiffré :*  
> Ce texte d’apparence anodine contient l’indivulgable secret de cette énigme. Serez-vous celui ou celle qui trouvera la clé ?

#### Message 2
 *Chiffré :*  
> UCVLGH YUU BEQEMF TG ORETORI RIVDXQA
> QLNO82OP9CK1WU0SCY3SWR74SBDUHNB5JT6O
> KEORBB

 *Déchiffré :*  
> SUIVEZ LES TRACES DE GEORGES PAINVIN AJFB82YN9UX1GS0KPI3QOE74CZVHRLT5WD6M CRYPTO

#### Message 3
 *Chiffré :*  
> AFXFFG XADXGFV GDFDVVVVDAFX-FVDXXFAGFAGVF XGDDGAXXADFDV GFGVVDXDVFGXF FX
> VD GGGDVVXG GV VVGGGGV GAAF GVVXAVGFGG XDDFAVAF.AGGVXDG
> F VGVXVGGD
> VFXXFXAXDFAGGDAVG VGGG VVAXDGAGVVAGXAGFGXADGDVG:GXFXVFXDVFXDGGVGXDFG GGF V X VVGGGGD
> XVAGVAVVGDFFGGXGVAG!DAGFX AFDAGFFFVAAAGGAGXVFFG!FX G DGDAG 4XDG

 *Déchiffré :*
> FELICITATIONS! VOUS ALLEZ BIENTOT RECEVOIR UN CODE QUI VOUS SERVIRA PAR LA SUITE. GARDEZ-LE PRECIEUSEMENT! VOICI LE CODE A RENTRER SUR CELENE : KU4VQMKESDCDM
---

### Methodes de chiffrement utilisees
#### Message 1

Pour le premier message, la méthode de chiffrement relevée est celle de César, un chiffrement de type substitution consistant à substituer une lettre de l’alphabet par une autre selon une clé de décalage logique. Cette clé est un nombre qui est > compris entre 1 et 26 (nombre de lettres dans l’alphabet).

Nous avions pour intention de déchiffrer en utilisant une logique de fréquence d’apparition des lettres dans les mots de la langue française, afin d’augmenter l’efficacité du décryptage. Néanmoins par manque de temps, nous sommes restés sur un déchiffrement dit ‘ naïf ’ qui teste les 26 combinaisons différentes possibles. Ainsi à l’aide d’une fonction de vérification, nous renvoyons le résultat le plus cohérent et dont l’origine des mots est bien française. Cette vérification s’effectue sur les 4 premiers mots du message décrypté.

#### Message 2

Pour le second message, la méthode de chiffrement s’est avérée être celle de Vernam, un chiffrement comparable à un celui de Vigenère à l’exception de quelques conditions pour la clé : 
- Elle doit être aussi longue que le texte à chiffrer
- Elle doit être aléatoire
- Elle ne doit être utilisé qu’une seule fois
Ce chiffrement est considéré incassable si la clé ne nous est pas fournie.

Afin de déchiffrer le message, nous avons récupéré la clé ‘CINQ’ obtenue dans le message 1 et aligner avec celui à déchiffrer. On applique la substitution inverse pour chacune des lettres.
Le message obtenu après le déchiffrement nous a permis de connaître la méthode de chiffrement utilisée pour le dernier message.



#### Message 3

Pour le dernier message, à l'aide du déchiffrement du message 2 nous avons découvert la méthode de chiffrement ADFKVX. Cette méthode consiste à effectuer une substitution des lettres en réalisation une grille de 36 cases. Une fois que nous avons obtenu le message substitué, nous devons réaliser une transposition en mélangeant le mot clé dans l'ordre d'apparition de l'alphabet français. Ainsi le résultat obtenu est le message crypté.

Nous avons récupéré la grille "AJFB82YN9UX1GS0KPI3QOE74CZVHRLT5WD6M" et nous avons obtenu le mot "CRYPTO". Tout d'abord, nous avons dû créer une grille de déchiffrement avec le mot clé, pour ensuite découper le message chiffré en groupe de 2 caractères. Nous avons par la suite placé ces groupes dans la grille et inversé la permutation. Ainsi, nous avons obtenu le message chiffré intermédiaire dont il fallait comparer chaque groupement de 2 caractères avec la grille de départ. Après comparaison, 'AF' pouvait correspondre à la lettre 'A' par exemple.

### Partie 2
Pour cette partie, l'ensemble des informations telles que notre analyse, notre raisonnement et nos résultats, se trouvent dans le rapport.
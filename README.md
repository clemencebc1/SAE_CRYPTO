# SAE_CRYPTO

## Table des matieres
- Introduction
- Messages en clair et chiffrés
  * Message 1
  * Message 2
  * Message 3
- Methodes de chiffrement utilisees
  * Message 1
  * Message 2
  * Message 3
- Conclusion

---

### Introduction
 Dans le cadre de la SAé 3.04, nos enseignants nous ont demandé de réaliser plusieurs fonctions de déchiffrement de messages cryptés. Par groupe de 4, nous avons donc produit différentes méthodes afin de déchiffrer chacun des messages donnés. 

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

Afin de déchiffrer le message, nous avons récupéré la clé ‘CINQ’ obtenue dans le message 1 et aligner avec celui à déchiffrer. On applique la substitution inverse pour chacune des lettres et on décale la clé pour chaque mot.
Le message obtenu après le déchiffrement nous a permis de connaître la méthode de chiffrement utilisée pour le dernier message.



#### Message 3


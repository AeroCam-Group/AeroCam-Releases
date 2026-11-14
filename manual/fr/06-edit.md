<!-- translated from zh-TW at commit 968641f -->

# 6. Retouche photo et styles

## Éditeur photo (gratuit)
Ouvrez une photo dans **Photos du téléphone** puis appuyez sur **Modifier**. Trois onglets s'affichent en bas : **Recadrer**, **Régler** et **.np3**.

📷 Capture d'écran : éditeur photo (Recadrer, Régler, .np3)

### Recadrer
- Formats : Original, Libre, 1:1, 4:5, 3:2, 16:9, ainsi que les formats cinéma 1.66, 1.85, 2, 2.20 et 2.39. Les photos verticales utilisent automatiquement l'orientation portrait.
- Faites glisser l'intérieur du cadre pour le déplacer ; tirez sur les quatre coins pour redimensionner.
- Redressement ±45° et rotation de 90° dans le sens antihoraire (`↺`).

### Régler
Choisissez un outil dans la barre pour l'ajuster avec la molette graduée de précision, puis appuyez sur **Terminé** (les outils modifiés portent un petit point) :
- **Lumière** : Exposition, Contraste, Hautes lumières, Ombres, Blancs, Noirs.
- **Couleur** : Température, Teinte, Saturation, Vibrance.
- **Détails** : Clarté, Netteté, Vignettage.

Molette graduée : s'aligne sur chaque cran entier (0,1 IL pour l'exposition, 1° pour le redressement, 1 pour les autres) avec une légère vibration. Maintenez une extrémité pour faire défiler en continu, appuyez sur le chiffre pour saisir une valeur directement, ou appuyez deux fois / sur `↺` pour remettre à zéro.

### Commandes communes
- **↶ ↷** Annuler / Rétablir.
- Maintenez **Original** pour voir l'image avant vos retouches.
- **◧ Comparer** : curseur de séparation gauche/droite entre l'original et la photo retouchée ; le zoom à deux doigts reste synchronisé des deux côtés.
- Appuyez sur **Histogramme** en bas à droite pour afficher l'histogramme en direct.

### Enregistrement
- Originaux de l'appareil photo (toujours sur la carte mémoire) : **l'enregistrement remplace la copie sur votre téléphone**. AeroCam conserve une sauvegarde de l'original pendant 7 jours avec une option « Restaurer l'original » dans la visionneuse. Si l'appareil n'est pas connecté, l'application demande s'il faut « Remplacer » ou « Enregistrer une copie ».
- Les photos présentes uniquement sur le téléphone (prises sans carte, panoramas, fusions Shake) sont toujours enregistrées comme nouveau fichier se terminant par `_E`.
- Conserve les métadonnées EXIF avec une qualité JPEG de 95. Si l'enregistrement est interrompu, AeroCam le termine automatiquement à la prochaine ouverture de l'application.
- Filtrez par **Modifiées** dans Photos du téléphone pour retrouver vos images retouchées (marquées d'un petit `✎` en bas à gauche).
- Retoucher une copie compressée (`JPEG.S`) affiche un rappel vous conseillant de retoucher plutôt l'original de l'appareil pour une meilleure qualité.
- Les vidéos ne peuvent pas être retouchées.

---

## Retouche RAW sur téléphone (expérimental)
Les fichiers NEF s'ouvrent dans le même éditeur et s'enregistrent à côté sous `DSC_xxxx_E.JPG` (un nouvel enregistrement met à jour ce fichier). **Le fichier NEF original n'est jamais modifié**, et les données EXIF sont conservées.
- **NEF compression sans perte** : développé directement sur votre téléphone avec la balance des blancs de l'appareil photo.
- **NEF Haute efficacité / Haute efficacité★** : cette compression propriétaire ne peut pas être décodée sur téléphone ; AeroCam retouche à la place le JPEG pleine définition intégré dans le NEF. Le bandeau supérieur indique « JPEG intégré 8 bits » et « Style d'appareil appliqué : xxx ».
- Les fichiers ne contenant qu'une petite miniature sans JPEG pleine définition ne peuvent pas être retouchés (l'application explique pourquoi).

### RAW modifiable sur téléphone (basculer la compression RAW de l'appareil)
Pour que vos prochains clichés NEF puissent tous être développés directement sur votre téléphone, vous pouvez passer l'appareil en « Compression sans perte » depuis AeroCam :
- Accès via « Prendre des RAW sans perte la prochaine fois » sur le bandeau Haute efficacité de l'éditeur, ou en appuyant sur le badge de qualité d'image en haut à droite de la carte Cartes mémoire sur l'accueil (actif dès que l'appareil est réglé en RAW).
- Demande toujours confirmation avant écriture, écrit le réglage dans l'appareil, le relit pour vérification et affiche l'évolution du nombre de vues restantes (les fichiers sans perte étant plus lourds, le nombre de vues baisse légèrement).
- AeroCam mémorise le réglage précédent de cet appareil pour vous permettre de le restaurer ensuite, et ne l'écrase pas si vous l'avez déjà modifié sur le boîtier.

---

## Aperçu des styles .np3 (gratuit)
Dans l'onglet **.np3** de l'éditeur, appliquez des fichiers Nikon Picture Control (`.np3`, `.ncp`) pour prévisualiser leur rendu sur votre téléphone.
- Appuyez sur un style pour l'appliquer, réglez son intensité de 0 à 100 % et affinez le résultat dans **Régler**.
- Balayez la photo vers la gauche ou la droite pour faire défiler les styles, ou maintenez l'appui pour voir l'original. Les filtres rapides `★` Favoris et Récents apparaissent en dessous.
- Appuyez sur **Tous N ▴** pour déplier toute la bibliothèque de styles (voir ci-dessous) avec recherche et filtres.
- L'aperçu simule les courbes et la saturation : les fichiers comportant une courbe utilisent leur propre courbe, tandis que ceux créés avec les curseurs Flexible Color (« Ton par curseurs ») sont convertis en courbes d'après nos mesures sous NX Studio. **Le mélangeur de couleurs et l'étalonnage ne sont pas encore simulés** : le rendu est donc approximatif.
- Fonctionne idéalement sur les fichiers NEF. Si un JPEG a déjà reçu un Picture Control à la prise de vue, les effets se cumulent (l'application vous avertit).

📷 Capture d'écran : onglet .np3 dans l'éditeur

---

## Styles de l'appareil C1–C9 (Pro)
Gérez les emplacements Picture Control personnalisés C1–C9 de votre appareil photo depuis votre téléphone. Appuyez sur la carte **Styles de l'appareil** sur l'accueil (nécessite une connexion Wi‑Fi ou USB).
- Chaque emplacement affiche un aperçu, un nom et des badges indiquant s'il est actif, avec courbe ou Flexible Color.
- **Appuyez sur un emplacement** pour choisir un style dans votre bibliothèque et l'écrire dans l'appareil photo. AeroCam le relit pour vérification et n'affiche `✓` qu'en cas de correspondance exacte. **Appui long** ou `⋮` pour vider un emplacement. Si une photo est en cours de transfert, l'écriture attend la fin de ce fichier.
- L'appareil n'est interrogé que lorsque vous ouvrez cet écran, appuyez sur `↻`, écrivez ou effacez ; l'accueil affiche les dernières valeurs lues et l'heure de lecture.
- En dessous de C1–C9 figurent en lecture seule les 9 recettes Nikon Imaging Cloud (à ajouter via Nikon Imaging Cloud).

### Ce qui est écrit dans l'appareil photo
Les emplacements personnalisés de l'appareil reçoivent un **Picture Control de base + des curseurs de réglage**, et non un fichier `.np3` brut :
- Appuyez sur **＋ Nouveau style** dans la bibliothèque pour choisir une base (Standard, Neutre, Creative Picture Control…) et régler Accentuation, Clarté, Contraste, Luminosité, Saturation et Teinte.
- **Écriture de `.np3` / `.ncp` dans l'appareil (approximative)** : les fichiers avec courbe — ainsi que les fichiers « Ton par curseurs » convertis en courbe — écrivent **Nom + Courbe + Accentuation (Accentuation, Accentuation moyenne, Clarté)** dans un emplacement C avec la base choisie. **La saturation, le mélangeur de couleurs et l'étalonnage ne peuvent pas être écrits via la connexion** ; AeroCam liste toutes les valeurs du fichier et indique clairement ce qui ne sera pas transféré avant l'écriture.
- Pour un rendu 100 % fidèle, copiez le fichier `.np3` sur une carte mémoire et importez-le via le menu de l'appareil photo.

### Bibliothèque de styles
- Contient jusqu'à 256 styles (`.np3` et `.ncp`).
- Barre de recherche `🔍`, filtres (Tous, `★`, Récents, Avec courbe, Sur l'appareil, Inscriptibles) et **＋ Nouveau**.
- Chaque style affiche une miniature d'aperçu utilisant votre propre photo de référence importée (`＋ → « Image de référence d'aperçu… »`), ou une mire de couleurs tant qu'aucune image n'est importée.

📷 Capture d'écran : styles de l'appareil C1–C9 et bibliothèque de styles

---

## Traitement d'image : assemblage panoramique et fusion antibruit (Pro)
Sélectionnez plusieurs photos dans **Photos du téléphone** et **faites glisser la barre d'actions inférieure vers le haut** (ou touchez sa poignée) pour ouvrir « Traitement d'image ».

### Assemblage (panorama)
- Sélectionner à l'intérieur d'une pile « Panorama » assemble les vues selon leurs positions de grille enregistrées à la prise de vue et enregistre le résultat dans cette même pile avec la mention « Panorama ».
- Sélectionner n'importe quelles photos qui se chevauchent dans la galerie normale permet à AeroCam de détecter automatiquement leur agencement et d'enregistrer le résultat dans une nouvelle pile.
- Les photos impossibles à raccorder ne font pas échouer tout le lot : AeroCam assemble le plus grand groupe cohérent et indique les noms des fichiers ignorés. Pour un panorama en grille, toutes les cases doivent être présentes afin d'éviter tout trou dans l'image finale.
- Un tour complet à 360° génère un panorama à 360°. Les résultats sont automatiquement mis de niveau grâce aux données d'inclinaison enregistrées, sans effet fantôme, et conservent les données EXIF.
- Voir [Chapitre 5 Panorama](05-remote.md#panorama-assemblage) pour la méthode de prise de vue.

### Fusion antibruit (Shake)
- Aligne et fusionne par moyenne les vues sélectionnées pour réduire le bruit tout en préservant les détails ; les zones en mouvement proviennent d'une seule vue pour éviter tout dédoublement.
- Sélectionner à l'intérieur d'une pile « Shake » enregistre le résultat dans cette pile (libellé « Fusionné »), ou vous pouvez appuyer sur **Fusionner** / **Refusionner** au-dessus de la pile.
- Voir [Chapitre 5 Shake](05-remote.md#shake-fusion-antibruit) pour la méthode de prise de vue.

> Une seule tâche d'assemblage ou de fusion s'exécute à la fois. La progression s'affiche à l'écran et un appui sur la bannière ouvre le résultat une fois terminé.

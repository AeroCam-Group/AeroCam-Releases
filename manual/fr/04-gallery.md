<!-- translated from zh-TW at commit 968641f -->

# 4. Galerie

En haut de l'onglet **Pellicule**, deux sous-onglets sont disponibles : **Photos du téléphone** (déjà enregistrées sur votre téléphone) et **Carte SD de l'appareil** (parcourir directement les photos sur l'appareil photo).

## Carte SD de l'appareil
Parcourez les cartes mémoire de votre appareil photo directement depuis votre téléphone (double logement pris en charge), **sans avoir à sélectionner les photos sur l'appareil au préalable** ni à lancer la réception automatique.
- Gratuit en USB ; Pro en Wi‑Fi.
- Ouvrir l'onglet n'occupe pas l'appareil tant que vous n'appuyez pas sur « Se connecter pour parcourir la carte SD ». Comme l'appareil n'accepte qu'une seule connexion à la fois, la réception automatique se met en pause pendant la navigation et reprend automatiquement à la sortie.
- Changer d'onglet ou afficher une photo en plein écran maintient la connexion pendant 20 secondes pour reprendre instantanément. Passer l'application en arrière-plan libère immédiatement l'appareil (les téléchargements en cours se terminent d'abord).
- Si vous prenez une photo pendant que la galerie est ouverte, elle apparaît en haut en 1 à 2 secondes environ (plus rapide en USB).

📷 Capture d'écran : grille de la carte SD de l'appareil

### Navigation et filtres
- Regroupées par date de prise de vue ; appuyez sur l'icône calendrier en haut à droite pour aller directement à un jour précis (Année → Mois → Jour).
- Filtres : Tout, RAW, JPEG, Vidéo, **Non téléchargées** (uniquement les fichiers absents du téléphone) et Avec étoiles. Avec « Non téléchargées » ou « Avec étoiles », un bouton « Tout sélectionner (N) » s'affiche en bas.
- **Colonnes par ligne** : appuyez sur l'icône grille en haut à droite pour choisir entre 2 et 7 colonnes, ou pincez pour zoomer. Le mode paysage ajoute 50 % de colonnes supplémentaires.
- Pour les vidéos, seul l'en-tête est lu sans télécharger tout le fichier : en bas à gauche apparaît `▶ 0:12` (durée) et en haut à gauche `1080 24p` (définition et cadence).

### Badges sur les miniatures
Appuyez sur **ⓘ** à l'extrémité droite de la barre de filtres pour afficher la légende complète :

| Coin | Signification |
|---|---|
| Haut gauche | Deuxième carte (`SD2`) ou format vidéo |
| Haut droite | Note en étoiles |
| Bas gauche | Format de fichier : `RAW` (ambre), `JPEG` (gris) ou `▶` durée vidéo |
| Bas droite | Versions déjà sur le téléphone : **✓RAW**, **✓JPEG**, **✓JPEG.S** (plusieurs badges peuvent se superposer). Vert = original de l'appareil, bleu = copie, aucun badge = pas encore sur le téléphone |

### Sélection
- Maintenez le doigt sur une photo puis **faites glisser** pour sélectionner toute une plage ; approcher du bord de l'écran fait défiler automatiquement.
- Appuyez sur « Sélectionner » à droite d'une date pour sélectionner toute la journée.
- Pendant la sélection, la barre de navigation inférieure laisse place à la barre d'actions (Télécharger, Noter, Supprimer). Appuyez sur **✕** en haut à gauche pour annuler.

### Téléchargement
Sélectionnez des photos puis appuyez sur **Télécharger**. Chaque option indique **l'espace qu'elle occupera sur le téléphone**, avec l'espace libre affiché tout en bas :
- **Originaux** : fichiers RAW, JPEG ou vidéo complets.
- **JPEG uniquement** (Pro) : extrait le JPEG pleine taille intégré dans les fichiers RAW, ou recompresse les JPEG originaux sur le téléphone (même résolution). Enregistrés sous `DSC_1234_S.JPG` avec toutes les données EXIF. La qualité de compression (60 / 70 / 80 / 90 %, 80 % par défaut) se règle dans **Paramètres → Réception et notifications → Galerie**.
- Les téléchargements s'exécutent en file d'attente avec progression et bouton d'arrêt ; les fichiers déjà sur le téléphone sont ignorés automatiquement et consignés dans l'Historique.
- Après le téléchargement, l'application demande « Conserver la sélection ? » et l'efface automatiquement à la fin du compte à rebours pour éviter d'appuyer par erreur sur « Supprimer de l'appareil ». Cochez « Mémoriser mon choix » pour ne plus afficher cette question.

### Supprimer de l'appareil photo (Pro)
Sélectionnez des photos puis appuyez sur le bouton **rouge** « Supprimer de l'appareil photo (N) ». Après confirmation, les fichiers sont **supprimés définitivement** de la carte mémoire sans récupération possible. Les photos non encore téléchargées déclenchent un avertissement supplémentaire. Les fichiers protégés (🔑) sont ignorés par l'appareil.

> Seul le bouton rouge plein agit sur la carte mémoire de l'appareil photo. Toutes les autres suppressions ne concernent que votre téléphone.

### Affichage plein écran
Appuyez sur une miniature pour l'ouvrir en plein écran. Balayez à gauche/droite pour changer de photo ; pincez ou appuyez deux fois pour zoomer.
- **Portrait** : nom de fichier, heure et taille en haut ; paramètres de prise de vue (`vitesse · ouverture · ISO · focale`) sous la photo ; boutons d'action en bas.
- **Paysage** : la photo remplit l'écran avec les infos à droite ; touchez la photo pour masquer ou afficher les informations.
- Activer **Détails** : affiche l'histogramme RVB, le Picture Control, la balance des blancs, l'objectif, les dimensions et la taille du fichier lus directement sur l'appareil sans téléchargement préalable.

### Notation par étoiles
Notez vos photos de 1 à 5 étoiles dans la galerie, puis filtrez par « Avec étoiles » pour ne télécharger que votre sélection. Les étoiles sont écrites dans la balise EXIF Rating du fichier téléchargé et reconnues par Lightroom et les autres logiciels.

---

## Photos du téléphone
Affiche les photos déjà enregistrées sur votre téléphone, sans connexion à l'appareil photo.
- N'affiche que les fichiers toujours présents sur le téléphone : si vous supprimez une photo dans Google Photos ou une autre application, elle disparaît ici aussi, et réapparaît automatiquement si vous la restaurez depuis la corbeille.
- Triées par heure de prise de vue, avec filtres « Modifiées », « Panorama », « Shake », etc.
- **Affichage plein écran** : paramètres de prise de vue et **Détails** (heure de prise de vue, heure de transfert, histogramme RVB, Picture Control, balance des blancs, objectif, dimensions, type de fichier et source). Actions en bas : **Partager**, **Ouvrir avec…**, **Modifier** et **Supprimer**.
- **Supprimer** : sélectionnez des photos puis appuyez sur **Supprimer** pour choisir « Tout supprimer sur le téléphone », « RAW uniquement », « JPEG uniquement (.S inclus) » ou « Vidéos uniquement ». Les fichiers partent dans la **corbeille** du téléphone (récupérables pendant 30 jours dans la galerie système) ; **la carte mémoire de l'appareil reste totalement intacte**.
- **Traitement d'image** : sélectionnez plusieurs photos et faites glisser la barre d'actions inférieure vers le haut pour ouvrir « Traitement d'image » avec **Assemblage (Panorama)** et **Fusion antibruit (Shake)** — voir [Chapitre 6](06-edit.md#traitement-dimage--assemblage-panoramique-et-fusion-antibruit-pro).
- Photos manquantes ? Lancez **Paramètres → Stockage et batterie → « Réanalyser les photos du téléphone »**.

📷 Capture d'écran : grille Photos du téléphone et affichage plein écran

---

## Sauvegarde de la carte mémoire (Pro)
Sauvegardez la carte mémoire de votre appareil sur votre téléphone depuis la tuile USB (« Sauvegarder la carte mémoire ») ou le menu en haut à droite de la Pellicule (« Sauvegarde »).
- **Portée** : carte entière ou personnalisée (date de prise de vue, uniquement les fichiers absents du téléphone, SD1 / SD2).
- **Types de fichiers** : RAW + JPEG, RAW uniquement, JPEG uniquement, ou Enregistrer uniquement le JPEG depuis RAW, avec vidéos en option.
- Appuyez sur **Calculer** pour voir le nombre de fichiers, la taille totale, la durée estimée et l'espace libre sur le téléphone. Sauvegarder des RAW ou des vidéos en Wi‑Fi affiche un avertissement sur la durée.
- S'exécute en arrière-plan (mise en pause possible depuis les notifications). En cas d'interruption, l'application propose de reprendre la fois suivante.
- Chaque fichier enregistré est relu et vérifié. Une fois la sauvegarde terminée sans aucune erreur, vous pouvez appuyer sur **Supprimer les fichiers sauvegardés de l'appareil** (supprime uniquement les fichiers vérifiés de cette session, avec double confirmation).

---

## Partage par QR Code
Permettez aux personnes autour de vous de scanner un QR Code avec leur téléphone pour voir et télécharger vos photos dans leur navigateur, **sans installer d'application**.

### Comment partager
1. Dans **Photos du téléphone**, faites un appui long pour sélectionner des photos puis appuyez sur le premier bouton de la barre d'actions : **Partager**. Seules les photos déjà présentes sur le téléphone (JPEG, RAW) peuvent être partagées ; les vidéos ne sont pas encore prises en charge.
2. Un grand QR Code et une adresse courte (par ex. `192.168.43.1:8080/k7Qx2mPa`) s'affichent. Il suffit de scanner le code avec l'appareil photo d'un autre téléphone.
3. Vous pouvez aussi utiliser **Copier le lien** ou **Envoyer le lien** (LINE, Messenger, etc.).

> **Les destinataires doivent être sur le même réseau Wi‑Fi ou connectés au point d'accès mobile de votre téléphone.** Les Wi‑Fi publics des hôtels et cafés bloquent souvent les connexions entre appareils — activez votre point d'accès mobile si la page ne s'ouvre pas.

### Options
- **Définir un mot de passe** (désactivé par défaut) : demande un code PIN à 4 chiffres avant l'affichage. Le mot de passe n'est jamais inclus dans les messages partagés — communiquez-le de vive voix.
- **Qualité** : la version gratuite partage des JPEG réduits (2048 px sur le grand côté) téléchargeables un par un. La version Pro débloque la **pleine résolution**, **inclure les fichiers RAW** et le téléchargement groupé au format **ZIP**.
- **Conserver la localisation (GPS)** (désactivé par défaut) : les données GPS sont retirées par défaut des JPEG partagés et ne sont jamais affichées sur la page web. Vos fichiers originaux sur le téléphone ne sont pas modifiés.
- Arrêt automatique : réglable dans **Paramètres → Réception et notifications → Galerie** (15 / 30 / 60 minutes, 30 par défaut).

### Pendant le partage
- Le partage continue en arrière-plan même si vous quittez l'écran ou éteignez l'affichage ; la barre de notifications propose « Afficher le QR Code » et « Arrêter le partage ».
- En cas de brève coupure réseau, l'application attend 30 secondes ; si votre adresse IP change, le même code de lien est conservé et l'écran invite à rescanner.
- La page web du destinataire s'affiche automatiquement en chinois traditionnel, chinois simplifié, japonais ou anglais selon la langue de son téléphone, avec aperçu plein écran, infos EXIF et réessai en un geste en cas d'échec de téléchargement.
- **Sécurité** : l'URL contient un jeton aléatoire de 8 caractères avec blocage en cas d'essais répétés ; seules les photos sélectionnées sont accessibles ; les visiteurs peuvent uniquement voir et télécharger (aucun envoi ni suppression). Appuyer sur **Arrêter le partage** invalide le lien immédiatement.

> Les téléphones Xiaomi, OPPO et marques similaires ferment souvent les applications en arrière-plan. L'écran de partage vous rappelle de régler l'utilisation de la batterie d'AeroCam sur « Non restreinte ».

📷 Capture d'écran : écran de partage QR Code et vue navigateur du destinataire

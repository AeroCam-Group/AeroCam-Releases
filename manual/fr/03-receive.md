<!-- translated from zh-TW at commit 968641f -->

# 3. Réception automatique et enregistrement

## Tableau de bord de l'appareil
Une fois connecté, la carte supérieure de l'écran d'accueil affiche l'état en direct de votre appareil :

| Élément | Détails |
|---|---|
| Modèle, objectif | Par exemple « Nikon Z f » et « NIKKOR Z 24–120 mm f/4 » |
| Batterie | Pourcentage (passe au rouge à 20 % ou moins) |
| Connexion | Point d'accès mobile, Même Wi‑Fi, Wi‑Fi de l'appareil ou USB |
| Cartes mémoire | Espace utilisé/total et vues restantes par carte ; les deux logements sont affichés séparément |
| Qualité | Par exemple `RAW` ou `JPEG fine★ L` ; se met à jour automatiquement si vous changez la qualité ou insérez/retirez une carte |
| Destination | Par exemple « Enregistrement : carte ✓ » — voir [Destination et prise de vue sans carte](#destination-et-prise-de-vue-sans-carte) ci-dessous |
| Transfert | État actuel, avec « Historique › » en haut à droite |
| Styles de l'appareil | Derniers emplacements C1–C9 lus — voir [Chapitre 6](06-edit.md#styles-de-lappareil-c1c9-pro) |

Les éléments non fournis par l'appareil dans son mode actuel sont masqués. Passer en « Contrôle de l'appareil photo » et ouvrir la prise de vue à distance permet généralement d'afficher davantage d'informations.

### Gérer les appareils
Dépliez **Gérer les appareils (n)** sous le tableau de bord pour modifier, supprimer ou ajouter un boîtier. La page « Détails » de chaque appareil affiche :
- Modèle, numéro de série (chiffres centraux masqués ; appuyez pour afficher en entier), version du firmware, **nombre de déclenchements** et date de lecture.
- **Déclenchements mensuels** : graphique en barres des 6 derniers mois (données enregistrées depuis le début d'utilisation).
- Date, mode, objectif, niveau de batterie et espace libre sur carte lors de la dernière connexion.
- Nombre de fichiers transférés sur le téléphone, date de première connexion et profils réseau enregistrés.

Le nombre de déclenchements est lu dans les métadonnées de la photo la plus récente sur la carte mémoire ; il doit donc y avoir au moins une photo sur la carte.

### Alerte batterie faible
Envoie une notification lorsque la batterie de l'appareil descend sous le seuil défini (15 % par défaut). Une nouvelle alerte n'est envoyée que si la batterie remonte d'au moins 5 % au-dessus du seuil. Réglable dans **Paramètres → Réception et notifications**.

📷 Capture d'écran : tableau de bord de l'appareil

---

## Réception automatique (Pro)
1. Sur l'accueil, appuyez sur Wi‑Fi → **Démarrer la réception**. L'application maintient la connexion en arrière-plan (visible dans la barre de notifications).
2. En mode lecture sur l'appareil photo, appuyez sur **i → Envoyer vers l'ordinateur / Sélectionner pour envoyer** (Send to PC / Select to send, le libellé varie selon le modèle) : les photos sont transférées sur le téléphone.

Pour que chaque photo arrive automatiquement dès le déclenchement, utilisez la [Réception FTP](08-ftp.md). Lorsqu'un câble USB est branché, la réception bascule automatiquement sur l'USB.

### Mettre en pause la réception
Pendant la réception automatique Wi‑Fi, appuyez sur **⏸ Pause** en haut à droite de la carte « Transfert » (ou sur « Pause » dans la notification) pour suspendre temporairement :
- Le Wi‑Fi reste connecté ; la Pellicule et la prise de vue à distance fonctionnent normalement.
- Les photos en attente restent sur l'appareil photo et seront transférées dans l'ordre dès que vous appuierez sur **Reprendre la réception**. Le fichier en cours de transfert se termine d'abord.
- La réception reprend automatiquement si vous appuyez sur Reprendre, arrêtez la réception, fermez l'application depuis les applications récentes, perdez le Wi‑Fi, éteignez l'appareil ou branchez un câble USB.

### En cas de déconnexion
- Si la connexion coupe, AeroCam se reconnecte automatiquement. Après plusieurs échecs, l'application relance une recherche par identifiant de l'appareil afin de le retrouver même si son adresse IP a changé.
- **L'appareil bascule vers le transfert Bluetooth** : comme l'appareil n'a qu'une seule puce sans fil, il coupe le Wi‑Fi pendant un envoi Bluetooth. L'accueil affiche « L'appareil envoie des photos par Bluetooth… Le Wi‑Fi se reconnectera automatiquement ensuite » sans le compter comme une erreur.
- **La Pellicule ou la prise de vue à distance emprunte la connexion** : l'appareil n'accepte qu'une seule connexion à la fois. Lorsque vous ouvrez la Pellicule ou la prise de vue à distance, la réception automatique cède la liaison puis reprend automatiquement lorsque vous quittez l'écran.
- **Lorsque l'appareil est introuvable en Wi‑Fi** : passé le délai configuré (3 minutes par défaut), la réception s'arrête automatiquement et vous avertit pour éviter de vider la batterie. Réglable dans **Paramètres → Réception et notifications**.

---

## Règles de réception
Configurez ces options dans **Paramètres → Réception et notifications**. Le Wi‑Fi, l'USB et le FTP appliquent tous les mêmes règles.

### Types de fichiers à recevoir
Choisissez quoi enregistrer : Tous les fichiers, JPG uniquement, JPG + RAW, Photos + vidéos, ou Personnalisé (JPEG, RAW, HEIF, TIFF, Vidéo, Autre).

Trois interrupteurs supplémentaires (Pro) :

| Interrupteur | Rôle |
|---|---|
| **Enregistrer uniquement le JPEG depuis RAW** | Lors de la réception d'un RAW, extrait uniquement le JPEG pleine définition intégré au fichier (généralement 2 à 5 Mo au lieu de 20 à 50 Mo) sans perte de résolution et avec toutes les données EXIF, enregistré sous `DSC_1234_S.JPG`. Idéal pour les réseaux sociaux et le tri rapide |
| **Enregistrer un JPEG compressé** | Recompresse sur le téléphone les JPEG reçus de l'appareil (`_S.JPG`, même définition en pixels, qualité définie dans les paramètres Galerie) |
| **Remplacer la copie compressée à l'arrivée de l'original** | Supprime la copie `_S.JPG` sur le téléphone dès que le JPEG original est enregistré |

> Pour recevoir des fichiers RAW, réglez la qualité d'image de l'appareil sur RAW ou RAW+JPEG, et choisissez RAW+JPEG (et non « JPEG uniquement ») dans les options d'envoi « Connexion à l'ordinateur » de l'appareil. Le nom du menu varie selon le modèle.

### Autres règles
| Règle | Détails |
|---|---|
| Mode de réception | Continu, ou arrêt après réception d'un seul fichier |
| Vidéos volumineuses | Les vidéos dépassant le seuil (1024 Mo par défaut) sont ignorées en réception automatique, notées « Filtré » et téléchargeables manuellement |
| Dossier d'enregistrement | Par appareil, Par date, Par appareil et date, ou Par type de fichier |
| Nom de fichier | Nom d'origine (`DSC_1234.NEF`), préfixe date (`20261011_DSC_1234.NEF`), ou préfixe date et heure (`20261011_153012_DSC_1234.NEF` — permet de trier chronologiquement les photos de plusieurs boîtiers). S'applique uniquement aux fichiers enregistrés par la suite |

### Emplacement des fichiers
- Photos : `Pictures/AeroCam/…`
- Vidéos : `Movies/AeroCam/…`
- Autres fichiers : `Download/AeroCam/…`

Les autres applications comme Google Photos les voient immédiatement. Si vous désinstallez puis réinstallez AeroCam, utilisez **Paramètres → Stockage et batterie → « Réanalyser les photos du téléphone »** pour réintégrer vos anciennes photos dans la galerie.

### Détection des doublons
- Vérifiée à l'aide du numéro de série de l'appareil, du nom de fichier, de la taille, de l'heure de prise de vue et de l'empreinte du fichier. Les doublons ne sont pas enregistrés deux fois et sont notés « Doublon » dans l'historique.
- Si vous supprimez une photo sur le téléphone (y compris dans la corbeille) et la renvoyez, AeroCam l'enregistre à nouveau.
- Il n'est pas nécessaire d'arrêter puis de relancer la réception pour renvoyer une même photo.

### Même photo reçue par Bluetooth et Wi‑Fi
Le Wi‑Fi transférant les fichiers en pleine résolution, il est prioritaire :
- Si le Wi‑Fi arrive en premier et le Bluetooth ensuite : la copie Bluetooth est ignorée.
- Si le Bluetooth arrive en premier et le Wi‑Fi reçoit la même photo plus tard, l'application suit **Paramètres → Réception et notifications → « Photos déjà reçues par Bluetooth »** :
  - **Remplacer par l'original à la réception Wi‑Fi** (recommandé) : enregistre le fichier pleine taille et supprime la version réduite Bluetooth.
  - **Ne pas télécharger à nouveau en Wi‑Fi**.
  - **Conserver les deux copies**.
- Les fichiers RAW originaux sont toujours conservés.

---

## Destination et prise de vue sans carte
Détermine où sont enregistrées les photos au déclenchement. AeroCam vérifie si une carte mémoire est insérée et choisit automatiquement :
- **Carte insérée** : applique **Paramètres → Prise de vue → Destination** :
  - **Carte mémoire** : enregistre sur la carte de l'appareil photo.
  - **Carte + téléphone** (Pro) : enregistre sur la carte tout en copiant sur le téléphone.
- **Aucune carte insérée** (Pro) : bascule automatiquement vers **Téléphone uniquement (prise de vue sans carte)**. Vous pouvez déclencher normalement et les photos arrivent directement sur le téléphone, nommées d'après l'heure de prise de vue (par ex. `AC_20261025_193805.JPG`). Insérer une carte rétablit automatiquement le mode précédent.

Fonctionne depuis l'Accueil, la Pellicule et la prise de vue à distance, aussi bien en Wi‑Fi qu'en USB.

**Configuration initiale :**
1. Dans le menu Réglages personnalisés de l'appareil photo, réglez **Déclenchement sans carte** (Slot empty release lock) sur **Déclenchement autorisé** (Enable release), sinon l'appareil bloque le déclencheur sans carte.
2. En Wi‑Fi, réglez le Type de connexion de l'appareil sur **Contrôle de l'appareil photo** (Camera control). S'il est sur « Transfert des images », AeroCam vous rappelle de basculer environ 3 secondes après la première vue ; la photo reste en mémoire tampon dans le boîtier et est transférée automatiquement dès que vous changez de mode. L'USB n'a pas cette contrainte.
3. La connexion en un geste ne prend pas en charge la prise de vue sans carte — utilisez un point d'accès mobile ou le même Wi‑Fi.

**Comprendre la barre d'état** (en haut de l'Accueil et de la Pellicule) :

| Affichage | Signification |
|---|---|
| Enregistrement : carte ✓ | Enregistre sur la carte mémoire de l'appareil |
| Enregistrement : carte + téléphone ✓ | Enregistre sur la carte et sur le téléphone |
| Enregistrement : téléphone uniquement (aucune carte dans l'appareil) | Les photos sont transférées directement sur le téléphone |
| L'appareil est en mode « Transfert des images »… (rouge) | Passez le Type de connexion sur « Contrôle de l'appareil photo » |
| Wi‑Fi en un geste : pas de carte mémoire, prise de vue impossible (rouge) | Insérez une carte ou passez en point d'accès / même Wi‑Fi |
| Carte mémoire pleine (rouge) | Changez de carte ou libérez de l'espace (ne bascule pas automatiquement vers Téléphone uniquement) |
| Aucune carte mémoire dans l'appareil, prise de vue impossible (rouge) | Version gratuite, ou moins de 1 Go d'espace libre sur le téléphone |

> Sans carte mémoire, l'enregistrement vidéo est impossible et la rafale est plus lente car chaque photo doit être transférée vers le téléphone.

---

## Localisation des photos (GPS)
Dans **Paramètres → Réception et notifications → Localisation des photos**, deux interrupteurs sont proposés :
- **Envoyer la position à l'appareil photo (Bluetooth)** (activé par défaut) : à l'allumage de l'appareil ou lors d'un transfert Bluetooth, le téléphone transmet sa position GPS au boîtier pour qu'il l'inscrive dans les nouvelles photos.
- **Ajouter la position aux JPEG reçus (téléphone)** : ajoute la position du téléphone selon l'heure de prise de vue aux JPEG reçus via Wi‑Fi, USB, FTP, téléchargement galerie ou prise de vue à distance. Demande confirmation une première fois au lancement de la réception.
  - Les fichiers RAW ne sont jamais modifiés, et les photos contenant déjà des coordonnées GPS conservent les leurs.
  - L'historique de position enregistré pendant une session reste uniquement sur ce téléphone et est supprimé au bout de 24 heures.
  - Si l'heure de prise de vue ne correspond à aucun relevé, rien n'est écrit (mieux vaut aucune position qu'une position erronée).
  - AeroCam doit être ouvert au démarrage de la réception pour enregistrer la position.

> Les coordonnées GPS intégrées accompagnent le fichier original lorsque vous le partagez. Le partage par QR Code supprime la localisation par défaut — voir [Chapitre 4](04-gallery.md#partage-par-qr-code).

---

## Historique
Appuyez sur **Historique ›** en haut à droite de la carte « Transfert » sur l'accueil. Liste tous les résultats de réception, téléchargement galerie et prise de vue à distance (Réussi, Doublon, Ignoré, Échec) avec miniatures.
- Appuyez sur une ligne pour l'afficher en plein écran dans l'application.
- Vous pouvez rechercher, filtrer par appareil ou effacer l'historique. Effacer l'historique ne supprime pas les fichiers sur le téléphone.

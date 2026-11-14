<!-- translated from zh-TW at commit 968641f -->

# 2. Connecter l'appareil photo

AeroCam propose quatre méthodes de connexion. Vous pouvez en configurer plusieurs : l'application utilise automatiquement celle qui est disponible. Les quatre tuiles de l'écran d'accueil (Wi‑Fi, USB, Bluetooth, FTP) indiquent leur état respectif.

> Vous hésitez sur la procédure ? Appuyez sur **ⓘ** à côté de l'état de connexion sur l'écran d'accueil, ou en haut à droite de chaque étape dans « Ajouter un appareil photo », pour ouvrir un guide illustré (une page par méthode : point d'accès mobile, même Wi‑Fi, connexion en un geste, USB, Bluetooth et FTP) avec des captures d'écran du téléphone et de l'appareil photo, ainsi qu'une liste de vérification en cas d'échec.

## Comment choisir

| Votre besoin | Option recommandée |
|---|---|
| Recevoir les photos même appareil éteint, sans y penser | **Bluetooth** (JPEG réduits, gratuit) |
| En extérieur, sans activer de partage de connexion, pour les fichiers originaux, la galerie et la prise de vue à distance | **Connexion en un geste** (Pro) |
| Transfert automatique immédiat juste après chaque déclenchement, vitesse sans fil maximale | **[Réception FTP](08-ftp.md)** (Pro, nécessite un point d'accès mobile) |
| Connexion la plus stable, moniteur vidéo, longues sessions à distance | **Câble USB** (sélection et téléchargement manuels gratuits) |
| À la maison ou en studio | **Même Wi‑Fi** (Pro) |

## Vitesses indicatives (testé sur Nikon Zf et Pixel 10 Pro)

| Méthode | Un fichier RAW (env. 18 Mo) |
|---|---|
| Réception FTP | env. 1 s (env. 17 Mo/s) |
| Téléchargement galerie Wi‑Fi | env. 1,3 s (env. 13 Mo/s) |
| USB | Généralement plus rapide que le Wi‑Fi selon le câble (env. 35 Mo/s avec un câble USB 2.0) |
| Bluetooth | JPEG réduit (env. 2 Mo), 15 à 20 s par photo |

## Voyants de connexion sur l'écran d'accueil
Les quatre boutons Wi‑Fi, USB, Bluetooth et FTP changent de couleur selon leur état (gris lorsqu'ils ne sont pas connectés) :

| Couleur | Signification |
|---|---|
| 🟢 Vert | Connecté ou prêt (vert pâle sur Bluetooth = en veille, prêt pour l'envoi hors tension) |
| 🔵 Bleu | Transfert en cours |
| 🟠 Orange | Connexion en cours (clignotant), ou action requise (autorisation, blocage, erreur) |
| 🔴 Rouge | Le Wi‑Fi ou le Bluetooth du téléphone est désactivé |

---

## Bluetooth (gratuit, remplace SnapBridge)

### Appairage
1. Sur l'appareil photo : **MENU → Menu Réseau → Connexion au périphérique mobile → Pairage (Bluetooth) → Démarrer le pairage**.
2. Si l'appareil était déjà appairé à SnapBridge, supprimez d'abord l'appairage dans SnapBridge et oubliez l'appareil dans les réglages Bluetooth du téléphone (deux applications ne peuvent pas être appairées simultanément au même boîtier).
3. Dans AeroCam : Accueil « Bluetooth » → **Appairer l'appareil photo** → Démarrer. Le téléphone et l'appareil affichent le même code : validez sur les deux. L'appareil affiche votre téléphone sous le nom `AeroCam_<modèle du téléphone>`.

📷 Capture d'écran : tuile Bluetooth

### Après l'appairage
Une fois appairé, le Bluetooth reste actif jusqu'à ce que vous supprimiez l'appairage (avec demande de confirmation).
- En temps normal, AeroCam **écoute** simplement le signal Bluetooth en arrière-plan sans réveiller un appareil en veille.
- **À l'allumage de l'appareil photo** : AeroCam se connecte brièvement pour synchroniser l'heure et la position GPS du téléphone (afin que l'appareil l'inscrive dans les photos), puis se déconnecte.
- **Lorsque l'appareil a des photos à envoyer** : activez **Envoyer lorsque l'appareil est hors tension** (Send while off) dans le menu « Connexion au périphérique mobile » de l'appareil. L'appareil se connecte automatiquement en Bluetooth pour envoyer les photos, même une fois éteint.
- Les fichiers reçus sont des JPEG d'environ 2 Mo générés par l'appareil (les prises de vue RAW sont d'abord converties en JPEG par le boîtier), à raison de 15 à 20 secondes par image. Pour les fichiers originaux, utilisez le Wi‑Fi, l'USB ou le FTP.
- Pour récupérer les photos immédiatement, appuyez sur **Recevoir maintenant** sur la tuile Bluetooth.
- Le service reprend automatiquement après avoir désactivé/réactivé le Bluetooth, redémarré le téléphone ou mis à jour l'application. Pendant l'attente, Android impose une notification permanente discrète, que vous pouvez masquer dans les réglages système.

### États de la tuile Bluetooth
🟢 Appareil à proximité · Allumé / 🟢 Vert pâle : En veille (prêt pour l'envoi hors tension) / ⚪ Appareil introuvable (affiche l'heure de dernière détection) / 🔵 Transfert en cours / 🟠 Semble bloqué / 🔴 Bluetooth du téléphone désactivé.

Le Bluetooth n'étant pas connecté en continu, cette tuile indique si l'appareil est détecté à proximité et ce qu'il fait actuellement.

### En cas de blocage
- Si aucune donnée n'arrive pendant 30 secondes durant un transfert, l'application se déconnecte automatiquement et l'appareil réessaie plus tard ; après 20 secondes d'inactivité, la tuile passe au jaune (« Semble bloqué »).
- **Déconnecter et reconnecter** : interrompt uniquement le transfert en cours.
- **⋮ → Redémarrer le service Bluetooth** : relance tout le service Bluetooth en arrière-plan tout en conservant l'appairage.
- En prise de vue RAW, l'appareil doit convertir chaque photo en JPEG avant l'envoi. Manipuler l'appareil pendant le transfert (mi-course du déclencheur, prise de vue) annule l'envoi. Le plus simple est d'éteindre l'appareil après la prise de vue et de le laisser transférer en arrière-plan.

---

## Wi‑Fi (Pro) : trois méthodes

| Méthode | Fonctionnement | Quand l'utiliser |
|---|---|---|
| **Connexion en un geste** (recommandée) | Demande par Bluetooth à l'appareil d'activer son propre Wi‑Fi et y connecte le téléphone automatiquement | En extérieur, sans vouloir activer de partage de connexion |
| **Point d'accès mobile** (recommandé dans le guide) | L'appareil photo se connecte au partage de connexion de votre téléphone | Si la connexion en un geste est instable, ou pour utiliser le FTP ou la prise de vue sans carte |
| **Même Wi‑Fi** | Le téléphone et l'appareil se connectent au même routeur | À la maison ou en studio |

### Connexion en un geste
1. Effectuez d'abord l'**appairage Bluetooth**.
2. Sur l'accueil, appuyez sur Wi‑Fi → « Connexion en un geste ».
3. La première fois, saisissez le **mot de passe** Wi‑Fi de l'appareil photo (le nom du réseau, du type `NIKON_…`, est rempli automatiquement). Il reste enregistré uniquement sur votre téléphone.
4. Lorsque Android demande l'autorisation de se connecter au Wi‑Fi, acceptez.
5. Dès que « Connecté au Wi‑Fi de l'appareil » s'affiche, la galerie, la prise de vue à distance et la réception automatique passent par cette liaison. Appuyez sur « Déconnecter » pour revenir à votre Wi‑Fi habituel.

Si la galerie ou la prise de vue à distance n'est pas encore connectée, un bouton « Se connecter via le Wi‑Fi de l'appareil » apparaît aussi directement à l'écran.

> - Tant que vous êtes connecté au Wi‑Fi de l'appareil photo, le téléphone utilise les données mobiles pour Internet.
> - La connexion en un geste **n'est pas compatible avec le FTP** et **ne prend pas en charge la prise de vue sans carte** (utilisez un point d'accès mobile ou le même Wi‑Fi s'il n'y a pas de carte dans l'appareil).

📷 Capture d'écran : carte Connexion en un geste et état connecté

### Point d'accès mobile / Même Wi‑Fi (premier appairage)
1. Sur l'appareil photo : **MENU → Menu Réseau → Connexion à l'ordinateur** (Connect to PC), et créez un profil réseau (vers le point d'accès de votre téléphone ou votre Wi‑Fi domestique).
   - Modèles récents (disposant de « Type de connexion » dans le menu) : réglez « Type de connexion » sur **Transfert des images**.
   - Modèles plus anciens : sélectionnez simplement **Connexion à l'ordinateur**.
2. Dans AeroCam : **Accueil → « ＋ » Ajouter un appareil photo**, puis choisissez le mode de connexion (Même Wi‑Fi ou Point d'accès mobile). L'application vérifie le réseau et recherche l'appareil automatiquement ; vous pouvez aussi saisir son adresse IP manuellement.
3. L'écran de l'appareil photo affiche un **code PIN à 4 chiffres**. Saisissez-le sur le téléphone, puis appuyez sur OK sur l'appareil.
4. Une fois terminé, un « profil d'appareil photo » est enregistré pour les prochaines connexions directes. Vous pouvez enregistrer plusieurs boîtiers et plusieurs réseaux ; **aucun réappairage n'est nécessaire** après une mise à jour de l'application, et AeroCam retrouve l'appareil même si son adresse IP change.

> Si l'appareil affiche « Déjà appairé avec un autre périphérique », ce profil réseau est utilisé par une autre application. Créez un nouveau profil réseau sur l'appareil et recommencez l'appairage.

📷 Capture d'écran : assistant d'ajout d'appareil et saisie du code PIN

### Vérifications avant connexion
- Lorsque vous appuyez sur « Démarrer la réception » ou ouvrez la Pellicule / Prise de vue à distance, AeroCam vérifie d'abord le réseau. Si le profil utilise « Point d'accès mobile » alors qu'il est éteint (ou « Même Wi‑Fi » sans y être connecté), un bandeau jaune s'affiche (par ex. « Veuillez d'abord activer le point d'accès mobile ») avec des raccourcis « Paramètres point d'accès » et « Paramètres Wi‑Fi ». Une fois activé, revenez dans AeroCam et le bandeau disparaît.
- Si l'appareil reste introuvable sur le Wi‑Fi ou le point d'accès, l'accueil affiche « Appareil photo introuvable sur le réseau » (souvent parce que « Connexion à l'ordinateur » n'est pas activé sur le boîtier) avec un bouton « Voir le guide de connexion ».

### Type de connexion (Connection type) sur l'appareil
Modèles récents (Z9, Z8, Z6III, Zf, Z5II, Z50II…) : **MENU → Menu Réseau → Connexion à l'ordinateur → Type de connexion**
- **Transfert des images** (Image transfer) : pour la réception automatique et la navigation sur la carte mémoire.
- **Contrôle de l'appareil photo** (Camera control) : pour la prise de vue à distance et la prise de vue sans carte.

Le changement coupe brièvement le Wi‑Fi de l'appareil ; AeroCam se reconnecte automatiquement sans réappairage. Si vous ouvrez la prise de vue à distance alors que l'appareil est encore sur « Transfert des images », l'application indique la marche à suivre.

---

## Câble USB
Plus rapide et plus stable que le Wi‑Fi, **sans appairage** et sans avoir à ajouter l'appareil au préalable.
1. Réglez l'option USB de l'appareil photo sur **MTP/PTP** (pas « iPhone » ni « UVC/UAC »).
2. Utilisez un câble USB‑C **compatible transfert de données** (certains câbles ne font que la charge). Un câble USB 3 certifié 5 Gbit/s ou 10 Gbit/s offre de meilleurs débits.
3. Sur l'accueil, la tuile USB affiche « Z f détecté · Autorisation d'accès requise » → appuyez sur « Autoriser l'accès » et validez la demande Android une fois.

### Couleurs de la tuile USB
| Couleur | Signification |
|---|---|
| ⚪ Gris | Aucun appareil détecté (ou câble de charge uniquement) |
| 🟠 Orange | Appareil détecté ; autorisation d'accès requise |
| 🔴 Rouge | Réglage USB différent de MTP/PTP, accès refusé ou échec du test (motif affiché) |
| 🟢 Vert | Connecté par câble USB |

### Lorsque le câble est branché
- La Pellicule, la prise de vue à distance et la réception automatique **basculent automatiquement sur l'USB** ; débrancher le câble repasse automatiquement en Wi‑Fi. Brancher le câble pendant une prise de vue à distance Wi‑Fi bascule aussi vers l'USB sans coupure (sauf pendant un intervallomètre, un bracketing ou une pose Bulb en cours).
- **Réception USB** (Pro) : appuyez sur « Démarrer la réception » sur la tuile USB pour enregistrer les nouvelles photos et celles envoyées via « Envoyer vers l'ordinateur » sur l'appareil. Activé automatiquement au branchement par défaut (**Paramètres → Prise de vue → « Démarrer automatiquement la réception au branchement USB »**).
- **Synchronisation de l'horloge** : synchronise l'heure de l'appareil au branchement (corrige uniquement si l'écart dépasse 2 secondes ; demande confirmation au-delà de 1 jour d'écart).
- **Maintien en éveil** : envoie un léger signal toutes les 10 secondes tant que la Pellicule ou la prise de vue à distance est ouverte pour éviter la mise en veille ; s'arrête après 30 minutes d'inactivité ou si la batterie de l'appareil est faible.
- Le téléphone peut alimenter l'appareil via l'USB — prévoyez une batterie externe pour les longues sessions.
- **Test USB** (⋮ en haut à droite de la tuile USB) : teste la connexion, les infos de l'appareil, les cartes mémoire, la cadence d'aperçu et la vitesse de lecture.

📷 Capture d'écran : tuile USB

---

## FTP
L'appareil photo pousse lui-même les photos vers le téléphone juste après la prise de vue — voir [Chapitre 8](08-ftp.md).

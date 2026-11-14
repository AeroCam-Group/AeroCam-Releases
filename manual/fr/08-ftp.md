<!-- translated from zh-TW at commit 968641f -->

# 8. Réception FTP (Pro)

Votre appareil photo **envoie directement les photos vers votre téléphone en FTP** juste après chaque déclenchement — inutile de sélectionner les photos sur le boîtier ou d'ouvrir la galerie. Testé sur un Nikon Zf, chaque fichier RAW d'environ 18 Mo arrive sur le téléphone en 1 seconde environ.

AeroCam intègre son propre serveur FTP : **vous n'avez aucun serveur externe à installer**.

## Idéal pour
- Événements, mariages et sport : les photos arrivent sur le téléphone au fur et à mesure des prises de vue.
- Contrôle immédiat et partage sur les réseaux sociaux juste après avoir déclenché.

## Prérequis
- Un appareil photo doté d'une fonction d'envoi FTP intégrée (Nikon Z f, Z 8, Z 9, Z 6III, etc.).
- Le **point d'accès mobile** de votre téléphone activé avec l'appareil photo connecté dessus (ou les deux connectés au même routeur).
- Une carte mémoire insérée dans l'appareil photo (le FTP transfère les fichiers depuis la carte).

## Première configuration
1. Activez le point d'accès mobile de votre téléphone.
2. Dans AeroCam, ouvrez la carte **FTP** sur l'accueil → appuyez tout en haut sur **Démarrer la réception**. La carte affiche les paramètres du serveur — appuyez sur chaque champ pour le copier :
   - Adresse du serveur (par ex. `10.14.29.30`)
   - Port : `2121`
   - Nom d'utilisateur : `aerocam`
   - Mot de passe : mot de passe à 8 caractères généré par l'application (appuyez sur « Régénérer » à tout moment)
   - Mode passif (PASV) : **Activé**
3. Sur votre appareil photo : **MENU → Menu Réseau → Connexion au serveur FTP → Réglages réseau → Créer un profil** :
   - Sélectionnez le point d'accès mobile de votre téléphone pour le Wi‑Fi.
   - Choisissez `FTP` comme type de serveur, saisissez l'adresse, le port, le nom d'utilisateur et le mot de passe ci-dessus, puis activez le mode passif.
4. Activez cette connexion FTP sur l'appareil photo. La configuration est terminée dès que la tuile FTP d'AeroCam affiche « Connecté ».
5. Dans le menu FTP de l'appareil photo, activez **Envoi automatique** (Auto send / envoi après prise de vue) pour que chaque nouvelle photo soit transférée automatiquement.

Un doute sur une étape ? Appuyez sur **ⓘ** à côté de la tuile FTP pour ouvrir un guide illustré.

📷 Capture d'écran : carte de paramètres FTP dépliée

## En cours d'utilisation
- Voyant d'état : Désactivé, Actif · En attente de l'appareil, Connecté, Réception en cours ou Erreur.
- La notification indique « Réception FTP · N reçues » ainsi que le nom du fichier en cours et la vitesse de transfert.
- Les photos sont enregistrées selon vos règles **Paramètres → Réception et notifications** (dossier, nom de fichier, JPEG uniquement, Enregistrer uniquement le JPEG depuis RAW, etc.) et consignées avec la source `FTP`.
- Si le transfert coupe ou si l'appareil s'éteint en cours d'envoi, les fichiers incomplets sont supprimés automatiquement afin qu'aucun fichier corrompu n'apparaisse dans votre galerie.
- Une fois l'appareil éteint, l'état passe à déconnecté en 1 minute environ ; rallumer l'appareil rétablit la connexion automatiquement.
- **Arrêt automatique en cas d'inactivité** : **Paramètres → Réception et notifications → « Arrêt automatique FTP en cas d'inactivité »** (Jamais, 5, 10 ou 30 minutes). Décompté depuis la dernière photo reçue, n'interrompt jamais un transfert en cours et envoie une notification à l'arrêt.

## Points importants
- **Gardez votre point d'accès mobile activé.** Certains téléphones coupent automatiquement leur point d'accès lorsqu'aucun appareil n'utilise de données Internet — désactivez « Désactiver automatiquement le point d'accès » dans les paramètres de partage de connexion de votre téléphone.
- Désactiver puis réactiver le point d'accès peut modifier l'adresse IP de votre téléphone ; mettez-la à jour sur l'appareil photo si nécessaire.
- La réception FTP et la **réception automatique Wi‑Fi ne peuvent pas fonctionner en même temps** — démarrer l'une arrête automatiquement l'autre.
- Tant que le FTP est actif, l'appareil photo est en mode FTP : **la Pellicule et la prise de vue à distance ne peuvent pas se connecter en Wi‑Fi**. Utilisez un câble USB, ou arrêtez la réception FTP et repassez l'appareil sur « Connexion à l'ordinateur ».
- Le serveur FTP écoute uniquement sur votre point d'accès mobile ou réseau Wi‑Fi local et n'est jamais exposé sur Internet.
- La connexion en un geste n'est pas compatible avec le FTP (elle active le Wi‑Fi propre de l'appareil photo, alors que le FTP demande à l'appareil de rejoindre le réseau de votre téléphone).

## Envoi direct vers un NAS
Vous pouvez également configurer les réglages FTP de votre appareil photo directement vers un NAS domestique sans passer par le téléphone. Il s'agit d'une fonction intégrée à l'appareil photo qui ne nécessite pas AeroCam.

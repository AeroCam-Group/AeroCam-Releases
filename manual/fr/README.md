<!-- translated from zh-TW at commit 968641f -->

# Manuel d'utilisation d'AeroCam (Français)

> Correspond à la **Beta 92.04.08.10** (mise à jour le 2026-11-15). Les lignes marquées 📷 indiquent l'emplacement des futures captures d'écran.

AeroCam transfère directement les photos de votre appareil photo vers votre téléphone Android. L'application permet aussi de contrôler l'appareil à distance, de retoucher vos photos sur le téléphone et d'écrire des profils de style dans l'appareil photo. Les appareils **Nikon série Z** sont pris en charge pour le moment, et d'autres marques suivront.

AeroCam est une application tierce développée de manière indépendante, sans aucune affiliation ni autorisation de Nikon ou de tout autre fabricant d'appareils photo.

## Sommaire

1. [Installation et premiers pas](01-install.md) : installation, autorisations, visite de l'interface, clé de test, mises à jour, langue
2. [Connecter l'appareil photo](02-connect.md) : Bluetooth, Wi‑Fi (Connexion en un geste / point d'accès mobile / même Wi‑Fi), câble USB, comment choisir, guide de connexion
3. [Réception automatique et enregistrement](03-receive.md) : démarrer/mettre en pause la réception, règles de réception, dossiers et noms de fichiers, prise de vue sans carte, localisation des photos, tableau de bord de l'appareil, historique
4. [Galerie](04-gallery.md) : carte mémoire de l'appareil, photos du téléphone, téléchargement et suppression, notation par étoiles, sauvegarde de la carte mémoire, partage par QR Code
5. [Prise de vue à distance et télécommande](05-remote.md) : prise de vue à distance Wi‑Fi/USB, méthodes de prise de vue, aides à la prise de vue, télécommande Bluetooth, moniteur vidéo, mode nuit étoilée
6. [Retouche photo et styles](06-edit.md) : éditeur, aperçu des styles .np3, retouche RAW sur téléphone, styles de l'appareil C1–C9, assemblage panoramique, fusion antibruit (Shake)
7. [Détail des paramètres](07-settings.md)
8. [Réception FTP](08-ftp.md) : l'appareil photo envoie automatiquement les photos vers le téléphone après la prise de vue
9. [Gratuit / Pro / Cine](09-tiers.md)
10. [Confidentialité et statistiques anonymes](10-privacy.md)
11. [Questions fréquentes et dépannage](11-faq.md)
12. [Signaler un problème](12-report.md)

## Appareils photo pris en charge

| Modèle | Réception automatique, galerie de l'appareil | Prise de vue à distance | État |
|---|---|---|---|
| Z9, Z8, Z6III, Zf, Z5II, Z50II, ZR et autres modèles ayant « Type de connexion » (Connection type) dans le menu | ✅ | ✅ | Testé sur Zf ; retours bienvenus pour les autres modèles |
| Z6, Z7, Z6II, Z7II, Z5, Z50, Zfc, Z30 et modèles plus anciens | ✅ | ❌ (non pris en charge par le protocole de connexion de ces modèles) | Retours bienvenus |
| Canon, Sony, Fujifilm | En préparation | En préparation | |

Si vous avez testé l'application avec un autre modèle, indiquez-nous ce qui fonctionne ou non via le formulaire [Rapport d'appareil photo](https://github.com/AeroCam-Group/AeroCam-Releases/issues/new/choose).

## Prérequis
- Un téléphone sous Android 10 ou version ultérieure.
- Un appareil photo Nikon série Z.

## Glossaire
| Terme utilisé dans ce manuel | Signification |
|---|---|
| Galerie de l'appareil / carte mémoire de l'appareil | Photos présentes sur la carte mémoire de l'appareil photo, consultées depuis le téléphone via une connexion |
| Photos du téléphone / galerie du téléphone | Photos déjà enregistrées sur votre téléphone |
| RAW | Fichiers NEF de Nikon |
| JPEG.S | JPEG compressé (JPEG extrait d'un RAW, JPEG recompressé par le téléphone ou version réduite envoyée par Bluetooth), se terminant par `_S.JPG` |
| Picture Control | Profils de couleurs de l'appareil photo, comme Standard ou Neutre ; les profils personnalisés sont enregistrés dans C1–C9 |
| Pro / Cine | Niveaux payants ; pendant la Beta, saisissez la clé de test gratuite pour tout débloquer — voir [Chapitre 9](09-tiers.md) |

<!-- translated from zh-TW at commit 968641f -->

# 1. Installation et premiers pas

## Installation
1. Téléchargez le dernier APK Beta (`…-Beta-xx.xx.xx.apk`) depuis [Releases](https://github.com/AeroCam-Group/AeroCam-Releases/releases/latest).
2. Ouvrez l'APK sur votre téléphone. La première fois, Android vous demande d'autoriser « Installer des applications inconnues » — acceptez.
3. Lorsqu'une nouvelle version sort, téléchargez-la et installez-la simplement par-dessus l'ancienne : vos appareils appairés et vos paramètres sont conservés.

> Téléchargez l'application uniquement depuis AeroCam-Releases. Les APK provenant d'autres sources peuvent avoir été modifiés. Si le message « Ceci n'est pas une version officielle » s'affiche à l'ouverture, l'application a été reconditionnée par un tiers : elle refusera les clés de test et pourrait contenir du code indésirable. Désinstallez-la et téléchargez-la à nouveau depuis AeroCam-Releases.

> Si vous utilisiez une **ancienne Beta antérieure à la 92.03.09** : les nouvelles versions s'installent comme une application distincte. Appairez à nouveau votre appareil photo, saisissez la clé de test, puis désinstallez l'ancienne version une fois que tout fonctionne.

📷 Capture d'écran : écran système « Installer des applications inconnues »

## Autorisations
L'application ne demande une autorisation qu'au moment où vous utilisez la fonction correspondante. Vous pouvez refuser celles dont vous n'avez pas besoin :

| Autorisation | Utilité |
|---|---|
| Bluetooth, Appareils à proximité | Appairage Bluetooth, transfert photo Bluetooth, télécommande Bluetooth ; également requis sous Android 13+ pour détecter les appareils photo Wi‑Fi |
| Position | Envoyer la position GPS du téléphone à l'appareil photo pour l'inscrire dans les photos, ou ajouter la localisation aux JPEG reçus ; également requis par Android pour lire le nom du réseau Wi‑Fi |
| Notifications | Progression de réception, photos reçues, problèmes de transfert, alerte batterie faible de l'appareil |
| Photos et vidéos | Afficher et organiser les photos sur votre téléphone |

Le détail de chaque autorisation est expliqué dans [Confidentialité et statistiques anonymes](10-privacy.md).

## Visite de l'interface
Quatre onglets se trouvent en bas de l'écran :

| Onglet | Contenu |
|---|---|
| **Accueil** | Tableau de bord de l'appareil (batterie, objectif, cartes mémoire, état de connexion), quatre modes de connexion (Wi‑Fi, USB, Bluetooth, FTP), état et historique des transferts, styles de l'appareil, gérer les appareils |
| **Pellicule** | Deux sous-onglets : « Photos du téléphone » et « Carte SD de l'appareil » — voir [Chapitre 4](04-gallery.md) |
| **Prise de vue à distance** | Afficher la visée écran de l'appareil sur le téléphone, régler les paramètres, prendre des photos et des vidéos — voir [Chapitre 5](05-remote.md) |
| **Paramètres** | Cinq catégories — voir [Chapitre 7](07-settings.md) |

Si vous ne savez pas comment connecter votre appareil photo, appuyez sur **ⓘ** à côté de l'état de connexion sur l'écran d'accueil, ou en haut à droite de chaque étape dans « Ajouter un appareil photo », pour ouvrir un guide illustré étape par étape.

📷 Capture d'écran : écran d'accueil

## Clé de test (débloquer Pro et Cine)
La version Beta démarre en version gratuite.
1. Copiez la clé de test actuelle sur la [page d'accueil AeroCam-Releases](https://github.com/AeroCam-Group/AeroCam-Releases). Dans l'application, **Paramètres → Assistance → « Obtenir une clé gratuite »** ouvre directement cette page.
2. Allez dans **Paramètres → Assistance → « Saisir une clé de test »**, collez le texte complet et appuyez sur « Appliquer ». Appuyer sur une fonction verrouillée affiche également « Saisir une clé de test » dans la boîte de dialogue.
3. Chaque clé est valable 14 jours et renouvelée chaque semaine. À expiration, l'application repasse en version gratuite — collez simplement la nouvelle clé.

> La Beta et les clés de test sont **gratuites** et publiées uniquement sur GitHub dans AeroCam-Releases. Si quelqu'un vous demande de payer, il ne s'agit pas d'un canal officiel.

## Rechercher des mises à jour
La Beta vérifie automatiquement les mises à jour une fois par jour au premier lancement. Vous pouvez aussi vérifier manuellement via **Paramètres → Assistance → « Rechercher des mises à jour »**.

## Langue
L'interface prend en charge le chinois traditionnel, le chinois simplifié, le japonais, l'anglais, 한국어, Deutsch, Français, Español, Tiếng Việt, ไทย et Bahasa Indonesia. Par défaut, elle suit la langue système de votre téléphone, mais vous pouvez la changer dans **Paramètres → Apparence et langue → Langue**.

L'anglais, le chinois traditionnel et le japonais sont toujours traduits à 100 %. Dans les autres langues, les nouvelles fonctions peuvent d'abord apparaître en anglais avant d'être traduites ultérieurement. Si vous repérez une erreur de traduction, signalez-la via le formulaire « Erreur de traduction » dans [Signaler un problème](12-report.md).

## Statistiques d'utilisation anonymes
Lors de votre première connexion à un appareil photo, l'application explique une fois l'envoi de statistiques d'utilisation anonymes. Vous pouvez choisir « OK » ou « Désactiver » — rien n'est envoyé avant votre réponse. Vous pouvez les désactiver à tout moment dans **Paramètres → Assistance**. Pour savoir ce qui est envoyé ou jamais envoyé, consultez [Confidentialité et statistiques anonymes](10-privacy.md).

<!-- translated from zh-TW at commit 968641f -->

# 10. Confidentialité et statistiques anonymes

AeroCam n'utilise aucun compte utilisateur. Vos photos sont transférées directement entre votre appareil photo et votre téléphone et **ne sont jamais envoyées vers un quelconque serveur**. Seuls les quelques éléments ci-dessous quittent votre téléphone.

## Connexions à Internet de l'application
| Fonction | Ce qui est envoyé | Désactivable ? |
|---|---|---|
| Rechercher des mises à jour (Beta) | Interroge uniquement GitHub pour obtenir les infos de dernière version | S'exécute automatiquement une fois par jour |
| Statistiques d'utilisation anonymes | Voir ci-dessous | Oui, dans Paramètres → Assistance |
| Partage par QR Code | Fonctionne uniquement sur votre réseau local (même Wi‑Fi ou point d'accès mobile) pour permettre aux personnes qui scannent de voir vos photos sélectionnées | S'arrête lorsque vous appuyez sur Arrêter ou à la fin du minuteur |

## Statistiques d'utilisation anonymes
Servent à estimer le nombre d'utilisateurs d'AeroCam, les appareils photo et fonctions les plus utilisés, ainsi que les points de blocage afin d'orienter les prochains développements. **Jamais vendues à qui que ce soit et jamais utilisées à des fins publicitaires.**

- **Interrupteur** : **Paramètres → Assistance → « Envoyer des statistiques d'utilisation anonymes »**, activé par défaut.
- Expliqué une fois lors de la première connexion à un appareil photo, où vous pouvez choisir « OK » ou « Désactiver ». **Rien n'est envoyé avant votre réponse.**
- **Une fois désactivé** : l'envoi s'arrête immédiatement, et l'identifiant aléatoire ci-dessous ainsi que toutes les données non encore envoyées sont supprimés. Le réactiver génère un nouvel identifiant.
- Hors ligne (par exemple lorsque vous êtes connecté au Wi‑Fi propre de l'appareil photo), les événements sont conservés sur votre téléphone et envoyés plus tard dès qu'une connexion Internet est disponible.
- Les versions Dev n'enregistrent et n'envoient jamais de statistiques.

### Données envoyées
- **Identifiant aléatoire généré par l'application** : non dérivé de votre téléphone ou de votre appareil photo ; réinitialisé si vous réinstallez l'application ou désactivez les statistiques.
- Modèle d'appareil photo (par exemple Nikon Z f) — uniquement le nom du modèle.
- Mode de connexion (Bluetooth, Wi‑Fi, USB, FTP) et type de Wi‑Fi (Wi‑Fi propre de l'appareil, point d'accès mobile, routeur).
- Fonctions utilisées chaque jour (noms des fonctions uniquement, une fois par jour), y compris les fonctions verrouillées touchées.
- Nombre de connexions réussies ou échouées ; en cas d'échec, seul un code de catégorie (comme « délai dépassé ») est envoyé, jamais le texte des messages d'erreur.
- Étapes d'ajout d'appareil photo : démarré, réussi, appareil introuvable et motif d'échec.
- Nombre de photos reçues chaque jour (compteurs pour JPEG, RAW et vidéo — uniquement les quantités).
- Autorisations accordées ou refusées.
- Niveau actuel (Gratuit, clé Beta…), version de l'application, langue de l'application et version majeure d'Android.
- Pays : déterminé à partir de la connexion ; seul le code pays est enregistré.

### Données jamais envoyées
Numéro de série de l'appareil photo, nom du propriétaire ou du copyright enregistré dans l'appareil, localisation (GPS), photos et vidéos, noms de fichiers, métadonnées de prise de vue (EXIF), noms et mots de passe Wi‑Fi, identifiants du téléphone (IMEI, Android ID, identifiant publicitaire), nom, e-mail, compte, ou contenu des messages d'erreur.

### Conservation
- Les détails quotidiens par appareil sont conservés pendant 90 jours, après quoi seuls les totaux globaux journaliers sont gardés.
- Les identifiants aléatoires inactifs pendant environ 13 mois sont supprimés.
- Le serveur voit techniquement votre adresse IP lors du traitement d'une requête ; elle sert uniquement à déterminer le pays et prévenir les abus, et **n'est jamais enregistrée dans les données statistiques**.

## Informations de localisation
- **Envoyer la position à l'appareil photo (Bluetooth)** : votre téléphone envoie sa position à l'appareil photo afin qu'il l'inscrive dans les photos.
- **Ajouter la position aux JPEG reçus (téléphone)** : désactivé par défaut. Lorsqu'il est activé, les points de localisation relevés pendant une session de réception restent uniquement sur ce téléphone et sont supprimés après 24 heures.
- Les deux interrupteurs se trouvent dans **Paramètres → Réception et notifications → Localisation des photos** — voir [Chapitre 3](03-receive.md#localisation-des-photos-gps).
- La localisation intégrée dans une photo accompagne le fichier lorsque vous partagez l'original. **Le partage par QR Code supprime la localisation par défaut.**

## Utilisation des autorisations
| Autorisation | Utilité |
|---|---|
| Bluetooth, Appareils à proximité | Appairage avec l'appareil photo, transfert photo Bluetooth, télécommande Bluetooth, recherche d'appareils Wi‑Fi |
| Position | Envoi de la position à l'appareil photo ou ajout aux photos ; également requis par Android pour lire les noms Wi‑Fi |
| Notifications | Progression de réception, photos reçues, problèmes de transfert, alerte batterie faible de l'appareil |
| Photos et vidéos | Affichage et organisation des photos dans Photos du téléphone |

## Infos de diagnostic
**Paramètres → Assistance → « Copier les infos de diagnostic »** copie uniquement du texte dans votre presse-papiers — **c'est vous qui décidez** de nous l'envoyer ou non. Ce texte contient la version de l'application, l'état du téléphone et du réseau, les capacités de l'appareil photo et les journaux de connexion récents, avec uniquement les 4 derniers chiffres du numéro de série de l'appareil. Avant de le coller dans une Issue GitHub publique, relisez-le pour vérifier qu'aucune information que vous souhaitez garder privée n'y figure.

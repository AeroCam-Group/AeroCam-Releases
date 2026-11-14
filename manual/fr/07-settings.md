<!-- translated from zh-TW at commit 968641f -->

# 7. Détail des paramètres

Les **Paramètres** sont regroupés en cinq catégories. Les options indisponibles dans la version gratuite sont masquées. Vous avez une suggestion ou pensez qu'une valeur par défaut devrait changer ? Écrivez-nous via [Signaler un problème](12-report.md).

## Réception et notifications

### Réception
| Paramètre | Options | Défaut | Détails |
|---|---|---|---|
| Types de fichiers à recevoir | Tous les fichiers / JPG uniquement / JPG + RAW / Photos + vidéos / Personnalisé ; plus Enregistrer uniquement le JPEG depuis RAW, Enregistrer un JPEG compressé, Remplacer la copie compressée à l'arrivée de l'original (Pro) | Tous les fichiers | Voir [Chapitre 3](03-receive.md#types-de-fichiers-à-recevoir) |
| Dossier d'enregistrement | Par appareil / Par date / Par appareil et date / Par type de fichier | Par appareil et date | Organisation des sous-dossiers sous `Pictures/AeroCam` et `Movies/AeroCam` |
| Nom de fichier | Nom d'origine / Préfixe date / Préfixe date et heure | Nom d'origine | S'applique uniquement aux fichiers futurs ; la détection des doublons utilise toujours le nom d'origine |
| Mode de réception (Pro) | Continu / Fichier unique | Continu | Fichier unique s'arrête après avoir reçu un fichier |
| Ignorer les vidéos volumineuses (Pro) | Taille en Mo | 1024 Mo | Les vidéos plus lourdes sont notées « Filtré » pour téléchargement manuel |
| Délai d'attente recherche Wi‑Fi | 30 s / 1 / 2 / 3 / 5 / 10 min / Illimité | 3 min | Arrête la réception automatique passé ce délai pour éviter d'épuiser la batterie |
| Arrêt automatique FTP en cas d'inactivité | Jamais / 5 / 10 / 30 min | Jamais | Décompté depuis la dernière photo reçue ; n'interrompt jamais un transfert en cours |
| Photos déjà reçues par Bluetooth | Remplacer par l'original à la réception Wi‑Fi / Ne pas télécharger à nouveau en Wi‑Fi / Conserver les deux copies | Remplacer par l'original | Le Bluetooth reçoit une copie réduite d'environ 2 Mo |

### Localisation des photos
| Paramètre | Défaut | Détails |
|---|---|---|
| Envoyer la position à l'appareil photo (Bluetooth) | Activé | Transmet le GPS du téléphone à l'appareil photo à l'allumage ou lors d'un transfert Bluetooth pour l'inscrire dans les photos |
| Ajouter la position aux JPEG reçus (téléphone) | Désactivé (demande à la 1re réception) | Inscrit la position du téléphone selon l'heure de prise de vue dans les JPEG reçus par Wi‑Fi, USB ou FTP ; les RAW ne sont pas modifiés |

Voir [Chapitre 3 Localisation des photos](03-receive.md#localisation-des-photos-gps) pour les détails.

### Galerie
| Paramètre | Options | Défaut | Détails |
|---|---|---|---|
| Qualité des JPEG compressés (Pro) | 60 / 70 / 80 / 90 % | 80 % | Qualité des JPEG recompressés sur le téléphone (env. 3 à 4 Mo en 24 Mpx) |
| Sélection après téléchargement/suppression | Toujours demander / Toujours conserver / Toujours effacer | Toujours demander | Évite d'appuyer par erreur sur « Supprimer de l'appareil photo » |
| Compte à rebours de confirmation | 3 / 5 / 8 / 10 s | 5 s | Efface automatiquement la sélection sans réponse lorsque « Toujours demander » est choisi |
| Arrêt automatique du partage QR Code | 15 / 30 / 60 min | 30 min | Le lien expire automatiquement passé ce délai |

### Notifications
| Paramètre | Défaut | Détails |
|---|---|---|
| Ne pas déranger | Désactivé | Coupe toutes les notifications AeroCam (la notification permanente « Réception » reste affichée comme l'exige Android) |
| Début de transfert | Désactivé | |
| Photo reçue | Activé | |
| Problèmes de transfert | Activé | Transfert bloqué, annulé par l'appareil photo ou espace insuffisant sur le téléphone |
| Masquer la notification permanente | — | Ouvre les paramètres de notification Android pour la masquer tout en gardant la réception active |
| Alerte batterie faible de l'appareil | Activé, 15 % | Seuils : 10 / 15 / 20 / 30 % ; vérifié tant que l'appareil est connecté |

## Prise de vue

### Destination
| Paramètre | Options | Détails |
|---|---|---|
| Destination | Carte mémoire / Carte + téléphone (Pro) | Utilisé lorsqu'une carte est insérée ; bascule automatiquement vers Téléphone uniquement sans carte (Pro). Affiche l'état actuel de la carte une fois connecté. Voir [Chapitre 3](03-receive.md#destination-et-prise-de-vue-sans-carte) |

### Prise de vue à distance
| Paramètre | Options | Défaut | Détails |
|---|---|---|---|
| Activé par défaut en prise de vue à distance | Mise au point avant déclenchement, Histogramme, Alerte surexposition, Focus peaking, Posemètre | Mise au point avant déclenchement, Posemètre | Reste modifiable à tout moment pendant la prise de vue |
| Couleur du posemètre | Automatique / Blanc / Noir | Automatique | Automatique s'adapte à la luminosité de l'arrière-plan |
| Couleur du focus peaking | Rouge / Jaune / Bleu / Blanc | Rouge | Changez de couleur lorsque le sujet est rouge |
| Garder l'écran allumé en prise de vue à distance | Activé / Désactivé | Activé | Empêche la mise en veille de l'écran pendant les intervallomètres ou poses longues |
| Mode gaucher | Activé / Désactivé | Désactivé | Déplace le déclencheur en bas à gauche en mode paysage |

### Connexion filaire (USB‑C)
| Paramètre | Options | Défaut | Détails |
|---|---|---|---|
| Cadence d'aperçu USB | 30 / 60 ips / Illimitée | 30 ips | 30 ips économise la batterie et chauffe moins ; 60 ips est plus fluide |
| Aperçu USB haute résolution | Activé / Désactivé | Activé | Aperçu plus net avec une cadence légèrement réduite ; revient au mode normal si non pris en charge |
| Démarrer automatiquement la réception au branchement USB (Pro) | Activé / Désactivé | Activé | Lance la réception USB dès le branchement du câble |
| Synchroniser l'horloge de l'appareil à la connexion | Activé / Désactivé | Activé | Ajuste uniquement si l'écart dépasse 2 s ; demande confirmation au-delà de 1 jour |
| Maintenir l'appareil éveillé via USB | Activé / Désactivé | Activé | Envoie un léger signal toutes les 10 s ; s'arrête après 30 min d'inactivité ou si la batterie est faible |

## Apparence et langue
| Paramètre | Options | Défaut |
|---|---|---|
| Thème | Suivre le système / Clair / Sombre / Nuit étoilée (lumière rouge) | Suivre le système |
| Luminosité minimale de l'écran de l'application | Activé / Désactivé (en mode nuit étoilée) | Désactivé |
| Langue | Suivre le système / 繁中 / 简中 / 日本語 / English / 한국어 / Deutsch / Français / Español / Tiếng Việt / ไทย / Bahasa Indonesia | Suivre le système |

## Stockage et batterie
| Élément | Détails |
|---|---|
| Cache des miniatures | Affiche la taille du cache avec un bouton pour vider (rechargé depuis l'appareil au besoin) |
| Fichiers temporaires de téléchargements incomplets | Affiche la taille avec un bouton pour effacer |
| Réanalyser les photos du téléphone | Retrouve les photos revenues sur le téléphone (restaurées depuis la corbeille ou enregistrées avant une réinstallation) |
| Optimisation de la batterie | Il est conseillé de la désactiver (affiche « Non optimisée ✓ ») afin que les transferts en arrière-plan ne soient pas coupés |

## Assistance
| Élément | Détails |
|---|---|
| Copier les infos de diagnostic | À coller lors d'un signalement : version de l'application, état du téléphone et du réseau, capacités de l'appareil photo, journal des commandes récentes et dernier rapport de plantage. Seuls les 4 derniers chiffres du numéro de série sont inclus |
| Effacer les journaux | Supprime les journaux de la session en cours, de la précédente et les rapports de plantage |
| Rechercher des mises à jour | Vérifie manuellement si une nouvelle version est disponible ; affiche la version actuelle en dessous |
| Clé de test | « Obtenir une clé gratuite » ouvre AeroCam-Releases ; « Saisir une clé de test » permet de la coller ; affiche le niveau actuel et la date d'expiration |
| Licences open source | Bibliothèques tierces utilisées (comme LibRaw pour le développement RAW) |
| Envoyer des statistiques d'utilisation anonymes | Interrupteur unique, activé par défaut. Voir [Confidentialité et statistiques anonymes](10-privacy.md) |

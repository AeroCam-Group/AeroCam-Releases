<!-- translated from zh-TW at commit 968641f -->

# 11. Questions fréquentes et dépannage

## Général
**Puis-je transférer les photos de mon appareil photo vers mon téléphone sans passer à Pro ?**
Oui. Avec la version gratuite, vous pouvez recevoir automatiquement en Bluetooth des JPEG réduits d'environ 2 Mpx, ou parcourir la carte SD de l'appareil via un câble USB pour choisir et télécharger manuellement les originaux en pleine résolution.

**La Beta ou les clés de test sont-elles payantes ?**
Non. Les deux sont publiées gratuitement uniquement sur GitHub dans AeroCam-Releases. Si quelqu'un vous demande de payer, ce n'est pas un canal officiel.

**L'application affiche « Ceci n'est pas une version officielle » au lancement**
L'APK a été reconditionné par un tiers. Il n'acceptera pas les clés de test et pourrait contenir du code indésirable. Désinstallez-le et téléchargez-le à nouveau depuis AeroCam-Releases.

**Après une mise à jour, mon appareil photo appairé et ma clé de test ont disparu**
À partir de la version 92.03.09, les nouvelles versions s'installent comme une application distincte et ne reprennent pas les données des anciennes versions. Appairez à nouveau votre appareil photo et saisissez la clé de test.

**Où sont enregistrées les photos ?**
Les photos vont dans `Pictures/AeroCam`, les vidéos dans `Movies/AeroCam` et les autres fichiers dans `Download/AeroCam`. Google Photos et les autres galeries les affichent directement. Les fichiers enregistrés par des versions antérieures à la 92.03.09 restent dans leur dossier d'origine.

**J'ai supprimé une photo sur mon téléphone et je veux la transférer à nouveau**
Renvoyez-la simplement depuis l'appareil photo — AeroCam détecte que le fichier n'est plus sur votre téléphone et l'enregistre à nouveau.

**Les photos n'apparaissent pas après restauration depuis la corbeille ou réinstallation de l'application**
Lancez **Paramètres → Stockage et batterie → « Réanalyser les photos du téléphone »**.

---

## Connexion
**Impossible de connecter l'appareil photo en Wi‑Fi**
1. Vérifiez que l'appareil photo est bien sur l'écran « Connexion à l'ordinateur » avec l'icône Wi‑Fi affichée ; appuyez à mi-course sur le déclencheur si l'écran s'est éteint.
2. Vérifiez le Type de connexion : **Transfert des images** pour la réception automatique et la galerie ; **Contrôle de l'appareil photo** pour la prise de vue à distance et la prise de vue sans carte.
3. Mode point d'accès mobile : vérifiez que votre partage de connexion est activé et que l'appareil y est connecté.
4. Mode même Wi‑Fi : vérifiez que le téléphone et l'appareil sont connectés exactement au même nom de réseau (le téléphone bascule parfois automatiquement vers un autre Wi‑Fi ou les données mobiles).
5. Essayez la **Connexion en un geste** — sans point d'accès ni routeur.
6. Appuyez sur **ⓘ** et suivez le guide de connexion illustré étape par étape.

**L'appareil photo reste introuvable sur le Wi‑Fi d'un hôtel ou d'un salon**
Les réseaux Wi‑Fi publics bloquent généralement les communications entre appareils. Utilisez votre point d'accès mobile ou la connexion en un geste.

**L'appareil photo affiche « Déjà appairé avec un autre périphérique »**
Ce profil réseau sur l'appareil est associé à une autre application. Créez un nouveau profil réseau sur l'appareil photo et recommencez l'appairage.

**La connexion en un geste ne trouve pas le Wi‑Fi de l'appareil photo**
Après avoir reçu la commande Bluetooth, l'appareil met 10 à 30 secondes à activer son Wi‑Fi, et AeroCam réessaie automatiquement. Si cela échoue encore, vérifiez le mot de passe Wi‑Fi de l'appareil.

**Le point d'accès mobile se coupe tout seul**
Certains téléphones désactivent leur partage de connexion lorsqu'aucun appareil connecté n'utilise Internet. Désactivez « Désactiver automatiquement le point d'accès » dans les paramètres de votre téléphone, ou utilisez la connexion en un geste.

**L'appareil photo ne se reconnecte pas après avoir relancé le point d'accès mobile**
L'adresse IP du point d'accès de votre téléphone a peut-être changé. La réception automatique Wi‑Fi retrouve l'appareil d'elle-même, tandis que le FTP nécessite de mettre à jour l'adresse IP du serveur sur l'appareil photo.

**Rien ne se passe quand je branche le câble USB**
1. Vérifiez que le réglage USB de l'appareil est sur **MTP/PTP**.
2. Assurez-vous que le câble permet le transfert de données (certains câbles ne font que charger).
3. Appuyez sur Autoriser lorsque Android demande l'accès USB.
4. Appuyez sur `⋮` en haut à droite de la tuile USB → **Test USB** pour voir quelle étape échoue.

**La réception en arrière-plan s'interrompt souvent**
Désactivez l'optimisation de la batterie dans **Paramètres → Stockage et batterie**. Sur les téléphones Xiaomi, OPPO et similaires, réglez aussi AeroCam sur « Non restreinte » dans les paramètres batterie du système.

---

## Bluetooth
**Le transfert photo Bluetooth reste bloqué**
- En RAW, l'appareil doit convertir chaque image en JPEG avant l'envoi, et toute manipulation du boîtier annule le transfert. Le plus efficace est d'éteindre l'appareil après la prise de vue pour le laisser transférer en arrière-plan.
- Appuyez sur **Déconnecter et reconnecter** sur la tuile Bluetooth, ou **⋮ → Redémarrer le service Bluetooth** (votre appairage est conservé).

**Appuyer sur AF dans la télécommande Bluetooth ne fait pas la mise au point**
L'appareil photo doit autoriser l'autofocus à mi-course du déclencheur. Si vous utilisez uniquement le bouton AF‑ON arrière, vérifiez dans les réglages personnalisés de l'appareil que **Activation AF** (AF activation) est réglé sur **Déclencheur/AF-ON**.

**Recevoir la même photo en Bluetooth et en Wi‑Fi enregistre-t-il deux fichiers ?**
Non par défaut : dès que le Wi‑Fi reçoit le fichier original, la copie réduite Bluetooth est supprimée automatiquement. Vous pouvez modifier ce comportement dans **Paramètres → Réception et notifications → « Photos déjà reçues par Bluetooth »**.

---

## Prise de vue à distance
**Impossible de régler la vitesse d'obturation ou l'ISO**
- La vitesse nécessite le mode S ou M, l'ouverture le mode A ou M ; désactivez l'ISO auto avant de régler l'ISO manuellement.
- Sur les appareils à molettes physiques comme le Zf : placez la molette de vitesse sur **1/3 STEP** et la molette ISO sur **C**.

**Toucher l'aperçu ne déplace pas le collimateur AF**
Réglez le mode de zone AF de l'appareil sur un mode permettant de déplacer le point (comme AF point sélectif). En zone AF automatique, l'appareil choisit seul.

**Certaines infos manquent sur le tableau de bord (objectif, vues restantes, déclenchements)**
Certains boîtiers ne transmettent ces données que dans certains modes. Basculer sur « Contrôle de l'appareil photo » et ouvrir la prise de vue à distance les rend généralement disponibles. Le compteur de déclenchements nécessite au moins une photo sur la carte mémoire.

**Où voir la température de couleur exacte (en Kelvin) ?**
Nikon enregistre la valeur Kelvin mesurée dans une balise MakerNote chiffrée ; « Détails » affiche donc uniquement le nom du préréglage de balance des blancs.

---

## Destination et prise de vue sans carte
**Appuyer sur le déclencheur ne fait rien lorsqu'il n'y a pas de carte**
Vérifiez que **Déclenchement sans carte** est réglé sur **Déclenchement autorisé** sur l'appareil photo, et qu'AeroCam est connecté (la barre d'état affiche « téléphone uniquement »).

**Les photos affichent « DEMO » sur l'appareil**
Si aucune carte n'est insérée et qu'AeroCam n'est pas connecté en mode « téléphone uniquement », l'appareil marque les vues **DEMO** et ne les enregistre pas. Insérez une carte ou photographiez en étant connecté à AeroCam.

**Les photos n'arrivent pas sur le téléphone et un bandeau rouge apparaît en haut de l'accueil**
- « L'appareil est en mode "Transfert des images" » : la prise de vue sans carte exige **Contrôle de l'appareil photo**. Changez de mode sur l'appareil ; il se reconnectera et transférera automatiquement les vues en mémoire tampon.
- « Wi‑Fi en un geste : pas de carte mémoire » : la connexion en un geste ne prend pas en charge la prise de vue sans carte. Insérez une carte ou passez sur un point d'accès mobile / même Wi‑Fi.

**« Connexion perdue » s'affiche**
En mode téléphone uniquement, une coupure de plus de 10 secondes déclenche une alerte car les photos prises pendant la coupure ne sont enregistrées sur aucune carte. AeroCam reprend automatiquement dès la reconnexion.

---

## Retouche et styles
**Un fichier NEF ne s'ouvre pas ou ne peut pas être retouché**
Les fichiers NEF Haute efficacité / Haute efficacité★ sont retouchés via leur JPEG pleine définition intégré ; les fichiers ne contenant qu'une petite miniature ne peuvent pas être retouchés. Pour développer de vrais fichiers RAW sur votre téléphone, passez l'appareil en **Compression sans perte** — voir [Chapitre 6](06-edit.md#raw-modifiable-sur-téléphone-basculer-la-compression-raw-de-lappareil).

**Le rendu .np3 diffère de celui de l'appareil photo**
L'éditeur du téléphone simule les courbes et la saturation ; le mélangeur de couleurs et l'étalonnage ne sont pas encore simulés, le rendu est donc approximatif. Si un JPEG avait déjà un Picture Control appliqué à la prise de vue, les effets se cumulent.

**Les couleurs sont différentes après écriture d'un .np3 dans l'appareil photo**
Les emplacements personnalisés de l'appareil n'acceptent que **Base + Courbe + Accentuation** ; la saturation, le mélangeur de couleurs et l'étalonnage ne peuvent pas être écrits via la connexion. Pour un résultat complet, copiez le fichier `.np3` sur une carte mémoire et importez-le via le menu de l'appareil.

**L'assemblage panoramique échoue ou ignore des photos**
Chaque vue doit chevaucher ses voisines d'environ 30 %. Les fichiers non raccordés sont listés par nom, et les panoramas en grille nécessitent toutes les cases avant l'assemblage.

---

## FTP
**L'appareil affiche Err.31 ou Err.32**
Mettez à jour vers la dernière Beta et vérifiez que l'adresse IP, le port `2121`, le nom d'utilisateur `aerocam` et le mot de passe sur l'appareil correspondent exactement à la tuile FTP d'AeroCam, avec le mode passif activé.

**L'appareil affiche un échec de connexion**
Le mot de passe doit correspondre exactement (majuscules/minuscules comprises) à celui affiché sur la tuile FTP d'AeroCam. Si vous avez appuyé sur « Régénérer », mettez-le aussi à jour sur l'appareil photo.

**Impossible de connecter la Pellicule ou la prise de vue à distance pendant que le FTP tourne**
En mode FTP, l'appareil photo n'accepte pas de connexion Wi‑Fi pour la galerie ou la prise de vue à distance. Utilisez un câble USB, ou arrêtez la réception FTP et repassez l'appareil sur « Connexion à l'ordinateur ».

---

## Autres
**L'application plante**
Rouvrez AeroCam, allez dans **Paramètres → Assistance → « Copier les infos de diagnostic »**, et collez le contenu lors du [signalement du problème](12-report.md) — il contient l'emplacement exact de la dernière erreur.

**Comment désactiver les statistiques d'utilisation anonymes ?**
Désactivez **Paramètres → Assistance → « Envoyer des statistiques d'utilisation anonymes »** — voir [Confidentialité et statistiques anonymes](10-privacy.md).

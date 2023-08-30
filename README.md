# VittaPi: Interface Raspberry Pi pour VittaScience

VittaPi est une interface conçue pour faciliter la communication entre [VittaScience](https://fr.vittascience.com/code) et un Raspberry Pi. Ce package est conçu pour le système d'exploitation Raspberry Pi OS Bullseye.

---

## Table des matières

- [VittaPi: Interface Raspberry Pi pour VittaScience](#vittapi-interface-raspberry-pi-pour-vittascience)
  - [Table des matières](#table-des-matières)
  - [Configuration du système](#configuration-du-système)
  - [Prérequis et Dépendances](#prérequis-et-dépendances)
    - [Mise à jour des paquets système](#mise-à-jour-des-paquets-système)
    - [Activer la communication I2C pour les modules Grove](#activer-la-communication-i2c-pour-les-modules-grove)
    - [Dépendances](#dépendances)
  - [Installation](#installation)
  - [Utilisation](#utilisation)
  - [Fonctionnement](#fonctionnement)
  - [Avertissement](#avertissement)

---

## Configuration du système

**Système d'exploitation pris en charge :** Bullseye

---

## Prérequis et Dépendances

### Mise à jour des paquets système

Exécutez la commande suivante pour mettre à jour les paquets du système :

```bash
sudo apt-get update
```

### Activer la communication I2C pour les modules Grove

Si vous utilisez des modules Grove nécessitant une communication I2C (par exemple, LCD16x2), suivez ces étapes :

1. Accédez à la configuration du Raspberry Pi :

    ```bash
    sudo raspi-config
    ```

2. Sélectionnez "3 Interface Options".

3. Sélectionnez "I5 I2C".

4. Redémarrez le système pour appliquer les modifications :

    ```bash
    sudo reboot
    ```

### Dépendances

Ce package dépend de plusieurs bibliothèques et modules :

- SenseHat de la Fondation Raspberry Pi - [astro-pi](https://astro-pi.org/).
- GrovePi de Seeed Studio - [github - GrovePi](https://github.com/Seeed-Studio/grove.py).
- Module dht de Seeed Studio [github - dht](https://github.com/Seeed-Studio/Seeed_Python_DHT)

Toutes ces dépendances sont sous licence MIT.

---

## Installation

Pour installer VittaPi, suivez les étapes ci-dessous :

1. Téléchargez le package depuis le dépôt :

    ```bash
    git clone [URL_du_dépôt]
    ```

2. Construisez le package :

    ```bash
    sudo dpkg --build vittapi
    ```

3. Installez le package :

    ```bash
    sudo dpkg -i vittapi.deb
    ```

---

## Utilisation

Après l'installation, un raccourci sera créé sur le bureau de votre Raspberry Pi. Vous avez deux options :

- Cliquez sur le raccourci, ce qui lancera le programme et son interface graphique dans une nouvelle fenêtre de terminal.
  
  **OU**
  
- Lancez le programme directement depuis un terminal avec la commande suivante :

    ```bash
    vittapi.sh
    ```

---

## Fonctionnement

Pour téléverser du code, vous devrez spécifier le nom d'hôte de votre Raspberry Pi à l'aide d'un bloc `[raspberry]`. Vous pouvez également utiliser l'adresse IP de votre Raspberry Pi.

---

## Avertissement

Ce package est encore en développement. Des bugs peuvent être présents. Si vous en découvrez, merci de créer une issue sur notre dépôt GitHub.

**Note de sécurité :** La communication entre vittascience.com et le Raspberry Pi se fait via un serveur web Flask. Une connexion Internet est nécessaire. La communication utilise le protocole HTTP et non HTTPS. Il est donc recommandé de n'utiliser ce package que sur un réseau privé et sécurisé.

---

Pour toute autre question ou feedback, n'hésitez pas à nous contacter.
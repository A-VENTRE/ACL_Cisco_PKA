# 📚 ACL Tutorial and Exercises

## ✨ Introduction

Les **Listes de Contrôle d'Accès (ACL)** sont essentielles pour la sécurité informatique et des réseaux. Ce guide regroupe des ressources et exercices pour maîtriser les ACL dans divers environnements.

## 🗂️ Structure du Dépôt

### 📁 `1_Unix_ACL/`
- **Description** : Initiation aux ACL sous UNIX/Linux.
- **Contenu** :
  - Utilisation des commandes `getfacl` et `setfacl`.
  - Exemples pratiques pour une gestion fine des permissions.

### 📁 `2_Windows_ACL/`
- **Description** : Gestion des ACL dans les systèmes Windows avec NTFS.
- **Contenu** :
  - Configuration des permissions avancées pour fichiers et dossiers.
  - Commandes et cas d'usage illustrés.

### 📁 `3_Network_ACL/`
- **Description** : Configuration des ACL sur les équipements réseau Cisco.
- **Contenu** :
  - ACL standard, étendue, réflexive et nommée.
  - Fichiers Packet Tracer et GNS3 pour simulations.

### 📁 `4_Exercices/`
- **Description** : Scénarios pratiques pour appliquer les ACL.
- **Exercices** :
  - Scénario 1 : Isolation de réseaux.
  - Scénario 2 : Limitation d'accès aux services.
  - Scénario 3 : Blacklistage d'hôtes spécifiques.

## 🎯 Points Clés sur les ACL

### ✅ Qu'est-ce qu'une ACL ?
Une ACL est une liste de règles qui :
- Contrôle l'accès aux ressources (fichiers, dossiers, services).
- Filtre le trafic réseau selon des critères prédéfinis.

### 🛠️ Types d'ACL
1. **ACL Standard** : Filtre basé sur l’adresse IP source.
2. **ACL Étendue** : Filtre selon les adresses IP, protocoles et ports.
3. **ACL Nommée** : ACL identifiée par un nom pour une meilleure lisibilité.
4. **ACL Réflexive** : ACL dynamique pour gérer les connexions.

## 📝 Exemple de Configuration Cisco

### Création d'une ACL Standard
```bash
Router(config)# access-list 10 deny host 192.168.1.10
Router(config)# access-list 10 permit any

### Application de l'ACL à une Interface

```bash
Router(config-if)# ip access-group 10 in

### 🚀 Utilisation

#### 🔧 Prérequis
- Logiciels : Packet Tracer, GNS3.
- Accès à des environnements UNIX/Linux ou Windows.

#### 📖 Instructions
1. Clonez le dépôt :
   ```bash
   git clone https://github.com/your-username/ACL_Tutorial_and_Exercises.git
#### 📖 Instructions (Suite)
- Explorez les dossiers pour accéder aux exemples et exercices.
- Utilisez les fichiers de simulation (.pkt, .gns3) pour expérimenter.

### 🛡️ Bonnes Pratiques
- **Ordre des règles** : Placez les règles spécifiques avant les générales.
- **Tests** : Vérifiez vos ACL après configuration.
- **Documentation** : Notez toutes vos configurations pour une maintenance simplifiée.

### 📎 Ressources
- [Documentation Cisco sur les ACL](https://www.cisco.com)
- [Tutoriel ACL Linux](https://linux.die.net/man/1/getfacl)
- [Gestion NTFS ACL sous Windows](https://learn.microsoft.com)

# Email Automation Demo

Démonstration **simplifiée** d'un script Python qui montre la logique d'un traitement automatique de boîte mail (protocole IMAP) : recherche des e-mails non lus dont le sujet contient « Facture », puis détection de leurs pièces jointes.

Cette version est un **exemple de démonstration** :
- les identifiants et le serveur sont des valeurs fictives, **aucune donnée ni identifiant réel** ;
- la connexion et l'enregistrement des pièces jointes sont désactivés (lignes commentées) : le script se contente d'afficher un message ;
- elle illustre la logique d'un projet réalisé en stage dans un cabinet comptable en 2023.

## Fichier

- `cleaner.py` : connexion IMAP, recherche des e-mails, extraction des pièces jointes (logique de démonstration).

## Pour l'essayer

1. Renseigner ses propres identifiants dans les variables prévues (ne jamais les publier) ou utiliser des variables d'environnement.
2. Décommenter les lignes de connexion et d'enregistrement dans `cleaner.py`.
3. Lancer `python cleaner.py`.

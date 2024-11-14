
# Programme de Chiffrement et Déchiffrement en Code Morse

Ce programme Python permet de **chiffrer** un message en code Morse ou de **déchiffrer** un message en Morse en utilisant une interface en ligne de commande (CLI) créée avec la bibliothèque `click`.

## Prérequis

Assurez-vous d'avoir Python installé sur votre machine. Ce programme nécessite également la bibliothèque `click`. Pour l'installer, utilisez la commande suivante :

```bash
pip install click
```

## Installation

Clonez ce dépôt ou copiez les fichiers nécessaires.

## Structure du Programme

- `main.py` : Fichier principal qui contient le code de chiffrement et de déchiffrement en Morse.
- `encode_morse` : Fonction qui chiffre un texte en code Morse.
- `decode_morse` : Fonction qui déchiffre un code Morse en texte.

## Utilisation

Le programme utilise une seule commande CLI avec l'option `--mode` pour choisir entre chiffrement et déchiffrement. 

### Lancer le programme

Exécutez `main.py` avec les arguments suivants :

```bash
python main.py "MESSAGE" --mode MODE
```

- **MESSAGE** : Le texte à chiffrer ou le code Morse à déchiffrer.
- **MODE** : Indique l'action à réaliser. Les valeurs acceptées sont :
  - `encode` : Pour convertir un texte en code Morse.
  - `decode` : Pour convertir un code Morse en texte.

### Exemples d'Utilisation

1. **Chiffrer un message en Morse**

   Pour chiffrer le message "HELLO WORLD" en code Morse :

   ```bash
   python main.py "HELLO WORLD" --mode chiffrer
   ```

   **Résultat attendu** :

   ```
   Message chiffré en Morse : .... . .-.. .-.. --- / .-- --- .-. .-.. -..
   ```

2. **Déchiffrer un message en Morse**

   Pour déchiffrer le message Morse ".... . .-.. .-.. --- / .-- --- .-. .-.. -.." en texte clair :

   ```bash
   python main.py ".... . .-.. .-.. --- / .-- --- .-. .-.. -.." --mode déchiffrer
   ```

   **Résultat attendu** :

   ```
   Message déchiffré : HELLO WORLD
   ```

## Notes

- **Séparation des mots en Morse** : Dans ce programme, un `/` est utilisé pour séparer les mots en code Morse.
- **Respect de la casse** : Le texte est converti en majuscules pour le chiffrement en Morse, conformément aux conventions de code Morse.
- **Exécution directe** : Ce programme utilise l'instruction `if __name__ == '__main__':` pour garantir que la fonction CLI `cli()` n’est exécutée que si le fichier est exécuté directement.

## Auteurs

Créé par François RICHARD.

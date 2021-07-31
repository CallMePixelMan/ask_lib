<p align="center">
    <img src="./img/ask_lib_logo.png">
    Demande de confirmation utilisateur pour CLI
</p>

***

![](https://img.shields.io/pypi/l/ask_lib) ![](https://img.shields.io/pypi/v/ask_lib) ![](https://img.shields.io/pypi/pyversions/ask_lib)

## Présentation

`ask_lib` est un module pour le langage Python proposant une seule fonction; `ask()`.
Le but principal de cette fonction est de proposer un wrapper de la fonction `input()` pour demander la confirmation de l'utilisateur avant de réaliser une action. `ask_lib` est donc particulièrement utile pour la création de [CLI](https://fr.wikipedia.org/wiki/Interface_en_ligne_de_commande).

## Exemple
```py
import os

from ask_lib import AskResult, ask

reponse = ask("Êtes-vous sûr de vouloir supprimer ce fichier ?", AskResult.YES)
if reponse:
    try:
        os.remove("fichier.txt") # Supprime le fichier | A titre d'exemple
    except Exception:
        print("Quelque chose s'est mal passé...")
    else:
        print("Le fichier vient d'être supprimé.")
else:
    print("Le fichier n'a pas été supprimé.") 
```

Point de vu de l'utilisateur ;
```
Êtes-vous sûr de vouloir supprimer ce fichier ? [Y/n] n
Le fichier n'a pas été supprimé.
```
```
Êtes-vous sûr de vouloir supprimer ce fichier ? [Y/n] y
Le fichier vient d'être supprimé.
```

## Particularités
- `ask_lib` est entièrement documenté avec des docstrings riches et claires.
- `ask_lib` est conforme aux principes de [SOLID](https://fr.wikipedia.org/wiki/SOLID_(informatique)). Le principe de responsabilité unique y est totalement respecté.
- `ask_lib` est très simple d'implémentation et d'utilisation.

## Prérequis
`ask_lib` est compatible avec les versions de Python 3 à partir de la version 3.6.

## Installation
Vous pouvez installer `ask_lib` en utilisant pip, avec la commande suivante ;
> `pip install ask_lib`

## Documentation
Vous pouvez consulter la documentation en cliquant [ICI](./docs/fr_documentation.md).  
Vous pouvez retrouver `asl_lib` sur PyPi en cliquant [ICI](https://pypi.org/project/ask-lib/).

## Licence
`ask_lib` est disponible sous licence [MIT](./LICENCE).
# Documentation
Pour plus d'informations sur `ask_lib`, cliquez [ICI](../README.md).

***

## Importer ask_lib
Comment tout module Python, `ask_lib` s'importe de la manière suivante :
```python
import ask_lib

reponse = ask_lib.ask("Voulez-vous installer ce fichier ?", ask_lib.AskResult.YES)
```
Vous pouvez également importer `ask_lib` de cette façon, afin d'obtenir un code plus concis :
```python
from ask_lib import AskResult, ask

reponse = ask("Voulez-vous installer ce fichier ?", AskResult.YES)
```

***

## Fonction
### ask
La fonction `ask()` vous permet de demander l'avis de l'utilisateur avant de réaliser une action.

```
function ask_lib.ask(message, default_option=ask_lib.AskResult.YES, flag=None)
```

Paramètres
- `message` (`str`)
  - La demande faite à l'utilisateur.
- `default_option` (`str`, `optional`)
  - Le choix par défaut. Si l'utilateur ne donne aucune réponse ou une réponse non reconnue, alors ce sera ce choix qui sera utilisé. Doit être `AskResult.YES` ("yes") ou `AskResult.NO` ("no").
- `flag` (`Union[str,None]`, `optional`)
  - Permet de passer la confirmation en appliquant un choix par défaut à la place l'utilisateur. Utile pour l'utilisation de flag dans une CLI.  
    **Attention !** Si `flag` n'est pas `None`, alors aucun message ne sera affiché !
 
Renvoie
- `bool` 
  - `True` si l'utisateur a accepté, `False` dans le cas contraire.
  - Renvoie `True` si l'utilsateur a donné une reponse qui n'est pas supportée, et que `default_option == AskResult.YES`.
  - Renvoie `False` si l'utilsateur a donné une reponse qui n'est pas supportée, et que `default_option == AskResult.NO`.
  - Renvoie `True` si `flag == AskFlag.YES_TO_ALL`.
  - Renvoie `False` si `flag == AskFlag.NO_TO_ALL`.
  - Renvoie `default_option` si `flag == AskFlag.DEFAULT_TO_ALL`.
  
Lève l'erreur
- `ValueError`
  - Si `default_option` n'est pas `AskResult.YES` ("yes") ou `AskResult.NO` ("no").
- `ValueError`
  - Si `flag` n'est pas `AskFlag.YES_TO_ALL` ("yes_to_all"), `AskFlag.NO_TO_ALL` ("no_to_all"), `AskFlag.DEFAULT_TO_ALL` ("default_to_all") ou `None`.

***

## Classes
### AskResult
La classe `AskResult` contient des constantes, celles-ci ne doivent pas être modifiées. Il s'agit d'une classe qui simplifie l'usage de la fonction `ask()`.

```
class AskResult
```

Attributs de classe
- YES (`str`)
  - "yes"
- NO (`str`)
  - "no"

### AskFlag
La classe `AskFlag` contient des constantes, celles-ci ne doivent pas être modifiées. Il s'agit d'une classe qui simplifie l'usage de la fonction `ask()`.

```
class AskResult
```

Attributs de classe

- YES_TO_ALL (`str`)
  - "yes_to_all"
- NO_TO_ALL (`str`)
  - "no_to_all"
- DEFAULT_TO_ALL (`str`)
  - "default_to_all"
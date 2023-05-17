# Projet 7 DA-Python
***Calcul de la meilleure combinaison d'actions en fonction de leurs bénéfices selon deux approches ;***

- ***Bruteforce***

- ***Programmation dynamique (algorithme du sac à dos)***


## Initialisation du projet

### Windows :
    git clone https://github.com/Maiphuongthao/MaiPhuongThao_7_042023.git

    cd MaiPhuongThao_7_042023
    python -m venv env 
    env\scripts\activate

    pip install -r requirements.txt


### MacOS et Linux :
    git clone https://github.com/Maiphuongthao/MaiPhuongThao_7_042023.git

     cd MaiPhuongThao_7_042023
    python3 -m venv env 
    source env/bin/activate

    pip install -r requirements.txt



## Exécution du programme

### Bruteforce

    python bruteforce.py


*Note : Le bruteforce ne traîte que les données du fichier "test.csv", contenant 20 actions. Les datasets 1 et 2 résulteraient à un temps d'exécution extrêmement long.*

### Programmation dynamique

    python optimized.py


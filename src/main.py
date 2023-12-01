import os

def custom_ls(path="."):
    try:
        files = os.listdir(path)
        for file in files:
            print(file)
    except FileNotFoundError:
        print(f"Le répertoire '{path}' n'existe pas.")
    except PermissionError:
        print(f"Vous n'avez pas la permission d'accéder au répertoire '{path}'.")
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")
custom_ls()

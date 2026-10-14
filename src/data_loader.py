import os
from pathlib import Path

VALID_EXTENSIONS = {'.jpg', '.jpeg', '.png', '.bmp'}


def get_raw_image_paths_and_labels():
    """function to return images path and labels"""
    image_paths = []
    labels = []

    ROOT_DIR = Path(__file__).resolve().parent.parent
    raw_path = ROOT_DIR / "data" / "raw"

    if not raw_path.exists():
        raise FileNotFoundError(f"Le dossier spécifié n'existe pas : {raw_path}")

    # Parcourt chaque sous-dossier de classe (glioma, meningioma, notumor, pituitary)
    for class_folder in sorted(os.listdir(raw_path)):
        class_path = raw_path / class_folder

        if class_path.is_dir():
            for filename in os.listdir(class_path):
                file_path = class_path / filename
                ext = file_path.suffix.lower()

                # Vérification de l'extension
                if ext in VALID_EXTENSIONS:
                    image_paths.append(str(file_path))
                    labels.append(class_folder)
                else:
                    # Gestion des fichiers non conformes (ex: .DS_Store, .txt)
                    try:
                        os.remove(file_path)
                        print(f"[SUPPRIMÉ] Fichier non conforme supprimé : {file_path}")
                    except Exception as e:
                        print(f"[ERREUR] Impossible de supprimer {file_path} : {e}")

    return image_paths, labels
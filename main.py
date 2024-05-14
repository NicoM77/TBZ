import os
import json
import shutil

# Pfad zur JSON-Datei
json_file_path = os.path.join(os.path.dirname(__file__), 'data.json')

# Laden des JSON aus der Datei
with open(json_file_path, 'r') as file:
    repos = json.load(file)


def extract_project_name(url):
    # Teile die URL an jedem Schrägstrich '/'
    parts = url.split('/')
    # Nimm das letzte Element der Teile
    last_part = parts[-1]
    # Entferne die Endung '.git', falls vorhanden
    project_name = last_part.replace('.git', '')
    return project_name

# Git-Repositorys klonen und .git-Ordner löschen
for person, repos_list in repos.items():
        # Branch wechseln (falls vorhanden)
    os.system(f"git checkout -b {person} || git checkout {person}")
    # Den gesamten Inhalt löschen
    # for root, dirs, files in os.walk(".", topdown=False):
    #     for name in files:
    #         os.remove(os.path.join(root, name))
    #     for name in dirs:
    #         os.rmdir(os.path.join(root, name))

    for repo_info in repos_list:
        repo_name = repo_info['name']
        repo_url = repo_info['url']

        # Ordnername wird der Name des Repositorys sein
        repo_dir = repo_name

        # Git-Repo klonen
        os.system(f"git clone {repo_url}")
        

        os.rename(extract_project_name(repo_url), repo_dir)
        # In das geklonte Repository wechseln
        os.chdir(repo_dir)

        os.rename(".git", "git")

        os.chdir("..")
    os.system("git add .")

    # Commit durchführen
    os.system("git commit -m 'feat: commit'")

    # # Pushen der Änderungen
    os.system("git push origin HEAD")

        # Zum main-Branch wechseln
    os.system("git checkout main")



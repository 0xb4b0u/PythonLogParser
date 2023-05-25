"""Fichier de l'examen du juin 2023"""
from main import *


def process_id_which_open_sessions(logs: list, date_min: str, date_max: str) -> list:
    """
    Pre :
    - logs est une liste où chaque élément est une ligne de log bien formée
    - date_min et _max sont des str représentant une date (et heure) au format "MM:JJ HH:MM:SS".
    - date_min est plus petit que date_max
    Post :
    - retourne une liste (sans doublon) des process id qui ouvrent une session dans le temps
     défini par date_min et date_max.
    """
    process_id_list = []
    logs = logs_with_tag(logs, "session opened for user")
    for log in logs:
        date = formatted_date(get_complete_date(log))
        if date_min <= date <= date_max:
            process_id = get_process_id(log)
            if process_id not in process_id_list and process_id != -1:
                process_id_list.append(process_id)
    return process_id_list


def error_process(logs: list, program: str, date: str) -> list:
    """
     Pre :
        - logs est une liste où chaque élément est une ligne de log bien formée
        - program est le programme recherché
            - date est une date au format MM:JJ (exemple: 24 Octobre = 10:24)
    Post :
        - retourne une liste (sans doublon) des processus qui ont émis au moins un message d’erreur.
    """
    process_id_with_error = []
    for log in logs:
        if (
            program == get_program(log)
            and "error" in get_message(log).lower()
            and date in formatted_date(get_complete_date(log))
        ):
            process_id = get_process_id(log)
            if process_id != -1 and process_id not in process_id_with_error:
                process_id_with_error.append(process_id)
    return process_id_with_error


def sessions_kali(logs: list) -> int:
    """
    Pre:
        - logs est une liste où chaque élément est une ligne de log bien formée
    Post:
        - retourne le nombre de sessions différentes ouvertes par l'utilisateur kali
    """
    session_ids = []
    for log in logs:
        message = get_message(log)
        if "of user kali." in message:
            session_id = message.split()[2]
            if session_id not in session_ids:
                session_ids.append(session_id)
    return len(session_ids)

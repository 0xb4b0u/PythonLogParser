# ************************************************************************** #
#                       Introduction à la programmation                      #
#                               PROJET DECEMBRE                              #
#                              _ ____ ____ _  _                              #
#                              | |___ [__  |\ |                              #
#                              | |___ ___] | \|                              #
#                                                                            #
#   By: Baptiste OGER <etu51216@henallux.be>                                 #
#   Created: 2022/07/11                                                      #
#   Last edit: 2022/07/28                                                    #
#                                                                            #
# ************************************************************************** #

def lines_from_file(path: str) -> list:
    """
    PRECONDITIONS :
        path (str) : chemin menant au fichier à lire (à partir d'un dossier courant)

    POSTCONDITIONS :
        Retourne une liste où chaque élément est une ligne du fichier.
        En cas d'erreur, retourne une liste vide
    """

    try:
        with open(path) as f:
            log = f.readlines()
            return log
    except Exception as e:
        print(e)
        return []


def get_host(line: str) -> str:
    """
     PRECONDITIONS :
        line (str) : une ligne du fichier log bien formée

    POSTCONDITIONS :
        Retourne le hostname
    """

    split_line = line.split()
    hostname = split_line[3]

    return hostname


def get_complete_date(line: str) -> str:
    """
    PRECONDITIONS :
        line (str) : une ligne du fichier log bien formée

    POSTCONDITIONS :
        Retourne la date et l’heure sous forme de chaine de caractère sans changer le format.
    """

    split_line = line.split()
    return f"{split_line[0]} {split_line[1]} {split_line[2]}"


def get_message(line: str) -> str:
    """
    PRECONDITIONS :
        line (str) : une ligne du fichier log bien formée

    POSTCONDITIONS :
        Retourne le message de la ligne
    """

    split_line = line.split()
    return "".join(f" {word}" for word in split_line[5:])


def get_program(line: str) -> str:
    """
    PRECONDITIONS :
        line (str) : une ligne du fichier log bien formée

    POSTCONDITIONS :
        Retourne le nom du programme
    """

    split_line = line.split()
    program = split_line[4].split("[")[0]

    return program.replace(":", "") if ":" in program else program


def get_process_id(line: str) -> int:
    """
    PRECONDITIONS :
        line (str) : une ligne du fichier log bien formée

    POSTCONDITIONS :
        Retourne le numéro du processus. Si aucun ID n'est trouvé (ex : kernel), -1 est retourné
    """

    split_line = line.split()
    program_and_id = split_line[4]

    if "[" in program_and_id:
        end_of_id = split_line[4].split("[")[1]
        process_id = int(end_of_id.split("]")[0])

        return process_id
    return -1


def logs_by_day(logs: list, day: str) -> list:
    """
    PRECONDITIONS :
        logs (list) : liste contenant des lignes du fichier log
        day (str) : date au format "Moi JJ"

    POSTCONDITIONS :
        Retourne une liste de lignes du fichier log qui contiennent le jour de la semaine passé en paramètre
    """
    days_log = []

    for log in logs:
        if day in log:
            days_log.append(log)

    return days_log


def formated_date(date: str) -> str:
    """
    PRECONDITIONS :
        date (str) est la date au format "Mois JJ HH:MM:SS" où :
            - Mois : est les 3 première lettres du mois en anglais(commencant par une majuscule)
            - JJ : est le numéro du jour (sur 2 chiffres)
            - HH : est l'heure (sur 2 chiffres)
            - MM : sont les minutes (sur 2 chiffres)
            - SS : sont les secondes (sur 2 chiffres)
    POSTCONDITIONS :
        Retourne la date sous le format "xx:JJ HH:MM:SS" où xx est le nombre du mois (sur 2 chiffres)
    """
    split_date = date.split()

    match split_date[0]:
        case "Jan":
            month = "01"
        case "Feb":
            month = "02"
        case "Mar":
            month = "03"
        case "Apr":
            month = "04"
        case "May":
            month = "05"
        case "Jun":
            month = "06"
        case "Jul":
            month = "07"
        case "Aug":
            month = "08"
        case "Sep":
            month = "09"
        case "Oct":
            month = "10"
        case "Nov":
            month = "11"
        case "Dec":
            month = "12"
        case _:
            return "ERROR"

    return "".join(month + ":" + split_date[1] + " " + split_date[2])


def logs_between(
    logs: list, date_min="00:00 00:00:00", date_max="99:99 00:00:00"
) -> list:
    """
    PRECONDITIONS :
        - logs (list) : liste où chaque élément est une ligne de log bien formée
        - date_min et date_max (str) : deux chaines de caractères représentant une date
        (et heure) au format "Moi JJ HH:MM:SS".
        Par défaut, ils ont de valeurs absurdes permettant de prendre tout.
        - ! Date_min est plus petit que date_max !
    POSTCONDITIONS :
        - retourne une liste de logs qui concernent des dates entre date_min et date_max (inclus).
    """
    logs_between_dates = []

    for log in logs:
        if date_min <= formated_date(get_complete_date(log)) <= date_max:
            logs_between_dates.append(log)

    return logs_between_dates


def logs_with_tag(logs: list, tag="error") -> list:
    """
     PRECONDITIONS :
        - logs (list) : liste où chaque élément est une ligne de log bien formée
        - tag (str) : une chaine de caractères à trouver dans le message.
            Par défaut : "error"
    POSTCONDITIONS :
        - retourne une liste de logs qui concernent des uniquement des logs contenant le tag (min ou MAJ)
            dans le message.
    """
    tagged_logs = []
    tag = tag.lower()

    for log in logs:
        log_message = get_message(log)
        if tag in log_message or tag in log_message.lower():
            tagged_logs.append(log)

    return tagged_logs


def logs_from_program(logs: list, program: str) -> list:
    """
    PRECONDITIONS :
        - logs (list) : liste où chaque élément est une ligne de log bien formée
        - program (str) : le programme à trouver

    POSTCONDITIONS :
        - retourne une liste de logs qui concernent des uniquement les programmes correspondant à "program"
    """
    program_logs = []

    for log in logs:
        log_program = get_program(log)
        if log_program == program:
            program_logs.append(log)

    return program_logs


def list_process_for_program(logs: list, program: str) -> list:
    """
    PRECONDITIONS :
        - logs (list) : liste où chaque élément est une ligne de log bien formée
        - program (str) : le programme à trouver

    POSTCONDITIONS :
        - retourne une liste des process_id gérés par le programme.
            La liste ne contient pas de doublons.
    """
    process_id_list = []

    for log in logs:
        log_program = get_program(log)
        process_id = get_process_id(log)
        if (
            log_program == program
            and process_id != -1
            and process_id not in process_id_list
        ):
            process_id_list.append(process_id)

    return process_id_list


def suspects(logs: list, limit: int) -> list:
    """
    PRECONDITIONS :
        - logs (list) : liste où chaque élément est une ligne de log bien formée
        - limit (int) : le nombre limite d'erreurs tolérées pour un programme.

    POSTCONDITIONS :
        - retourne une liste des programmes (sans doublons) qui ont généré + que le nombre limite de log
            signalant des erreurs (error)
    """
    suspect_logs = []

    for log in logs_with_tag(logs):
        program = get_program(log)
        if (
            program not in suspect_logs
            and len(logs_with_tag(logs_from_program(logs, program))) > limit
        ):
            suspect_logs.append(program)
    return suspect_logs

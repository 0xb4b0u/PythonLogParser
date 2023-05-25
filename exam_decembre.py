""" FICHIER EXAMEN """
from main import (
    get_program,
    get_process_id,
    get_complete_date,
    logs_with_tag,
    lines_from_file,
)


def network_message_times(logs: list) -> list:
    """
    PRECONDITIONS :
        logs (list) : liste où chaque élément est une ligne de log bien formée

    POSTCONDITIONS :
         retourne une liste des moments (date et heure) sans doublon
         où le programme NetworkManager a émi un "<warn>"
    """
    ntwrk_msg_times = []
    networkmanager_logs = []

    for log in logs:
        if get_program(log) == "NetworkManager":
            networkmanager_logs.append(log)

    tagged_logs = logs_with_tag(networkmanager_logs, "<warn>")

    for log in tagged_logs:
        date = get_complete_date(log)
        if date not in ntwrk_msg_times:
            ntwrk_msg_times.append(date)

    return ntwrk_msg_times


def programs_with_process_id(logs: list) -> list:
    """
    PRECONDITIONS :
        logs (liste) où chaque élément est une ligne de log bien formée

    POSTCONDITIONS :
        retourne une liste (sans doublon) des programmes avec process id
     qui sont présents dans logs
    """
    process_id_program = []

    for log in logs:
        log_program = get_program(log)
        log_process_id = get_process_id(log)

        if log_program not in process_id_program and log_process_id != -1:
            process_id_program.append(log_program)

    return process_id_program


def bonus():
    """Retourne la réponse à la question bonus"""

    logs = lines_from_file("./log/auth.log")
    logs_opened_by_root = logs_with_tag(logs, "session opened for user root by (uid=0)")
    logs_closed_by_root = logs_with_tag(logs, "session closed for user root")

    return len(logs_opened_by_root) - len(logs_closed_by_root)

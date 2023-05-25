import exam_decembre

L_TEST_2 = [
    "Oct JJ 08:08:08 host sudo: Hello :)",
    "Nov JJ 12:44:55 host sudooo: session opened for user root ",
    "Jan JJ 12:32:44 host sudo: session opened for user root",
    "Feb JJ 12:32:44 host NetworkManager[5]: <warn> : FATAL ERRoR",
    "Mar JJ HH:MM:SS host program: message",
    "Mar JJ HH:MM:SS host program: Demande au canard !?",
    "Mar JJ HH:MM:SS host CRON[1307]: Ca va ? Tu t'en sors ?",
    "Mar JJ HH:MM:SS host CRON[1307]: olala eRRoR",
    "Dec JJ HH:MM:SS host unSuspect[5]: session opened for user root",
    "Jan JJ HH:MM:SS host unSuspect[42]: session opened for user root",
    "Apr JJ HH:MM:SS host unAutreSuspect[18]: session opened for user root...",
    "May JJ 00:00:12 host NetworkManager[42]: <info> : warn : La progra c'est génial ! Youpie !",
    "Jun JJ HH:MM:SS host unSuspect[5]: session closed for user root",
    "Jul JJ 12:34:56 host NetworkManager[7]: <warn> : Saperlipopette",
    "Jul JJ 12:34:56 host NetworkManager[7]: <warn> : didondidonc... ça ne fonctionne pas",
    "Jul JJ 12:34:57 host NetworkManager[7]: <warn> : hum... ennuyeux",
    "Jul JJ 12:34:56 host NetworkManager[1]: <warn> : fICHTRE, encore un... et en plus, j'étais CAPS lock",
    "Jul JJ 12:34:50 host NetworkManager[1]: <info> : c'est bon",
    "Jul JJ 12:34:56 host NetworkManager[1]: <warnnnn> : c'est bon",
    "Sept JJ HH:MM:SS host CRON[1300]: session opened for user root mais lui, il peut !",
]


def test_network_message_times_default_args():
    """Test unitaire pour network_message_times avec parametres par défaut"""
    output = exam_decembre.network_message_times(L_TEST_2)
    expected = ["Jul JJ 12:34:56", "Feb JJ 12:32:44", "Jul JJ 12:34:57"]
    assert len(output) == len(expected)
    for elem in output:
        assert elem in expected
    for elem in expected:
        assert elem in output


def test_programs_with_process_id():
    """Test unitaire pour programs_with_process_id"""
    output = exam_decembre.programs_with_process_id(L_TEST_2)
    expected = ["NetworkManager", "CRON", "unSuspect", "unAutreSuspect"]
    assert len(output) == len(expected)
    for elem in output:
        assert elem in expected
    for elem in expected:
        assert elem in output

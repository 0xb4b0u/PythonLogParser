import exam_juin

L_TEST_1 = [
    "Oct 01 10:42:42 host sudo: Hello :)",
    "Nov 20 10:42:42 host sudooo: session opened for user root ",
    "Jan 13 10:42:42 host sudo: session opened for user root",
    "Feb 02 10:42:42 host programB[5]: FATAL ERRoR",
    "Mar 14 10:42:42 host program: message",
    "Mar 14 10:42:42 host program: Demande au canard !",
    "Mar 14 10:42:42 host CRON[1307]: Ca va ? Tu t'en sors ?",
    "Mar 15 10:42:42 host CRON[1307]: olala eRRoR",
    "Dec 24 10:42:42 host unSuspect[5]: session opened for user root",
    "Jan 20 10:42:42 host unSuspect[42]: session opened for user root",
    "Apr 05 10:42:42 host unAutreSuspect[18]: session opened for user root...",
    "May 17 10:42:42 host programA[42]: La progra c'est génial ! Youpie !",
    "Jun 25 10:42:42 host unSuspect[5]: session closed for user root",
    "Jul 01 10:42:42 host programC[7]: message important : Coucou les copains !",
    "Aug 09 10:42:42 host programC[1]: hello host :)",
    "Sep 10 10:42:42 host CRON[1300]: session opened for user root mais lui, il peut !",
]
L_TEST_2 = [
    "Oct 01 10:42:42 host sudo: Hello :)",
    "Nov 20 10:42:42 host sudooo: session opened for user root ",
    "Jan 13 10:42:42 host sudo: session opened for user root",
    "Feb 02 10:42:42 host programB[5]: FATAL ERRoR",
    "Feb 02 10:42:42 host programB[5]: FATAL ERRoR",
    "Mar 14 10:42:42 host program: message",
    "Mar 14 10:42:42 host program: Demande au canard !",
    "Mar 14 10:42:42 host CRON[1307]: Ca va ? Tu t'en sors ?",
    "Mar 15 10:42:SS host CRON[1307]: olala eRRoR",
    "Dec 24 10:42:42 host unSuspect[5]: Error, j'ai planté",
    "Jan 20 10:42:42 host unSuspect[42]: Error, j'ai encore planté :'(",
    "Apr 05 10:42:42 host unAutreSuspect[18]: session opened for user root...",
    "May 17 10:42:42 host programA[42]: La progra c'est génial ! Youpie !",
    "Jun 25 10:42:42 host unSuspect[5]: Error, j'en ai marre de planter ><",
    "Jul 01 10:42:42 host programC[7]: message important : Coucou les copains !",
    "Aug 09 10:42:42 host programC[1]: hello host :)",
    "Sep 10 10:42:42 host CRON[1300]: session opened for user root mais on a une erreur inconnue !",
]
logs_1 = """Oct 21 06:13:30 kali systemd-logind[433]: Removed session c2.
Oct 21 06:13:41 kali systemd: pam_unix(systemd-user:session): session closed for user lightdm
Oct 21 06:13:51 kali sudo: pam_unix(sudo:auth): Couldn't open /etc/securetty: No such file or directory
Oct 21 06:13:54 kali sudo: pam_unix(sudo:auth): Couldn't open /etc/securetty: No such file or directory
Oct 21 06:13:54 kali sudo:     kali : TTY=pts/0 ; PWD=/var/log ; USER=root ; COMMAND=/usr/sbin/shutdown -h now
Oct 21 06:13:54 kali sudo: pam_unix(sudo:session): session opened for user root by (uid=0)
Oct 25 02:34:11 kali systemd-logind[434]: New seat seat0.
Oct 25 02:34:11 kali systemd-logind[434]: Watching system buttons on /dev/input/event1 (Power Button)
Oct 25 02:34:11 kali systemd-logind[434]: Watching system buttons on /dev/input/event2 (Sleep Button)
Oct 25 02:34:11 kali systemd-logind[434]: Watching system buttons on /dev/input/event0 (AT Translated Set 2 keyboard)
Oct 25 02:34:18 kali sshd[590]: Server listening on 0.0.0.0 port 22.
Oct 25 02:34:18 kali sshd[590]: Server listening on :: port 22.
Oct 25 02:34:29 kali lightdm: pam_unix(lightdm-greeter:session): session opened for user lightdm by (uid=0)
Oct 25 02:34:29 kali systemd-logind[434]: New session c1 of user lightdm.
Oct 25 02:34:29 kali systemd: pam_unix(systemd-user:session): session opened for user lightdm by (uid=0)
Oct 25 02:34:43 kali lightdm: pam_unix(lightdm:auth): Couldn't open /etc/securetty: No such file or directory
Oct 25 02:34:46 kali lightdm: pam_unix(lightdm:auth): Couldn't open /etc/securetty: No such file or directory
Oct 25 02:34:46 kali lightdm: gkr-pam: unable to locate daemon control file
Oct 25 02:34:46 kali lightdm: gkr-pam: stashed password to try later in open session
Oct 25 02:34:46 kali lightdm: pam_unix(lightdm-greeter:session): session closed for user lightdm
Oct 25 02:34:46 kali lightdm: pam_unix(lightdm:session): session opened for user kali by (uid=0)
Oct 25 02:34:46 kali systemd-logind[434]: Removed session c1.
Oct 25 02:34:46 kali systemd-logind[434]: New session 2 of user kali.
Oct 25 02:34:46 kali systemd: pam_unix(systemd-user:session): session opened for user kali by (uid=0)
Oct 25 02:34:47 kali lightdm: gkr-pam: gnome-keyring-daemon started properly and unlocked keyring
Oct 25 02:34:51 kali polkitd(authority=local): Registered Authentication Agent for unix-session:2 (system bus name :1.33 [/usr/lib/policykit-1-gnome/polkit-gnome-authentication-agent-1], object path /org/gnome/PolicyKit1/AuthenticationAgent, locale en_US.utf8)
Oct 25 02:34:57 kali systemd: pam_unix(systemd-user:session): session closed for user lightdm
Oct 25 02:35:01 kali CRON[1176]: pam_unix(cron:session): session opened for user root by (uid=0)""".split(
    "\n"
)

logs_2 = """Oct 21 04:18:05 kali lightdm: pam_unix(lightdm-greeter:session): session opened for user lightdm by (uid=0)
Oct 21 04:18:05 kali systemd-logind[433]: New session c1 of user lightdm.
Oct 21 04:18:05 kali systemd-logind[433]: New session c1 of user lightdm.
Oct 21 04:18:05 kali systemd-logind[433]: New session c1 of user kali.
Oct 21 04:18:05 kali systemd-logind[433]: New session c2 of user kali.
Oct 21 04:18:05 kali systemd: pam_unix(systemd-user:session): session opened for user lightdm by (uid=0)
Oct 21 04:18:20 kali lightdm: pam_unix(lightdm:auth): Couldn't open /etc/securetty: No such file or directory
Oct 21 04:18:23 kali lightdm: pam_unix(lightdm:auth): Couldn't open /etc/securetty: No such file or directory
Oct 21 04:18:23 kali lightdm: gkr-pam: unable to locate daemon control file
Oct 21 04:18:23 kali lightdm: gkr-pam: stashed password to try later in open session
Oct 21 04:18:23 kali systemd-logind[433]: New session c1 of user kali.
Oct 21 04:18:23 kali lightdm: pam_unix(lightdm-greeter:session): session closed for user lightdm
Oct 21 04:18:23 kali lightdm: pam_unix(lightdm:session): session opened for user kali by (uid=0)
Oct 21 04:18:05 kali systemd-logind[433]: New session c2 of user lightdm.""".split(
    "\n"
)


def test_programs_which_open_sessions():
    """Test unitaire pour programs_which_open_session"""
    output = exam_juin.process_id_which_open_sessions(
        L_TEST_1, "05:17 10:42:42", "11:20 10:42:42"
    )
    expected = [1300]
    assert len(output) == len(expected)
    for elem in output:
        assert elem in expected, f"{elem} ne devrait pas se trouver dans la liste"
    for elem in expected:
        assert elem in output, f"{elem} aurait du se trouver dans la liste"


def test_programs_which_open_sessions_2():
    output = exam_juin.process_id_which_open_sessions(
        L_TEST_2, "04:05 10:41:00", "04:05 10:43:00"
    )
    expected = [18]
    assert len(output) == len(expected)
    for elem in output:
        assert elem in expected, f"{elem} ne devrait pas se trouver dans la liste"
    for elem in expected:
        assert elem in output, f"{elem} aurait du se trouver dans la liste"


def test_error_process():
    """Test unitaire pour error_process"""
    output = exam_juin.error_process(L_TEST_1, "programB", "02:02")
    expected = [5]
    assert len(output) == len(expected)
    for elem in output:
        assert elem in expected, f"{elem} ne devrait pas être dans la liste produite"
    for elem in expected:
        assert elem in output, f"{elem} aurait du se trouver dans la liste"


def test_error_process_2():
    """Test unitaire pour error_process"""
    output = exam_juin.error_process(L_TEST_2, "program", "03:15")
    expected = []
    assert len(output) == len(expected)
    for elem in output:
        assert elem in expected, f"{elem} ne devrait pas être dans la liste produite"
    for elem in expected:
        assert elem in output, f"{elem} aurait du se trouver dans la liste"


def test_sessions_kali_1():
    assert 1 == exam_juin.sessions_kali(logs_1)


def test_sessions_kali_2():
    assert 2 == exam_juin.sessions_kali(logs_2)

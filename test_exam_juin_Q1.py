import exam_juin

logs = """Oct 21 04:18:05 kali lightdm: pam_unix(lightdm-greeter:session): session opened for user lightdm by (uid=0)
Oct 21 04:18:05 kali systemd-logind[433]: New session c1 of user lightdm.
Oct 21 04:18:05 kali systemd: pam_unix(systemd-user:session): session opened for user lightdm by (uid=0)
Oct 21 04:18:20 kali lightdm: pam_unix(lightdm:auth): Couldn't open /etc/securetty: No such file or directory
Oct 21 04:18:23 kali lightdm: pam_unix(lightdm:auth): Couldn't open /etc/securetty: No such file or directory
Oct 21 04:18:23 kali lightdm: gkr-pam: unable to locate daemon control file
Oct 21 04:18:23 kali lightdm: gkr-pam: stashed password to try later in open session
Oct 21 04:18:23 kali lightdm: pam_unix(lightdm-greeter:session): session closed for user lightdm
Oct 21 04:18:23 kali lightdm: pam_unix(lightdm:session): session opened for user kali by (uid=0)
Oct 21 04:18:23 kali systemd-logind[433]: Removed session c1.
Oct 21 04:18:23 kali systemd-logind[433]: session opened for user root .
Oct 21 04:18:23 kali systemd: pam_unix(systemd-user:session): session opened for user kali by (uid=0)
Oct 21 04:18:25 kali lightdm: gkr-pam: gnome-keyring-daemon started properly and unlocked keyring
Oct 21 04:18:30 kali polkitd(authority=local): Registered Authentication Agent for unix-session:2 (system bus name :1.36 [/usr/lib/policykit-1-gnome/polkit-gnome-authentication-agent-1], object path /org/gnome/PolicyKit1/AuthenticationAgent, locale en_US.utf8)
Oct 21 04:19:59 kali sudo: pam_unix(sudo:auth): Couldn't open /etc/securetty: No such file or directory
Oct 21 04:20:02 kali sudo: pam_unix(sudo:auth): Couldn't open /etc/securetty: No such file or directory
Oct 21 04:20:03 kali sudo:     kali : TTY=pts/0 ; PWD=/var/log ; USER=root ; COMMAND=/usr/bin/cat syslog
Oct 21 04:20:03 kali sudo: pam_unix(sudo:session): session opened for user root by (uid=0)
Oct 21 04:20:03 kali sudo: pam_unix(sudo:session): session closed for user root
Oct 21 04:22:32 kali sudo:     kali : TTY=pts/0 ; PWD=/var/log ; USER=root ; COMMAND=/usr/bin/cat secure
Oct 21 04:22:32 kali sudo: pam_unix(sudo:session): session opened for user root by (uid=0)
Oct 21 04:22:32 kali sudo: pam_unix(sudo:session): session closed for user root
Oct 21 04:23:03 kali sudo:     kali : TTY=pts/0 ; PWD=/var/log ; USER=root ; COMMAND=/usr/bin/cat auth.log
Oct 21 04:23:03 kali sudo: pam_unix(sudo:session): session opened for user root by (uid=0)
Oct 21 04:23:03 kali sudo: pam_unix(sudo:session): session closed for user root
Oct 21 04:25:01 kali CRON[1307]: pam_unix(cron:session): session opened for user root by (uid=0)
Oct 21 04:25:01 kali CRON[1307]: pam_unix(cron:session): session closed for user root
Oct 21 04:29:08 kali sudo:     kali : TTY=pts/0 ; PWD=/var/log ; USER=root ; COMMAND=/usr/bin/cat auth.log
Oct 21 04:29:08 kali sudo: pam_unix(sudo:session): session opened for user root by (uid=0)
Oct 21 04:29:08 kali sudo: pam_unix(sudo:session): session closed for user root
Oct 21 04:35:01 kali CRON[1480]: pam_unix(cron:session): session opened for user root by (uid=0)
Oct 21 04:35:01 kali CRON[1480]: pam_unix(cron:session): session closed for user root
Oct 21 04:39:01 kali CRON[1545]: pam_unix(cron:session): session opened for user root by (uid=0)
Oct 21 04:39:01 kali CRON[1545]: pam_unix(cron:session): session closed for user root
Oct 21 04:45:01 kali CRON[1709]: pam_unix(cron:session): session opened for user root by (uid=0)
Oct 21 04:45:01 kali CRON[1709]: pam_unix(cron:session): session closed for user root
Oct 21 04:54:00 kali lightdm: pam_unix(lightdm-greeter:session): session opened for user lightdm by (uid=0)
Oct 21 04:54:00 kali systemd-logind[433]: New session c2 of user lightdm.
Oct 21 04:54:00 kali systemd: pam_unix(systemd-user:session): session opened for user lightdm by (uid=0)
Oct 21 04:55:01 kali CRON[1979]: pam_unix(cron:session): session opened for user root by (uid=0)
Oct 21 04:55:01 kali CRON[1979]: pam_unix(cron:session): session closed for user root
Oct 21 05:05:01 kali CRON[2206]: pam_unix(cron:session): session opened for user root by (uid=0)
Oct 21 05:05:01 kali CRON[2206]: pam_unix(cron:session): session closed for user root
Oct 21 05:09:01 kali CRON[2328]: pam_unix(cron:session): session opened for user root by (uid=0)
Oct 21 05:09:01 kali CRON[2328]: pam_unix(cron:session): session closed for user root
Oct 21 05:15:01 kali CRON[2444]: pam_unix(cron:session): session opened for user root by (uid=0)
Oct 21 05:15:01 kali CRON[2444]: pam_unix(cron:session): session closed for user root
Oct 21 05:17:01 kali CRON[2482]: pam_unix(cron:session): session opened for user root by (uid=0)
Oct 21 05:17:01 kali CRON[2482]: pam_unix(cron:session): session closed for user root
Oct 21 05:25:01 kali CRON[2637]: pam_unix(cron:session): session opened for user root by (uid=0)
Oct 21 05:25:01 kali CRON[2637]: pam_unix(cron:session): session closed for user root
Oct 21 05:35:01 kali CRON[2816]: pam_unix(cron:session): session opened for user root by (uid=0)
Oct 21 05:35:01 kali CRON[2816]: pam_unix(cron:session): session closed for user root
Oct 21 05:39:01 kali CRON[2942]: pam_unix(cron:session): session opened for user root by (uid=0)
Oct 21 05:39:01 kali CRON[2942]: pam_unix(cron:session): session closed for user root
Oct 21 05:45:01 kali CRON[3063]: pam_unix(cron:session): session opened for user root by (uid=0)
Oct 21 05:45:01 kali CRON[3063]: pam_unix(cron:session): session closed for user root
Oct 21 05:55:01 kali CRON[3254]: pam_unix(cron:session): session opened for user root by (uid=0)
Oct 21 05:55:01 kali CRON[3254]: pam_unix(cron:session): session closed for user root
Oct 21 06:05:01 kali CRON[3452]: pam_unix(cron:session): session opened for user root by (uid=0)
Oct 21 06:05:01 kali CRON[3452]: pam_unix(cron:session): session closed for user root
Oct 21 06:09:01 kali CRON[3530]: pam_unix(cron:session): session opened for user root by (uid=0)
Oct 21 06:09:01 kali CRON[3530]: pam_unix(cron:session): session closed for user root
Oct 21 06:13:26 kali lightdm: pam_unix(lightdm:auth): Couldn't open /etc/securetty: No such file or directory
Oct 21 06:13:30 kali lightdm: pam_unix(lightdm:auth): Couldn't open /etc/securetty: No such file or directory
Oct 21 06:13:30 kali lightdm: gkr-pam: unable to locate daemon control file
Oct 21 06:13:30 kali lightdm: gkr-pam: stashed password to try later in open session
Oct 21 06:13:30 kali lightdm: pam_unix(lightdm-greeter:session): session closed for user lightdm
Oct 21 06:13:30 kali systemd-logind[433]: Removed session c2.
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
Oct 25 02:35:01 kali CRON[1176]: pam_unix(cron:session): session opened for user root by (uid=0)
Oct 25 02:35:01 kali CRON[1176]: pam_unix(cron:session): session closed for user root
Oct 25 02:39:01 kali CRON[1257]: pam_unix(cron:session): session opened for user root by (uid=0)
Oct 25 02:39:01 kali CRON[1257]: pam_unix(cron:session): session closed for user root
Oct 25 02:45:01 kali CRON[1311]: pam_unix(cron:session): session opened for user root by (uid=0)
Oct 25 02:45:01 kali CRON[1311]: pam_unix(cron:session): session closed for user root
Oct 25 02:48:18 kali lightdm: pam_unix(lightdm-greeter:session): session opened for user lightdm by (uid=0)
Oct 25 02:48:18 kali systemd-logind[434]: New session c2 of user lightdm.
Oct 25 02:48:18 kali systemd: pam_unix(systemd-user:session): session opened for user lightdm by (uid=0)
Oct 25 02:48:18 kali lightdm: pam_unix(lightdm:auth): Couldn't open /etc/securetty: No such file or directory
Oct 25 02:48:18 kali lightdm: pam_unix(lightdm:auth): Couldn't open /etc/securetty: No such file or directory
Oct 25 02:55:01 kali CRON[1412]: pam_unix(cron:session): session opened for user root by (uid=0)
Oct 25 02:55:01 kali CRON[1412]: pam_unix(cron:session): session closed for user root
Oct 25 03:05:01 kali CRON[1420]: pam_unix(cron:session): session opened for user root by (uid=0)
Oct 25 03:05:02 kali CRON[1420]: pam_unix(cron:session): session closed for user root
Oct 25 03:09:02 kali CRON[1430]: pam_unix(cron:session): session opened for user root by (uid=0)
Oct 25 03:09:02 kali CRON[1430]: pam_unix(cron:session): session closed for user root
Oct 25 03:10:01 kali CRON[1481]: pam_unix(cron:session): session opened for user root by (uid=0)
Oct 25 03:10:01 kali CRON[1481]: pam_unix(cron:session): session closed for user root
Oct 25 03:15:01 kali CRON[1487]: pam_unix(cron:session): session opened for user root by (uid=0)
Oct 25 03:15:01 kali CRON[1487]: pam_unix(cron:session): session closed for user root
Oct 25 03:16:19 kali lightdm: pam_unix(lightdm:auth): Couldn't open /etc/securetty: No such file or directory
Oct 25 03:16:19 kali lightdm: gkr-pam: unable to locate daemon control file
Oct 25 03:16:19 kali lightdm: gkr-pam: stashed password to try later in open session
Oct 25 03:16:19 kali lightdm: pam_unix(lightdm-greeter:session): session closed for user lightdm
Oct 25 03:16:19 kali systemd-logind[434]: Removed session c2.
Oct 25 03:17:01 kali CRON[1502]: pam_unix(cron:session): session opened for user root by (uid=0)
Oct 25 03:17:01 kali CRON[1502]: pam_unix(cron:session): session closed for user root
Oct 25 03:25:01 kali CRON[1581]: pam_unix(cron:session): session opened for user root by (uid=0)
Oct 25 03:25:01 kali CRON[1581]: pam_unix(cron:session): session closed for user root
Oct 25 03:30:00 kali lightdm: pam_unix(lightdm-greeter:session): session opened for user lightdm by (uid=0)
Oct 25 03:30:00 kali systemd: pam_unix(systemd-user:session): session opened for user lightdm by (uid=0)
Oct 25 03:30:00 kali systemd-logind[434]: New session c3 of user lightdm.
Oct 25 03:30:00 kali lightdm: pam_unix(lightdm:auth): Couldn't open /etc/securetty: No such file or directory
Oct 25 03:30:00 kali lightdm: pam_unix(lightdm:auth): Couldn't open /etc/securetty: No such file or directory
Oct 25 03:35:01 kali CRON[1675]: pam_unix(cron:session): session opened for user root by (uid=0)
Oct 25 03:35:01 kali CRON[1675]: pam_unix(cron:session): session closed for user root
Oct 25 03:39:01 kali CRON[1678]: pam_unix(cron:session): session opened for user root by (uid=0)
Oct 25 03:39:01 kali CRON[1678]: pam_unix(cron:session): session closed for user root
Oct 25 03:45:01 kali CRON[1738]: pam_unix(cron:session): session opened for user root by (uid=0)
Oct 25 03:45:01 kali CRON[1738]: pam_unix(cron:session): session closed for user root
""".split(
    "\n"
)


def test_question_1():
    """Test unitaire pour programs_which_open_session"""
    output = exam_juin.process_id_which_open_sessions(
        logs, "10:21 04:18:00", "10:25 03:45:01"
    )
    print(output)
    expected = [
        433,
        1307,
        1480,
        1545,
        1709,
        1979,
        2206,
        2328,
        2444,
        2482,
        2637,
        2816,
        2942,
        3063,
        3254,
        3452,
        3530,
        1176,
        1257,
        1311,
        1412,
        1420,
        1430,
        1481,
        1487,
        1502,
        1581,
        1675,
        1678,
        1738,
    ]
    assert len(output) == len(expected)
    for elem in output:
        assert elem in expected, f"{elem} ne devrait pas se trouver dans la liste"
    for elem in expected:
        assert elem in output, f"{elem} aurait du se trouver dans la liste"

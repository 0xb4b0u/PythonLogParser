import exam_juin

logs = """Oct 21 04:18:05 kali lightdm: pam_unix(lightdm-greeter:session): session opened for user lightdm by (uid=0)
Oct 21 04:18:05 kali systemd-logind[433]: New session c1 of user lightdm.
Oct 21 04:18:05 kali systemd: pam_unix(systemd-user:session): session opened for user lightdm by (uid=0)
Oct 21 04:18:20 kali lightdm: pam_unix(lightdm:auth): Error Couldn't open /etc/securetty: No such file or directory
Oct 21 04:18:23 kali lightdm: pam_unix(lightdm:auth): Error Couldn't open /etc/securetty: No such file or directory
Oct 21 04:18:23 kali lightdm[5]: error: unable to locate daemon control file
Oct 21 04:18:23 kali lightdm: gkr-pam: stashed password to try later in open session
Oct 21 04:18:23 kali lightdm: pam_unix(lightdm-greeter:session): session closed for user lightdm
Oct 21 04:18:23 kali lightdm: pam_unix(lightdm:session): session opened for user kali by (uid=0)
Oct 21 04:18:23 kali systemd-logind[433]: Removed session c1.
Oct 21 04:18:23 kali systemd-logind[433]: session opened for user root .
Oct 21 04:18:23 kali systemd: pam_unix(systemd-user:session): session opened for user kali by (uid=0)
Oct 21 04:18:25 kali lightdm: gkr-pam: gnome-keyring-daemon started properly and unlocked keyring
Oct 21 04:18:30 kali polkitd(authority=local): Registered Authentication Agent for unix-session:2 (system bus name :1.36 [/usr/lib/policykit-1-gnome/polkit-gnome-authentication-agent-1], object path /org/gnome/PolicyKit1/AuthenticationAgent, locale en_US.utf8)
Oct 21 04:19:59 kali sudo: pam_unix(sudo:auth): Error Couldn't open /etc/securetty: No such file or directory
Oct 21 04:20:02 kali sudo: pam_unix(sudo:auth): Error Couldn't open /etc/securetty: No such file or directory
Oct 21 04:20:03 kali sudo:     kali : TTY=pts/0 ; PWD=/var/log ; USER=root ; COMMAND=/usr/bin/cat syslog
Oct 21 04:20:03 kali sudo: pam_unix(sudo:session): session opened for user root by (uid=0)
Oct 21 04:20:03 kali sudo: pam_unix(sudo:session): session closed for user root
Oct 21 04:22:32 kali sudo:     kali : TTY=pts/0 ; PWD=/var/log ; USER=root ; COMMAND=/usr/bin/cat secure
Oct 21 04:22:32 kali sudo: pam_unix(sudo:session): session opened for user root by (uid=0)
Oct 21 04:22:32 kali sudo: pam_unix(sudo:session): session closed for user root
Oct 21 04:23:03 kali sudo:     kali : TTY=pts/0 ; PWD=/var/log ; USER=root ; COMMAND=/usr/bin/cat auth.log
Oct 21 04:23:03 kali sudo: pam_unix(sudo:session): session opened for user root by (uid=0)
Oct 22 04:23:03 kali sudo[4]: pam_unix(sudo:session): Error session""".split(
    "\n"
)


def test_question_2():
    """Test unitaire pour error_process"""
    output = exam_juin.error_process(logs, "lightdm", "10:21")
    expected = [5]
    assert len(output) == len(expected)
    for elem in output:
        assert elem in expected, f"{elem} ne devrait pas être dans la liste produite"
    for elem in expected:
        assert elem in output, f"{elem} aurait du se trouver dans la liste"

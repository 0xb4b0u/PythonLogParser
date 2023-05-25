import exam_juin

logs = []
with open("./log/auth_exam.log", "r") as file:
    logs = file.readlines()


def test_bonus():
    assert 3 == exam_juin.sessions_kali(logs)

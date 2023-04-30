import mysql.connector
import os

# connect to mysql
# user and password are your user and password not "????"
db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "mamypoko185",
    database = "school"
)

__ = db.cursor()

with open(os.path.join("Phần 2", "out", "others.sql"), "r", encoding='utf8') as file:
    file_reader = file.readlines()
    for line in file_reader:
        if line.strip() == "":
            continue
        else:
            try:
                __.execute(line.strip())
                db.commit()
            except mysql.connector.errors.IntegrityError:
                continue


names = ["gdtx", "mn", "tih", "thcs", "thpt"]
paths = [os.path.join("Phần 2", "out", name + ".sql") for name in names]

for path in [paths[0]]:
    with open(path, "r", encoding='utf8') as file:
        file_reader = file.readlines()
        for line in file_reader:
            if line.strip() == "":
                continue
            else:
                try:
                    __.execute(line.strip())
                    db.commit()
                except mysql.connector.errors.IntegrityError:
                    continue
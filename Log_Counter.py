import datetime

timestamp = datetime.datetime.now()

log_entry = f"{timestamp}"

with open("log_file.txt", "a") as file:
    file.write(log_entry)

with open("log_file.txt", "a") as file:
    file.write("\n")

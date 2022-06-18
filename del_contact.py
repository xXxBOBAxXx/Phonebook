# импорты pb и id

id = 1 # Петр Петров (пример)

def d_contact(pb, id):
    with open("phonebook copy.csv", mode="w", encoding='utf-8') as file:
        file_writer = csv.writer(file)
    with open("phonebook copy.csv", mode="a", encoding='utf-8') as file:
        file_writer = csv.writer(file, delimiter = "|", lineterminator="\r")
        pb.remove(pb[id])
        for i in pb:
            file_writer.writerow(i)

def export_1_contact(pb):
    with open("phonebook copy.csv", mode="a", encoding='utf-8') as file:
        file_writer = csv.writer(file, delimiter = "|")
        file_writer.writerow(pb)

# чтобы записывать контакты построчно
# Иван
# Иванов
# 891...
# вместо delimiter = "|" написать delimiter = "\r"

def export_all_contacts(pb):
    with open("phonebook copy.csv", mode="a", encoding='utf-8') as file:
        file_writer = csv.writer(file, delimiter = "|", lineterminator="\r")
        for i in pb:
            file_writer.writerow(pb)

def add_new_contact():
    with open("phonebook.csv", mode="a", encoding='utf-8') as file:
        file_writer = csv.writer(file, delimiter = "|")
        npb = ['', '', '', ''] 
        npb[0] = input('Введите имя нового контакта: ') 
        npb[1] = input('Введите фамилию нового контакта: ') 
        npb[2] = input('Введите номер телефона нового контакта: ') 
        npb[3] = input('Введите комментарий для нового контакта: ') 
        file_writer.writerow(npb)



# считывает файл записвнный построчно:

def pb_on_string():
    with open("phonebook copy.csv", encoding = 'utf-8') as file:
        reader = csv.reader(file, delimiter = "|")
        for id in reader:
            id = str(id)
            id = id.replace(']','')
            id = id.replace('[','')
            id = id.replace("'",'')
            pb.append(id)
        pb = [[pb[id],pb[id+1],pb[id+2],pb[id+3]] for id in range(0,len(pb),4)]

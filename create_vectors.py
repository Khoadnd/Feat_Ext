import re
import csv
import os


def csv_gen(txt_file, folder):
    header = []
    Feature = []

    with open(txt_file, 'rt') as myfile:
        for myline in myfile:
            Feature.append(myline.rstrip('\n').rstrip(' '))

    Services = []
    for index, line in enumerate(Feature):
        if " Services :" in str(line):
            for a in range(index + 1, index + 100):
                if len(Feature[a]) == 0:
                    break
                else:
                    try:
                        serv = re.search(r'(\w+)Service', Feature[a]).group(1)
                        Services.append(serv + "Service")
                    except:
                        #print(" None !!!! ")
                        pass

    Permissions = []
    for index, line in enumerate(Feature):
        if " Permissions :" in str(line):
            for a in range(index + 1, index + 100):
                if len(Feature[a]) == 0:
                    break
                else:
                    try:
                        perm = re.search(
                            r'".*.permission.([^"]*)"', Feature[a]).group(1)
                        Permissions.append("permission." + perm)
                    except:
                        #print(" None !!!! ")
                        pass

    Categories = []
    for index, line in enumerate(Feature):
        if " Intents Category :" in str(line):
            for a in range(index + 1, index + 100):
                if len(Feature[a]) == 0:
                    break
                else:
                    try:
                        cate = re.search(
                            r'".*.category.([^"]*)"', Feature[a]).group(1)
                        Categories.append("category." + cate)
                    except:
                        #print("None !!!!")
                        pass

    Actions = []
    for index, line in enumerate(Feature):
        if " Intents Action :" in str(line):
            for a in range(index + 1, index + 100):
                if len(Feature[a]) == 0:
                    break
                else:
                    try:
                        actio = re.search(
                            r'".*.action.([^"]*)"', Feature[a]).group(1)
                        Actions.append("action." + actio)
                    except:
                        #print("None !!!!")
                        pass

    header.append("apk_name")
    Values = []
    Values.append(txt_file.split('/')[1].split('_features.txt')[0])
    with open('./1_List_Permissions.csv') as csvFile:
        dataPer = csvFile.readlines()

    csvFile.close()
    for i in dataPer:
        if(i.strip() == ""):
            continue
        header.append(i.strip())
        if i.strip() in Permissions:
            Values.append(1)
        else:
            Values.append(0)

    with open('./3_List_Actions.csv') as csvFile:
        dataAct = csvFile.readlines()
    csvFile.close()
    for i in dataAct:
        if(i.strip() == ""):
            continue
        header.append(i.strip())
        if i.strip() in Actions:
            Values.append(1)
        else:
            Values.append(0)

    with open('./2_List_Services.csv') as csvFile:
        dataSer = csvFile.readlines()
    csvFile.close()
    for i in dataSer:
        if(i.strip() == ""):
            continue
        header.append(i.strip())
        if i.strip() in Services:
            Values.append(1)
        else:
            Values.append(0)

    with open('./4_List_Categories.csv') as csvFile:
        dataCat = csvFile.readlines()
    csvFile.close()
    for i in dataCat:
        if(i.strip() == ""):
            continue
        header.append(i.strip())
        if i.strip() in Categories:
            Values.append(1)
        else:
            Values.append(0)

    if not os.path.isfile('./output.csv'):
        with open('./output.csv', 'a') as cs:
            writer = csv.writer(cs)
            writer.writerow(header)

    with open('./output.csv', 'a+') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(Values)
    csvFile.close()

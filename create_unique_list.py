import re


def func(txt_file):
    Feature = []
    name = ""
    with open(txt_file, 'rt') as myfile:
        for myline in myfile:
            Feature.append(myline.rstrip('\n').rstrip(' '))

    Permissions = []
    for index, line in enumerate(Feature):
        if " Permissions :" in str(line):
            for a in range(index+1, index + 100):
                if len(Feature[a]) == 0:
                    break
                else:
                    try:
                        perm = re.search(
                            r'".*.permission.([^"]*)"', Feature[a]).group(1)
                        Permissions.append("permission."+perm)
                    except:
                        #print(" None !!!! ")
                        pass

    # Create the Unique Permission List
    Per = []
    for i in Permissions:
        Per.append(i)

    for i in Per:
        # print(i)
        if i in open('./1_List_Permissions.csv').read():
            pass
        else:
            with open('./1_List_Permissions.csv', 'a+') as csvfile:
                csvfile.write(i)
                csvfile.write('\n')
            csvfile.close()

    Services = []
    for index, line in enumerate(Feature):
        if " Services :" in str(line):
            for a in range(index+1, index + 100):
                if len(Feature[a]) == 0:
                    break
                else:
                    try:
                        serv = re.search(r'(\w+)Service', Feature[a]).group(1)
                        Services.append(serv+"Service")
                    except:
                        #print(" None !!!! ")
                        pass

    Ser = []
    for i in Services:
        Ser.append(i)

    for i in Ser:
        # print(i)
        if i in open('./2_List_Services.csv').read():
            pass
        else:
            with open('./2_List_Services.csv', 'a+') as csvfile:
                csvfile.write(i)
                csvfile.write('\n')
            csvfile.close()

    Actions = []
    for index, line in enumerate(Feature):
        if " Intents Action :" in str(line):
            for a in range(index+1, index + 100):
                if len(Feature[a]) == 0:
                    break
                else:
                    try:
                        actio = re.search(
                            r'".*.action.([^"]*)"', Feature[a]).group(1)
                        Actions.append("action."+actio)
                    except:
                        #print("None !!!!")
                        pass

    Act = []
    for i in Actions:
        Act.append(i)

    for i in Act:
        # print(i)
        if i in open('./3_List_Actions.csv').read():
            pass
        else:
            with open('./3_List_Actions.csv', 'a+') as csvfile:
                csvfile.write(i)
                csvfile.write('\n')
            csvfile.close()

    Categories = []
    for index, line in enumerate(Feature):
        if " Intents Category :" in str(line):
            for a in range(index+1, index + 100):
                if len(Feature[a]) == 0:
                    break
                else:
                    try:
                        cate = re.search(
                            r'".*.category.([^"]*)"', Feature[a]).group(1)
                        Categories.append("category."+cate)
                    except:
                        #print("None !!!!")
                        pass

    Cat = []
    for i in Categories:
        Cat.append(i)

    for i in Cat:
        # print(i)
        if i in open('./4_List_Categories.csv').read():
            pass
        else:
            with open('./4_List_Categories.csv', 'a+') as csvfile:
                csvfile.write(i)
                csvfile.write('\n')
            csvfile.close()

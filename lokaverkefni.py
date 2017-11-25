#Daníel Arnarsson
#22.11.2017

#workplace
#make input values input("")?


class workplace:
    def __init__(self):
        employeeInfo = {}
        self.employeeInfo = employeeInfo

    def create_employee(self, fyrsta_nafn, sidasta_nafn, starfsgrein, laun):
        nafn = str(fyrsta_nafn + " " + sidasta_nafn)

        try:
            id = len(self.employeeInfo) + 1
            nafnOgId = (nafn, id)
            self.employeeInfo[nafnOgId] = [id, fyrsta_nafn, sidasta_nafn, starfsgrein, laun]

        except NameError:
            employeeInfo = {}
            id = len(employeeInfo) + 1
            nafnOgId = (nafn, id)
            self.employeeInfo = employeeInfo
            self.employeeInfo[nafnOgId] = [id, fyrsta_nafn, sidasta_nafn, starfsgrein, laun]
        else:
            pass

    def search_employee(self, name=None, id=None):
        fjoldiStarfsmanna = len(self.employeeInfo)
        teljari=0
        success = False
        try:
            for key, value in self.employeeInfo.items(): #key er key, value er listinn um employee
                teljari = teljari + 1
                if name is not None and id is not None:
                    if name in key and id in key:
                        success = True
                        print(value)
                    elif teljari == fjoldiStarfsmanna and success == False:
                        print("Error: id and name didn't match any key.")
                    else:
                        pass

                elif name in key and id is None:
                    if name in key:
                        print(value)
                        success = True
                    elif teljari == fjoldiStarfsmanna and success == False:
                        print("Error: name didn't match any key.")
                    else:
                        pass

                elif id in key and name is None:
                    if id in key:
                        print(value)
                        success = True
                    elif teljari == fjoldiStarfsmanna and success == False:
                        print("Error: id didn't match any key.")
                    else:
                        pass

                elif id not in key and name is None:
                    pass

                elif name not in key and id is None:
                    pass

        except NameError as error:
            print(error)

x = workplace()
x.create_employee("Daníel","Arnarsson","Forritari", 90000)
x.create_employee("Ragnar", "Jónsson", "UI Designer", 85000)
x.search_employee(id = 1, name ="Ragnar Jónsson")

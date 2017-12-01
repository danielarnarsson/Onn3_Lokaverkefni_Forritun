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
        id = len(self.employeeInfo) + 1
        nafnOgId = (nafn, id)
        self.employeeInfo[nafnOgId] = [id, fyrsta_nafn, sidasta_nafn, starfsgrein, laun]


    def search_employee(self, name=None, id=None):
        fjoldiStarfsmanna = len(self.employeeInfo)
        teljari = 0
        success = False
        try:
            for key, value in self.employeeInfo.items(): #key er key, value er listinn um employee
                teljari += 1
                if name is not None and id is not None:
                    if name in key and id in key:
                        x=0
                        for v in value:
                            x += 1
                            if x == 1:
                                print("Employee ID", str(v) + ":")
                            elif x == 2:
                                print(" First name: ", v)
                            elif x == 3:
                                print(" Last name:", v)
                            elif x == 4:
                                print(" Position:", v)
                            elif x == 5:
                                print(" Salary:", v)
                        success = True
                        print()

                    elif teljari == fjoldiStarfsmanna and success == False:
                        print("Error: id and name didn't match any key.")
                    else:
                        pass

                elif name in key and id is None:
                    if name in key:
                        x=0
                        for v in value:
                            x += 1
                            if x == 1:
                                print("Employee ID", str(v) + ":")
                            elif x == 2:
                                print(" First name: ", v)
                            elif x == 3:
                                print(" Last name:", v)
                            elif x == 4:
                                print(" Position:", v)
                            elif x == 5:
                                print(" Salary:", v)
                        success = True
                        print()

                    elif teljari == fjoldiStarfsmanna and success == False:
                        print("Error: name didn't match any key.")
                    else:
                        pass

                elif id in key and name is None:
                    if id in key:
                        x=0
                        for v in value:
                            x += 1
                            if x == 1:
                                print("Employee ID", str(v) + ":")
                            elif x == 2:
                                print(" First name: ", v)
                            elif x == 3:
                                print(" Last name:", v)
                            elif x == 4:
                                print(" Position:", v)
                            elif x == 5:
                                print(" Salary:", v)
                        success = True
                        print()

                    elif teljari == fjoldiStarfsmanna and success == False:
                        print("Error: id didn't match any key.")
                    else:
                        pass

                elif id not in key and name is None:
                    if teljari == fjoldiStarfsmanna:
                        print("ID not in any key")
                        print()

                elif name not in key and id is None:
                    if teljari == fjoldiStarfsmanna:
                        print("Name not in any key")
                        print()

        except NameError as error:
            print(error)

    def delete_employee(self, name=None, id=None):
        fjoldiStarfsmanna = len(self.employeeInfo)
        teljari = 0
        success = False
        try:
            for key, value in list(self.employeeInfo.items()):
                teljari += 1
                if name is not None and id is not None:
                    if name in key and id in key:
                        del self.employeeInfo[key]
                        print("Employee deleted.")
                        success = True
                    elif teljari == fjoldiStarfsmanna and success == False:
                        print("Error: id and name didn't match any key.")

                elif name in key and id is None:
                    del self.employeeInfo[key]
                    if teljari  == 1:
                        print(teljari, "employee deleted.")
                        print()
                    elif teljari > 1:
                        print(teljari, "employees deleted.")

                elif id in key and name is None:
                    del self.employeeInfo[key]
                    print("Employee deleted")

                elif id not in key and name is None:
                    if teljari == fjoldiStarfsmanna:
                        print("ID not in any key")

                elif name not in key and id is None:
                    if teljari == fjoldiStarfsmanna:
                        print("Name not in any key")

        except NameError as error:
            print(error)
        print()

    def print_employees(self):
        for key, value in self.employeeInfo.items():
            x = 0
            for v in value:
                x += 1
                if x == 1:
                    print("Employee ID", str(v) + ":")
                elif x == 2:
                    print(" First name: ", v)
                elif x == 3:
                    print(" Last name:", v)
                elif x == 4:
                    print(" Position:", v)
                elif x == 5:
                    print(" Salary:", v)
            print()

    def change_salary(self, id, salary=None, percentage=None):

        try:
            pass
        except Exception as e:
            print(e)

    def change_employee(self, id, id_change=None, fyrsta_nafn_change=None, sidasta_nafn_change=None, starfsgrein_change=None, laun=None):
        employeeInfo = self.employeeInfo
        for key, value in employeeInfo.items():
            x = 0
            if id == key[1]:
                if id_change is not None:
                    if key[1] == id_change:
                        print("Error: ID already exists")
                        print()
                    else:
                        listi = list(key)
                        listi[1] = id_change
                        del employeeInfo[key]
                        key = tuple(listi)
                        value[0] = id_change
                        employeeInfo[key] = value
                        print()

            else:
                if x == len(employeeInfo):
                    print("Error: input id does not match id in any key")
        self.employeeInfo = employeeInfo
        print()


x = workplace()
x.create_employee("Daníel","Arnarsson","Forritari", 90000)
x.create_employee("Ragnar", "Jónsson", "UI Designer", 85000)
x.create_employee("Ragnar", "Jónsson", "UI Designer", 85000)
x.create_employee("Sigurður", "andrason","HalloHallo",44444)
x.search_employee(id = 2, name = "Ragnar Jónsson")
x.delete_employee(id = 3, name = "Ragnar Jónsson")
x.change_employee(id = 1, id_change = 5)
x.print_employees()
x.search_employee(id = 5)
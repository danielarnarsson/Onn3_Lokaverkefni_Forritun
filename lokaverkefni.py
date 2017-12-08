#Daníel Arnarsson
#22.11.2017

class workplace:
    """A class that includes functions for storing, creating, searching, modifying, and deleting information about employees within a single company."""

    def __init__(self):
        employeeInfo = {}
        self.employeeInfo = employeeInfo

    def create_employee(self, fyrsta_nafn, sidasta_nafn, starfsgrein, laun):
        """Function for creating an employee."""
        nafn = str(fyrsta_nafn + " " + sidasta_nafn)
        id = len(self.employeeInfo) + 1
        nafnOgId = (nafn, id)
        self.employeeInfo[nafnOgId] = [id, fyrsta_nafn, sidasta_nafn, starfsgrein, laun]


    def search_employee(self, name=None, id=None):
        """Function for searching for an employee/employees."""
        print("-----Search employee------")
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
        """Function for deleting an employee/employees."""
        print("-----Delete employee------")
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
        """Function to print all employees."""
        print("-----Print employees------")
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

    def change_employee(self, id, id_change=None, fyrsta_nafn_change=None, sidasta_nafn_change=None, starfsgrein_change=None, laun_change=None):
        """Function for modifying an employees information."""
        print("-----Change employee------")
        try:
            employeeInfo = self.employeeInfo
            success = False
            stop = False
            x=0
            for key, value in employeeInfo.items():
                x = x + 1
                if id == key[1]:
                    if id_change is not None:
                        for key, value in employeeInfo.items():
                            if key[1] == id_change and key[1] == id:
                                print("Error: id_change is same as id. All changes canceled.")
                                stop = True

                            elif key[1] == id_change and key[1] != id:
                                print("Error: id already exists. All changes canceled.")
                                stop = True

                    if stop is False:
                        if id_change is not None:
                            listi = list(key)
                            listi[1] = id_change
                            del employeeInfo[key]
                            keyChange = tuple(listi)
                            value[0] = id_change
                            employeeInfo[keyChange] = value

                        if fyrsta_nafn_change is not None:
                            value[1] = fyrsta_nafn_change
                            listi = list(key)
                            listi[0] = value[1] + " " + value[2]
                            del employeeInfo[key]
                            keyChange = tuple(listi)
                            employeeInfo[keyChange] = value
                            success = True

                        if sidasta_nafn_change is not None:
                            value[2] = sidasta_nafn_change
                            listi = list(key)
                            key = value[1] + " " + value[2]
                            del employeeInfo[key]
                            keyChange = tuple(listi)
                            employeeInfo[keyChange] = value
                            success = True

                        if starfsgrein_change is not None:
                            value[3] = starfsgrein_change
                            success = True

                        if laun_change is not None:
                            value[4] = laun_change
                            success = True

                    elif x == len(employeeInfo) and success is False and stop is False:
                        print("Error: input id does not match any id")
            print()
        except Exception as e:
            print("EXCEPTION", e)
            print("PROBABLY THIS BUG: if more than one argument that changes the key of an employee is passed into the function it won't work")


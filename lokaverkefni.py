#Daníel Arnarsson
#22.11.2017
import collections
#workplace
#make input values input("")?


class workplace:
    def __init__(self):
        employeeInfo = collections.OrderedDict()
        self.employeeInfo = employeeInfo


    def create_employee(self, fyrsta_nafn, sidasta_nafn, starfsgrein, laun):
        nafn = str(fyrsta_nafn + " " + sidasta_nafn)
        id = len(self.employeeInfo) + 1
        nafnOgId = (nafn, id)
        employee = collections.OrderedDict()
        employeeAttributes = collections.OrderedDict({"id": id, "fyrsta nafn": fyrsta_nafn, "sidasta nafn": sidasta_nafn, "starfsgrein": starfsgrein, "laun": laun})
        employee.update({nafnOgId:employeeAttributes})
        self.employeeInfo.update(employee)


    def search_employee(self, name=None, id=None):
        fjoldiStarfsmanna = len(self.employeeInfo)
        employeeInfo = self.employeeInfo
        teljari = 0
        success = False
        try:
            for key, value in employeeInfo.items():
                if name is not None and id is None:
                    if name in key:
                        for v, k in value.items():
                            teljari += 1
                            if teljari == 1:
                                employeeid = value.get("id")
                                print("Employee ID:", employeeid)
                            else:
                                print(" ", v + ":", k)
                    else:
                        print("Name not in key")

                elif name is None and id is not None:
                    if id in key:
                        for v, k in value.items():
                            teljari += 1
                            if teljari == 1:
                                employeeid = value.get("id")
                                print("Employee ID:", employeeid)
                            else:
                                print(" ", v + ":", k)
                    else:
                        print("ID not in any key")

                elif name is not None and id is not None:
                    if name in key and id in key:
                        for v,k in value.items():
                            teljari += 1
                            if teljari == 1:
                                employeeid = value.get("id")
                                print("Employee ID:", employeeid)
                            else:
                                print(" ", v + ":", k)
                    else:
                        print("name and ID did not match any key")

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
        teljari = 0
        for key, value in self.employeeInfo.items():
            for v, k in value.items():
                print(" ", v + ":", k)


    def change_salary(self, id, salary=None, percentage=None):

        try:
            pass
        except Exception as e:
            print(e)

    def change_employee(self, id, id_change=None, fyrsta_nafn_change=None, sidasta_nafn_change=None, starfsgrein_change=None, change_laun=None):
        print()

x = workplace()
x.create_employee("Daníel","Arnarsson","Forritari", 90000)
x.create_employee("Ragnar", "Jónsson", "UI Designer", 85000)
x.create_employee("Ragnar", "Jónsson", "UI Designer", 85000)
x.create_employee("Sigurður", "andrason","HalloHallo",44444)
x.print_employees()
print(x.employeeInfo)
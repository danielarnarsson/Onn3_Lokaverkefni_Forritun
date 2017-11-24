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

    def search_employee(self, **kwargs):
        employeeInfo = self.employeeInfo
        print(kwargs.items())
        print("Name in kwargs")
        teljari=0
        for keykw, valuekw in kwargs.items():
            if keykw == "name" or keykw == "id":
                for key, value in employeeInfo.items():
                    for k in key:
                        if valuekw == k:
                            teljari=teljari+1
                            if teljari == len(kwargs.items()):
                                print(value)


x = workplace()
x.create_employee("Daníel","Arnarsson","Forritari", 90000)
x.create_employee("Ragnar", "Jónsson", "UI Designer", 85000)
x.search_employee(name = "Daníel Arnarsson")






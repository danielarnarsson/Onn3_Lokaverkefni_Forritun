#Daníel Arnarsson
#22.11.2017

class workplace:
    """A class that includes functions for storing, creating, searching, modifying, and deleting information about employees within a single company."""




    def __init__(self):
        """Constructor that creates a dictionary that will store all employees"""
        employeeInfo = {}
        self.employeeInfo = employeeInfo




    def create_employee(self, fyrsta_nafn, sidasta_nafn, starfsgrein, laun,id=None):
        """Function for creating an employee."""
        print("-----Create employee-----")
        nafn = str(fyrsta_nafn + " " + sidasta_nafn)
        if id is None:
            try:
                largest = max([key[1] for key, value in self.employeeInfo])
                id = largest + 1


            except ValueError:
                id = len(self.employeeInfo) + 1


            except TypeError:
                id = len(self.employeeInfo) + 1

            print("Successfully created employee with ID '" + str(id) + "' and full name '" + nafn + "'")

        else:
            print("Successfully created employee with ID '" + str(id) + "' and full name '" + nafn + "'")
            if isinstance(id, int):
                pass
            else:
                print("WARNING: all id's should be integers for auto incrementation to work well.")

        nafnOgId = (nafn, id)
        self.employeeInfo[nafnOgId] = [id, fyrsta_nafn, sidasta_nafn, starfsgrein, laun]
        print()





    def search_employee(self, name=None, id=None):
        """Function for searching for an employee/employees."""
        print("-----Search employee-----")
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



                elif name in key and id is None:
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



                elif id in key and name is None:
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


            if success == False:
                print("Error: employee not found.")
            print()


        except NameError as error:
            print(error)




    def delete_employee(self, name=None, id=None):
        """Function for deleting an employee/employees."""
        print("-----Delete employee-----")
        fjoldiStarfsmanna = len(self.employeeInfo)
        teljari = 0
        success = False
        try:
            for key, value in list(self.employeeInfo.items()):

                if name is not None and id is not None:

                    if name in key and id in key:
                        del self.employeeInfo[key]
                        print("Employee deleted.")
                        success = True


                elif name in key and id is None:
                    teljari += 1
                    del self.employeeInfo[key]
                    success = True


                elif id in key and name is None:
                    del self.employeeInfo[key]
                    print("Employee deleted")
                    success = True

            if teljari == 1:
                print(teljari, "employee deleted.")
                print()

            elif teljari > 1:
                print(teljari, "employees deleted.")

            if success is False:
                print("Error: no employees found.")

        except NameError as error:
            print(error)
        print()




    def print_employees(self):
        """Function to print all employees."""
        print("-----Print employees-----")
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
        """Function for modifying an employee's information."""
        print("-----Change employee-----")
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
                            print("ID for employee with id", key[1], "changed to: ", id_change)


                        if fyrsta_nafn_change is not None:
                            value[1] = fyrsta_nafn_change
                            listi = list(key)
                            listi[0] = value[1] + " " + value[2]
                            del employeeInfo[key]
                            keyChange = tuple(listi)
                            employeeInfo[keyChange] = value
                            success = True
                            print("First name for employee with id", key[1], "changed to: ", fyrsta_nafn_change)


                        if sidasta_nafn_change is not None:
                            value[2] = sidasta_nafn_change
                            listi = list(key)
                            key = value[1] + " " + value[2]
                            del employeeInfo[key]
                            keyChange = tuple(listi)
                            employeeInfo[keyChange] = value
                            success = True
                            print("Final name for employee with id",key[1], "changed to: ", sidasta_nafn_change)

                        if starfsgrein_change is not None:
                            value[3] = starfsgrein_change
                            success = True
                            print("starfsgrein for employee with id",key[1], "changed to: ", starfsgrein_change)


                        if laun_change is not None:
                            value[4] = laun_change
                            success = True
                            print("Laun for employee with id", key[1], "changed to:", laun_change)

                        if id_change is None and fyrsta_nafn_change is None and sidasta_nafn_change is None and starfsgrein_change is None and laun_change is None:
                            print("Error: no modification arguments were specified.")

                    elif x == len(employeeInfo) and success is False and stop is False:
                        print("Error: input id does not match any id")


        except Exception as e:
            print("EXCEPTION:", e)
            print("PROBABLY THIS BUG: if  id_change, first name and/or last name are changed at once it will act weird.")
        print()



#Forritið virkar best ef id eru bara integer
print("\n\n____________PARTUR 1____________\n")
braudsmidjan = workplace()
braudsmidjan.create_employee("Daníel", "Arnarsson", "Forritari", 500000) #Bý til starfsmann sem heitir fyrsta nafnið "Daníel", annað nafn "Arnarsson" með starfsgrein "Forritari" og laun 500000
braudsmidjan.create_employee("Daníel", "Arnarsson", "Forritari", 500000) # id er sett sjálfkrafa ef þú skilgreinir það ekki og fer þá eftir hvað hæsta id er + 1  o.fl.
braudsmidjan.create_employee("Telma", "Árnadóttir", "Markaðssetning", 750000, 10) #id = 10
#braudsmidjan.create_employee("Ragnar", "Sigfusson", 560000) Verður að fylla allt út (fyrir utan id) annars kemur typeError
braudsmidjan.create_employee("Rósa", "Bjarnadóttir", "Gagnagrunns hönnuður", 560000, "Hallo") #id = "Hallo". Output er WARNING sem segir...
braudsmidjan.create_employee("Konráð", "Guðmundsson", "Forritari", 9999999999999999999999999999999999) #Bý til starfsmann
braudsmidjan.print_employees() #Prentar út alla starfsmenn
print("\n\n\n____________PARTUR 2____________\n")
braudsmidjan.search_employee(id = 1) #Prentar út starfsmann með id = 1
braudsmidjan.search_employee(id = "Hallo") #Prentar út starfsmann með id = "Hallo"
braudsmidjan.search_employee(name = "Daníel Arnarsson") #Prentar út alla sem hafa fullt nafn "Daníel Arnarsson"
braudsmidjan.change_employee(id = 5, id_change = 500) #Virkar
braudsmidjan.search_employee(id = 500) #Prentar út starfsmann með id = 500
braudsmidjan.change_employee(id = 1, id_change = 1, fyrsta_nafn_change="Flosi", laun_change=462624624246) #Ef id_change er hið sama og id þá er hætt við allar breytingar.
braudsmidjan.change_employee(id = 1, id_change = 2, fyrsta_nafn_change="Flosi", laun_change=462624624246) #Ef id_change er núþegar til á öðrum starfsmanni, þá er líka hætt við allar breytingar.
braudsmidjan.search_employee(id = 1) #ekkert hefur breyst
print("\n\n\n____________PARTUR 3____________\n")
braudsmidjan.create_employee("Andrés", "Önd", "staða 1", 400000, 5000) #Bý til starfsmann með id 5000
braudsmidjan.create_employee("Andrés", "Önd", "staða 2", 450000, 6000) #Bý til starfsmann með id 6000
braudsmidjan.create_employee("Andrés", "Önd", "staða 3", 550000, 7000) #Bý til starfsmann með id 7000
braudsmidjan.search_employee("Andrés Önd") #Leitar af starfsmönnum sem heita fullu nafni Andrés Önd
braudsmidjan.delete_employee(id = 5) #Gerði if statement fyrir þegar id er ekki til
braudsmidjan.delete_employee(id = 5000) #Eyðir starfsmanni með id 5000
braudsmidjan.search_employee(id = 5000) #Error: no employees found.
braudsmidjan.delete_employee(name="Andrés Önd") #Eyðir öllum sem heita andrés önd
braudsmidjan.search_employee(name="Andrés Önd") #Error: no employees found.
print("\n\n\n____________PARTUR 4____________\n")
braudsmidjan.change_employee(id = 1) # bjó til if villumeldingu fyrir þetta (output: Error: no modification arguments were specified.)
braudsmidjan.change_employee(id = 1, fyrsta_nafn_change = "Danni") #Virkar en prentar út staðfestinguna of oft
braudsmidjan.search_employee(id = 1) #prentar út starfsmann með id = 1
braudsmidjan.change_employee(id = 10, fyrsta_nafn_change = "Tanja", sidasta_nafn_change="Magnúsdóttir") #virkar en kemur samt villumelding (sem er ekki gott) (output: PROBABLY THIS BUG: ...)
braudsmidjan.search_employee(id = 10) #prentar út starfsmann með id = 10
braudsmidjan.change_employee(id = 10, id_change = 40, sidasta_nafn_change="Ásgeirsdóttir") #virkar en kemur samt villumelding (sem er ekki gott) (output: PROBABLY THIS BUG: ...)
braudsmidjan.search_employee(id = 40) #prentar út starfsmann með id = 40
braudsmidjan.change_employee(id = 40, id_change = 50, fyrsta_nafn_change="Svandís", sidasta_nafn_change="Friðriksdóttir") #Virkar að hluta til, fyrsta nafnið breytist en ekki síðasta. (output: PROBABLY THIS BUG: ...)
braudsmidjan.search_employee(id = 50)
braudsmidjan.print_employees() #prentar út alla starfsmenn
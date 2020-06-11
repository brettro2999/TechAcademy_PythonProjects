
#Protected encapsulation
class Prot:
    def __init__(self):
        self._pyProt = "This string uses encapsulation."

Encap1 = Prot()
Encap1._pyProt = "Encapsulation."
print(Encap1._pyProt)

#Private encapsulation
class Priv:
    def __init__(self):
        self.__pyPriv = "Private Encap"

    def showString(self):
        print(self.__pyPriv)

    def changeString(self, private):
        self.__pyPriv = private

Encap2 = Priv()
Encap2.showString()
Encap2.changeString("The change.")
Encap2.showString()

    

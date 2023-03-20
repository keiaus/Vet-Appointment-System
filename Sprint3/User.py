class User:
    
    #private
    __userID 
    __userLoginID
    __userUserName
    __userPW
    __userFirst
    __userLast
    __userPhone
    __userEmail
    __userStreet
    __userCity
    __userState
    __userZip


    #public
 

    #setters
    def setUID(self, setuID):
        self.__userID = setuID

    def setULoginID(self, setuLoginID):
        self.__userLoginID = setuLoginID

    def setUUserName(self, setuName):
        self.__userUserName = setuName

    def setUPW(self, setuPW):
        self.__userPW = setuPW

    def setUFirst(self, setuFirst):
        self.__userFirst = setuFirst

    def setULast(self, setuLast):
        self.__userLast = setuLast

    def setUPhone(self, setuPhone):
        self.__userPhone = setuPhone

    def setUEmail(self, setuEmail):
        self.__userEmail = setuEmail

    def setUStreet(self, setuStreet):
        self.__userStreet = setuStreet

    def setUCity(self, setuCity):
        self.__userCity = setuCity

    def setUState(self, setuState):
        self.__userState = setuID

    def setUZip(self, setuZip):
        self.__userZip = setuID

    #getters
    def getUID(self):
        return self.__userID

    def getULoginID(self):
        return self.__userLoginID

    def getUName(self):
        return self.__userUserName

    def getUPW(self):
        return self.__userPW

    def getUFirst(self):
        return self.__userFirst

    def getULast(self):
        return self.__userLast
  
    def getUPhone(self):
        return self.__userPhone

    def getUEmail(self):
        return self.__userEmail

    def getUStreet(self):
        return self.__userStreet

    def getUCity(self):
        return self.__userCity

    def getUState(self):
        return self.__userState

    def getUZip(self):
        return self.__userZip

    #constructor

    def __init__(self, uID, uLID, uUname, uPW, uFName, uLName, uPNum, uEmail, uStreet, uCity, uState, uZip):
        self.setUID(uID)
        self.setULoginID(uLID)
        self.setUUserName(uUname)
        self.setUPW(uPW)
        self.setUFirst(uFName)
        self.setULast(uLName)
        self.setUPhone(uPNum)
        self.setUEmail(uEmail)
        self.setUStreet(uStreet)
        self.setUCity(uCity)
        self.setUState(uState)
        self.setUZip(uZip)


    #copy constructors
    def shallowC(self,theCopy):
        self.copy(theCopy)

    def deepC(self,thedCopy):
        self.deepcopy(theDcopy)


    #deconstructor
    def __del__(self):
        print("deleted self")







# Developed by: Maya Lekhi
# Date: Apr 10, 2023
# Inputs: airport code, airport city, airport country, airport continent

class Airport:

    # initializing the instance variables based on constructor parameters
    def __init__(self, code, city, country, continent):
        self._code = code
        self._city = city
        self._country = country
        self._continent = continent

    # returning airport representation
    def __repr__(self):
        return f"{self._code} ({self._city}, {self._country})"

    # returns airport code
    def getCode(self):
        return self._code

    # returns airport city
    def getCity(self):
        return self._city

    # returns airport country
    def getCountry(self):
        return self._country

    # returns airport continent
    def getContinent(self):
        return self._continent

    # updates airport city
    def setCity(self, city):
        self._city = city

    # updates airport country
    def setCountry(self,country):
        self._country = country

    # updates airport continent
    def setContinent(self,continent):
        self._continent = continent

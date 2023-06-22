from Flight import *
from Airport import *

class Aviation:
    # initializing the instance variables based on constructor parameters
    def __init__(self):
        # setting the variables to dictionaries
        self._allAirports = {}
        self._allFlights = {}
        self._allCountries = {}

    # returns all airports
    def getAllAirports(self):
        return self._allAirports

    # returns all flights
    def getAllFlights(self):
        return self._allFlights

    # returns all cities
    def getAllCountries(self):
        return self._allCountries

    # updates all airports
    def setAllAirports(self,_allAirports):
        self._allAirports = _allAirports

    # updates all flights
    def setAllFlights(self,_allFlights):
        self._allFlights = _allFlights

    # updates all countries
    def setAllCountries(self,_allCountries):
        self._allCountries = _allCountries

    # introducing a static method to make cleaning up the lines easier when the data is loaded
    @staticmethod
    def clean(lines):
        # making it so that the function splits the information in each line into its individual entries and cleaning up the whitespace around each
        return [list(map(str.strip, line.split(","))) for line in lines]

    # reads and extracts all data in the country file to add to the dictionaries defined in the initializing function
    def loadData(self, airportFile, flightFile, countriesFile):
        # try block so that if exceptions arise, false is returned
        try:
            countriesFile = open(countriesFile, "r", encoding='utf8')
            # opening countries file
            with countriesFile:
                # reading and cleaning up the file lines
                lines = countriesFile.readlines()
                lines = Aviation.clean(lines)
                # iterating through the lines in the file to extract country and continent data
                for line in lines:
                    [country, continent] = line
                    # adding continent data to the _allCountries dictionary with the country as the key
                    self._allCountries[country] = continent

            airportFile = open(airportFile, "r", encoding='utf8')
            # opening airport file
            with airportFile:
                # reading and cleaning up the file lines
                lines = airportFile.readlines()
                lines = Aviation.clean(lines)
                # iterating through the lines in the file to extract airport code, country and city data
                for line in lines:
                    [code,country,city] = line
                    # extracting continent for respective countries using the self._allCountries list created prior
                    continent = self._allCountries[country]
                    # making the information airport objects
                    airport = Airport(code,city,country,continent)
                    # adding airport data to the _allAirports dictionary with the airport code as the key
                    self._allAirports[code]= airport

            flightFile = open(flightFile, "r", encoding='utf8')
            # opening flight file
            with flightFile:
                # reading and cleaning up the file lines
                lines = flightFile.readlines()
                lines = Aviation.clean(lines)
                # iterating through the lines in the file to extract flight number, origin and destination
                for line in lines:
                    [flightNo, origin, destination] = line
                    # matching origin and destination airport to the corresponding code in the _allAirports dictionary
                    origin = self._allAirports[origin]
                    destination = self._allAirports[destination]
                    # making the information flight objects
                    newFlight = Flight(flightNo, origin, destination)
                    # creating a new list only if the origin code is not an existing key in the dictionary
                    if origin.getCode() not in self._allFlights:
                        self._allFlights[origin.getCode()] = []
                    # checking for duplicates and if not, adding flight data to the _allFlights dictionary with the origin airport code as the key
                    if not any(flight.getFlightNumber() == flightNo for flight in self._allFlights[origin.getCode()]):
                        self._allFlights[origin.getCode()].append(newFlight)
            return True
        # false is returned if exceptions arise when loading the data from the file
        except:
            return False

    # returns airport data based on given code
    def getAirportByCode(self, code):
        # try block so that if exceptions arise, -1 is returned
        try:
            return self._allAirports[code]
        # false is returned if exceptions like the given code being invalid arise
        except:
            return -1

    # returns all flights coming from or headed to a given city
    def findAllCityFlights(self, city):
        # creating an empty list of matching city flights to add to
        cityFlights = []
        # iterating through the _allFlights dictionary
        for x in self._allFlights:
            for entries in self._allFlights[x]:
                x = 0
                # examining each origin and destination and see if the origin or destination matches the given city
                if entries.getOrigin().getCity() == city or entries.getDestination().getCity() == city:
                    x += 1
                    # appending the flight information to the cityFlights list if the origin or destination matches the given city
                    cityFlights.append(entries)
        return cityFlights

    # returns the flight matching a given flight number
    def findFlightByNo(self,flightNo):
        # try block so that if exceptions arise, -1 is returned
        try:
            # iterating through the _allFlights dictionary
            for origin in self._allFlights:
                for flight in self._allFlights[origin]:
                    # examining a flight number in the list matches the given flight number and returning the flight information if so
                    if flight.getFlightNumber() == flightNo:
                        return flight
        # false is returned if exceptions like the given number being invalid arise
        except:
            return -1

    # returns all flights coming from or headed to a given country
    def findAllCountryFlights(self, country):
        # creating an empty list of matching country flights to add to
        countryFlights = []
        # iterating through the _allFlights dictionary
        for x in self._allFlights:
            for entries in self._allFlights[x]:
                x = 0
                # examining each origin and destination and see if the origin or destination matches the given country
                if entries.getOrigin().getCountry() == country or entries.getDestination().getCountry() == country:
                    x += 1
                    # appending the flight information to the countryFlights list if the origin or destination matches the given country
                    countryFlights.append(entries)
        return countryFlights

    # returns flight info if there are direct or layover flights between a given origin and destination
    def findFlightBetween(self, origAirport, destAirport):
        # creating a variable to check if direct flights exist
        directFlight = False

        # iterating through the _allFlights dictionary for origin airports that match the given origin
        for flight in self._allFlights.get(origAirport.getCode(), []):
            # checking if the destination code is the same as the given destination code
            if flight.getDestination().getCode() == destAirport.getCode():
                # setting directFlight to true so that it just outputs the direct flight
                directFlight = True
                # returning the formatted direct flight information
                return f"Direct Flight({flight._flightNo}): {origAirport.getCode()} to {destAirport.getCode()}"

        # looking for single-hop connecting flight if there are no direct flights
        if not directFlight:
            # creating a connections set to store all possible airport codes that could be connecting airports between the origin and destination
            connections = set()
            # iterating through the _allFlights dictionary for origin airports that match the given origin
            for flight in self._allFlights.get(origAirport.getCode(), []):
                # iterating through the _allFlights dictionary for origin airports that match the given destination
                for secondFlight in self._allFlights.get(flight.getDestination().getCode(), []):
                    # checking if the origin of the second flight matches the destination of the first flight
                    if secondFlight.getDestination().getCode() == destAirport.getCode():
                        # adding the flight code to the connections set
                        connections.add(flight.getDestination().getCode())
            # checking if there are connections in the set and returning those should there be connections
            if connections:
                return connections
            # returning -1 if there are no direct flight or single-hop connecting flights from the given origin to the given destination
            else:
                return -1

    # returns a returning flight for the given flight
    def findReturnFlight(self, firstFlight):
        # finds the destination and origin codes of the given flight
        firstDestination = firstFlight.getDestination().getCode()
        firstOrigin = firstFlight.getOrigin().getCode()
        # setting returnInfo and returnFlight variables to store return flight details
        returnInfo = None
        returnFlightExists = False
        # iterating through the _allFlights dictionary
        for entry in self._allFlights:
            for i in range(len(self._allFlights[entry])):
                # checking if any entries in the _allFlights dictionary has an origin matching the given destination and a destination matching the given origin
                if self._allFlights[entry][i].getOrigin().getCode() == firstDestination and self._allFlights[entry][
                    i].getDestination().getCode() == firstOrigin:
                    # adding the return flight information to returnInfo and indicating that return flights exist
                    returnInfo = self._allFlights[entry][i]
                    returnFlightExists = True
        # checking if there are return flights and returning their info if so
        if returnFlightExists:
            return returnInfo
        # returning -1 if there are no matching return flights
        else:
            return -1

    # returns flights that cross a given ocean
    def findFlightsAcross(self, ocean):
        # indicating the 3 zones and the continents within them
        green = {"North America", "South America"}
        red = {"Asia", "Australia"}
        blue = {"Europe", "Africa"}
        # defining the atlantic and pacific oceans based on what zones are crossed
        oceans = {'Atlantic': (blue, green), 'Pacific': (green, red)}

        # creating an empty set to store flights that cross a given ocean
        crossingFlights = set()
        # iterating through _allFlights dictionary
        for x in self._allFlights:
            for entries in self._allFlights[x]:
                # creating originZone and destinationZone variables to be filled later
                originZone, destinationZone = None, None
                # getting the continent for each origin and destination
                originContinent = entries.getOrigin().getContinent()
                destinationContinent = entries.getDestination().getContinent()
                # matching the origin and destination continents to a zone
                for zone in oceans[ocean]:
                    if originContinent in zone:
                        originZone = zone
                    if destinationContinent in zone:
                        destinationZone = zone
                # adding a flight to the crossingFlights set if the origin and destination zones cross the given ocean
                if originZone != destinationZone:
                    if originZone and destinationZone:
                        crossingFlights.add(entries._flightNo)
        # checking if there are flights that cross the given ocean and returning their info if so
        if crossingFlights:
            return crossingFlights
        # returning -1 if there is no flights crossing a given ocean
        else:
            return -1

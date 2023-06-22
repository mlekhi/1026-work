# Developed by: Maya Lekhi
# Date: Apr 10, 2023
# Inputs: flight number, flight origin airport, flight destination airport

from Airport import *

class Flight:
    # initializing the instance variables based on constructor parameters
    def __init__(self, flightNo, origAirport, destAirport):
        # checking if flight number is a string of 6-character code containing 3 letters followed by 3 digits; raising a TypeError if not
        if len(flightNo) == 6 and flightNo[:3].isalpha() and flightNo[3:].isdigit():
            # checking if origAirport and destAirport are Airport objects; raising a TypeError if not
            if isinstance(origAirport, Airport) and isinstance(destAirport,Airport):
                self._flightNo = flightNo
                self._origin = origAirport
                self._destination = destAirport
            else:
                raise TypeError("The origin and destination must be Airport objects")
        else:
            raise TypeError("The flight number format is incorrect")

    # returning flight representation
    def __repr__(self):
        flightType = None
        # checking if the flight country equals destination country
        if self.isDomesticFlight() == True:
            # marking the flight as domestic if the countries match
            flightType = 'domestic'
        elif self.isDomesticFlight() == False:
            # marking the flight as international if the countries don't match
            flightType = 'international'
        return f"Flight({self._flightNo}): {self._origin._city} -> {self._destination._city} [{flightType}]"

    # checking if the flight objects are equal
    def __eq__(self, other):
        # checking if self and other flights are the same flight
        if isinstance(other,Flight):
            # checking if origin and destination are the same for both flights
            if self._origin == other._origin and self._destination == other._destination:
                return True
            # returning false if the origin and destination are different between both flights
            else:
                return False
        # returning false if other isn't the same flight
        else:
            return False

    # returns flight number
    def getFlightNumber(self):
        return self._flightNo

    # returns flight origin
    def getOrigin(self):
        return self._origin

    # returns flight destination
    def getDestination(self):
        return self._destination

    # function that returns true if flight is domestic; false if international
    def isDomesticFlight(self):
        if self._origin._country == self._destination._country:
            return True
        else:
            return False

    # updates flight origin
    def setOrigin(self, origin):
        self._origin = origin

    # updates flight destination
    def setDestination(self, destination):
        self._destination = destination
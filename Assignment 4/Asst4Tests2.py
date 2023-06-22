from Aviation import *

avi = Aviation()

flightsFileName = "flights.txt"

def equals (expected, student):
    expected = expected.replace(" ", "")
    expected = expected.replace("\t", "")
    expected = expected.lower()
    student = student.replace(" ", "")
    student = student.replace("\t", "")
    student = student.lower()
    return expected == student


print('--------------- Test 12 - findFlightsAcross() ---------------')
avi.loadData("airports.txt", flightsFileName, "countries.txt")
res=avi.findFlightsAcross('Pacific')
print(res)
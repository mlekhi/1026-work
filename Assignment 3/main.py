# Developed by: Maya Lekhi
# Date: Mar 27, 2023
# Desc: an information system for electronic medical records

from typing import List, Dict, Optional


# defining the function that will read patient information from the given text file
def readPatientsFromFile(fileName):
    """
    Reads patient data from a plaintext file.

    fileName: The name of the file to read patient data from.
    Returns a dictionary of patient IDs, where each patient has a list of visits.
    The dictionary has the following structure:
    {
        patientId (int): [
            [date (str), temperature (float), heart rate (int), respiratory rate (int), systolic blood pressure (int), diastolic blood pressure (int), oxygen saturation (int)],
            [date (str), temperature (float), heart rate (int), respiratory rate (int), systolic blood pressure (int), diastolic blood pressure (int), oxygen saturation (int)],
            ...
        ],
        patientId (int): [
            [date (str), temperature (float), heart rate (int), respiratory rate (int), systolic blood pressure (int), diastolic blood pressure (int), oxygen saturation (int)],
            ...
        ],
        ...
    }
    """

    # creating an empty dictionary that will be filled with the patient information upon reading the file
    patients = {}

    # quitting the program if file cannot be found
    try:

        # opening the file
        fileToRead = open(fileName, 'r')

        # reading the file to assign its data to the correct variables
        with fileToRead:

            # loop to go through each line of the file and split it to add the data to the dictionary
            for line in fileToRead:
                fields = line.strip().split(",")

                # printing error message if there are not 8 fields
                if len(fields) != 8:
                    print(f"Invalid number of fields ({len(fields)}) in line: {line}")
                    continue

                # converting and assigning the fields to their respective categories by using variables
                try:
                    patientId = int(fields[0])
                    date = fields[1]
                    temp = float(fields[2])
                    hr = int(fields[3])
                    rr = int(fields[4])
                    sbp = int(fields[5])
                    dbp = int(fields[6])
                    spo2 = int(fields[7])

                # error message if the data values are not in the correct format
                except ValueError:
                    print(f"Invalid data type in line: {line}")
                    continue

                # error message if temperature is not in correct range
                if not (42 >= temp >= 35):
                    print(f"Invalid temperature value ({temp}) in line: {line}")
                    continue

                # error message if heart rate is not in correct range
                if not (180 >= hr >= 30):
                    print(f"Invalid heart rate value ({hr}) in line: {line}")
                    continue

                # error message if respiratory rate is not in correct range
                if not (40 >= rr >= 5):
                    print(f"Invalid respiratory rate value ({rr}) in line: {line}")
                    continue

                # error message if systolic blood pressure is not in correct range
                if not (200 >= sbp >= 70):
                    print(f"Invalid systolic blood pressure value ({sbp}) in line: {line}")
                    continue

                # error message if diastolic blood pressure is not in correct range
                if not (120 >= dbp >= 40):
                    print(f"Invalid diastolic blood pressure value ({dbp}) in line: {line}")
                    continue

                # error message if oxygen saturation is not in correct range
                if not (100 >= spo2 >= 70):
                    print(f"Invalid oxygen saturation value ({spo2}) in line: {line}")
                    continue

                # create new key if patient id on the line is new
                if patientId not in patients:
                    patients[patientId] = []

                # adding the new patient data from the line as an entry to the dictionary
                patients[patientId].append([str(date), temp, hr, rr, sbp, dbp, spo2])

            return patients

    # error message if the given file is not found
    except FileNotFoundError:
        print(f"The file '{fileName}' could not be found.")
        exit()

# defining the function to display patient data
def displayPatientData(patients, patientId=0):
    """
    Displays patient data for a given patient ID.

    patients: A dictionary of patient dictionaries, where each patient has a list of visits.
    patientId: The ID of the patient to display data for. If 0, data for all patients will be displayed.
    """

    # if they want to see a specific patient's data (AKA when patientId is given and not 0)
    if patientId != 0:

        # testing if the patient ID the user inputted is invalid
        if patientId not in range(1, len(patients)+1):
            print(f"Patient with ID {patientId} not found.")

        # displaying the data of the patient matching the patient ID that was inputted
        else:
            patient = patients[patientId]

            # displaying the patient information if the patient ID is valid
            print(f"Patient ID: {patientId}")
            # iterating through all the visit information for that patient ID and printing
            for visit in patient:
                if isinstance(visit, int):
                    continue
                print(" Visit Date:", visit[0])
                print("  Temperature:", "%.2f" % visit[1], "C")
                print("  Heart rate:", visit[2], "bpm")
                print("  Respiratory rate:", visit[3], "bpm")
                print("  Systolic blood pressure:", visit[4], "mmHg")
                print("  Diastolic blood pressure:", visit[5], "mmHg")
                print("  Oxygen saturation:", visit[6], "%")

    # if they want to see all patient data (AKA when patientId is equal to 0)
    else:
        for patient_id, visits in patients.items():
            print(f"Patient ID: {patient_id}")
            # iterating through all the visit information for that patient ID and printing
            for visit in visits:
                print(" Visit Date:", visit[0])
                print("  Temperature:", "%.2f" % visit[1], "C")
                print("  Heart rate:", visit[2], "bpm")
                print("  Respiratory rate:", visit[3], "bpm")
                print("  Systolic blood pressure:", visit[4], "mmHg")
                print("  Diastolic blood pressure:", visit[5], "mmHg")
                print("  Oxygen saturation:", visit[6], "%")

    return


# defining the function to display patient stats
def displayStats(patients, patientId=0):
    """
    Prints the average of each vital sign for all patients or for the specified patient.

    patients: A dictionary of patient IDs, where each patient has a list of visits.
    patientId: The ID of the patient to display vital signs for. If 0, vital signs will be displayed for all patients.
    """

    # checking if patients parameter is a dictionary; prints error message if not
    if type(patients) is not dict:
        print("Error: 'patients' should be a dictionary.")
        return

    # checking if patient ID is an integer; prints patient stats if so
    try:
        # converting patient ID to an integer
        patientId = int(patientId)

        # calculating patient stats of all patients if patient ID is 0
        if patientId == 0:
            # making empty lists to store patient information for stats calculations
            visits = []
            for patient_visits in patients.values():
                visits += patient_visits
            temperatures = []
            heart_rates = []
            blood_pressures = []
            systolic_pressure = []
            diastolic_pressure = []
            oxygen_saturation = []

            # iterating through all the visit information and filling the lists with information from each patient
            for visit in visits:
                temperatures.append(visit[1])
                heart_rates.append(visit[2])
                blood_pressures.append(visit[3])
                systolic_pressure.append(visit[4])
                diastolic_pressure.append(visit[5])
                oxygen_saturation.append(visit[6])

            # calculating the average of each type of patient information to display as stats
            avg_temperature = sum(temperatures) / len(temperatures)
            avg_heart_rate = sum(heart_rates) / len(heart_rates)
            avg_blood_pressure = sum(blood_pressures) / len(blood_pressures)
            avg_systolic_pressure = sum(systolic_pressure) / len(systolic_pressure)
            avg_diastolic_pressure = sum(diastolic_pressure) / len(diastolic_pressure)
            avg_oxygen_saturation = sum(oxygen_saturation) / len(oxygen_saturation)

            # printing the vital signs calculated for all patients
            print("Vital Signs for All Patients:")
            print(" Average temperature:", "%.2f" % avg_temperature, "C")
            print(" Average heart rate:", "%.2f" % avg_heart_rate, "bpm")
            print(" Average respiratory rate:", "%.2f" % avg_blood_pressure, "bpm")
            print(" Average systolic blood pressure:", "%.2f" % avg_systolic_pressure, "mmHg")
            print(" Average diastolic blood pressure:", "%.2f" % avg_diastolic_pressure, "mmHg")
            print(" Average oxygen saturation:", "%.2f" % avg_oxygen_saturation, "%")
            return

        # checking if patient ID (not 0) corresponds to an existing patient ID
        elif patientId not in patients:
            print(f'No data found for patient with ID {patientId}.')

        # calculating patient stats for a given patient ID
        else:
            # making empty lists to store patient information for stats calculations
            visits = patients.get(patientId, [])
            temperatures = []
            heart_rates = []
            blood_pressures = []
            systolic_pressure = []
            diastolic_pressure = []
            oxygen_saturation = []

            # iterating through all the visit information and filling the lists with information from visits of that patient ID
            for visit in visits:
                temperatures.append(visit[1])
                heart_rates.append(visit[2])
                blood_pressures.append(visit[3])
                systolic_pressure.append(visit[4])
                diastolic_pressure.append(visit[5])
                oxygen_saturation.append(visit[6])

            # calculating the average of each type of patient information to display as stats
            avg_temperature = sum(temperatures) / len(temperatures)
            avg_heart_rate = sum(heart_rates) / len(heart_rates)
            avg_blood_pressure = sum(blood_pressures) / len(blood_pressures)
            avg_systolic_pressure = sum(systolic_pressure) / len(systolic_pressure)
            avg_diastolic_pressure = sum(diastolic_pressure) / len(diastolic_pressure)
            avg_oxygen_saturation = sum(oxygen_saturation) / len(oxygen_saturation)

            # printing the vital signs calculated for given patient ID
            print("Vital Signs for Patient", patientId, ":")
            print("  Average temperature:", "%.2f" % avg_temperature, "C")
            print("  Average heart rate:", "%.2f" % avg_heart_rate, "bpm")
            print("  Average respiratory rate:", "%.2f" % avg_blood_pressure, "bpm")
            print("  Average systolic blood pressure:", "%.2f" % avg_systolic_pressure, "mmHg")
            print("  Average diastolic blood pressure:", "%.2f" % avg_diastolic_pressure, "mmHg")
            print("  Average oxygen saturation:", "%.2f" % avg_oxygen_saturation, "%")
            return

    # checking if patient ID is an integer; prints error message if not
    except ValueError:
        print("Error: 'patientId' should be an integer.")
        return


# defining a function to add patient data 
def addPatientData(patients, patientId, date, temp, hr, rr, sbp, dbp, spo2, fileName):
    """
    Adds new patient data to the patient list.

    patients: The dictionary of patient IDs, where each patient has a list of visits, to add data to.
    patientId: The ID of the patient to add data for.
    date: The date of the patient visit in the format 'yyyy-mm-dd'.
    temp: The patient's body temperature.
    hr: The patient's heart rate.
    rr: The patient's respiratory rate.
    sbp: The patient's systolic blood pressure.
    dbp: The patient's diastolic blood pressure.
    spo2: The patient's oxygen saturation level.
    fileName: The name of the file to append new data to.
    """

    # checks if date is in the xxxx-xx-xx format
    if len(date) == 10 and date[4] == '-' and date[7] == '-':
        year = date[:4]
        month = date[5:7]
        day = date[8:]
        # checking if all the date entries are digits
        if year.isdigit() and month.isdigit() and day.isdigit():
            year = int(year)
            month = int(month)
            day = int(day)
    # prints error message if it does not follow the correct date format
    else:
        print("Invalid date format. Please enter date in the format 'yyyy-mm-dd'.")
        return

    # checks if date is valid; displays error message if invalid
    if month not in range(1, 13) or day not in range(1, 32) or year < 1900:
        print("Invalid date. Please enter a valid date.")
        return

    # checks if temperature is valid; displays error message if invalid
    if temp not in range(35, 43):
        print("Invalid temperature. Please enter a temperature between 35.0 and 42.0 Celsius.")
        return

    # checks if heart rate is valid; displays error message if invalid
    if hr not in range(30, 181):
        print("Invalid heart rate. Please enter a heart rate between 30 and 180 bpm.")
        return

    # checks if respiratory rate is valid; displays error message if invalid
    if rr not in range(5, 41):
        print("Invalid respiratory rate. Please enter a respiratory rate between 5 and 40 bpm.")
        return

    # checks if systolic blood pressure is valid; displays error message if invalid
    if sbp not in range(70, 201):
        print("Invalid systolic blood pressure. Please enter a systolic blood pressure between 70 and 200 mmHg.")
        return

    # checks if diastolic blood pressure is valid; displays error message if invalid
    if dbp not in range(40, 121):
        print("Invalid diastolic blood pressure. Please enter a diastolic blood pressure between 40 and 120 mmHg.")
        return

    # checks if oxygen saturation is valid; displays error message if invalid
    if spo2 not in range(70, 101):
        print("Invalid oxygen saturation. Please enter an oxygen saturation between 70 and 100%.")
        return

    # add new visit to list of visits under patient ID should patient; creates a new list in the patient dictionary should the patient ID be new
    if patientId not in patients:
        patients[patientId] = []
    patients[patientId].append([date, temp, hr, rr, sbp, dbp, spo2])

    # writes new patient information into the file
    try:
        with open(fileName, 'a') as f:
            f.write(f"\n{patientId},{date},{temp},{hr},{rr},{sbp},{dbp},{spo2}")

    # prints error message if there was a problem reading the file
    except:
        print("An unexpected error occurred while adding new data.")
        return

    print("Visit saved successfully for Patient #", patientId)


# defining a function that searches for existing patient visits based on year and month inputs
def findVisitsByDate(patients, year=None, month=None):
    """
    Find visits by year, month, or both.

    patients: A dictionary of patient IDs, where each patient has a list of visits.
    year: The year to filter by.
    month: The month to filter by.
    return: A list of tuples containing patient ID and visit that match the filter.
    """

    # creates empty list for visits that match the year and month input provided
    matchingVisits = []

    # case where the patient dictionary is empty; returns an empty list
    if not patients:
        return matchingVisits

    # case where the month or year is not valid; returns an empty list
    if (month is not None and month not in range(1, 13)) or (year < 1900 and year is not None):
        return matchingVisits

    # looping over the visits to find ones that match the year & month
    for patient_id, visits in patients.items():
        for visit in visits:

            # getting the year and month from the dates in the visits stored in the patients list
            givenYear = int(visit[0].split("-")[0])
            givenMonth = int(visit[0].split("-")[1])

            # if only year is provided, return all visits in that year
            if year is not None and givenYear == year and month is None:
                visit_info = [visit[0], float(visit[1]), int(visit[2]), int(visit[3]), int(visit[4]), int(visit[5]), int(visit[6])]
                matchingVisits.append((patient_id, visit_info))

            # if year and month are provided, return all visits in that month and year
            elif month is not None and givenMonth == month and year is None:
                visit_info = [visit[0], float(visit[1]), int(visit[2]), int(visit[3]), int(visit[4]), int(visit[5]), int(visit[6])]
                matchingVisits.append((patient_id, visit_info))

            # case when invalid year or month is provided; returns an empty list
            if year is not None and givenYear == year and month is not None and givenMonth == month:
                visit_info = [visit[0], float(visit[1]), int(visit[2]), int(visit[3]), int(visit[4]), int(visit[5]), int(visit[6])]
                matchingVisits.append((patient_id, visit_info))

    # returns the list of visits that match the year and month provided
    return matchingVisits


# defining a function that detects patients with abnormal vital signs for a follow up
def findPatientsWhoNeedFollowUp(patients):
    """
    Find patients who need follow-up visits based on abnormal vital signs.

    patients: A dictionary of patient IDs, where each patient has a list of visits.
    return: A list of patient IDs that need follow-up visits to to abnormal health stats.
    """

    # making an empty list to fill with the patients that need follow ups
    followup_patients = []

    # looping through the visits to check if the vital signs are in a normal range
    for patient_id, visits in patients.items():
        for visit in visits:

            # checking if systolic BP is in a normal range
            if int(visit[4]) > 140:
                if patient_id not in followup_patients:
                    followup_patients.append(patient_id)

            # checking if diastolic BP is in a normal range
            if int(visit[5]) > 90:
                if patient_id not in followup_patients:
                    followup_patients.append(patient_id)

            # checking if heart rate is in a normal range
            if 100 < int(visit[2]) or int(visit[2]) < 60:
                if patient_id not in followup_patients:
                    followup_patients.append(patient_id)

            # checking if oxygen saturation is in a normal range
            if int(visit[6]) < 90:
                if patient_id not in followup_patients:
                    followup_patients.append(patient_id)

    return followup_patients


# defining a function to delete all visits of a specified patient ID
def deleteAllVisitsOfPatient(patients, patientId, filename):
    """
    Delete all visits of a particular patient.

    patients: The dictionary of patient IDs, where each patient has a list of visits, to delete data from.
    patientId: The ID of the patient to delete data for.
    filename: The name of the file to save the updated patient data.
    return: None
    """

    # if the patient ID is not valid, indicates that nothing was found or deleted
    if patientId not in patients:
        print(f"No data found for patient with ID {patientId}")

    # creates a list of the visits that are not meant to be deleted
    else:
        visitsToSave = []
        for patient_id, visits in patients.items():
            # adding patient IDs that are not the one specified to delete to the remaining visits list
            if patient_id != patientId:
                visitsToSave.extend([(patient_id, *visit) for visit in visits])

        # rewriting the file to only include the patients that were not requested to be deleted
        fileToRewrite = open(filename, "w")
        with fileToRewrite:
            for visit in visitsToSave:
                fileToRewrite.write(",".join(str(v) for v in visit) + "\n")

        print(f"Data for patient {patientId} has been deleted.")

    return


# given function for main console functionality
def main():
    patients = readPatientsFromFile('patients.txt')
    while True:
        print("\n\nWelcome to the Health Information System\n\n")
        print("1. Display all patient data")
        print("2. Display patient data by ID")
        print("3. Add patient data")
        print("4. Display patient statistics")
        print("5. Find visits by year, month, or both")
        print("6. Find patients who need follow-up")
        print("7. Delete all visits of a particular patient")
        print("8. Quit\n")

        choice = input("Enter your choice (1-8): ")
        if choice == '1':
            displayPatientData(patients)
        elif choice == '2':
            patientID = int(input("Enter patient ID: "))
            displayPatientData(patients, patientID)
        elif choice == '3':
            patientID = int(input("Enter patient ID: "))
            date = input("Enter date (YYYY-MM-DD): ")
            try:
                temp = float(input("Enter temperature (Celsius): "))
                hr = int(input("Enter heart rate (bpm): "))
                rr = int(input("Enter respiratory rate (breaths per minute): "))
                sbp = int(input("Enter systolic blood pressure (mmHg): "))
                dbp = int(input("Enter diastolic blood pressure (mmHg): "))
                spo2 = int(input("Enter oxygen saturation (%): "))
                addPatientData(patients, patientID, date, temp, hr, rr, sbp, dbp, spo2, 'patients.txt')
            except ValueError:
                print("Invalid input. Please enter valid data.")
        elif choice == '4':
            patientID = input("Enter patient ID (or '0' for all patients): ")
            displayStats(patients, patientID)
        elif choice == '5':
            year = input("Enter year (YYYY) (or 0 for all years): ")
            month = input("Enter month (MM) (or 0 for all months): ")
            visits = findVisitsByDate(patients, int(year) if year != '0' else None,
                                      int(month) if month != '0' else None)
            if visits:
                for visit in visits:
                    print("Patient ID:", visit[0])
                    print(" Visit Date:", visit[1][0])
                    print("  Temperature:", "%.2f" % visit[1][1], "C")
                    print("  Heart Rate:", visit[1][2], "bpm")
                    print("  Respiratory Rate:", visit[1][3], "bpm")
                    print("  Systolic Blood Pressure:", visit[1][4], "mmHg")
                    print("  Diastolic Blood Pressure:", visit[1][5], "mmHg")
                    print("  Oxygen Saturation:", visit[1][6], "%")
            else:
                print("No visits found for the specified year/month.")
        elif choice == '6':
            followup_patients = findPatientsWhoNeedFollowUp(patients)
            if followup_patients:
                print("Patients who need follow-up visits:")
                for patientId in followup_patients:
                    print(patientId)
            else:
                print("No patients found who need follow-up visits.")
        elif choice == '7':
            patientID = input("Enter patient ID: ")
            deleteAllVisitsOfPatient(patients, int(patientID), "patients.txt")
        elif choice == '8':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")


# checks if the file is being run as the main program
if __name__ == '__main__':
    main()

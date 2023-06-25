patient_name = input("What is the patient's name? ")
patient_age = input("What is the patient age? ")
bool_input = bool(input("Is new patient? "))
print(str(bool_input))

def is_new_patient():
    new_patient_status = input("Is this a new patient? Y/N ")
    if new_patient_status == "Y":
        return True
    if new_patient_status == "N":
        return False



print("Is this a new patient? " + str(is_new_patient()))
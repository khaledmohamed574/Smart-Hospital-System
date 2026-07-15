from abc import ABC
from typing import List

class Person(ABC):
    def __init__(self, id: int, name: str, contactInfo: str):
        self.id: int = id
        self.name: str = name
        self.contactInfo: str = contactInfo

    def getId(self) -> int:
        return self.id

    def getName(self) -> str:
        return self.name

    def getContactInfo(self) -> str:
        return self.contactInfo

    def setContactInfo(self, contactInfo: str) -> None:
        self.contactInfo = contactInfo

    def __str__(self) -> str:
        return f"ID: {self.id}, Name: {self.name}, Contact: {self.contactInfo}"


class Doctor(Person):
    def __init__(self, id: int, name: str, contactInfo: str, specialization: str):
        super().__init__(id, name, contactInfo)
        self.specialization: str = specialization
        self.patients: List['Patient'] = []

    def diagnose(self, patient: 'Patient', diagnosis: str) -> None:
        patient.medicalHistory.append(diagnosis)
        print("Diagnosis Added Successfully.")

    def prescribeMedication(self, patient: 'Patient', medicine: str) -> None:
        patient.addPrescription(medicine)
        print("Medication Added Successfully.")

    def addPatient(self, patient: 'Patient') -> None:
        if patient not in self.patients:
            self.patients.append(patient)

    def viewPatients(self) -> None:
        if not self.patients:
            print("No Patients.")
        else:
            for patient in self.patients:
                print(patient)

    def displayInfo(self) -> None:
        print(f"Doctor ID : {self.id}")
        print(f"Name : {self.name}")
        print(f"Contact : {self.contactInfo}")
        print(f"Specialization : {self.specialization}")

    def __str__(self) -> str:
        return f"Doctor(ID={self.id}, Name={self.name})"


class Patient(Person):
    def __init__(self, id: int, name: str, contactInfo: str):
        super().__init__(id, name, contactInfo)
        self.medicalHistory: List[str] = []
        self.prescriptions: List[str] = []
        self.appointments: List['Appointment'] = []

    def addPrescription(self, medicine: str) -> None:
        self.prescriptions.append(medicine)

    def viewAppointments(self) -> None:
        if not self.appointments:
            print("No Appointments.")
        else:
            for appointment in self.appointments:
                print(appointment)

    def viewMedicalHistory(self) -> None:
        if not self.medicalHistory:
            print("Medical History is Empty.")
        else:
            for record in self.medicalHistory:
                print(record)

    def displayInfo(self) -> None:
        print(f"Patient ID : {self.id}")
        print(f"Name : {self.name}")
        print(f"Contact : {self.contactInfo}")

    def __str__(self) -> str:
        return f"Patient(ID={self.id}, Name={self.name})"


class Appointment:
    def __init__(self, patient: 'Patient', doctor: 'Doctor', date: str, time: str):
        self.patient: 'Patient' = patient
        self.doctor: 'Doctor' = doctor
        self.date: str = date
        self.time: str = time
        self.status: str = "Scheduled"

    def confirm(self) -> None:
        self.status = "Confirmed"

    def cancel(self) -> None:
        self.status = "Cancelled"

    def __str__(self) -> str:
        return (
            f"Patient: {self.patient.name} | "
            f"Doctor: {self.doctor.name} | "
            f"Date: {self.date} | "
            f"Time: {self.time} | "
            f"Status: {self.status}"
        )


class Staff(Person):
    def __init__(self, id: int, name: str, contactInfo: str, position: str):
        super().__init__(id, name, contactInfo)
        self.position: str = position

    def scheduleAppointment(self, patient: 'Patient', doctor: 'Doctor', date: str, time: str) -> 'Appointment':
        appointment = Appointment(patient, doctor, date, time)
        patient.appointments.append(appointment)
        return appointment

    def cancelAppointment(self, appointment: 'Appointment') -> None:
        appointment.cancel()

    def displayInfo(self) -> None:
        print(f"Staff ID : {self.id}")
        print(f"Name : {self.name}")
        print(f"Position : {self.position}")

    def __str__(self) -> str:
        return f"Staff(ID={self.id}, Name={self.name})"


class Hospital:
    def __init__(self):
        self.doctors: List[Doctor] = []
        self.patients: List[Patient] = []
        self.staffMembers: List[Staff] = []
        self.appointments: List[Appointment] = []

    def addDoctor(self, doctor: Doctor) -> None:
        self.doctors.append(doctor)
        print("Doctor added successfully.")

    def removeDoctor(self, doctor: Doctor) -> None:
        if doctor in self.doctors:
            self.doctors.remove(doctor)
            print("Doctor removed successfully.")
        else:
            print("Doctor not found.")

    def addPatient(self, patient: Patient) -> None:
        self.patients.append(patient)
        print("Patient added successfully.")

    def removePatient(self, patient: Patient) -> None:
        if patient in self.patients:
            self.patients.remove(patient)
            print("Patient removed successfully.")
        else:
            print("Patient not found.")

    def addStaff(self, staff: Staff) -> None:
        self.staffMembers.append(staff)
        print("Staff added successfully.")

    def removeStaff(self, staff: Staff) -> None:
        if staff in self.staffMembers:
            self.staffMembers.remove(staff)
            print("Staff removed successfully.")
        else:
            print("Staff member not found.")

    def addAppointment(self, appointment: Appointment) -> None:
        self.appointments.append(appointment)
        print("Appointment added successfully.")

    def removeAppointment(self, appointment: Appointment) -> None:
        if appointment in self.appointments:
            self.appointments.remove(appointment)
            print("Appointment removed successfully.")
        else:
            print("Appointment not found.")

    def viewAppointments(self) -> None:
        if not self.appointments:
            print("No appointments available.")
        else:
            for appointment in self.appointments:
                print(appointment)

def run_cli():
    hospital = Hospital()

    while True:
        print("\n========== Hospital Management System ==========")
        print("1. Add Doctor")
        print("2. Add Patient")
        print("3. Add Staff")
        print("4. Schedule Appointment")
        print("5. View Appointments")
        print("6. Diagnose Patient")
        print("7. Prescribe Medication")
        print("8. View Doctor Patients")
        print("9. Exit")

        choice = input("Choose: ")

        if choice == "1":
            id = int(input("Doctor ID: "))
            name = input("Doctor Name: ")
            contact = input("Contact Info: ")
            specialization = input("Specialization: ")

            doctor = Doctor(id, name, contact, specialization)
            hospital.addDoctor(doctor)

        elif choice == "2":
            id = int(input("Patient ID: "))
            name = input("Patient Name: ")
            contact = input("Contact Info: ")

            patient = Patient(id, name, contact)
            hospital.addPatient(patient)

        elif choice == "3":
            id = int(input("Staff ID: "))
            name = input("Staff Name: ")
            contact = input("Contact Info: ")
            position = input("Position: ")

            staff = Staff(id, name, contact, position)
            hospital.addStaff(staff)

        elif choice == "4":
            if len(hospital.doctors) == 0:
                print("No doctors available.")
                continue

            if len(hospital.patients) == 0:
                print("No patients available.")
                continue

            if len(hospital.staffMembers) == 0:
                print("No staff available.")
                continue

            print("\nDoctors")
            for doctor in hospital.doctors:
                print(doctor.id, doctor.name)

            doctor_id = int(input("Choose Doctor ID: "))

            doctor = None
            for d in hospital.doctors:
                if d.id == doctor_id:
                    doctor = d
                    break

            if doctor is None:
                print("Doctor not found.")
                continue

            print("\nPatients")
            for patient in hospital.patients:
                print(patient.id, patient.name)

            patient_id = int(input("Choose Patient ID: "))

            patient = None
            for p in hospital.patients:
                if p.id == patient_id:
                    patient = p
                    break

            if patient is None:
                print("Patient not found.")
                continue

            date = input("Date (YYYY-MM-DD): ")
            time = input("Time: ")

            staff = hospital.staffMembers[0]

            appointment = staff.scheduleAppointment(
                patient,
                doctor,
                date,
                time
            )

            hospital.addAppointment(appointment)
            doctor.addPatient(patient)

        elif choice == "5":
            hospital.viewAppointments()

        elif choice == "6":
            doctor_id = int(input("Doctor ID: "))
            patient_id = int(input("Patient ID: "))
            diagnosis = input("Enter Diagnosis: ")

            doctor = None
            patient = None

            for d in hospital.doctors:
                if d.id == doctor_id:
                    doctor = d

            for p in hospital.patients:
                if p.id == patient_id:
                    patient = p

            if doctor and patient:
                doctor.diagnose(patient, diagnosis)
            else:
                print("Doctor or Patient not found.")

        elif choice == "7":
            doctor_id = int(input("Doctor ID: "))
            patient_id = int(input("Patient ID: "))
            medicine = input("Medicine: ")

            doctor = None
            patient = None

            for d in hospital.doctors:
                if d.id == doctor_id:
                    doctor = d

            for p in hospital.patients:
                if p.id == patient_id:
                    patient = p

            if doctor and patient:
                doctor.prescribeMedication(patient, medicine)
            else:
                print("Doctor or Patient not found.")

        elif choice == "8":
            doctor_id = int(input("Doctor ID: "))

            found = False
            for doctor in hospital.doctors:
                if doctor.id == doctor_id:
                    doctor.viewPatients()
                    found = True
                    break

            if not found:
                print("Doctor not found.")

        elif choice == "9":
            print("Good Bye")
            break

        else:
            print("Invalid Choice")


if __name__ == "__main__":
    run_cli()


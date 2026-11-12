'''Hospital patient management
Create a hospital management system that tracks doctors,patients and appointments
*Doctors can have specialities and patients may have differnt ailments
*Each appointment should store the doctor-patint relationships,along with the date and time
*Add functionality for doctors' schedules and ensuring no double booking
'''
class Doctor:
    def __init__(self,doctor_id,name,specialty):
        self.doctor_id=doctor_id
        self.name=name
        self.specialty=specialty
        self.schedule=[]
    def display_details(self):
        print(f"Dr. {self.name} | Specialty: {self.specialty}")
class Patient:
    def __init__(self,patient_id,name,ailment):
        self.patient_is=patient_id
        self.name=name
        self.ailment=ailment
    def display_details(self):
        print(f"Patient: {self.name} | Ailment: {self.ailment}")
class Appointment:
    def __init__(self,doctor,patient,date,time):
        self.doctor=doctor
        self.patient=patient
        self.date=date
        self.time=time
    def display_details(self):
        print(f"Appointment: Dr. {self.doctor.name} & {self.patient.name} on {self.date} at {self.time}")
class Hospital:
    def __init__(self,name):
        self.name=name
        self.doctors={}
        self.patients={}
        self.appointments=[]
    def add_doctor(self,doctor_id,name,specialty):
        if doctor_id not in self.doctors:
            self.doctors[doctor_id]=Doctor(doctor_id,name,specialty)
            print(f"Doctor Dr. {name} added successfully.")
        else:
            print("Doctor ID already exists.")
    def add_patient(self,patient_id,name,ailment):
        if patient_id not in self.patients:
            self.patients[patient_id]=Patient(patient_id,name,ailment)
            print(f"Patient {name} registered successfully.")
        else:
            print("Patient ID already exits.")
    def schedule_appointment(self,doctor_id,patient_id,date,time):
        if doctor_id not in self.doctors:
            print("Doctor not found.")
        if patient_id not in self.patients:
            print("Patient not found.")
            return 
        doctor=self.doctors[doctor_id]
        patient=self.patients[patient_id]

        for appt in self.appointments:
            if appt.doctor.doctor_id==doctor_id and appt.date==date and appt.time==time:
                print(f"Conflict: Dr. {doctor.name} is already booked at {time} on {date}.")
                return
        new_appointment=Appointment(doctor,patient,date,time)
        self.appointments.append(new_appointment)
        doctor.schedule.append((date,time))
        print(f"Appointment successfully scheduled with Dr. {doctor.name} for {patient.name} on {date} at {time}.")
    def display_appointment(self):
        print("\nAll Hospital Appointments:")
        if not self.appointments:
            print("No appointments scheduled.")
        for appt in self.appointments:
            appt.display_details()
hospital=Hospital("CityCare Hospital")
hospital.add_doctor("D1","Anupriya","Cardiologist")
hospital.add_doctor("D2","Priya","Neurologist")

hospital.add_patient("P1","Manu","Chest pain")
hospital.add_patient("P2","Vinod","Migraine")

hospital.schedule_appointment("D1","P1", "2026-11-15", "10:00 AM")
hospital.schedule_appointment("D1", "P2", "2026-11-15", "10:00 AM")
hospital.schedule_appointment("D1", "P2", "2026-11-15", "11:30 AM")

hospital.display_appointment()
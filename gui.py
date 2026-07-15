import tkinter as tk
from tkinter import messagebox, ttk
import json
import os

from Main import Doctor, Hospital, Patient, Staff


def build_gui():
    hospital = Hospital()

    TEXTS = {
        "ar": {
            "window_title": "نظام إدارة المستشفى",
            "ready": "جاهز",
            "header_title": "نظام إدارة المستشفى",
            "header_subtitle": "واجهة منظمة لإضافة البيانات وعرضها بسهولة",
            "language": "اللغة",
            "lang_ar": "العربية",
            "lang_en": "English",
            "tab_add": "إضافة بيانات",
            "tab_actions": "الإجراءات الطبية",
            "tab_reports": "تقارير",
            "tab_data": "كل البيانات",
            "doctor_data": "بيانات الطبيب",
            "patient_data": "بيانات المريض",
            "staff_data": "بيانات الممرض",
            "id": "الرقم",
            "name": "الاسم",
            "contact": "التواصل",
            "specialization": "التخصص",
            "position": "الوظيفة",
            "save_doctor": "حفظ الطبيب",
            "save_patient": "حفظ المريض",
            "save_staff": "حفظ الممرض",
            "appointment": "حجز موعد",
            "diagnosis": "تشخيص",
            "medication": "وصفة دواء",
            "doctor": "الدكتور",
            "patient": "المريض",
            "staff": "الممرض",
            "date": "التاريخ (YYYY-MM-DD)",
            "time": "الوقت",
            "confirm_appointment": "تأكيد الحجز",
            "save_diagnosis": "حفظ التشخيص",
            "medicine": "الدواء",
            "save_prescription": "حفظ الوصفة",
            "show_patients": "عرض المرضى",
            "patient_record": "سجل المريض",
            "show_record": "عرض السجل",
            "history_diag": "التشخيص",
            "history_pres": "الوصفات",
            "history_apps": "مواعيد المريض",
            "details": "البيان",
            "tab_doctors": "الأطباء",
            "tab_patients": "المرضى",
            "tab_staff": "الممرضون",
            "tab_appointments": "المواعيد",
            "refresh_tables": "تحديث الجداول",
            "exit": "خروج",
            "state": "الحالة",
            "invalid_data": "بيانات غير صحيحة",
            "duplicate_id": "رقم مكرر",
            "missing_data": "بيانات ناقصة",
            "not_found": "غير موجود",
            "doctor_invalid": "أدخل بيانات طبيب صحيحة.",
            "doctor_duplicate": "رقم الطبيب موجود بالفعل.",
            "doctor_added": "تمت إضافة الطبيب بنجاح.",
            "patient_invalid": "أدخل بيانات مريض صحيحة.",
            "patient_duplicate": "رقم المريض موجود بالفعل.",
            "patient_added": "تمت إضافة المريض بنجاح.",
            "staff_invalid": "أدخل بيانات ممرض صحيحة.",
            "staff_duplicate": "رقم الممرض موجود بالفعل.",
            "staff_added": "تمت إضافة الممرض بنجاح.",
            "need_base_data": "أضف طبيبًا ومريضًا وممرضًا قبل الحجز.",
            "appointment_invalid": "اختر الطبيب/المريض/الممرض وأدخل التاريخ والوقت.",
            "appointment_not_found": "تعذر العثور على الطبيب أو المريض أو الممرض.",
            "appointment_added": "تم حجز الموعد بنجاح.",
            "diagnosis_invalid": "اختر الطبيب والمريض وأدخل التشخيص.",
            "doctor_patient_not_found": "الطبيب أو المريض غير موجود.",
            "diagnosis_added": "تمت إضافة التشخيص بنجاح.",
            "medicine_invalid": "اختر الطبيب والمريض وأدخل الدواء.",
            "medicine_added": "تم حفظ الوصفة بنجاح.",
            "select_doctor_first": "اختر طبيبًا أولًا.",
            "doctor_not_found": "الطبيب غير موجود.",
            "doctor_no_patients": "لا يوجد مرضى لهذا الطبيب.",
            "doctor_patients_loaded": "تم تحميل {count} مريض للطبيب {name}.",
            "select_patient_first": "اختر مريضًا أولًا.",
            "patient_not_found": "المريض غير موجود.",
            "no_diagnoses": "لا يوجد تشخيصات للمريض المحدد.",
            "no_prescriptions": "لا يوجد وصفات للمريض المحدد.",
            "no_medical_data": "لا يوجد بيانات طبية للمريض المحدد.",
            "patient_data_loaded": "تم تحميل السجل الطبي للمريض {name}.",
            "lang_changed": "تم تغيير اللغة إلى العربية.",
            "conflict_doctor": "هذا الطبيب لديه موعد آخر بنفس التاريخ والوقت.",
            "conflict_patient": "هذا المريض لديه موعد آخر بنفس التاريخ والوقت.",
            "delete_selected": "حذف المحدد",
            "no_selection": "اختر عنصرًا من الجدول أولًا.",
            "item_deleted": "تم حذف العنصر المحدد.",
            "data_loaded": "تم تحميل البيانات المحفوظة.",
            "data_load_failed": "تعذر تحميل البيانات المحفوظة.",
            "welcome_title": "مرحبا بك في نظام إدارة المستشفى",
            "welcome_message": "اضغط زر البدء للانتقال إلى لوحة التحكم.",
            "welcome_button": "ابدأ",
        },
        "en": {
            "window_title": "Hospital Management System",
            "ready": "Ready",
            "welcome_title": "Welcome to the Hospital Management System",
            "welcome_message": "Press Start to go to the dashboard.",
            "welcome_button": "Start",
            "header_title": "Hospital Management Dashboard",
            "header_subtitle": "Organized UI to add and review data quickly",
            "language": "Language",
            "lang_ar": "Arabic",
            "lang_en": "English",
            "tab_add": "Add Records",
            "tab_actions": "Medical Actions",
            "tab_reports": "Reports",
            "tab_data": "All Data",
            "doctor_data": "Doctor Data",
            "patient_data": "Patient Data",
            "staff_data": "Nurse Data",
            "id": "ID",
            "name": "Name",
            "contact": "Contact",
            "specialization": "Specialization",
            "position": "Position",
            "save_doctor": "Save Doctor",
            "save_patient": "Save Patient",
            "save_staff": "Save Nurse",
            "appointment": "Appointment",
            "diagnosis": "Diagnosis",
            "medication": "Medication",
            "doctor": "Doctor",
            "patient": "Patient",
            "staff": "Nurse",
            "date": "Date (YYYY-MM-DD)",
            "time": "Time",
            "confirm_appointment": "Confirm Appointment",
            "save_diagnosis": "Save Diagnosis",
            "medicine": "Medicine",
            "save_prescription": "Save Prescription",
            "show_patients": "Show Patients",
            "patient_record": "Patient Record",
            "show_record": "Show Record",
            "history_diag": "Diagnoses",
            "history_pres": "Prescriptions",
            "history_apps": "Patient Appointments",
            "details": "Details",
            "tab_doctors": "Doctors",
            "tab_patients": "Patients",
            "tab_staff": "Nurses",
            "tab_appointments": "Appointments",
            "refresh_tables": "Refresh Tables",
            "exit": "Exit",
            "state": "Status",
            "invalid_data": "Invalid Data",
            "duplicate_id": "Duplicate ID",
            "missing_data": "Missing Data",
            "not_found": "Not Found",
            "doctor_invalid": "Enter valid doctor information.",
            "doctor_duplicate": "Doctor ID already exists.",
            "doctor_added": "Doctor added successfully.",
            "patient_invalid": "Enter valid patient information.",
            "patient_duplicate": "Patient ID already exists.",
            "patient_added": "Patient added successfully.",
            "staff_invalid": "Enter valid nurse information.",
            "staff_duplicate": "Nurse ID already exists.",
            "staff_added": "Nurse added successfully.",
            "need_base_data": "Add at least one doctor, patient, and nurse first.",
            "appointment_invalid": "Select doctor/patient/nurse and enter date + time.",
            "appointment_not_found": "Could not find selected doctor, patient, or nurse.",
            "appointment_added": "Appointment scheduled successfully.",
            "diagnosis_invalid": "Select doctor + patient and enter diagnosis.",
            "doctor_patient_not_found": "Doctor or patient not found.",
            "diagnosis_added": "Diagnosis added successfully.",
            "medicine_invalid": "Select doctor + patient and enter medicine.",
            "medicine_added": "Prescription saved successfully.",
            "select_doctor_first": "Select a doctor first.",
            "doctor_not_found": "Doctor not found.",
            "doctor_no_patients": "Selected doctor has no patients.",
            "doctor_patients_loaded": "Loaded {count} patients for doctor {name}.",
            "select_patient_first": "Select a patient first.",
            "patient_not_found": "Patient not found.",
            "no_diagnoses": "No diagnoses found for selected patient.",
            "no_prescriptions": "No prescriptions found for selected patient.",
            "no_medical_data": "No medical data found for selected patient.",
            "patient_data_loaded": "Loaded medical data for {name}.",
            "lang_changed": "Language changed to English.",
            "conflict_doctor": "This doctor already has an appointment at this date and time.",
            "conflict_patient": "This patient already has an appointment at this date and time.",
            "delete_selected": "Delete Selected",
            "no_selection": "Please select an item from the table first.",
            "item_deleted": "Selected item deleted.",
            "data_loaded": "Saved data loaded.",
            "data_load_failed": "Could not load saved data.",
        },
    }

    def t(key, **kwargs):
        template = TEXTS[current_lang.get()][key]
        return template.format(**kwargs) if kwargs else template

    root = tk.Tk()
    root.title("Hospital Management System")
    root.geometry("1120x760")
    root.minsize(980, 680)
    current_lang = tk.StringVar(master=root, value="ar")

    style = ttk.Style()
    style.configure("TButton", padding=6)
    style.configure("Header.TLabel", font=("Segoe UI", 16, "bold"))
    style.configure("SubHeader.TLabel", font=("Segoe UI", 10))

    status_var = tk.StringVar(value=t("ready"))

    def set_status(message):
        status_var.set(message)

    def find_doctor(doctor_id):
        for doctor in hospital.doctors:
            if doctor.id == doctor_id:
                return doctor
        return None

    def find_patient(patient_id):
        for patient in hospital.patients:
            if patient.id == patient_id:
                return patient
        return None

    def parse_selected_id(combo):
        return int(combo.get().split(" - ")[0])

    def clear_entries(entries):
        for entry in entries:
            entry.delete(0, tk.END)

    def clear_tree(tree):
        for item in tree.get_children():
            tree.delete(item)

    DATA_FILE = os.path.join(os.path.dirname(__file__), "hospital_data.json")

    def save_data():
        data = {
            "doctors": [
                {
                    "id": doctor.id,
                    "name": doctor.name,
                    "contact": doctor.contactInfo,
                    "specialization": doctor.specialization,
                }
                for doctor in hospital.doctors
            ],
            "patients": [
                {
                    "id": patient.id,
                    "name": patient.name,
                    "contact": patient.contactInfo,
                    "medicalHistory": patient.medicalHistory,
                    "prescriptions": patient.prescriptions,
                }
                for patient in hospital.patients
            ],
            "staff": [
                {
                    "id": staff.id,
                    "name": staff.name,
                    "contact": staff.contactInfo,
                    "position": staff.position,
                }
                for staff in hospital.staffMembers
            ],
            "appointments": [
                {
                    "doctor_id": appointment.doctor.id,
                    "patient_id": appointment.patient.id,
                    "date": appointment.date,
                    "time": appointment.time,
                    "status": appointment.status,
                }
                for appointment in hospital.appointments
            ],
        }
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    def load_data():
        if not os.path.exists(DATA_FILE):
            return

        with open(DATA_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)

        hospital.doctors.clear()
        hospital.patients.clear()
        hospital.staffMembers.clear()
        hospital.appointments.clear()

        for d in data.get("doctors", []):
            hospital.addDoctor(Doctor(d["id"], d["name"], d["contact"], d["specialization"]))

        for p in data.get("patients", []):
            patient = Patient(p["id"], p["name"], p["contact"])
            patient.medicalHistory = list(p.get("medicalHistory", []))
            patient.prescriptions = list(p.get("prescriptions", []))
            hospital.addPatient(patient)

        for s in data.get("staff", []):
            hospital.addStaff(Staff(s["id"], s["name"], s["contact"], s["position"]))

        for a in data.get("appointments", []):
            doctor = find_doctor(a["doctor_id"])
            patient = find_patient(a["patient_id"])
            if doctor is None or patient is None:
                continue

            staff_member = hospital.staffMembers[0] if hospital.staffMembers else None
            if staff_member is None:
                continue

            appointment = staff_member.scheduleAppointment(patient, doctor, a["date"], a["time"])
            appointment.status = a.get("status", "Scheduled")
            hospital.addAppointment(appointment)
            doctor.addPatient(patient)

    def refresh_dropdowns():
        doctor_values = [f"{doctor.id} - {doctor.name}" for doctor in hospital.doctors]
        patient_values = [f"{patient.id} - {patient.name}" for patient in hospital.patients]
        staff_values = [f"{staff.id} - {staff.name}" for staff in hospital.staffMembers]

        doctor_combos = [
            appointment_doctor_combo,
            diagnose_doctor_combo,
            med_doctor_combo,
            report_doctor_combo,
        ]
        patient_combos = [
            appointment_patient_combo,
            diagnose_patient_combo,
            med_patient_combo,
            history_patient_combo,
        ]

        for combo in doctor_combos:
            combo["values"] = doctor_values
        for combo in patient_combos:
            combo["values"] = patient_values
        appointment_staff_combo["values"] = staff_values

    def refresh_tables():
        clear_tree(doctors_tree)
        clear_tree(patients_tree)
        clear_tree(staff_tree)
        clear_tree(appointments_tree)

        for doctor in hospital.doctors:
            doctors_tree.insert("", tk.END, values=(doctor.id, doctor.name, doctor.specialization, doctor.contactInfo))

        for patient in hospital.patients:
            patients_tree.insert("", tk.END, values=(patient.id, patient.name, patient.contactInfo))

        for staff_member in hospital.staffMembers:
            staff_tree.insert("", tk.END, values=(staff_member.id, staff_member.name, staff_member.position))

        for appointment in hospital.appointments:
            appointments_tree.insert(
                "",
                tk.END,
                values=(
                    appointment.patient.name,
                    appointment.doctor.name,
                    appointment.date,
                    appointment.time,
                    appointment.status,
                ),
            )

    def refresh_ui():
        refresh_dropdowns()
        refresh_tables()

    def add_doctor():
        try:
            doctor_id = int(doctor_id_entry.get())
            name = doctor_name_entry.get().strip()
            contact = doctor_contact_entry.get().strip()
            specialization = doctor_specialty_entry.get().strip()
            if not name or not contact or not specialization:
                raise ValueError
        except ValueError:
            messagebox.showerror(t("invalid_data"), t("doctor_invalid"))
            return

        if find_doctor(doctor_id):
            messagebox.showerror(t("duplicate_id"), t("doctor_duplicate"))
            return

        hospital.addDoctor(Doctor(doctor_id, name, contact, specialization))
        clear_entries([doctor_id_entry, doctor_name_entry, doctor_contact_entry, doctor_specialty_entry])
        save_data()
        refresh_ui()
        set_status(t("doctor_added"))

    def add_patient():
        try:
            patient_id = int(patient_id_entry.get())
            name = patient_name_entry.get().strip()
            contact = patient_contact_entry.get().strip()
            if not name or not contact:
                raise ValueError
        except ValueError:
            messagebox.showerror(t("invalid_data"), t("patient_invalid"))
            return

        if find_patient(patient_id):
            messagebox.showerror(t("duplicate_id"), t("patient_duplicate"))
            return

        hospital.addPatient(Patient(patient_id, name, contact))
        clear_entries([patient_id_entry, patient_name_entry, patient_contact_entry])
        save_data()
        refresh_ui()
        set_status(t("patient_added"))

    def add_staff():
        try:
            staff_id = int(staff_id_entry.get())
            name = staff_name_entry.get().strip()
            contact = staff_contact_entry.get().strip()
            position = staff_position_entry.get().strip()
            if not name or not contact or not position:
                raise ValueError
        except ValueError:
            messagebox.showerror(t("invalid_data"), t("staff_invalid"))
            return

        for staff_member in hospital.staffMembers:
            if staff_member.id == staff_id:
                messagebox.showerror(t("duplicate_id"), t("staff_duplicate"))
                return

        hospital.addStaff(Staff(staff_id, name, contact, position))
        clear_entries([staff_id_entry, staff_name_entry, staff_contact_entry, staff_position_entry])
        save_data()
        refresh_ui()
        set_status(t("staff_added"))

    def schedule_appointment():
        if not hospital.doctors or not hospital.patients or not hospital.staffMembers:
            messagebox.showerror(t("missing_data"), t("need_base_data"))
            return

        try:
            doctor_id = parse_selected_id(appointment_doctor_combo)
            patient_id = parse_selected_id(appointment_patient_combo)
            staff_id = parse_selected_id(appointment_staff_combo)
            date = appointment_date_entry.get().strip()
            time = appointment_time_entry.get().strip()
            if not date or not time:
                raise ValueError
        except (ValueError, IndexError):
            messagebox.showerror(t("invalid_data"), t("appointment_invalid"))
            return

        doctor = find_doctor(doctor_id)
        patient = find_patient(patient_id)
        staff_member = None
        for staff in hospital.staffMembers:
            if staff.id == staff_id:
                staff_member = staff
                break

        if doctor is None or patient is None or staff_member is None:
            messagebox.showerror(t("not_found"), t("appointment_not_found"))
            return

        for existing in hospital.appointments:
            if existing.status == "Cancelled":
                continue
            if existing.date == date and existing.time == time:
                if existing.doctor.id == doctor_id:
                    messagebox.showerror(t("invalid_data"), t("conflict_doctor"))
                    return
                if existing.patient.id == patient_id:
                    messagebox.showerror(t("invalid_data"), t("conflict_patient"))
                    return

        appointment = staff_member.scheduleAppointment(patient, doctor, date, time)
        hospital.addAppointment(appointment)
        doctor.addPatient(patient)
        clear_entries([appointment_date_entry, appointment_time_entry])
        save_data()
        refresh_ui()
        set_status(t("appointment_added"))

    def diagnose_patient():
        try:
            doctor_id = parse_selected_id(diagnose_doctor_combo)
            patient_id = parse_selected_id(diagnose_patient_combo)
            diagnosis = diagnosis_entry.get().strip()
            if not diagnosis:
                raise ValueError
        except (ValueError, IndexError):
            messagebox.showerror(t("invalid_data"), t("diagnosis_invalid"))
            return

        doctor = find_doctor(doctor_id)
        patient = find_patient(patient_id)
        if doctor is None or patient is None:
            messagebox.showerror(t("not_found"), t("doctor_patient_not_found"))
            return

        doctor.diagnose(patient, diagnosis)
        diagnosis_entry.delete(0, tk.END)
        save_data()
        set_status(t("diagnosis_added"))

    def prescribe_medication():
        try:
            doctor_id = parse_selected_id(med_doctor_combo)
            patient_id = parse_selected_id(med_patient_combo)
            medicine = medicine_entry.get().strip()
            if not medicine:
                raise ValueError
        except (ValueError, IndexError):
            messagebox.showerror(t("invalid_data"), t("medicine_invalid"))
            return

        doctor = find_doctor(doctor_id)
        patient = find_patient(patient_id)
        if doctor is None or patient is None:
            messagebox.showerror(t("not_found"), t("doctor_patient_not_found"))
            return

        doctor.prescribeMedication(patient, medicine)
        medicine_entry.delete(0, tk.END)
        save_data()
        set_status(t("medicine_added"))

    def show_doctor_patients():
        clear_tree(report_tree)
        try:
            doctor_id = parse_selected_id(report_doctor_combo)
        except (ValueError, IndexError):
            messagebox.showerror(t("invalid_data"), t("select_doctor_first"))
            return

        doctor = find_doctor(doctor_id)
        if doctor is None:
            messagebox.showerror(t("not_found"), t("doctor_not_found"))
            return

        if not doctor.patients:
            set_status(t("doctor_no_patients"))
            return

        for patient in doctor.patients:
            report_tree.insert("", tk.END, values=(patient.id, patient.name, patient.contactInfo))
        set_status(t("doctor_patients_loaded", count=len(doctor.patients), name=doctor.name))

    def show_patient_medical_data():
        clear_tree(history_diagnosis_tree)
        clear_tree(history_prescriptions_tree)
        clear_tree(history_appointments_tree)

        try:
            patient_id = parse_selected_id(history_patient_combo)
        except (ValueError, IndexError):
            messagebox.showerror(t("invalid_data"), t("select_patient_first"))
            return

        patient = find_patient(patient_id)
        if patient is None:
            messagebox.showerror(t("not_found"), t("patient_not_found"))
            return

        if not patient.medicalHistory:
            set_status(t("no_diagnoses"))
        else:
            for diagnosis in patient.medicalHistory:
                history_diagnosis_tree.insert("", tk.END, values=(diagnosis,))

        if not patient.prescriptions:
            # Keep status from diagnoses if already set, otherwise clear.
            if not patient.medicalHistory:
                set_status(t("no_prescriptions"))
        else:
            for medicine in patient.prescriptions:
                history_prescriptions_tree.insert("", tk.END, values=(medicine,))

        if not patient.appointments:
            if not patient.medicalHistory and not patient.prescriptions:
                set_status(t("no_medical_data"))
        else:
            for appointment in patient.appointments:
                history_appointments_tree.insert(
                    "",
                    tk.END,
                    values=(appointment.doctor.name, appointment.date, appointment.time, appointment.status),
                )

        if patient.medicalHistory or patient.prescriptions or patient.appointments:
            set_status(t("patient_data_loaded", name=patient.name))

    def delete_selected_from_current_tab():
        current_tab = data_notebook.index(data_notebook.select())

        if current_tab == 0:
            selected = doctors_tree.selection()
            if not selected:
                messagebox.showerror(t("invalid_data"), t("no_selection"))
                return
            doctor_id = int(doctors_tree.item(selected[0], "values")[0])
            doctor = find_doctor(doctor_id)
            if doctor is None:
                messagebox.showerror(t("not_found"), t("doctor_not_found"))
                return
            hospital.removeDoctor(doctor)
            hospital.appointments = [a for a in hospital.appointments if a.doctor.id != doctor_id]
            for patient in hospital.patients:
                patient.appointments = [a for a in patient.appointments if a.doctor.id != doctor_id]

        elif current_tab == 1:
            selected = patients_tree.selection()
            if not selected:
                messagebox.showerror(t("invalid_data"), t("no_selection"))
                return
            patient_id = int(patients_tree.item(selected[0], "values")[0])
            patient = find_patient(patient_id)
            if patient is None:
                messagebox.showerror(t("not_found"), t("patient_not_found"))
                return
            hospital.removePatient(patient)
            hospital.appointments = [a for a in hospital.appointments if a.patient.id != patient_id]
            for doctor in hospital.doctors:
                doctor.patients = [p for p in doctor.patients if p.id != patient_id]

        elif current_tab == 2:
            selected = staff_tree.selection()
            if not selected:
                messagebox.showerror(t("invalid_data"), t("no_selection"))
                return
            staff_id = int(staff_tree.item(selected[0], "values")[0])
            target = None
            for staff in hospital.staffMembers:
                if staff.id == staff_id:
                    target = staff
                    break
            if target is None:
                messagebox.showerror(t("not_found"), t("appointment_not_found"))
                return
            hospital.removeStaff(target)

        else:
            selected = appointments_tree.selection()
            if not selected:
                messagebox.showerror(t("invalid_data"), t("no_selection"))
                return
            patient_name, doctor_name, date, time, _status = appointments_tree.item(selected[0], "values")
            target_appointment = None
            for appointment in hospital.appointments:
                if (
                    appointment.patient.name == patient_name
                    and appointment.doctor.name == doctor_name
                    and appointment.date == date
                    and appointment.time == time
                ):
                    target_appointment = appointment
                    break
            if target_appointment is None:
                messagebox.showerror(t("not_found"), t("appointment_not_found"))
                return
            hospital.removeAppointment(target_appointment)
            target_appointment.patient.appointments = [
                a
                for a in target_appointment.patient.appointments
                if not (
                    a.doctor.id == target_appointment.doctor.id
                    and a.date == target_appointment.date
                    and a.time == target_appointment.time
                )
            ]

        save_data()
        refresh_ui()
        set_status(t("item_deleted"))

    def apply_language():
        root.title(t("window_title"))
        status_var.set(t("ready"))

        header_title_label.config(text=t("header_title"))
        header_subtitle_label.config(text=t("header_subtitle"))
        language_label.config(text=f"{t('language')}:" )
        welcome_label.config(text=t("welcome_title"))
        welcome_desc.config(text=t("welcome_message"))
        welcome_button.config(text=t("welcome_button"))

        notebook.tab(0, text=t("tab_add"))
        notebook.tab(1, text=t("tab_actions"))
        notebook.tab(2, text=t("tab_reports"))
        notebook.tab(3, text=t("tab_data"))

        add_left.config(text=t("doctor_data"))
        add_mid.config(text=t("patient_data"))
        add_right.config(text=t("staff_data"))

        doctor_id_label.config(text=t("id"))
        doctor_name_label.config(text=t("name"))
        doctor_contact_label.config(text=t("contact"))
        doctor_specialty_label.config(text=t("specialization"))
        doctor_button.config(text=t("save_doctor"))

        patient_id_label.config(text=t("id"))
        patient_name_label.config(text=t("name"))
        patient_contact_label.config(text=t("contact"))
        patient_button.config(text=t("save_patient"))

        staff_id_label.config(text=t("id"))
        staff_name_label.config(text=t("name"))
        staff_contact_label.config(text=t("contact"))
        staff_position_label.config(text=t("position"))
        staff_button.config(text=t("save_staff"))

        appointment_frame.config(text=t("appointment"))
        diagnosis_frame.config(text=t("diagnosis"))
        medication_frame.config(text=t("medication"))

        app_doctor_label.config(text=t("doctor"))
        app_patient_label.config(text=t("patient"))
        app_staff_label.config(text=t("staff"))
        app_date_label.config(text=t("date"))
        app_time_label.config(text=t("time"))
        appointment_button.config(text=t("confirm_appointment"))

        diag_doctor_label.config(text=t("doctor"))
        diag_patient_label.config(text=t("patient"))
        diag_entry_label.config(text=t("diagnosis"))
        diagnosis_button.config(text=t("save_diagnosis"))

        med_doctor_label.config(text=t("doctor"))
        med_patient_label.config(text=t("patient"))
        med_entry_label.config(text=t("medicine"))
        medication_button.config(text=t("save_prescription"))

        report_doctor_label.config(text=t("doctor"))
        report_button.config(text=t("show_patients"))
        for col, text in [("id", t("id")), ("name", t("name")), ("contact", t("contact"))]:
            report_tree.heading(col, text=text)

        history_label.config(text=t("patient_record"))
        history_button.config(text=t("show_record"))
        history_notebook.tab(0, text=t("history_diag"))
        history_notebook.tab(1, text=t("history_pres"))
        history_notebook.tab(2, text=t("history_apps"))
        history_diagnosis_tree.heading("diagnosis", text=t("details"))
        history_prescriptions_tree.heading("medicine", text=t("medicine"))
        for col, text in [("doctor", t("doctor")), ("date", t("date")), ("time", t("time")), ("status", t("state"))]:
            history_appointments_tree.heading(col, text=text)

        refresh_button.config(text=t("refresh_tables"))
        delete_button.config(text=t("delete_selected"))
        data_notebook.tab(0, text=t("tab_doctors"))
        data_notebook.tab(1, text=t("tab_patients"))
        data_notebook.tab(2, text=t("tab_staff"))
        data_notebook.tab(3, text=t("tab_appointments"))

        for col, text in [("id", t("id")), ("name", t("name")), ("spec", t("specialization")), ("contact", t("contact"))]:
            doctors_tree.heading(col, text=text)
        for col, text in [("id", t("id")), ("name", t("name")), ("contact", t("contact"))]:
            patients_tree.heading(col, text=text)
        for col, text in [("id", t("id")), ("name", t("name")), ("position", t("position"))]:
            staff_tree.heading(col, text=text)
        for col, text in [
            ("patient", t("patient")),
            ("doctor", t("doctor")),
            ("date", t("date")),
            ("time", t("time")),
            ("status", t("state")),
        ]:
            appointments_tree.heading(col, text=text)

        exit_button.config(text=t("exit"))

    def on_language_change(_event=None):
        lang_display = language_combo.get()
        if lang_display in (TEXTS["ar"]["lang_ar"], "Arabic"):
            current_lang.set("ar")
        else:
            current_lang.set("en")
        apply_language()
        set_status(t("lang_changed"))

    header = ttk.Frame(root, padding=(12, 10, 12, 6))
    header.pack(fill="x")
    header_title_label = ttk.Label(header, text=t("header_title"), style="Header.TLabel")
    header_title_label.pack(anchor="w")
    header_subtitle_label = ttk.Label(header, text=t("header_subtitle"), style="SubHeader.TLabel")
    header_subtitle_label.pack(anchor="w")
    lang_frame = ttk.Frame(header)
    lang_frame.pack(anchor="e", pady=(4, 0))
    language_label = ttk.Label(lang_frame, text=f"{t('language')}:")
    language_label.pack(side="left", padx=(0, 6))
    language_combo = ttk.Combobox(lang_frame, state="readonly", values=[TEXTS["ar"]["lang_ar"], TEXTS["ar"]["lang_en"]], width=10)
    language_combo.set(TEXTS["ar"]["lang_ar"])
    language_combo.pack(side="left")
    language_combo.bind("<<ComboboxSelected>>", on_language_change)

    def show_main_ui():
        welcome_frame.pack_forget()
        notebook.pack(fill="both", expand=True, padx=12, pady=8)
        set_status(t("ready"))

    welcome_frame = ttk.Frame(root, padding=24)
    welcome_label = ttk.Label(welcome_frame, text=t("welcome_title"), style="Header.TLabel")
    welcome_label.pack(pady=(0, 8))
    welcome_desc = ttk.Label(welcome_frame, text=t("welcome_message"), style="SubHeader.TLabel", wraplength=800, justify="center")
    welcome_desc.pack(pady=(0, 16))
    welcome_button = ttk.Button(welcome_frame, text=t("welcome_button"), command=show_main_ui)
    welcome_button.pack()
    welcome_frame.pack(fill="both", expand=True, padx=12, pady=12)

    notebook = ttk.Notebook(root)

    def create_form_tab(title):
        tab = ttk.Frame(notebook, padding=12)
        notebook.add(tab, text=title)
        return tab

    add_tab = create_form_tab(t("tab_add"))
    actions_tab = create_form_tab(t("tab_actions"))
    reports_tab = create_form_tab(t("tab_reports"))
    data_tab = create_form_tab(t("tab_data"))

    add_left = ttk.LabelFrame(add_tab, text=t("doctor_data"), padding=10)
    add_mid = ttk.LabelFrame(add_tab, text=t("patient_data"), padding=10)
    add_right = ttk.LabelFrame(add_tab, text=t("staff_data"), padding=10)
    add_left.grid(row=0, column=0, padx=8, pady=8, sticky="nsew")
    add_mid.grid(row=0, column=1, padx=8, pady=8, sticky="nsew")
    add_right.grid(row=0, column=2, padx=8, pady=8, sticky="nsew")
    add_tab.columnconfigure((0, 1, 2), weight=1)

    def labeled_entry(parent, row, text):
        label = ttk.Label(parent, text=text)
        label.grid(row=row, column=0, sticky="w", pady=4)
        entry = ttk.Entry(parent)
        entry.grid(row=row, column=1, sticky="ew", padx=6, pady=4)
        parent.columnconfigure(1, weight=1)
        return label, entry

    doctor_id_label, doctor_id_entry = labeled_entry(add_left, 0, t("id"))
    doctor_name_label, doctor_name_entry = labeled_entry(add_left, 1, t("name"))
    doctor_contact_label, doctor_contact_entry = labeled_entry(add_left, 2, t("contact"))
    doctor_specialty_label, doctor_specialty_entry = labeled_entry(add_left, 3, t("specialization"))
    doctor_button = ttk.Button(add_left, text=t("save_doctor"), command=add_doctor)
    doctor_button.grid(row=4, column=1, sticky="e", pady=(8, 0))

    patient_id_label, patient_id_entry = labeled_entry(add_mid, 0, t("id"))
    patient_name_label, patient_name_entry = labeled_entry(add_mid, 1, t("name"))
    patient_contact_label, patient_contact_entry = labeled_entry(add_mid, 2, t("contact"))
    patient_button = ttk.Button(add_mid, text=t("save_patient"), command=add_patient)
    patient_button.grid(row=3, column=1, sticky="e", pady=(8, 0))

    staff_id_label, staff_id_entry = labeled_entry(add_right, 0, t("id"))
    staff_name_label, staff_name_entry = labeled_entry(add_right, 1, t("name"))
    staff_contact_label, staff_contact_entry = labeled_entry(add_right, 2, t("contact"))
    staff_position_label, staff_position_entry = labeled_entry(add_right, 3, t("position"))
    staff_button = ttk.Button(add_right, text=t("save_staff"), command=add_staff)
    staff_button.grid(row=4, column=1, sticky="e", pady=(8, 0))

    appointment_frame = ttk.LabelFrame(actions_tab, text=t("appointment"), padding=10)
    diagnosis_frame = ttk.LabelFrame(actions_tab, text=t("diagnosis"), padding=10)
    medication_frame = ttk.LabelFrame(actions_tab, text=t("medication"), padding=10)
    appointment_frame.grid(row=0, column=0, padx=8, pady=8, sticky="nsew")
    diagnosis_frame.grid(row=0, column=1, padx=8, pady=8, sticky="nsew")
    medication_frame.grid(row=0, column=2, padx=8, pady=8, sticky="nsew")
    actions_tab.columnconfigure((0, 1, 2), weight=1)

    app_doctor_label = ttk.Label(appointment_frame, text=t("doctor"))
    app_doctor_label.grid(row=0, column=0, sticky="w", pady=4)
    appointment_doctor_combo = ttk.Combobox(appointment_frame, state="readonly")
    appointment_doctor_combo.grid(row=0, column=1, padx=6, pady=4, sticky="ew")
    app_patient_label = ttk.Label(appointment_frame, text=t("patient"))
    app_patient_label.grid(row=1, column=0, sticky="w", pady=4)
    appointment_patient_combo = ttk.Combobox(appointment_frame, state="readonly")
    appointment_patient_combo.grid(row=1, column=1, padx=6, pady=4, sticky="ew")
    app_staff_label = ttk.Label(appointment_frame, text=t("staff"))
    app_staff_label.grid(row=2, column=0, sticky="w", pady=4)
    appointment_staff_combo = ttk.Combobox(appointment_frame, state="readonly")
    appointment_staff_combo.grid(row=2, column=1, padx=6, pady=4, sticky="ew")
    app_date_label, appointment_date_entry = labeled_entry(appointment_frame, 3, t("date"))
    app_time_label, appointment_time_entry = labeled_entry(appointment_frame, 4, t("time"))
    appointment_button = ttk.Button(appointment_frame, text=t("confirm_appointment"), command=schedule_appointment)
    appointment_button.grid(row=5, column=1, sticky="e", pady=(8, 0))

    diag_doctor_label = ttk.Label(diagnosis_frame, text=t("doctor"))
    diag_doctor_label.grid(row=0, column=0, sticky="w", pady=4)
    diagnose_doctor_combo = ttk.Combobox(diagnosis_frame, state="readonly")
    diagnose_doctor_combo.grid(row=0, column=1, padx=6, pady=4, sticky="ew")
    diag_patient_label = ttk.Label(diagnosis_frame, text=t("patient"))
    diag_patient_label.grid(row=1, column=0, sticky="w", pady=4)
    diagnose_patient_combo = ttk.Combobox(diagnosis_frame, state="readonly")
    diagnose_patient_combo.grid(row=1, column=1, padx=6, pady=4, sticky="ew")
    diag_entry_label, diagnosis_entry = labeled_entry(diagnosis_frame, 2, t("diagnosis"))
    diagnosis_button = ttk.Button(diagnosis_frame, text=t("save_diagnosis"), command=diagnose_patient)
    diagnosis_button.grid(row=3, column=1, sticky="e", pady=(8, 0))

    med_doctor_label = ttk.Label(medication_frame, text=t("doctor"))
    med_doctor_label.grid(row=0, column=0, sticky="w", pady=4)
    med_doctor_combo = ttk.Combobox(medication_frame, state="readonly")
    med_doctor_combo.grid(row=0, column=1, padx=6, pady=4, sticky="ew")
    med_patient_label = ttk.Label(medication_frame, text=t("patient"))
    med_patient_label.grid(row=1, column=0, sticky="w", pady=4)
    med_patient_combo = ttk.Combobox(medication_frame, state="readonly")
    med_patient_combo.grid(row=1, column=1, padx=6, pady=4, sticky="ew")
    med_entry_label, medicine_entry = labeled_entry(medication_frame, 2, t("medicine"))
    medication_button = ttk.Button(medication_frame, text=t("save_prescription"), command=prescribe_medication)
    medication_button.grid(row=3, column=1, sticky="e", pady=(8, 0))

    report_top = ttk.Frame(reports_tab)
    report_top.pack(fill="x", pady=(0, 8))
    report_doctor_label = ttk.Label(report_top, text=t("doctor"))
    report_doctor_label.pack(side="left")
    report_doctor_combo = ttk.Combobox(report_top, state="readonly", width=28)
    report_doctor_combo.pack(side="left", padx=8)
    report_button = ttk.Button(report_top, text=t("show_patients"), command=show_doctor_patients)
    report_button.pack(side="left")

    report_tree = ttk.Treeview(reports_tab, columns=("id", "name", "contact"), show="headings", height=9)
    for col, text, width in [("id", t("id"), 120), ("name", t("name"), 220), ("contact", t("contact"), 240)]:
        report_tree.heading(col, text=text)
        report_tree.column(col, width=width, anchor="w")
    report_tree.pack(fill="both", expand=True)

    history_top = ttk.Frame(reports_tab)
    history_top.pack(fill="x", pady=(10, 6))

    history_label = ttk.Label(history_top, text=t("patient_record"))
    history_label.pack(side="left", padx=(0, 10))
    history_patient_combo = ttk.Combobox(history_top, state="readonly", width=28)
    history_patient_combo.pack(side="left", padx=(0, 8))
    history_button = ttk.Button(history_top, text=t("show_record"), command=show_patient_medical_data)
    history_button.pack(side="left")

    history_notebook = ttk.Notebook(reports_tab)
    history_notebook.pack(fill="both", expand=True, pady=(0, 8))

    history_tab_diag = ttk.Frame(history_notebook, padding=8)
    history_tab_pres = ttk.Frame(history_notebook, padding=8)
    history_tab_apps = ttk.Frame(history_notebook, padding=8)

    history_notebook.add(history_tab_diag, text=t("history_diag"))
    history_notebook.add(history_tab_pres, text=t("history_pres"))
    history_notebook.add(history_tab_apps, text=t("history_apps"))

    history_diagnosis_tree = ttk.Treeview(history_tab_diag, columns=("diagnosis",), show="headings", height=10)
    history_diagnosis_tree.heading("diagnosis", text=t("details"))
    history_diagnosis_tree.column("diagnosis", width=520, anchor="w")
    history_diagnosis_tree.pack(fill="both", expand=True)

    history_prescriptions_tree = ttk.Treeview(history_tab_pres, columns=("medicine",), show="headings", height=10)
    history_prescriptions_tree.heading("medicine", text=t("medicine"))
    history_prescriptions_tree.column("medicine", width=520, anchor="w")
    history_prescriptions_tree.pack(fill="both", expand=True)

    history_appointments_tree = ttk.Treeview(
        history_tab_apps,
        columns=("doctor", "date", "time", "status"),
        show="headings",
        height=10,
    )
    for col, text, width in [
        ("doctor", t("doctor"), 200),
        ("date", t("date"), 120),
        ("time", t("time"), 110),
        ("status", t("state"), 120),
    ]:
        history_appointments_tree.heading(col, text=text)
        history_appointments_tree.column(col, width=width, anchor="w")
    history_appointments_tree.pack(fill="both", expand=True)

    data_top = ttk.Frame(data_tab)
    data_top.pack(fill="x", pady=(0, 8))
    refresh_button = ttk.Button(data_top, text=t("refresh_tables"), command=refresh_ui)
    refresh_button.pack(side="left")
    delete_button = ttk.Button(data_top, text=t("delete_selected"), command=delete_selected_from_current_tab)
    delete_button.pack(side="left", padx=(8, 0))

    data_notebook = ttk.Notebook(data_tab)
    data_notebook.pack(fill="both", expand=True)

    doctors_frame = ttk.Frame(data_notebook, padding=8)
    patients_frame = ttk.Frame(data_notebook, padding=8)
    staff_frame = ttk.Frame(data_notebook, padding=8)
    appointments_frame = ttk.Frame(data_notebook, padding=8)
    data_notebook.add(doctors_frame, text=t("tab_doctors"))
    data_notebook.add(patients_frame, text=t("tab_patients"))
    data_notebook.add(staff_frame, text=t("tab_staff"))
    data_notebook.add(appointments_frame, text=t("tab_appointments"))

    doctors_tree = ttk.Treeview(doctors_frame, columns=("id", "name", "spec", "contact"), show="headings", height=14)
    for col, text, width in [("id", t("id"), 80), ("name", t("name"), 180), ("spec", t("specialization"), 180), ("contact", t("contact"), 220)]:
        doctors_tree.heading(col, text=text)
        doctors_tree.column(col, width=width, anchor="w")
    doctors_tree.pack(fill="both", expand=True)

    patients_tree = ttk.Treeview(patients_frame, columns=("id", "name", "contact"), show="headings", height=14)
    for col, text, width in [("id", t("id"), 90), ("name", t("name"), 240), ("contact", t("contact"), 260)]:
        patients_tree.heading(col, text=text)
        patients_tree.column(col, width=width, anchor="w")
    patients_tree.pack(fill="both", expand=True)

    staff_tree = ttk.Treeview(staff_frame, columns=("id", "name", "position"), show="headings", height=14)
    for col, text, width in [("id", t("id"), 90), ("name", t("name"), 240), ("position", t("position"), 220)]:
        staff_tree.heading(col, text=text)
        staff_tree.column(col, width=width, anchor="w")
    staff_tree.pack(fill="both", expand=True)

    appointments_tree = ttk.Treeview(
        appointments_frame,
        columns=("patient", "doctor", "date", "time", "status"),
        show="headings",
        height=14,
    )
    for col, text, width in [
        ("patient", t("patient"), 180),
        ("doctor", t("doctor"), 180),
        ("date", t("date"), 130),
        ("time", t("time"), 110),
        ("status", t("state"), 120),
    ]:
        appointments_tree.heading(col, text=text)
        appointments_tree.column(col, width=width, anchor="w")
    appointments_tree.pack(fill="both", expand=True)

    footer = ttk.Frame(root, padding=(12, 6))
    footer.pack(fill="x")
    ttk.Label(footer, textvariable=status_var).pack(side="left")
    exit_button = ttk.Button(footer, text=t("exit"), command=root.destroy)
    exit_button.pack(side="right")

    try:
        load_data()
        set_status(t("data_loaded"))
    except Exception:
        set_status(t("data_load_failed"))

    apply_language()
    refresh_ui()
    root.protocol("WM_DELETE_WINDOW", lambda: (save_data(), root.destroy()))
    root.mainloop()


if __name__ == "__main__":
    build_gui()

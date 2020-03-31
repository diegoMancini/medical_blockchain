import hashlib
import uuid


class MedicalPatient:

    first_name = ''
    last_name = ''
    dni = ''
    medical_insurance = ''
    medical_insurance_plan = ''
    medical_insurance_member_number = ''
    city = ''
    province = ''
    country = ''
    phone = ''
    email = ''

    def __init__(self, first_name, last_name, dni, medical_insurance,
                 medical_insurance_plan, medical_insurance_member_number, city,
                 province, country, phone=None, email=None, patient_id=uuid.uuid1()):

        self.first_name = first_name
        self.last_name = last_name
        self.full_name = self.get_full_name()
        self.dni = dni
        self.medical_insurance = medical_insurance
        self.medical_insurance_plan = medical_insurance_plan
        self.medical_insurance_member_number = medical_insurance_member_number
        self.city = city
        self.province = province
        self.country = country
        self.location = self.get_location()
        self.phone = phone
        self.email = email
        self.patient_id = patient_id

        self.hash = self.get_hash()

    def get_hash(self):
        header_binary = (
                str(self.dni) +
                str(self.medical_insurance_member_number) +
                str(self.email) +
                str(self.province[0:2]) +
                str(self.patient_id)
        ).encode()

        inner_hash = hashlib.sha256(header_binary).hexdigest().encode()
        outer_hash = hashlib.sha256(inner_hash).hexdigest()

        return outer_hash

    def get_location(self):
        return {
            'city': self.city,
            'province': self.province,
            'country': self.country
        }

    def get_full_name(self):
        return f"{self.first_name.title()} {self.last_name.title()}"
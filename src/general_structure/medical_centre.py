import hashlib
import uuid


class MedicalCentre:

    name = ''
    social_reason = ''
    cuit = ''
    city = ''
    province = ''
    country = ''
    email = ''
    phone = ''
    medical_centre_registry_number = ''

    def __init__(self, name, social_reason, cuit, city, province, country,
                 medical_centre_registry_number, email=None, phone=None, medical_centre_id=uuid.uuid1()):

        self.medical_centre_id = medical_centre_id
        self.name = name
        self.social_reason = social_reason
        self.cuit = cuit
        self.city = city
        self.province = province
        self.country = country
        self.location = self.get_location()
        self.medical_centre_registry_number = medical_centre_registry_number
        self.email = email
        self.phone = phone

        self.hash = self.get_hash()

    def get_hash(self):
        header_binary = (
                str(self.cuit) +
                str(self.medical_centre_registry_number)
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



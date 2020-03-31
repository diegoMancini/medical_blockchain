import hashlib
import uuid


class Medic:

    first_name = ''
    last_name = ''
    specialty = ''
    dni = ''
    nro_matricula_nacional = ''
    nro_matricula_provincial = ''
    email = ''
    city = ''
    province = ''
    country = ''

    def __init__(self, first_name, last_name, specialty, dni, nro_matricula_nacional
                 , nro_matricula_provincial, email, city, province, country='Arg', birthday=None, medic_id=uuid.uuid1()):

        self.medic_id = medic_id
        self.first_name = first_name
        self.last_name = last_name
        self.full_name = self.get_full_name()
        self.specialty = specialty
        self.dni = dni
        self.nro_matricula_nacional = nro_matricula_nacional
        self.nro_matricula_provincial = nro_matricula_provincial
        self.email = email
        self.city = city
        self.province = province
        self.country = country
        self.location = self.get_location()

        self.birthday = birthday

        self.hash = self.get_hash()

    def get_hash(self):
        header_binary = (
                str(self.dni) +
                str(self.nro_matricula_nacional) +
                str(self.nro_matricula_provincial) +
                str(self.province[0:2]) +
                str(self.medic_id)
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

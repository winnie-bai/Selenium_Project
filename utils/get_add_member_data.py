from faker import Faker


class GetFakerData:

    def __init__(self):
        self.fk = Faker(locale="zh-CN")

    def get_random_name(self):
        return self.fk.name()

    def get_random_id(self):
        return self.fk.ssn()

    def get_random_phone(self):
        return self.fk.phone_number()

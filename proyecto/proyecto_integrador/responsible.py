class Responsible:
    def __init__(self,dni:int,name,last_name,email,phone):
      self.__dni=dni
      self.name=name
      self.last_name=last_name
      self._email=email
      self.phone=phone

    def get_dni(self):
      return self.__dni

    def get_email(self):
      return self._email


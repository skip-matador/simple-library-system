# patron.py

class Patron:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id

    def display(self):
        print(f"Name: {self.name}, Member ID: {self.member_id}")

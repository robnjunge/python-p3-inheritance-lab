#!/usr/bin/env python3


from user import User
import random

class Teacher(User):
    def __init__(self, first_name, last_name, knowledge=None):
        super().__init__(first_name, last_name)
        self.knowledge = knowledge if knowledge is not None else []


    def teach(self):
        if self.knowledge:
            get_random = random.randint(0, len(self.knowledge) - 1)
            return self.knowledge[get_random]
        else:
            raise Exception("No knowledge to teach")

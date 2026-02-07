from config import TESTER_BURNOUT_THRESHOLD


class Tester:
    def __init__(self):
        self.pay_rate = 80, 000
        self.burnout = 0
        self.skill = 0
        self.specialized_code_modules = []

    def specialize_code_module(self, code_module):
        # TODO: Implement specialization logic
        # this should affect how easy/difficult to test
        # a new feature
        # (thinking can probaby average the skill level of the testers
        # assigned to the feature)
        self.specialized_code_modules.append((code_module, self.skill))

    def is_burnt_out(self):
        return self.burnout > TESTER_BURNOUT_THRESHOLD

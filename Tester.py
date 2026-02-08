from config import TESTER_BURNOUT_THRESHOLD, TESTER_STARTING_PAY


class Tester:
    def __init__(self):
        self.pay_rate = TESTER_STARTING_PAY
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

    def __repr__(self):
        return f"Tester(pay_rate={self.pay_rate}, skill={self.skill}, burnout={self.burnout}, specialized_code_modules={self.specialized_code_modules})"

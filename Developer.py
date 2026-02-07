from config import DEVELOPER_BURNOUT_THRESHOLD


class Developer:
    def __init__(self):
        self.pay_rate = 100, 000
        self.burnout = 0
        self.skill = 0
        self.specialized_code_modules = []

    def specialize_code_module(self, code_module):
        # TODO: Implement specialization logic
        # this should affect how easy/difficult to develop
        # a new feature and how much technical debt is added
        # (thinking can probaby average the skill level of the developers
        # assigned to the feature)
        self.specialized_code_modules.append((code_module, self.skill))

    def is_burned_out(self):
        return self.burnout > DEVELOPER_BURNOUT_THRESHOLD

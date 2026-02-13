import random


class TeamMember:
    def __init__(self):
        self.pay_rate = 0
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
        return self.burnout > self.getBurnoutThreshold() and random.random() < 0.5

    def getBurnoutThreshold(self):
        # SHould be implemented by child classes
        return int(0)

    def __repr__(self):
        # Should be implemented by child classes
        return str("")

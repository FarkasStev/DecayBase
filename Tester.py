from config import TESTER_BURNOUT_THRESHOLD, TESTER_STARTING_PAY
from TeamMember import TeamMember


class Tester(TeamMember):
    def __init__(self):
        super().__init__()
        self.pay_rate = TESTER_STARTING_PAY

    def getBurnoutThreshold(self):
        return TESTER_BURNOUT_THRESHOLD

    def __repr__(self):
        return f"Tester(pay_rate={self.pay_rate}, skill={self.skill}, burnout={self.burnout}, specialized_code_modules={len(self.specialized_code_modules)})"

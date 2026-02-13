from config import DEVELOPER_BURNOUT_THRESHOLD, DEVELOPER_STARTING_PAY
from TeamMember import TeamMember


class Developer(TeamMember):
    def __init__(self):
        super().__init__()
        self.pay_rate = DEVELOPER_STARTING_PAY

    def getBurnoutThreshold(self):
        return DEVELOPER_BURNOUT_THRESHOLD

    def __repr__(self):
        return f"Developer(pay_rate={self.pay_rate}, skill={self.skill}, burnout={self.burnout}, specialized_code_modules={len(self.specialized_code_modules)})"

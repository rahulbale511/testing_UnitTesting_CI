class CheckRobotStateMachine:

    def __init__(self, current_battery_p, current_state):
        self.current_battery_p = current_battery_p
        self.current_state = current_state

    def increase_battery(self, inc_current_bt_p):
        self.current_battery_p += inc_current_bt_p

    def update_current_state(self, upd_current_state):
        self.current_state = upd_current_state


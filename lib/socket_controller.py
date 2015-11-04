import pimote
from scheduler import Scheduler


class SocketController(object):
    state = {
        1: False,
        2: False,
        3: False,
        4: False,
    }

    action_dict = {
        '1': ('1-on', '1-off'),
        '2': ('2-on', '2-off'),
        '3': ('3-on', '3-off'),
        '4': ('4-on', '4-off'),
    }

    def __init__(self, config):
        if getattr(config, 'ICAL_URL', None):
            self.scheduler = Scheduler(config.ICAL_URL,
                                       self._switch_by_code,
                                       self.action_dict,
                                       polling_interval=config.POLLING_INTERVAL)
        else:
            self.scheduler = None

    def start(self):
        pimote.init()
        pimote.switch('all-off')
        if self.scheduler:
            self.scheduler.start()

    def stop(self):
        if self.scheduler:
            self.scheduler.stop()
        pimote.term()

    def _switch_by_code(self, code):
        getattr(self, 'switch_' + code.replace("-", "_"))()

    def switch_1_on(self):
        if pimote.switch('1-on'):
            self.state[1] = True

    def switch_1_off(self):
        if pimote.switch('1-off'):
            self.state[1] = False

    def switch_2_on(self):
        if pimote.switch('2-on'):
            self.state[2] = True

    def switch_2_off(self):
        if pimote.switch('2-off'):
            self.state[2] = False

    def switch_3_on(self):
        if pimote.switch('3-on'):
            self.state[3] = True

    def switch_3_off(self):
        if pimote.switch('3-off'):
            self.state[3] = False

    def switch_4_on(self):
        if pimote.switch('4-on'):
            self.state[4] = True

    def switch_4_off(self):
        if pimote.switch('4-off'):
            self.state[4] = False

    def switch_all_on(self):
        if pimote.switch('all-on'):
            self.state[1] = True
            self.state[2] = True
            self.state[3] = True
            self.state[4] = True

    def switch_all_off(self):
        if pimote.switch('all-off'):
            self.state[1] = False
            self.state[2] = False
            self.state[3] = False
            self.state[4] = False

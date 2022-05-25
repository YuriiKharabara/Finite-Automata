"""Making big project simulatiom"""

import random
import time

from matplotlib.pyplot import get


class Simulator:
    """Simulator class"""
    def __init__(self):
        """Constructor"""
        self.hour = 0
        self.task_to_do = 700
        self.project_failed = False
        self.events = [Event().air_alert, Event().feedback, Event().beer_ended]
        self.status = currentState()
        self.previous_line = ''

    def run(self):
        """run the simulation
        """
        print('This is a simulation of me completing some project.\
 I have to make 700 tasks to complete project successfully. I do 10 task during studying, \
and lose time if some bad events happens.')

        for i in [10,9,8,7,6,5,4,3,2,1,0]:
            print(f'\rWe will begin in {i} seconds', end = '')
            time.sleep(1)
        print(f"\n\n{' '*10}Let's go!\n\n")
        
        self.day_of_month = 1
        while not self.project_failed:
            self.next_hour()
            self.random_event(self.status)
            if self.task_to_do <= self.status.tasks_done:
                self.task_to_do = self.status.tasks_done
                self.project_failed = 'Ended'
            if self.project_failed == 'Ended':
                self.status.mood = True
                print(self, '\nGoing to bed!')
                print('\n\nTask completed successfully\n\n')
                return True
                break
            print(self, end='')
            self.previous_line = '\n' + str(self)[1:]
            # print()

            if self.project_failed:
                print('\nProject failed.')
            if self.hour == 24:
                self.hour = 0
                self.day_of_month += 1
                self.status.mood = True
                print('\nSweet dreams!')
            if self.day_of_month == 31:
                if self.status.tasks_done < self.task_to_do:
                    self.project_failed = True
                    print('\nTask failed successfully\n')
                else:
                    print('\nTask completed successfully\n')
                    return True
                    break

            time.sleep(1)

    def next_hour(self):
        """Changes routine and hour to the next
        """
        status = self.status.get_current_state(self.hour)
        self.hour += 1

    def random_event(self, status):
        """Choose a random event"""
        random_event = random.choice(self.events)
        random_event(self.hour, self.status)

    def __str__(self):
        """String representation of the status"""
        hour = str(self.hour % 12)
        hour += ' AM' if self.hour < 12 else ' PM'
        if self.hour == 12:
            hour = '12 AM'
        status = self.status.current_state
        if status == 'beer' or status == 'whiskey'or status == 'family':
            status =  f"It's time for {self.status.current_state}."
        else:
            status = "I'm " + status + 'ing'
        line = f"\nIt is {self.day_of_month}th day. {hour} and I'm in {'good' if self.status.mood == True else 'bad'} mood. {status} right now. There is {self.status.tasks_done} tasks done and {self.task_to_do-self.status.tasks_done} tasks left."
        
        # Just help to create \r line. If nothing changed except time during sleeping
        if self.status.current_state == 'sleep' and self.previous_line == f"\nIt is {self.day_of_month}th day. {str(int(hour.split(' ')[0])-1)} AM and I'm in {'good' if self.status.mood == True else 'bad'} mood. {status} right now. There is {self.status.tasks_done} tasks done and {self.task_to_do-self.status.tasks_done} tasks left.":
            line = f"\rIt is {self.day_of_month}th day. {hour} and I'm in {'good' if self.status.mood == True else 'bad'} mood. {status} right now. There is {self.status.tasks_done} tasks done and {self.task_to_do-self.status.tasks_done} tasks left."
        return line


class Phase:
    """Phase"""
    def __init__(self, hour, status):
        """Constructor and choosing phase"""
        self.flag = False
        self.this_phase = False
        if status.current_state == 'hid':
            self.air_alarm_failure(hour, status)
            if status.current_state == 'hid':
                return None
        while self.this_phase != True:
            self.sleeping(hour, status)
            if self.flag == True:
                self.flag = False
                break
            self.eating(hour, status)
            if self.flag == True:
                self.flag = False
                break
            self.studying(hour, status)
            if self.flag == True:
                self.flag = False
                break
            self.outgoing(hour, status)
            if self.flag == True:
                self.flag = False
                break
            self.family_gathering(hour, status)
            if self.flag == True:
                self.flag = False
                break
            self.beer_whiskey_drinking(hour, status)
            if self.flag == True:
                self.flag = False
                break

    def sleeping(self, hour, status):
        """check whether the status should be sleeping"""
        if hour >= 0 and hour < 7:
            status.current_state = 'sleep'
            self.this_phase = True
            self.flag = True

    def eating(self, hour, status):
        """check whether the status should be eating"""
        if hour == 7 or hour == 14 or hour == 21:
            status.current_state = 'eat'
            self.this_phase = True
            self.flag = True

    def studying(self, hour, status):
        """check whether the status should be studying"""
        if hour >= 8 and hour <= 17:
            status.current_state = 'study'
            status.tasks_done += 3
            self.this_phase = True
            self.flag = True

    def outgoing(self, hour, status):
        """check whether the status should be outgoing"""
        if hour > 17 and hour <= 19:
            status.current_state = 'walk'
            self.this_phase = True
            self.flag = True

    def family_gathering(self, hour, status):
        """check whether the status should be family gathering"""
        if hour > 19 and hour <= 20:
            status.current_state = 'family'
            self.this_phase = True
            self.flag = True

    def beer_whiskey_drinking(self, hour, status):
        """check whether the status should be beer or whiskey drinking"""
        if hour > 20 and hour <= 24:
            if status.mood is True:
                status.current_state = 'beer'
            else:
                status.current_state = 'whiskey'
            self.this_phase = True
            self.flag = True

    def air_alarm_failure(self, hour, status):
        """check whether air alarm should end"""
        if random.random() < 0.6:
            status.current_state = 'end of alarm'
            print('\nAir alert ended!', end ='')
            
            


class Event:
    """Event"""
    def air_alert(self, hour, status):
        """check whether air alert should start"""
        if random.random() < 0.1 and status.current_state != 'hid':
            status.current_state = 'hid'
            status.mood = False
            print('\nAIR ALERT!', end='')

    def feedback(self, hour, status):
        """check whether feedback should be done"""
        if random.random() < 0.07 and (hour >= 8 or hour <= 1):
            status.mood = False
            if status.tasks_done >= 5:
                status.tasks_done -= 5  # delay because of the bad mood
            print('\nOh, bad grade for test :( Delay because of the bad mood', end='')
        elif hour >= 8 or hour <= 1:
            print('\nHaha, good grade for test :)', end ='')
            status.mood = True

    def beer_ended(self, hour, status):
        """check whether beer ended"""
        if random.random() < 0.1 and status.current_state == 'beer':
            if status.tasks_done >= 10:
                status.tasks_done -= 10  # delay because beer has ended
            status.current_state = 'sleep'
            status.mood = False
            print('\nAh shit, beer ended. Delay because beer has ended', end = '')


class currentState:
    """current state"""
    def __init__(self, current_state=None):
        """Initialize"""
        self.current_state = current_state or None
        self.tasks_done = 0
        self.mood = True

    def __str__(self):
        """Returns representation of current state"""
        return str(self.current_state)

    def get_current_state(self, hour):
        """Gets current state"""
        Phase(hour, self)
        return self.current_state

if __name__ == '__main__':
    my_life = Simulator()
    my_life.run()

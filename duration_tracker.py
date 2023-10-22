from datetime import datetime

class Timer():

    '''
    Tracker to measure multiple different timestamps, starting and stopping at various points
    Use the same identifier to link the start/stop times together

    Methods:
        ► Start: Initialise the stopwatch | Identifier = String text
        ► end: Stop the stopwatch | Identifier = String text
        ► Results: Calculate the duration from all start/stop timestamps and return the results table

	'''

    def __init__(self):
        self.timers = {}

    def start(self, identifier):
        '''
        Initialise a timer and update the dict
        Param: identifier (str) | Name for the specific time
        '''
        if self.timers.get(identifier) is None:
            self.timers.update({identifier: {'start': datetime.now()}})
        else:
            raise KeyError(f"The timer '{identifier}' already exists. Choose a new name")

    def end(self, identifier):
        '''
        End a timer and update the dict
        Param: identifier (str) | Name for the specific time. Must already exist
        '''
        if self.timers.get(identifier) is not None:
            self.timers[identifier].update({'end': datetime.now()})
            self._parse_duration(identifier)
        else:
            raise KeyError(f"The timer '{identifier}' has not been initialised yet")

    def _parse_duration(self, identifier):
        '''
        Calculate duration and update the dict
        Param: identifier (str) | Name for the specific time. Must already exist
        '''
        delta = self.timers[identifier]['end'] - self.timers[identifier]['start']
        self.timers[identifier].update({'duration': delta.total_seconds()})

    def results(self):
        '''
        Calculates the durations and returns a dict featuring the name of the timer and duration
        in seconds
        '''
        return {k: str(f"{v['duration']}s") for k,v in self.timers.items()}
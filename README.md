# duration-tracker

Duration tracker is a Python class containing methods for tracking the duration of various activities. The same object can be used to track the duration of several concurrent activities, and will output a dictionary with the identifier and duration afterwards using the results() method.

## Requirements

None. Uses standard library alone

## How to Use

Initialise with: `T = duration_tracker()`

To start a timer: `T.start(identifier_name)`

To end a time: `T.end(identifier_name)`

To show results: `T.results(identifier_name)`

## Example

```python
from duration_tracker import Timer

# Initialise timer object
timer = Timer()

# Initialise several timers
timer.start('Timer 1')
timer.start('Timer 2')
timer.start('Timer 3')

# End each of the timers after (time.sleep() shown here)
sleep(1)
timer.end('Timer 1')
sleep(1)
timer.end('Timer 2')
sleep(1)
timer.end('Timer 3')

# Results method used to get a dictionary of each timer and the duration in seconds
results = timer.results()
``````


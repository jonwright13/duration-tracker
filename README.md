# duration-tracker

Duration tracker is a Python class containing methods for tracking the duration of various activities. The same object can be used to track the duration of several concurrent activities, and will output a Pandas DataFrame with the results afterwards.

## Requirements

This only requires Pandas to use

## How to Use

Initialise with: `T = duration_tracker()`

To start a timer: `T.start(identifier_name)`

To end a time: `T.end(identifier_name)`

To show results: `T.results(identifier_name)`


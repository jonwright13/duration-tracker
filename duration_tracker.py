import pandas as pd

class duration():
	'''
		Tracker to measure multiple different timestamps, starting and stopping at various points
		Use the same identifier to link the start/stop times together

		Methods:
			► Start: Initialise the stopwatch | Identifier = String text
			► end: Stop the stopwatch | Identifier = String text
			► Results: Calculate the duration from all start/stop timestamps and return the results table

	'''

	duration_columns = ["Action", "Duration", "Start Time", "End Time"]
	duration_df = pd.DataFrame(columns=duration_columns)

	def start(self, identifier):
    # Start timer for specific identifier name
		timestamp = pd.Timestamp.now()
		data = {
                "Action": identifier, 
                "Duration": float(0), 
                "Start Time": timestamp, 
                "End Time": float(0)
                }

		self.duration_df = self.duration_df.append(data,ignore_index=True)

	def end(self, identifier):
    # End timer for specific identifier
		timestamp = pd.Timestamp.now()
		index = self.duration_df.index[self.duration_df["Action"] == identifier]

		self.duration_df.at[index, "End Time"] = timestamp
		self.duration_df.at[index, "Duration"] = timestamp - self.duration_df.iloc[index]["Start Time"]

	def results(self):
    # Display results for all timers
		self.duration_df["Duration"] = self.duration_df.apply(lambda row: pd.Timedelta(row["Duration"]).total_seconds(), axis=1)
		return self.duration_df[["Action", "Duration"]]

if __name__ == '__main__':
    pass

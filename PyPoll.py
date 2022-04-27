import datetime as dt
import os
import csv

#filename variable to path to file
file_to_load = os.path.join("Resources","election_results.csv")
file_to_save = os.path.join("Analysis","election_analysis.txt")

# open the election results and read the file
with open(file_to_load) as election_data:

        # read file object with reader function
        file_reader = csv.reader(election_data)

        #exclude headers
        headers = next(file_reader)

        for row in file_reader:

            

            



# open election results and read the file


# use the now() attribute in datetime class to get the present time

now = dt.datetime.now()

# print the present time

print("The time right now is ",now)

# total number of votes cast
# complete list of candidates who received votes
# total number of votes each candidate received
# percentage of votes each candidate won
# the winner of election based on popular vote


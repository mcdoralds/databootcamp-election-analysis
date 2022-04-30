import datetime as dt
import os
import csv

# filename variable results spreadsheet & analysis doc
file_to_load = os.path.join("Resources","election_results.csv")
file_to_save = os.path.join("Analysis","election_analysis.txt")

# initialize total vote counter
total_votes = 0

# initialize candidate options list
candidate_options = []

# initalize candidate votes dict
candidate_votes = {}

# initialize winner stat variables
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# open the election results and read the file
with open(file_to_load) as election_data:

        # read file object with reader function
        file_reader = csv.reader(election_data)

        # read headers
        headers = next(file_reader)
        
        # "for each row in the csv file..."
        for row in file_reader:

                # "... add one vote to the vote tally"
                total_votes += 1

                # print candidate name from each row
                candidate_name = row[2]

                # If the candidate does not match any existing candidate...
                if candidate_name not in candidate_options:
                        # Add it to the list of candidates.
                        candidate_options.append(candidate_name)

                        # begin tracking candidate's vote count
                        candidate_votes[candidate_name] = 0

                # add a vote for that particular candidate
                candidate_votes[candidate_name] += 1



# iterate through candidate list
for candidate_name in candidate_votes:

        # Retrieve vote coutn of a candidate
        votes = candidate_votes[candidate_name]

        # calculate the percentage of votes
        vote_percentage = float(votes) / float(total_votes) * 100

        # print the candidate name and percentage of votes
        print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # determine winning vote
        # step 1: determine if current votes are greater than winning count

        if (votes > winning_count) and (vote_percentage > winning_percentage):

                winning_count = votes
                winning_percentage = vote_percentage
                
                # And, set the winning_candidate equal to the candidate's name.

                winning_candidate = candidate_name

winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)

                


                


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


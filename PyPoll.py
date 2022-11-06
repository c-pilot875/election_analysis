# The data we need to retrieve.
# 1. The total number of votes cast
# 2. A complete list of candidates who recieved votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election base on popular vote.

#Direct path below
# Assign a variable for the file to load and the path.
#file_to_load = 'Resources/election_results.csv'
# open the election results and read the file.
#with open(file_to_load) as election_data:

#to do: perform analysis.

    #print(election_data)

#Indirect path
import csv
import os
#Assign a variable for the file to load and path
file_to_load = os.path.join("Resources", "election_results.csv")
#Open the election results and read the file.
with open(file_to_load, "r") as election_data:
    print(election_data)

import csv
import os

# Create a filename variable to a direct or indirect path to the file
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Using the open() functionn with the "w" mode we will write data to the file
open(file_to_save, "w")

#Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Use the open statement to open the file as a text file.
#outfile = open(file_to_save, "w")
#2 - use the with statement open the file as a text file
with open(file_to_save, "w") as txt_file:

#Write some data to the file.
#outfile.write("Hello World")
# Write three counties to the file.
    txt_file.write("Counties in the Election\n---------------\nArapahoe\nDenver\nJefferson")

#Close the file
#outfile.close()

#1. add total vote counter
total_votes = 0
#Candidate options
candidate_options = []
#1. Declair an empty dictionary.
candidate_votes = {}
# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#Open the election results and read the file.
with open(file_to_load) as election_data:

    #To do: Read and analyse the data here.
    #read the file object with the reader function.
    file_reader = csv.reader(election_data)
    #print the header row but skip the first row.
    headers = next(file_reader)
    #print each row in the CSV file
    for row in file_reader:
        print(row)
        #Add to the total vote counter.
        total_votes += 1

        #print the candidate name for each row.
        candidate_name = row[2]
        
        #If the candidate does not match any exsisting candidate..
        if candidate_name not in candidate_options:
            #add it to the list of candidates.
            candidate_options.append(candidate_name)
            #2 Begin tracking that candiate's vote count
            candidate_votes[candidate_name] = 0
        # Add a vote tot that candidate's count. Move out of if statemnet but align.
        candidate_votes[candidate_name] += 1
# Determine the percentage of votes for each candidate by looping through the counts.
#1. Iterate through the candidate list.
for candidate_name in candidate_votes:
    #2 Retrieve the vote count of a candidate.
    votes = candidate_votes[candidate_name]
    #3 Calculate the percentage of votes.
    vote_percentage = float(votes) / float(total_votes) * 100

    #To do: print out each candidate's name,vote count, and percentage of votes to terminal
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

    #4 Print the candidate name and percentage of votes. add :.1f after vote_percentage to get to one decimal
    #print(f"{candidate_name}: recieved {vote_percentage:.1f}% of the vote.")
    #Determine winning vote count and candidate
    #Determin if the votes are greater than the winning count.
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        #If true then set winning_count = votes and winning_percentage = vote percentage
        winning_count = votes
        winning_percentage = vote_percentage
        # and, set the winning_candidate equal to the candidate's name.
        winning_candidate = candidate_name
winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")

#To do: print out the winning candidate, vote count and percentage to terminal

print(winning_candidate_summary)

#3. Print the total votes.
#print(total_votes)

#4. Print the candidate list.
#print(candidate_options)

#5. Print the candidate vote dictionary
#print(candidate_votes)










# 0. add our dependencies
import csv
import os

# 1. Assign a variable for the file to load and path
file_to_load = os.path.join("Resources", "election_results.csv")

# 1.2Assign a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

# 2. Add total vote counter
total_votes = 0
# 2.2 Candidate options and votes
candidate_options = []
# 2.3 Declair an empty dictionary.
candidate_votes = {}
# 2.4 Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# 3. Open the election results and read the file.
with open(file_to_load) as election_data:
    # 3.2 read the file object with the reader function.
    file_reader = csv.reader(election_data)
    # 3.3 read the header row but skip the first row.
    headers = next(file_reader)

    # 4. Loop through all the rows
    for row in file_reader:
        # 4.2 Add to the total vote counter.
        total_votes += 1

        # 4.3 print the candidate name for each row.
        candidate_name = row[2]
        
        # 4.4 If the candidate does not match any exsisting candidate..
        if candidate_name not in candidate_options:
            #add it to the list of candidates.
            candidate_options.append(candidate_name)
            #2 Begin tracking that candiate's vote count
            candidate_votes[candidate_name] = 0
        # 5. Add a vote to that candidate's count. Move out of if statemnet but align.
        candidate_votes[candidate_name] += 1

    # 6. save results to our text file
with open(file_to_save, "w") as txt_file:

    # 7. after opening the file print the final vote count to the terminal
    election_results = (
        f"\nElection Results\n"
        f"----------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"----------------------\n")
    print(election_results, end="")

# 8. After printing the final vote count, save the final vote count to the text file.
    txt_file.write(election_results)

    # 8. Determine the percentage of votes for each candidate by looping through the counts.
    for candidate_name in candidate_votes:
        # 8.2 Retrieve the vote count of a candidate.
        votes = candidate_votes[candidate_name]
        # 8.2 Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100

        # 8.3 To do: print out each candidate's name,vote count, and percentage of votes to terminal
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        # 8.4 print each candidate, their voter count, and percentage tot the terminal.
        print(candidate_results)
        # 8.5 save the candidate results to our text file.
        txt_file.write(candidate_results)

        # 9. Print the candidate name and percentage of votes. add :.1f after vote_percentage to get to one decimal
        # 9.2 Determine winning vote count and candidate
        # 9.3 Determin if the votes are greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # 9.4 If true then set winning_count = votes and winning_percentage = vote percentage
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage
    # 10. format and print the winning candidates' results to the terminal on their own line.
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)

    # 11. Save the winning candidate's name to the text file.
    txt_file.write(winning_candidate_summary)









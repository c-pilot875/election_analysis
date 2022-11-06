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
#Open the election results and read the file.
with open(file_to_load) as election_data:

    #To do: Read and analyse the data here.
    #read the file object with the reader function.
    file_reader = csv.reader(election_data)
    #print the header row but skip the first row.
    headers = next(file_reader)
    print(headers)
    





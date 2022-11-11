# election_analysis
## Project Overview and Purpose
Request by Colorado Board of Elections staff to complete the most recent election audit of the local congressional election. Specific requests listed below:
1. Calculate the total number of votes cast.
2. Get a complete list of candidates who recieved votes.
3. Calculate the total number of votes each candidate recieved.
4. Calculate the percentage of votes each candidate won.
5. Determine and display the winner of the election based on popular vote.
6. Calculate the county percentage and vote county
7. Determine the largest county

##Resources
- Data Source: election_results.csv
- Software: Python 3.7.6 performed on Mac VS Code

## Summary Analysis
The analysis of the election data display:
- There were 369,711 votes cast in the election
- Candidates
    - Charles Casper Stockham
    - Diana DeGette
    - Raymon Anthony Doane
- Candidate results
    - Charles Casper Stockham recieved 23.0% of the vote and 85,213 number of votes.
    - Candidate 2 recieved 73.8% of the vote and 272,892 number of votes.
    - Candidate 2 recieved 3.1 of the vote and 11,606 number of votes.
    
- County results
    - Jefferson: 10.5% (38,855)
    - Denver: 82.8% (306,055)
    - Arapahoe: 6.7% (24,801)
    
- Largest County : Denver

- Election Winner:
    - Diana DeGetter, who recieved 73.8% of the vote and 272,892 number of votes.
   
- ## Election Audit Summary Statement
The attached code can be used for any election by modiying the specific scripts below:
1. Import a differnt csv file to read with pd.read.csv

## Challenge Overview
This was my first attempt at writing code with Python. Compaired to VBA, Python was much easier to work with, organize, and spot bugs as they happened. Naming varibales, and tabbing for loops and if statements were much cleaner and easier to see. I can see the benifit of Python coding when it easily worked though hundreds of thousands of data points quickly and was able to notify about potential bugs before running the code.

## Challenge Summary.
The ability to join csv files, create and write txt files to output the finidings can be helpful for the end user and compiling a clean report. I ran into a particulare challenge with joining the original election_analysis.csv file from my Resources file. An error of file not foudn would pop up despite running the code before writing it to a txt file. This was resolved by.:
I also had a challenge with pushing my changes to the election_analysis file through my Terminal to my GitHub repositry. Having previously created a token in Pre-Work of this program I was not able to porperly link it through my terminal.

My final challenged was that somewhere in my final code I was no longer able to print the winning candidate name, winning vote count, or the correct winning percentage. After numerous attempts to locate the bug I was able to run original code from a previous challenge that mirrored my new code in this challenge and was able to get the winning information but still not able to produce it on my final code.

# Election_Analysis

## Project Overview
The client, an employee of the Colorado Board of Elections, has requested an audit of the recent local congressional election results. They've requested that we make a script to parse the raw voting data and print an analysis report that summarizes the most pertinent information election information. 

## Resources
- Data Source: election_results.csv
- Software: Python 3.10.4, Visual Studio Code, 1.66.2

## Summary
### Candidates
- The candidates running in the election were:
   - Charles C. Stockham
   - Diana DeGette
   - Raymon A. Doane
### Counties
- The counties included in this election were:
   - Jefferson
   - Denver
   - Araphoe
   
### Election-Audit Results
![Capture1](https://user-images.githubusercontent.com/31219195/166092610-594e13c0-3843-4699-aa70-fe0253df69fb.PNG)

As shown in the screenshot, the analysis of the election show that:
- There were 369,711 total votes cast in the election.


![Capture2](https://user-images.githubusercontent.com/31219195/166092630-de47356b-90cf-4189-870f-24785460de10.PNG)

- The county results were:
   - Jefferson had 10.5% of the vote with 38,855 total votes.
   - Denver had 82.8% of the vote with 306,055 total votes.
   - Arapahoe had 6.7% of the vote with 24,801 total votes.

- The county with the most votes was:
   - Denver


![Capture3](https://user-images.githubusercontent.com/31219195/166092635-9afd99fa-c6bf-44e7-be7a-0bf3fbc80f56.PNG)


- The candidate results were:
   - Charles C. Stockham received 23.0% of the vote with 85,213 total votes.

   - Diana DeGette received 73.8% of the vote with 8272,892 total votes.
   - Raymon A. Doane received 3.1% of the vote with 11,606 total votes.
   
- The winner of the election was:
   - Diana DeGette, who received 73.8% of the vote with 8272,892 total votes.

## Election Audit Summary
### Overview
This script is a tool to efficiently and accurately summarize large datasets and report on the data points of interest. This code provides the client with a turnkey solution to any and all future election audits, meaning it's extremely customizable and plug-and-play. 

### Modifiable code
The code was written so that it is easy to modify and customize. For example, switch file name to analyze another similarly formatted tabular dataset

![Capture5](https://user-images.githubusercontent.com/31219195/166093029-1ffa7c8f-17fe-4993-bd2b-b9458cf6d513.PNG)

Another example would be to use this script for applications even beyond governmental elections--- it can be a cheap solution for election audits for school boards or any other organization wanting to analyze vote breakdowns. The variables can be switched out to break down the voters' city, age group, gender, or any other metric.

### Sharable .txt analysis
In addition to printing the results in the terminal, the script also saves the information in an external text document that can easily be shared with any stakeholders or interested parties.

![Capture7](https://user-images.githubusercontent.com/31219195/166093199-65cd4499-0a7d-4f3b-a8a7-161fc70baa8c.PNG)



import csv
from functools import reduce
import matplotlib.pyplot as plt
import pandas as pd
'''
Here is the detailed objective of the code:
1. we are going to filter the data from the CSV file because we need only the countries in east africa
2. we are going to observe their credit status
3. based on their credit status we are going to give them a credit score
4. the credit score is to be classified as follows:
     i)   serious - Here a legal notice of discontinuation should be sent
     ii)  bad - A warning stating that the dues are to be cleared before renewing the contract or continuing some existing contracts
     iii) average - send add 0.05% of the service charge to the actual service charge rate
     iv)  good - issue more contracts in the country
     v)   excellent - deduct 0.05% of the service charge to the actual service charge rate
5. in order to interpret this a graph will be designed for a visual clarity and better conclusions
'''
def first_calling():

    list_if_east_african_countries = ['Kenya','Tanzania','Uganda','Ethiopia','Somalia','Rwanda','Burundi','South Sudan','Djibouti','Comoros','Madagascar','Malawi']
    def filtered_east_african_countries(row):
        if row[4] in list_if_east_african_countries:
            return (row)

    with open('IDA_Statement_Of_Credits_and_Grants_-_Historical_Data.csv','r') as csv_file:
        csv_reader = csv.reader(csv_file)
        header = next(csv_reader) # we skip the header file
        #print(header)
        filtered_outcomes = filter(filtered_east_african_countries, csv_reader)

        f = open('east_african_countrues_statement_of_credits_and_grants.csv','w',newline= '')
        writer = csv.writer(f)
        writer.writerow(header)
        for row in filtered_outcomes:
            writer.writerow(row)
        f.close()
    csv_file.close()

    # Till here the process of filteration is done successfully
    # Now we need to
    df = pd.read_csv('east_african_countrues_statement_of_credits_and_grants.csv', low_memory=False) # low_memory= false tells Pandas to read data  in CHUNKS
    unique_names = df['Credit Status'].unique()

    credit_status_to_score = {
        'Terminated': 0, #This suggests the process was stopped or ended due to issues
        'Fully Cancelled':1,#Complete cancellation, likely indicating a failure or significant problem.
        'Cancelled':2,#Begin cancellation, but not necessarily as serious as "Fully Cancelled."
        'Disbursing': 3,#Funds are being distributed, but the process is not complete
        'Disbursing&Repaying': 4,#Funds are being both disbursed and repaid, indicating some action but room for improvement.
        'Signed': 5,#Indicates that the agreement has been signed, showing progress but further actions are still pending.
        'Approved':6,#Approval stage, where things are beginning, but action hasn't been fully taken.
        'Average':7,#Agreement has been signed, but further steps are pending.
        'Effective':8,#The process is in effect, and things are progressing as planned.
        'Disbursed':9,#Funds have been disbursed, which is a positive and significant milestone.
        'Repaying':10,#Repayment is underway, indicating the process is going smoothly.
        'Fully Disbursed': 11,#All funds have been successfully disbursed, a very positive outcome.
        'Repaid':12,#The funds have been repaid, indicating a high level of success.
        'Fully Repaid':13#Everything is complete both disbursement and repayment representing the best possible outcome.
    }

    #Here we have mapped successfully the scores to the credit status
    df ['SCORE ALLOCATION'] = df['Credit Status'].map(credit_status_to_score)


    '''
    to make my excel sheet more clean and more readable
    I decided to sort them based on the countries
    '''

    unique_country_names = df['Country'].unique() # get the unique contries from this column
    df['Country'] = pd.Categorical(df['Country'], categories=unique_country_names, ordered=True)
    # telling the computer, "Hey, let's turn this list of country names into a set of items that have a special order."
    df = df.sort_values(by='Country') # sorting these values by country

    df.to_csv('east_african_countrues_statement_of_credits_and_grants.csv', index=False)

    df = pd.read_csv('east_african_countrues_statement_of_credits_and_grants.csv', low_memory=False)

    grouping = df.groupby('Country') #This means all rows with the same country will be considered as a group.
    listed_credit_score=[]
    for country, group in grouping:
        credit_scores = group['SCORE ALLOCATION'].tolist()
        total_score = reduce(lambda x, y: x + y, credit_scores)
        listed_credit_score.append((country, total_score))

    # now that we have a listed credit score we need to amake it visible to people from a non technical background
    # the variable listed credit score is a list that has its every element in the form of a tuple
    # each tuple contains the country on the first index and the total credit score score of all the companies in that country
    # in order to make a graph i will seggregate the values from each tuple


    for country, total_score in listed_credit_score:
        print(f"Country: {country}, Total Credit Score: {total_score}")

    countries_east_africa = [item[0] for item in listed_credit_score]
    country_credit_score = [item[1] for item in listed_credit_score]

    #creating a bar chart from this data
    plt.figure(figsize=(10,6))
    plt.bar(countries_east_africa, country_credit_score, color = 'Red')


    # Giving them a title and labels
    plt.title('Credit Scores by Country', fontsize=14)
    plt.xlabel('Country', fontsize=12)
    plt.ylabel('Credit Score', fontsize=12)
    plt.xticks(rotation=45, ha='right')

    # Display the plot
    plt.tight_layout()
    plt.show()
first_calling()
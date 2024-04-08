import pandas as pd

# Load the data
men_results = pd.read_csv('men_results.csv')
women_results = pd.read_csv('women_results.csv')

# Print the first few rows to understand the data
print(men_results.head())
print(women_results.head())

# Convert the date column to datetime format
men_results['date'] = pd.to_datetime(men_results['date'])
women_results['date'] = pd.to_datetime(women_results['date'])

# Filter for matches after 2002-01-01
men_filtered = men_results[men_results['date'] > '2002-01-01']
women_filtered = women_results[women_results['date'] > '2002-01-01']

from scipy.stats import ttest_ind

# Assuming men_filtered and women_filtered are already defined and filtered as per your initial code

# Calculate the total number of goals for each match
men_filtered['total_goals'] = men_filtered['home_score'] + men_filtered['away_score']
women_filtered['total_goals'] = women_filtered['home_score'] + women_filtered['away_score']

# Perform the t-test using the 'total_goals' column
t_statistic, p_value = ttest_ind(men_filtered['total_goals'], women_filtered['total_goals'], alternative='greater')

# Extract p-value as a float
p_val = results_pg["p-val"].values[0]

# Determine hypothesis test result using sig. level
if p_val <= 0.01:
    result = "reject"
else:
    result = "fail to reject"

result_dict = {"p_val": p_val, "result": result}


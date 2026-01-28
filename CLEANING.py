# Step 1: Libraries import karo
import pandas as pd

# Step 2: CSV load karo
df = pd.read_csv("COVID_19.csv")

# Step 3: Data preview karo
print("Peechli 5 rows:")
print(df.tail())

# Step 4: Missing values check karo
print("\nMissing values per column:")
print(df.isnull().sum())

# Step 5: Data info check karo
print("\nData types aur info:")
print(df.info())

# Step 6: Date column ko datetime mein convert karo
df['date'] = pd.to_datetime(df['date'])

# Step 7: Missing per 100k columns fill karo (calculate kar ke)
df['unvaccinated_cases_per_100k'] = df['unvaccinated_cases_per_100k'].fillna((df['unvaccinated_cases'] / df['population_unvaccinated']) * 100000)
df['vaccinated_cases_per_100k'] = df['vaccinated_cases_per_100k'].fillna((df['vaccinated_cases'] / df['population_vaccinated']) * 100000)
df['unvaccinated_hosp_per_100k'] = df['unvaccinated_hosp_per_100k'].fillna((df['unvaccinated_hosp'] / df['population_unvaccinated']) * 100000)
df['vaccinated_hosp_per_100k'] = df['vaccinated_hosp_per_100k'].fillna((df['vaccinated_hosp'] / df['population_vaccinated']) * 100000)
df['unvaccinated_deaths_per_100k'] = df['unvaccinated_deaths_per_100k'].fillna((df['unvaccinated_deaths'] / df['population_unvaccinated']) * 100000)
df['vaccinated_deaths_per_100k'] = df['vaccinated_deaths_per_100k'].fillna((df['vaccinated_deaths'] / df['population_vaccinated']) * 100000)

# Step 8: Duplicate rows remove karo (agar hain)
df = df.drop_duplicates()

# Step 9: Cleaned data save karo
df.to_csv("COVID_19_cleaned.csv", index=False)

print("\nData cleaning complete! Cleaned file saved as 'COVID_19_cleaned.csv'.")

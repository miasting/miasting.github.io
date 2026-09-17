import pandas as pd


input_file = "Mennesker-Alder-Tæthedsværdi_v01.csv"
output_file = "Mennesker-Alder-Tæthedsværdi_long-reversed_v01.csv"
births_output_file = "Mennesker-Alder-Tæthedsværdi_long_births_v01.csv"

birth_ages = {
    "Freja": 0,
    "Nikolaj": 1,
    "Frederik": 3,
    "Kasper": 6,
    "Mathias": 6,
    "Ella": 14,
    "Carl": 24,
}

# Read the original comma-separated file.
data = pd.read_csv(input_file)
data = data.drop_duplicates()

birth_data = data.copy()
for person, birth_age in birth_ages.items():
    person_rows = birth_data["Navn"].str.strip().eq(person) & birth_data["Sted"].eq("Familie")
    for age in range(birth_age):
        birth_data.loc[person_rows, str(age)] = 8

# Turn age columns 0 through 26 into rows.
long_data = data.melt(
    id_vars=["Navn", "Sted"],
    var_name="Age",
    value_name="Closeness",
)

# Make Age numeric so Flourish recognizes it as a number.
long_data["Age"] = pd.to_numeric(long_data["Age"])
long_data["Closeness"] = 7 - pd.to_numeric(long_data["Closeness"])

# Save the reshaped data as a new CSV file.
long_data.to_csv(output_file, index=False, encoding="utf-8")

births_long_data = birth_data.melt(
    id_vars=["Navn", "Sted"],
    var_name="Age",
    value_name="Closeness",
)
births_long_data["Age"] = pd.to_numeric(births_long_data["Age"])
births_long_data["Closeness"] = pd.to_numeric(births_long_data["Closeness"])
births_long_data.to_csv(births_output_file, index=False, encoding="utf-8")

print(f"Created {output_file} with {len(long_data)} rows.")
print(f"Created {births_output_file} with {len(births_long_data)} rows.")
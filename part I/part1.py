import matplotlib.pyplot as plt
import pandas as pd

#  Extract data from xlsx and show plot
gdp_dataframe = pd.read_excel("GDP.xlsx")
pivot_table_gdp = gdp_dataframe.pivot_table(
    index="GEO (Labels)", values=["2017", "2018", "2019", "2020", "2021"]
)
pivot_table_gdp.sort_values(by=["2019", "2020", "2021"], inplace=True, ascending=False)
ax = pivot_table_gdp.plot(
    kind="bar", rot=90, ylabel="GDP 2017-2021", xlabel="EU Countries", legend=False
)
plt.show()

#  Extract data from CSV
survey_dataframe = pd.read_csv(
    "survey_results/survey_results_public.csv", usecols=["YearsCode", "Country", "Age"]
)
survey_dataframe.dropna(subset=["YearsCode", "Country", "Age"], inplace=True, thresh=3)

list_of_eu_countries = [
    "Belgium",
    "Bulgaria",
    "Czech Republic",
    "Denmark",
    "Germany",
    "Estonia",
    "United Kingdom of Great Britain and Northern Ireland",
    "Greece",
    "Spain",
    "France",
    "Croatia",
    "Italy",
    "Cyprus",
    "Latvia",
    "Lithuania",
    "Hungary",
    "Malta",
    "Netherlands",
    "Austria",
    "Poland",
    "Portugal",
    "Romania",
    "Slovenia",
    "Slovakia",
    "Finland",
    "Sweden",
    "Iceland",
    "Norway",
    "Switzerland",
    "United Kingdom of Great Britain and Northern Ireland",
    "Montenegro",
    "The former Yugoslav Republic of Macedonia",
    "Albania",
    "Serbia",
    "Turkey",
]

#  Extract data only for EU countries, 3 rows affected: ["YearsCode", "Country", "Age"], group
#  and getting top 2 for each country
survey_df = survey_dataframe[survey_dataframe["Country"].isin(list_of_eu_countries)]
sorted_df = (
    survey_df.sort_values(["Country", "YearsCode"], ascending=[True, True])
    .groupby("Country")
    .head(2)
)
sorted_df.to_excel("survey_results_public.xlsx", header=True)


# SRP.xlsx generated manually from survey_results_public.xlsx by getting the lowest interval by age for each country
SRP_dataframe = pd.read_excel("SRP.xlsx")
pivot_table_srp = SRP_dataframe.pivot_table(
    index="GEO (Labels)", values=["MAX age from interval"]
)

# Sorting the table SRP by ASC order to show age from lowest to highest and show plot
pivot_table_srp.sort_values(by=["MAX age from interval"], inplace=True, ascending=True)
ax_srp = pivot_table_srp.plot(
    kind="bar",
    rot=90,
    ylabel="Age first started coding in EU countries",
    xlabel="EU Countries",
    legend=False,
)
plt.show()

# import pandas as pd

# data = pd.read_csv('Iris.csv')


# def mean_and_std(datasets, column_name):
#     print(
#         f"\n\t{column_name[0]}\t\t|{column_name[1]}\t\t|{column_name[2]}\t\t|{column_name[3]}")
#     print("\t\tmean\t\tstd\t|\t\tmean\t\tstd\t|\t\tmean\t\tstd\t|")
#     for df in datasets:
#         # Get species name from first row
#         species_name = df['Species'].iloc[0]
#         mean_val1 = round(df[column_name[0]].mean(), 3)
#         std_val1 = round(df[column_name[0]].std(), 3)
#         mean_val2 = round(df[column_name[1]].mean(), 3)
#         std_val2 = round(df[column_name[1]].std(), 3)
#         mean_val3 = round(df[column_name[2]].mean(), 3)
#         std_val3 = round(df[column_name[2]].std(), 3)
#         print(
#             f"{species_name}\t| {mean_val1}\t\t{round(std_val1, 3)}\t| {mean_val2}\t\t{round(std_val2, 3)}\t| {mean_val3}\t\t{round(std_val3, 3)}\t|")


# setosa = data.loc[data['Species'] == 'Iris-setosa']
# versicolor = data.loc[data['Species'] == 'Iris-versicolor']
# virginica = data.loc[data['Species'] == 'Iris-virginica']

# mean_and_std([setosa, versicolor, virginica], ['PetalLengthCm',
#              'PetalWidthCm', 'SepalLengthCm', 'SepalWidthCm'])


import pandas as pd

data = pd.read_csv('Iris.csv')


def mean_and_std(datasets, column_names):
    # Header
    print("\n")
    print("-" * 120)
    print("{:<15} | {:<26} | {:<26} | {:<26} | {:<26}".format(
        "", column_names[0], column_names[1], column_names[2], column_names[3]))
    print("-" * 120)
    print("{:<15} | {:<13}   {:<10} | {:<13}   {:<10} | {:<13}   {:<10}".format(
        "", "mean", "std", "mean", "std","mean", "std"))
    print("-" * 120)

    # Rows for each species
    for df in datasets:
        species = df['Species'].iloc[0]
        values = []
        for col in column_names:
            mean = round(df[col].mean(), 3)
            std = round(df[col].std(), 3)
            values.append((mean, std))
        print("{:<15} | {:<15} {:<10} | {:<15} {:<10} | {:<15} {:<10} | {:<15} {:<10}".format(
            species,
            values[0][0], values[0][1],
            values[1][0], values[1][1],
            values[2][0], values[2][1],
            values[3][0], values[3][1]
        ))


# Filtering by species
setosa = data.loc[data['Species'] == 'Iris-setosa']
versicolor = data.loc[data['Species'] == 'Iris-versicolor']
virginica = data.loc[data['Species'] == 'Iris-virginica']

# Call function
mean_and_std([setosa, versicolor, virginica], ['PetalLengthCm',
             'PetalWidthCm', 'SepalLengthCm', 'SepalWidthCm'])

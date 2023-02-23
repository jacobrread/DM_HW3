import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from fitter import Fitter, get_common_distributions, get_distributions


path1 = "stock1.csv"
path2 = "stock2-1.csv"


def run_fitter(path):
    dataset = pd.read_csv(path)

    # Plot the histogram
    sns.set_style('white')
    sns.set_context("paper", font_scale=2)
    sns.displot(data=dataset, x="Price", kind="hist", bins=100, aspect=1.5)

    # Fit the distribution
    height = dataset["Price"].values
    f = Fitter(height)
            #    distributions=get_common_distributions())
            #     # distributions = get_distributions())

    f.fit()
    f.summary()

    print()
    print("Best for " + path + ": ")
    print(f.get_best(method='sumsquare_error'))

    # Display the graphs
    plt.title(path)
    plt.show()


# Run the fitter on the two provided csv files
run_fitter(path1)
run_fitter(path2)

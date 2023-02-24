import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from fitter import Fitter, get_common_distributions, get_distributions


def run_fitter(path):
    dataset = pd.read_csv(path)

    # Plot the histogram
    sns.set_style('white')
    sns.set_context("paper", font_scale=2)
    sns.displot(data=dataset, x="Price", kind="hist", bins=100, aspect=1.5)

    # Fit the distribution
    height = dataset["Price"].values
    f = Fitter(height,
               distributions=get_common_distributions())
    #     # distributions = get_distributions())

    f.fit()
    f.summary()

    print()
    print("Best for " + path + ": ")
    print(f.get_best(method='sumsquare_error'))
    print()

    # Display the graphs
    plt.title(path)
    plt.savefig("results_{}.png".format(path))

run_fitter("stock1.csv")
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

plt.rcParams.update({"text.usetex": True, "font.family": "sans-serif", "font.sans-serif": ["Helvetica"]})
plt.rcParams.update(
    {
        "text.usetex": True,
        "font.family": "serif",
        "font.serif": ["Palatino"],
    }
)

mpl.use("Agg")


class MonteCarloSimulator:
    # https://gist.github.com/youheiakimoto/0630db3d461f855fb09d799d5dc48dd8
    def __init__(self, k):
        self.std = k ** (-0.5)

    def __call__(self, x):
        return np.dot(x, x) + np.random.randn(1)[0] * self.std


def main():
    """
    https://matplotlib.org/stable/gallery/subplots_axes_and_figures/mosaic.html
    """
    np.random.seed(317)

    X = [np.array([0, 0]) for _ in range(100)]
    fidelity_levels = [1, 2, 4, 8]

    ax_dict = plt.figure(figsize=(16, 9)).subplot_mosaic(
        """
    ABCD
    EEFF
    """,
    )
    plt.subplots_adjust(wspace=0.5, hspace=0.4, left=0.075, top=0.95, right=0.98, bottom=0.08)

    # 100 sampling in each Fidelity level
    each_fidelity_level_results = []
    for fidelity_leval, ax_key in zip(fidelity_levels, ["A", "B", "C", "D"]):
        fidelity_func = MonteCarloSimulator(10**fidelity_leval)
        function_values = pd.DataFrame(np.array([fidelity_func(x) for x in X]), columns=["val"])
        function_values.index = np.arange(1, len(function_values) + 1)
        ax_dict[ax_key].plot(
            function_values,
            linewidth=2,
        )
        ax_dict[ax_key].tick_params(labelsize=20)
        ax_dict[ax_key].set_title(f"Fidelity level: {fidelity_leval}", fontsize=20)
        ax_dict[ax_key].set_xlabel("Itetation", fontsize=20)
        ax_dict[ax_key].set_xlim(1, len(function_values))
        ax_dict[ax_key].set_ylabel("Objective", fontsize=20)
        ax_dict[ax_key].set_ylim(-1, 1)
        ax_dict[ax_key].grid()
        each_fidelity_level_results.append(function_values)

    for fidelity_leval, fidelity_results in zip(fidelity_levels, each_fidelity_level_results):
        ax_dict["E"].plot(fidelity_results, linewidth=2, alpha=0.5, label=f"Fidelity_level: {fidelity_leval}")
        ax_dict["F"].errorbar(
            fidelity_leval,
            fidelity_results["val"].mean(),
            yerr=[
                [fidelity_results["val"].mean() - fidelity_results["val"].min()],
                [fidelity_results["val"].max() - fidelity_results["val"].mean()],
            ],
            fmt="*",
            markersize=15,
            capsize=20,
            elinewidth=3,
            capthick=4,
            alpha=1.0,
        )
    ax_dict["E"].tick_params(labelsize=20)
    ax_dict["E"].set_title(f"Compare fidelity level", fontsize=20)
    ax_dict["E"].set_xlabel("Itetation", fontsize=20)
    ax_dict["E"].set_xlim(1, len(function_values))
    ax_dict["E"].set_ylabel("Objective", fontsize=20)
    ax_dict["E"].set_ylim(-1, 1)
    ax_dict["E"].grid()
    ax_dict["E"].legend(bbox_to_anchor=(1, 1), loc="upper right", borderaxespad=0, fontsize=15, ncol=2)

    ax_dict["F"].tick_params(labelsize=20)
    ax_dict["F"].set_title(f"Compare fidelity level", fontsize=20)
    ax_dict["F"].set_xlabel("Fidelity level", fontsize=20)
    ax_dict["F"].set_xlim(min(fidelity_levels) - 1, max(fidelity_levels) + 1)
    ax_dict["F"].set_xticks(fidelity_levels)
    ax_dict["F"].set_ylabel("Objective", fontsize=20)
    ax_dict["F"].set_ylim(-1, 1)
    ax_dict["F"].grid()
    plt.savefig("plot_tile_figure.pdf")
    plt.close()


if __name__ == "__main__":
    main()
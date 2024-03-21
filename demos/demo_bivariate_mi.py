# %%
# Import classes
from idtxl.bivariate_mi import BivariateMI
from idtxl.data import Data
from idtxl.visualise_graph import plot_network
import matplotlib.pyplot as plt

# a) Generate test data
data = Data()
data.generate_mute_data(n_samples=1000, n_replications=5)

# b) Initialise analysis object and define settings
network_analysis = BivariateMI()
settings = {'cmi_estimator': 'JidtGaussianCMI',
            'max_lag_sources': 5,
            'min_lag_sources': 1}

# c) Run analysis
results = network_analysis.analyse_network(settings=settings, data=data)

# d) Plot inferred network to console and via matplotlib
results.print_edge_list(weights='max_te_lag', fdr=False)
plot_network(results=results, weights='max_te_lag', fdr=False)
plt.show()

# %%
results = network_analysis.analyse_single_target(settings=settings, data=data, target=0, sources=[1, 2, 3, 4])  

selected_source_mi = results.get_single_target(0, fdr=False)['selected_sources_mi']
mi = results.get_single_target(0, fdr=False)['mi']

selected_source_mi_str = ", ".join("{0:.5f}".format(num) for num in selected_source_mi)
mi_str = ", ".join("{0:.5f}".format(num) for num in mi)

print ("Selected source MI: {0}, MI: {1}".format(selected_source_mi_str, mi_str))
# %%
print(results.get_single_target(0, fdr=False).keys())
# %%

# KDE experiments
# from kde_experiment import KDEExperiment
# experiment = KDEExperiment(output_file="kde_results.xlsx", seed=42)
# results = experiment.run_experiments()

# MAF experiments
from maf_experiment import MAF_Multidimensional_Comparison_Experiment

experiment = MAF_Multidimensional_Comparison_Experiment(
    output_file="maf_results.xlsx", seed=42
)
results = experiment.run_experiments()

print("Hoera!")

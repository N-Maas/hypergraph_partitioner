# Hypergraph Partitioner Collection

This repository provides scripts for setup and execution of experiments with commonly used (hyper)graph partitioners and specifically Mt-KaHyPar.


## Worflow for Running Experiments

This assumes you are using bash or a compatible shell.

- Create a folder that contains the instances for the experiment (and preferably nothing else)
- Install the partitioners that should be used in the experiments
- Adjust the paths in `env.sh` with the path to the scripts and the installation path(s) of the partitioners, then execute `source <path-to-repo>/env.sh`
- Create a folder for the experiments and an `experiment.json` file within it
- Define the experimental setup within `experiment.json` (you can use `examples/experiment.json` as orientation). Specifically, the path to the instance folder is set here
- Execute `<path-to-repo>/setup_experiments.py experiment.json` within the same folder. This will create a new subfolder with a file `workload.txt` that contains one line for each run of the experiment
- Run the workload, either directly or by using `<path-to-repo>/experiments/execute_experiments.py experiment.json` to get a progress bar (Note: for execution with slurm, add the shebang line `#!/bin/bash` to the workload file)
- After the experiment is completed: Use `<path-to-repo>/grep_experiment_results.sh <generated-folder>` to collect the results into csv files

### Adding or modifying partitioner calls
- The partitioner calls are implemented by the python scripts in `scripts/`. The scripts may be extended, e.g. to collect additonal stats
- To add a new partitioner, an according script must be added and the mapping in `experiments/partitioner_mapping.py` must be updated accordingly

### Modifying Mt-KaHyPar
The `mt_kahypar.py` script (partitioner name `Mt-KaHyPar`) supports passing CLI arguments directly via the `args` attribute in the JSON config.
This can be used to select a different preset or override specific parameters.
Per default, the script also automatically distinguishes hmetis and metis (graph) input files and selects the according parameters, i.e. input file format and data structures.

The script is simple to extend with more output values due to the abstracted functionality in `mt_kahypar_common.py`.
It suffices to extend the script so that these values are parsed.
The setup scripts will then automatically update the csv header (note: this currently does not work for other partitioners).

### Using multiple instance directories
It is possible to use multiple directories for different instance types (e.g., regular and irregular instances). For each instance type a tag can be specified to simplify processing the data afterwards.
See `examples/multiple_directories.json` for an example.


## Hypergraph Formats

__hMetis__, __KaHyPar__, __Mt-KaHyPar__, and __Hype__ require that the input hypergraph file is in *hMetis* format (see hMetis User Guide). __Mt-KaHyPar__ alternatively accepts graph files in *Metis* format. __Parkway__ uses a binary representation of an already distributed hypergraph. However, our python interface expects the hypergraph in *hMetis* format and the conversion to the internal *Parkway* format is done inside our python script. Please make sure that the helper tool *HgrToParkway* is built inside the __Mt-KaHyPar__ partitioner (`make HgrToParkway`).

__Mondriaan__ uses a matrix representation as input hypergraph file. You can convert a hypergraph in *hMetis* format to *Mondriaan* form via tool *HgrToMondriaanMtx* inside the __KaHyPar__ partitioner (`make HgrToMondriaanMtx`). Please make sure that the corresponding *hMetis* hypergraph file is inside the same folder as the *Mondriaan* hypergraph file if you execute the mondriaan python interface script.

__PaToH__ and __Zoltan__ also use different hypergraph file representations. You can convert a *hMetis* hypergraph file via *HgrToPatoh* (inside the __KaHyPar__ partitioner) resp. *HgrToZoltan* (inside the __Mt-KaHyPar__ partitioner) to *PaToH* resp. *Zoltan* hypergraph file format. Please make sure that __Zoltan__ hypergraph file names ends with `.zoltan.hg`.

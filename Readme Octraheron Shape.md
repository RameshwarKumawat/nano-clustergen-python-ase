# Cluster Generator using ASE and EMT Calculator

This project generates and optimizes atomic clusters using the **Atomic Simulation Environment (ASE)**. Specifically, it creates **cubooctahedron (cubo)** clusters of silver (Ag) atoms, optimizes them using the **effective-medium theory (EMT)** calculator, and outputs the resulting structures in XYZ format.

## Features
- Generate clusters of atoms based on the **Octahedron** shape.
- Use **EMT** to compute the potential energy for the system.
- Optimize the atomic configuration using the **BFGS** algorithm.
- Save the optimized clusters in **XYZ** format for further analysis or visualization.

## Requirements

To run this project, you'll need the following Python packages:

- `ase` (Atomic Simulation Environment)
- `numpy` (optional, but often required for numerical computations in scientific projects)

You can install ASE using pip:

```pip install ase```

Script: cluster_generator.py
The script generates clusters based on the configuration provided in the clusters list and optimizes them. Each cluster is defined by the number of atoms, the length of the octahedron's edge, and a cutoff parameter.

Example Configuration:
In the script, clusters are defined as:

clusters = [
    {'atoms': 140, 'length': 6, 'cutoff': 1, 'filename': 'optimized_cluster_140.xyz'},
    {'atoms': 38, 'length': 4, 'cutoff': 1, 'filename': 'optimized_cluster_38.xyz'},
]

atoms: Number of atoms in the cluster.
length: The length of the octahedron's edge.
cutoff: Cutoff used for truncating the octahedron.
filename: Output filename in XYZ format.
You can modify the script to generate and optimize different cluster sizes by changing the parameters.

**Running the Script**
To run the script:
python cluster_generator.py

This will generate and optimize clusters based on the configurations defined in the script. The optimized structures will be saved in XYZ format with filenames like optimized_cluster_140.xyz.

Example Output
The script generates an optimized atomic structure and saves it to a file like optimized_cluster_140.xyz. This file contains the atomic positions after optimization and can be visualized using various molecular visualization tools (such as VMD or ASE's ase-gui).

Extending the Script
To add more clusters, simply add additional entries to the clusters list with the desired parameters, like so:

clusters = [
    {'atoms': 140, 'length': 6, 'cutoff': 1, 'filename': 'optimized_cluster_140.xyz'},
    {'atoms': 38, 'length': 4, 'cutoff': 1, 'filename': 'optimized_cluster_38.xyz'},
]

Visualization
Once you generate the XYZ files, you can visualize them using any molecular viewer that supports XYZ format, such as:

ase-gui
VMD
Avogadro
To visualize with ASE:

ase-gui optimized_cluster_140.xyz

Acknowledgments
ASE: Atomic Simulation Environment
EMT: Effective Medium Theory, a simple model used for metallic bonding.

License
This project is licensed under the MIT License. See the LICENSE file for details.

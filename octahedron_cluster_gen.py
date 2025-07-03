# Script prepared by Dr. Rameshwar L. Kumawat, Postdoctoral Researcher at Northwestern University
# This script generates Octahedron clusters of any element with a desired number of atoms
# Date: 07/03/2025

## Cluster Generator using ASE and EMT Calculator
from ase.calculators.emt import EMT
from ase.cluster import Octahedron
from ase.optimize import BFGS
from ase.io import write

# Define the clusters with their parameters
clusters = [
    {'atoms': 140, 'length': 6, 'cutoff': 1, 'filename': 'optimized_cluster_140.xyz'},
    {'atoms': 38, 'length': 4, 'cutoff': 1, 'filename': 'optimized_cluster_38.xyz'},

]

# Loop through each cluster configuration
for cluster in clusters:
    print(f"Creating truncated octahedron with {cluster['atoms']} atoms...")

    # Create truncated octahedron
    atoms = Octahedron('Ag', length=cluster['length'], cutoff=cluster['cutoff'])
    atoms.calc = EMT()

    # Optimize the structure
    opt = BFGS(atoms, trajectory=f'opt_{cluster["atoms"]}.traj')
    opt.run(fmax=0.01)

    # Save the optimized structure in XYZ format
    write(cluster['filename'], atoms)

    print(f"Saved optimized structure to {cluster['filename']}\n")

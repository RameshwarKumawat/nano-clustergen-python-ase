# Script prepared by Dr. Rameshwar L. Kumawat, Postdoctoral Researcher at Northwestern University
# This script generates nanocube clusters of any element in the FCC(111) phase with a desired number of atoms
# Date: 07/03/2025

from ase.cluster.cubic import FaceCenteredCubic
from ase.io import write
import os

# Parameters
lattice_constant = 4.09  # Silver lattice constant in Ångstroms
output_dir = "newAgNC_xyz_files"
os.makedirs(output_dir, exist_ok=True)  # Ensure output directory exists

# Target atom counts for nanocubes
target_atoms = [1099, 864, 666, 500, 365, 256, 172, 108, 63]

# Generate nanocubes
generated_files = []
for n_atoms in target_atoms:
    layers = 1
    atoms = None

    while True:
        # Build a cubic FCC nanocrystal
        atoms = FaceCenteredCubic(
            'Ag',
            surfaces=[(1, 0, 0), (0, 1, 0), (0, 0, 1)],
            layers=(layers, layers, layers),  # Cube: equal layers in x, y, z
            latticeconstant=lattice_constant
        )

        # Stop when the atom count exceeds or matches the target
        if len(atoms) >= n_atoms:
            break
        layers += 1

    # Adjust atom count to match the target as closely as possible
    if len(atoms) > n_atoms:
        atoms = atoms[:n_atoms]  # Trim excess atoms
    elif len(atoms) < n_atoms:
        print(f"Warning: Closest FCC nanocube to {n_atoms} atoms has {len(atoms)} atoms.")

    # Save the nanocube to an XYZ file
    filename = os.path.join(output_dir, f"AgNC_{n_atoms}_atoms.xyz")
    write(filename, atoms)
    generated_files.append(filename)

print(f"Generated nanocubes saved in '{output_dir}':")
for file in generated_files:
    print(file)

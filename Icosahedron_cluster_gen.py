'''Python script to generate Iocsahedron shape silver nanoparticles'''
# Script prepared by Dr. Rameshwar L. Kumawat, Postdoctoral Researcher at Northwestern University
# This script generates Icosahedron clusters of any element with a desired number of atoms
# Date: 07/03/2024

from ase.cluster import Icosahedron
from ase.io import write

# Function to generate and write icosahedral clusters
def generate_icosahedral_clusters(symbol, sizes):
    for size in sizes:
        cluster = Icosahedron(symbol, noshells=size)
        filename = f'{symbol}{len(cluster)}.xyz'
        write(filename, cluster)
        print(f'{filename} created with {len(cluster)} atoms.')

# Sizes corresponding to the number of shells required for each cluster
sizes = {
    13: 1,
    55: 2,
    147: 3,
    309: 4,
    561: 5,
    561: 6,
    923: 7,
    1415: 8,
    2057: 9,
    2869: 10,
}

# Generate and write clusters
generate_icosahedral_clusters('Ag', sizes.values())


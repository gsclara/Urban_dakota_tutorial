# Zephyr_dakota_tutorial

Coupling of OpenFOAM libraries and Dakota for uncertainty quantificatioon purposes.

Part of the codes used have been used from the freely accessible resources online (https://www.ehsanmadadi.com/cylinder-mesh/, https://holzmann-cfd.com/community/training-cases/geometric-variation)

Part of the codes have been developed within out group by: N. Hobeika, I. Padjen and C. Garcia-Sanchez

Other contributors: J. Sousa, C. Gorle


## What is inside?

casebase1.zip: openFOAM case folder with the cases from 0-90 degres in wind direction

casebase2.zip: openFOAM case folder with the cases from 0-90 degres in wind direction

templatedir.zip: ABLConditions.template, initialConditions.template files with symbolic UQ variables x1, x2, x3

cluster_submission.pbs: script to submit to cluster

dakota_of_ASKH.in: input file to run dakota (in this case for polynomial chaos)

LauchSimulationUQ: file to launch a set of simulations with a for loop

simulator_script_cluster: script to set-up the runs for a cluster run based on dakota input using the casebase1, casebase2 and templatedir

simulator_script_local: script to set-up the runs for a local computer run based on dakota input using the casebase1, casebase2 and templatedir

## Features

The current set-up works with OpenFOAM 2.3 and Dakota 6.

## Configuration

The current set-up uses wind velocity, direction and roughness length as uncertainty variables.

## Contributing

If you'd like to contribute, please fork the repository and use a feature
branch. Pull requests are warmly welcome.

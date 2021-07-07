# Zephyr_dakota_tutorial

Coupling of OpenFOAM libraries and Dakota for uncertainty quantificatioon purposes.

Part of the codes used have been used from the freely accessible resources online (https://www.ehsanmadadi.com/cylinder-mesh/, https://holzmann-cfd.com/community/training-cases/geometric-variation)

Part of the codes have been developed within out group by: N. Hobeika, I. Pađen and C. Garcia-Sanchez

Other contributors from the past work: J. Sousa, C. Gorle


## What is inside?

case16_probes: uncertainty quantification case for quasi-2D flow around a cube with post-processing of some probes

case16_coarse: uncertainty quantification case for quasi-2D flow around a cube with post-processing of full vtk surfaces (this case is very coarse mesh not good for CFD, but just for the training purpose)

Inside both cases the same structure is set-up with slight differences: 

- cube_case: is the template case that is copied for each of the evaluations
- postProcess: contains the python rutines to extract the probes/surfaces values for Umag/Udir and put them into a format that dakota can read
- simulator_script: it is the script that controls all the tasks performed by dakota
- simulator_script_post: same as the previous one but tricks dakota into doing only post-process (since we do not have pre-post feature in PCE, to use when all evaluations are run and just the post-process is missing)
- dakota_pce_cube.in: input file for dakota that uses simulator_script
- dakota_pce_cube_post.in: input file for dakota that use simulator_script_post

## Features

The current set-up works with OpenFOAM 8 and Dakota 6.13.

## Configuration

The current set-up uses wind velocity and direction as uncertainty variables.

## Contributing

If you'd like to contribute, please fork the repository and use a feature
branch. Pull requests are warmly welcome. Fixes and bug reporting as well
very welcome.

# Python-Showcase
Examples of Professional and Personal projects in Python 


# SF quantum state learning
[This project was performed on a Dell Latitude-E5540, Intel® Core™ i5-4310U CPU @ 2.00GHz × 4. OS: Ubuntu 16.04.5 LTS 64-bit.
This should be regarded as a lightweight proof-of-principle]

This project uses software developed by Xanadu called Strawberryfields:
https://strawberryfields.readthedocs.io/en/latest/ and builds on the machine learning method for state preparation introduced in: 
https://arxiv.org/abs/1807.10781

In the present work I use machine learning optimisation algorithms, provided by the TensorFlow backend, to engineer continuous variable states of particular interest to quantum metrology. The Python code for these states is given here:
https://github.com/anthayes92/Python-Showcase/blob/master/SF%20quantum%20state%20learning%20/learner/cv_states.py

The state of interest is the so called "squeezed entangled state" which has been shown to exhibit high precision gains for applications such as gravitational wave detection but is difficult to engineer in practise:
https://journals.aps.org/pra/abstract/10.1103/PhysRevA.93.033859

This was tried with a few different optimisation algorithms, the Adam optimiser was found to give the best fidelities ~0.7. The results of this are given here:
https://github.com/anthayes92/Python-Showcase/tree/master/SF%20quantum%20state%20learning%20/sim_results/SES_z%3D2_d20_c10_r500

Future work (ideally on better suited hardware!) would include optimisation of hyperparameters to increase fidelities (>0.9), state engineering of other non-Guassian states of interest to quantum metrology such as the "squeezed cat state" and engineering of multimode (more than 2 mode) states.

# Data Analysis Example:
This collaborative project (consisting of a bunch of physics PhDs with a passion for rock climbing!) used data scraped from the climbing website:
https://www.8a.nu/

In this folder we see part of this analysis in which the BMI of climbers around Europe is compared to that of the general population. This is done for the European countries for which there is the most data available on climbers. 

The results are divided between males and females: 
https://github.com/anthayes92/Python-Showcase/tree/master/Data%20Analysis%20Example/Results

Note that some female rock climbers are fairly underweight!
# Quantum Metrology
In this project we see an example of Python code used to produce results for the published paper:
https://iopscience.iop.org/article/10.1088/2058-9565/aac30b

The main interest of this code is the simulated evolution of quantum mechaical states: 
https://github.com/anthayes92/Python-Showcase/blob/master/Quantum%20Metrology/state_evolution.py

and the numerical optimisations of these processes which generate the data to be analysed:
https://github.com/anthayes92/Python-Showcase/blob/master/Quantum%20Metrology/optimisations---data_generation.py







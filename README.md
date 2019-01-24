# Python-Showcase
Examples of Professional and Personal projects in Python 


# Data Analysis Example:
This project used data scraped from the climbing website:
https://www.8a.nu/

In this folder we see part of this analysis in which the BMI of climbers around Europe is compared to that of the general population. This is done for the European countries in which for which there is the most data available on climbers. 

The results are divided between males and females: 
https://github.com/anthayes92/Python-Showcase/tree/master/Data%20Analysis%20Example/Results

# Quantum Metrology
In this project we see an example of Python code used to produce results for the published paper:
https://iopscience.iop.org/article/10.1088/2058-9565/aac30b

The main interest of this code is the simulated evolution of quantum mechaical states: 
https://github.com/anthayes92/Python-Showcase/blob/master/Quanutm%20Metrology/state_evolution.py

and the numerical optimisations of these processes which generate the data to be analysed:
https://github.com/anthayes92/Python-Showcase/blob/master/Quanutm%20Metrology/optimisations---data_generation.py

# SF quantum state learning
This project uses software developed by Xanadu called Strawberryfields:
https://strawberryfields.readthedocs.io/en/latest/

Here I use machine learning optimisation algorithms, provided by the TensorFlow backend, to engineer continuous variable states of particular interest to quantum metrology. The Python code for these states is given here:
https://github.com/anthayes92/Python-Showcase/blob/master/SF%20quantum%20state%20learning%20/learner/cv_states.py

The state of interest is the so called "squeezed entangled state" which has been shown to exhibit high presicion gains for applications such as gravitational wave detection:
https://journals.aps.org/pra/abstract/10.1103/PhysRevA.93.033859

The results of this optimisation are given here:
https://github.com/anthayes92/Python-Showcase/tree/master/SF%20quantum%20state%20learning%20/sim_results/SES_z%3D2_d20_c10_r500

Future work would include optimisation of hyperparameters to inrease fidelities, state engineering of other states of interst to quantum metrology such as the "squeezed cat state" and egineering of multimode (more than 2 mode) states.






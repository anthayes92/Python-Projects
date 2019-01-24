# Copyright 2018 Xanadu Quantum Technologies Inc.

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import numpy as np
from scipy.special import factorial as fac


# ============================================================
# States
# ============================================================

# Start with a simple 2 mode CV state; equal coherent states in each mode
# Keep displacements of vacuum in X quadrature for now so that alpha exsists in the reals (without loss of generality)
# Maintain equal displacement magnitude in each mode

def two_mode_coherent(alpha, cutoff):
    r"""Two mode coherent state |alpha>|alpha>

    Args:
        alpha (real): coherent state parameter
        cutoff (int): the Fock basis truncation of the returned state vector.

    Returns:
        array: a size [cutoff^2] complex array state vector.
    """
    state = np.zeros([cutoff])
    for n in range(len(state)):
        state[n]=(alpha**n)/np.sqrt(fac(n))
        two_mode_state=np.outer(state, state)
    return two_mode_state.flatten()*np.exp(-np.abs(alpha)**2)

# Introduce some non-clasicality in the form of a quadrature squeezed states
# Squeeze in position quadraure for now to keep parameters real for simplicity

def squeezed_vac(z,cutoff):
    r"""Squeezed vacuum state  |z>

    Args:
        z (real): squeezing parameter
        cutoff (int): the Fock basis truncation of the returned state vector.

    Returns:
        array: a size [cutoff] complex array state vector.
    """
    state = np.zeros([2*cutoff])
    for n in range(cutoff):
           state[2*n]=((-np.tanh(z))**n)*(np.sqrt(fac(2*n))/(fac(n)*(2**n)))
           sqz=state/(np.sqrt(np.cosh(z)))
    return sqz[0:cutoff]

# Introduce second mode in which a squeezed vacuum state of equal magnitude is injected

def two_mode_squeezed_vac(z,cutoff):
    r"""Two mode squeezed vacuum state  |z>|z>

    Args:
        z (real): squeezing parameters
        cutoff (int): the Fock basis truncation of the returned state vector.

    Returns:
        array: a size [cutoff] complex array state vector.
    """
    state = np.zeros([2*cutoff])
    for n in range(cutoff):
           state[2*n]=((-np.tanh(z))**n)*(np.sqrt(fac(2*n))/(fac(n)*(2**n)))
           sqz=state/(np.sqrt(np.cosh(z)))
           sqz=sqz[0:cutoff]
           two_mode_sqz=np.outer(sqz, sqz)
    return two_mode_sqz.flatten()


# Again, consider squeezing in position quadrature

def SES(z,cutoff):
    r"""Two mode squeezed-entangled state N(|z,0>+|0,z>) where N=normalisation

    Args:
        z (real): squeezing parameters
        cutoff (int): the Fock basis truncation of the returned state vector.

    Returns:
        array: a size [cutoff^2] complex array state vector.
    """
    state = np.zeros([2*cutoff])
    for n in range(cutoff):
           state[2*n]=((-np.tanh(z))**n)*(np.sqrt(fac(2*n))/(fac(n)*(2**n)))

    sqz=state[0:cutoff]

    S1=np.zeros([cutoff,cutoff])
    S2=np.zeros([cutoff,cutoff])
    S1[0:cutoff,0]=sqz/(np.sqrt(np.cosh(z))) # first ket of SES
    S2[0,0:cutoff]=sqz/(np.sqrt(np.cosh(z))) # second ket of SES
    N= 1/( np.sqrt(2 + 2/(np.cosh(z))) ) # normalising factor for SES
    SES=N*( S1 + S2 )

    return SES.flatten()






# ============================================================
# State auxillary functions
# ============================================================

def correct_global_phase(state):
    """Corrects the global phase of wavefunction."""
    maxentry = np.argmax(np.abs(state))
    phase = state[maxentry]/np.abs(state[maxentry])
    return state/phase

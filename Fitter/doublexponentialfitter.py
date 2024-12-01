import matplotlib.pyplot as plt
import numpy as np
from fitter import Fit

## DEFINE FIT
def doubleexponential(x, A1, f1, A2, f2):
    "Fit a double exponential, y = A1*f1^x + A2*f2^x, with x in number of filters"
    return A1*f1**x + A2*f2**x
doubleexponential.tex = r"A_1;f_1;A_2;f_2"
doubleexponential.function_tex = r"$A_1(f_1)^x + A_2(f_2)^x$"

def singleexponential(x, A, f):
    "Fit a double exponential, y = A1*f1^x + A2*f2^x, with x in number of filters"
    return A*f**x
singleexponential.tex = r"A;f"
singleexponential.function_tex = r"$A(f)^x$"

## DATA
    #Pmax
# x = [0,1,2,3,4,5,6,7]
# y = [307.5, 130.3333333, 55.33333333,24.5, 11.66666667, 5.266666667, 2.531666667, 1.355]
# yunc = [5.757168869, 2.389557349, 1.170100275, 0.5636686927, 0.5606476607, 0.3307415999, 0.0640249805, 0.06243721719]

    #Imax
x = [0,1,2,3,4,5,6,7]
y = [19.63666667, 9.166666667, 4.469333333, 2.336333333, 1.271666667, 0.72, 0.4083333333, 0.2551666667]
yunc = [0.2887088114, 0.110239638, 0.07058407123, 0.02969474327, 0.02147349788, 0.02020725942, 0.005270462767, 0.006180165406]


## FIT (REMEMBER TO CHANGE NAME)

f = Fit(
    x,                 # the independent variable
    y,                   # the dependent variable
    yunc=yunc,        # the uncertainties of the dependent variable
    function=doubleexponential,     # the fitting function
    p0=(10, 0.5, 10, 0.5)           # initial guesses for (A1, f1, A2, f2),
    )
f.plot(xlabel=r"$n$", ylabel=r"$I_{max}$")
f.fig.savefig("image.png", dpi=600)

# f = Fit(
#     x,                 # the independent variable
#     y,                   # the dependent variable
#     yunc=yunc,        # the uncertainties of the dependent variable
#     function=singleexponential,     # the fitting function
#     p0=(300, 0.5)           # initial guesses for (A, f),
#     )
# f.plot(xlabel=r"$n$", ylabel=r"$P_{max}$")
# f.fig.savefig("image.png", dpi=600)


# First exponential is not consistent with data
# Second exponential is not inconsistent with data, but cannot be necessarily proven
# It is unclear whether the two decay rates are genuinely the same or different, due to issues with the spectral information (counts==photons-ish)
# Parameters calculated by fit cannot be used in further application unless I were to go and do the exact same experiment with solely each peak of wavelength light separately (to then see if A and f match this model's conclusions)
# Since the spectral analysis does genuinely represent the LED array I used, and the manufacturer suggests the decay rates for each peak of wavelength are not appreciably different, a single exponential should also work as a fit too. Clearly, it doesn't, and the double exponential doesn't not work, so either the manufacturer is lying about the decay rates, or I'd need to find the decay rates myself by doing the wavelength-independent experiments. In total: more testing needed.
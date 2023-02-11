# This is python code that checks the algebra - spatial PDE - in paper "Emergent constraints for the climate system as effective parameters of bulk differential equations.
# To make the output look nice, run in "ipython qtconsole"
# This code checks the long-term non-seasonal solution.
# Chris Huntingford 2023 (chg@ceh.ac.uk)

import os, sys
from sympy.abc import t         # t is the independent variable.
from sympy.abc import omega     # omega gives the wavelength of 
from sympy.abc import kappa     # omega gives the wavelength of 
from sympy.abc import b         # t is the independent variable.
from sympy.abc import x         # t is the independent variable.
from sympy.abc import pi        # t is the independent variable.
from sympy.abc import T         # T is the state variable of temperature.
from sympy import Function, dsolve, Derivative, init_printing, symbols, diff, simplify
from sympy import sin, cos, exp, sqrt, erfc
from IPython.display import display
init_printing(use_latex=True)

# There are two equations we wish to check are being satisfied by our exact solution.

# The exact solution for a seasonal solution to Eqn(7). Then the solution to the boundary condition Eqn (8).
H0 = symbols(r'H_{0}')
c_p_dash = symbols(r"c_{p}'")
print(' ')
print('Proposed Solution that satisfies the PDE and long-term boundary condition')
print('************************************************************************')
factor1 = (2*H0) / kappa
factor2 = sqrt( ( (kappa/c_p_dash) * t) / (pi) )
factor3 = exp(-(x**2)/(4*(kappa/c_p_dash)*t))
factor4 = (x/2)*erfc(x/(2*sqrt((kappa/c_p_dash)*t)))
soln_test = factor1*(factor2*factor3 - factor4)
display(soln_test)

print(' ')
print('Now test if the solution satisfies the PDE itself')
print('Left-hand side minus right-hand side')
print('************************************************************************')

# Now take the derivatives
print(' ')
print('Left-hand side: c_p * Derivative wrt time')
print('*******************')
deriv_t = diff(c_p_dash*soln_test, t)
display(deriv_t)

print(' ')
print('Right-hand side: kappa * 2nd Derivative wrt x')
print('********************')
deriv_xx = diff(kappa*soln_test, x, x)
display(deriv_xx)

print(' ')
print('Equality check (should be zero)')
print('*******************************')
difference_expr = simplify(deriv_t - deriv_xx)
display(difference_expr)

print(' ')
print(' ')
print(' ')
print('Now print out the gradient, kappa dT/dx at x=0 - which should give -H0  (Eqn(12))')
print('*****************************************************')
deriv_x = diff(kappa*soln_test, x)
deriv_x_at_x_zero = deriv_x.subs(x, 0)
expr_gradient = simplify(deriv_x_at_x_zero)
display(expr_gradient)

print(' ')
print(' ')
print(' ')
print('And print out the solution as the surface, i.e. x=0 - should be Eqn(14)')
print('*****************************************************')
val_at_x_zero = soln_test.subs(x, 0)
display(val_at_x_zero)

sys.exit()

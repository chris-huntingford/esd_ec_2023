# This is python code that checks the algebra - box model - in paper "Emergent constraints for the climate system as effective parameters of bulk differential equations.
# To make the output look nice, run in "ipython qtconsole"
# Chris Huntingford 2023 (chg@ceh.ac.uk)
import os, sys
from sympy.abc import t         # t is the independent variable.
from sympy.abc import omega     # omega appears in the seasonal forcing
from sympy.abc import b         # b appears in the seasonal forcing

from sympy import Function, dsolve, Derivative, init_printing, simplify, symbols 
from sympy import sin, cos, diff
from IPython.display import display
init_printing(use_latex=True)

c_p_dash = symbols(r'c_{p}^{1}')
H_0 = symbols(r'H_{0}')

# First set the proposed solution for T. This is equation (5)
expr_T = ((H_0 * t) / c_p_dash) + (b/(c_p_dash*omega))*sin(omega*t)
print(' ')
print('Solution for the single-box - to be checked - Eqn(5) in paper')
print('*************************************************************')
display(expr_T)

print(' ')
print('Now calculate the left-hand derivative of Eqn (2), with the solution above')
print('**************************************************************************')
eqn_2_lhs = c_p_dash * diff(expr_T, t)
display(eqn_2_lhs)

print(' ')
print('Now confirm that the solution above equals the Forcing (top of Figure 1')
print('Here is the given forcing for the r.h.s of Eqn (2) i.e. H')
print('***********************************************************************')
expr_H_supplied = H_0 + b * cos(omega*t)
display(expr_H_supplied)

print(' ')
print('Now check that lhs = rhs of Eqn (2) - if so, should be zero')
print('***********************************************************************')
expr_check = eqn_2_lhs - expr_H_supplied
display(expr_check)
expr_check_simplified = simplify(eqn_2_lhs) - expr_H_supplied
display(expr_check_simplified)
#T = Function('T')
#print ' '
#print 'Solution with just fluctuations'
#print '*******************************'
#display(dsolve(c_p_dash*Derivative(T(t), t)- b*cos(omega*t), T(t)))

#print ' '
#print 'Full Solution'
#print '*************'
#H_zero = symbols('H_0')
#display(dsolve(c_p_dash*Derivative(T(t), t)- b*cos(omega*t) - H_zero, T(t)))

sys.exit() 

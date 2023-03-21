# This is the building of a schematic on ECs. Make this a two row diagram.
# This is Fig. 2 of the ESD paper "Emergent constraints for the climate system as effective parameters of bulk differential equations" 
# Chris Huntingford (chg@ceh.ac.uk)
import os, sys
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.patches as patches

fig=plt.figure(figsize=(5.0, 8.0))
plt.rcParams.update({
    "text.usetex": True,
    "font.family": "sans-serif",
    "font.sans-serif": ["Helvetica"]})
plt.rcParams["text.usetex"] = True
plt.rcParams["text.latex.preamble"] = r'\usepackage{amsmath}' 

plt.axis('off')
ax1=plt.subplot(111)
ax1.set_xlim(0.0, 4.0)
ax1.set_ylim(0.0, 7.0)

right_nudge=0.7
#up_nudge=0.0
up_nudge=0.4

prop_out = dict(arrowstyle="-|>, head_width=0.3, head_length=0.7", shrinkA=0, shrinkB=0, color='teal')
ft_size = 14

# Start with the ``box'', which is panel (a)
for i in range(0, 50):
    rect = patches.Rectangle((0.8+right_nudge+(float(i)*0.05), 5.3+up_nudge), 1.6*0.05, 0.7, facecolor='paleturquoise', edgecolor='paleturquoise', zorder=-10, alpha=1.0-float(i)*0.02)
    ax1.add_patch(rect)

ax1.text(2.0+right_nudge, 5.6+up_nudge, r'$c_{p_{i}}^{\prime} \dfrac{\partial T}{\partial t} = \kappa_{i} \dfrac{\partial^{2} T_{i}}{\partial z^{2}} $', ha='center', fontsize=ft_size+2, va='center')

ax1.text(1.0+right_nudge, 5.2+up_nudge, r'$z=0$', ha='center', fontsize=ft_size-3, va='center')
ax1.text(3.1+right_nudge, 5.2+up_nudge, r'$z \rightarrow \infty$', ha='center', fontsize=ft_size-3, va='center')

# Top arrow down
ax1.annotate('', xy=(2.0+right_nudge-1.2, 5.8+up_nudge), xytext=(2.0+right_nudge-1.7, 5.8+up_nudge), arrowprops=prop_out)
ax1.plot([2.0+right_nudge-1.7, 2.0+right_nudge-1.7], [6.6+up_nudge, 5.8+up_nudge], color='teal', zorder=-10)

# Bottom arrow down
ax1.annotate('', xy=(2.0+right_nudge-1.7, 4.7+up_nudge), xytext=(2.0+right_nudge-1.7, 5.5+up_nudge), arrowprops=prop_out)
ax1.plot([2.0+right_nudge-1.2, 2.0+right_nudge-1.7], [5.5+up_nudge, 5.5+up_nudge], color='teal', zorder=-10)


ax1.text(2.0+right_nudge - 0.25, 4.2+up_nudge, r'$T_{i}(0,t) = \underbrace{2H_{0} \sqrt{ \frac{t}{c_{p_{i}}^{\prime} \kappa_{i} \pi}}}_\text{\parbox{2cm}{\centering {\small Background\\[-4pt] Warming}}} + \underbrace{\frac{b \cos(\omega t - \pi/4)}{\sqrt{c_{p_{i}}^{\prime}\kappa_{i}\omega}} }_\text{\parbox{2cm}{\centering {\small Seasonal\\[-4pt] Variation}}}$', ha='center', fontsize=ft_size, va='center')

ax1.text(2.0+right_nudge - 0.2, 6.9+up_nudge, r'$H(t) = - \kappa_{i} \left.\dfrac{\partial T_{i}}{\partial z} \right|_{z=0}   = \underbrace{H_{0}}_\text{\parbox{2cm}{\centering {\small Background\\[-4pt] Forcing}}} + \underbrace{b \cos(\omega t)}_\text{\parbox{2cm}{\centering {\small Seasonal\\[-4pt] Forcing}}}$', ha='center', fontsize=ft_size, va='center')

ax1.text(-0.5, 7.1+up_nudge, r'$\textrm{Forcing}:$', ha='left', fontsize=15, va='center')
ax1.text(-0.5, 5.7+up_nudge, r'$\textrm{Model}:$', ha='left', fontsize=15, va='center')
ax1.text(-0.5, 4.5+up_nudge, r'$\textrm{Response}:$', ha='left', fontsize=15, va='center')

ax1.text(-0.5, 7.73, r'$\textbf{(a)}$', ha='left', fontsize=12, va='center') 

# Now present the emergent constraint, which is panel (b) 

prop_plot = dict(arrowstyle="-|>, head_width=0.3, head_length=0.7", shrinkA=0, shrinkB=0, color='black')
ax1.annotate('', xy=(0.5, 2.7), xytext=(0.5, 0.1), arrowprops=prop_plot)
ax1.annotate('', xy=(3.8, 0.1), xytext=(0.5, 0.1), arrowprops=prop_plot)
ax1.plot([0.7, 3.4],[0.28, 2.28], color='green',lw=1.5)

prop_plot_extra = dict(arrowstyle="-|>, head_width=0.15, head_length=0.4", shrinkA=0, shrinkB=0, color='black', linestyle='dashed')
ax1.annotate('', xy=(2.0, 0.95), xytext=(1.08, 0.25), arrowprops=prop_plot_extra)
ax1.text(1.25, 0.15, r'$\textrm{Decreasing } c_{p_{i}}^{\prime} \kappa_{i}$', fontsize=9, ha='left', va='bottom', rotation = 36.0)


ax1.text(-0.2, 2.8, r'$\sqrt{t} \left.\overline{\dfrac{\mbox{d}T_{i}}{\mbox{d}t}}\right|_{z=0} = \dfrac{H_{0}}{\sqrt{c_{p_{i}}^{\prime} \kappa_{i} \pi}}$', fontsize=15)
ax1.text(-0.02, 0.22, r'$\textrm{Annual running mean}$', fontsize=11, rotation=90.0, ha='left', va='bottom')
ax1.text(0.16, 0.22, r'$\textrm{warming rate $\times \sqrt{t}$ (K yr$^{-1/2}$)}$', fontsize=11, rotation=90.0, ha='left', va='bottom')

ax1.text(0.8, -0.2, r'$\textrm{Seasonal range (K)}$', fontsize=11, ha='left', va='bottom')
ax1.text(2.5, -0.55, r'$\left.\Delta T_{\textrm{S }}\right|_{z=0}=\dfrac{2b}{\sqrt{c_{p_{i}}^{\prime} \kappa_{i} \omega}}$', fontsize=15)
# Crazy thing - doube subscripts not working
ax1.text(2.9, -0.41, r'$i$', fontsize=11)


ax1.text(3.5, 2.5, r'$\textrm{Emergent}$', fontsize=11, color='green')
ax1.text(3.5, 2.3, r'$\textrm{Constraint}$', fontsize=11, color='green')

rect_ec = patches.Rectangle((2.2, 0.1), 0.6, 2.3, facecolor='yellow', edgecolor='yellow', zorder=-10)
ax1.plot([2.2, 2.2],[0.1, 0.1+2.3], color='orange', linestyle='dashed')
ax1.plot([2.2+0.3, 2.2+0.3],[0.1, 0.1+2.3], color='orange')
ax1.plot([2.2+0.6, 2.2+0.6],[0.1, 0.1+2.3], color='orange', linestyle='dashed')
ax1.text(2.18, 2.52, r'$\textrm{Data}, \Delta T_{S}^{*}$', fontsize=11, color='green')
ax1.add_patch(rect_ec)

rect_ec_2 = patches.Rectangle((0.5, 1.3), 2.9, 0.6, facecolor='greenyellow', edgecolor='greenyellow', zorder=-10, alpha=0.5)
ax1.plot([0.5, 0.5+2.9],[1.3, 1.3], color='orange', linestyle='dashed')
ax1.plot([0.5, 0.5+2.9],[1.3+0.3, 1.3+0.3], color='orange')
ax1.plot([0.5, 0.5+2.9],[1.9, 1.9], color='orange', linestyle='dashed')
ax1.add_patch(rect_ec_2)

ax1.text(0.6, 2.2, r'$\textrm{Constrained}$', fontsize=11, color='green')
ax1.text(0.6, 2.0, r'$\textrm{Projection}$', fontsize=11, color='green')

x_circle=[1.00, 1.10, 1.20, 1.40, 1.50, 1.60, 2.00, 2.10, 2.30, 2.50, 2.80, 2.88, 3.16]
y_circle=[0.50, 0.70, 0.62, 1.00, 0.97, 0.94, 1.17, 1.30, 1.47, 1.67, 2.00, 1.85, 2.15]
for i_point in range(0, len(x_circle)):
    circle_plot = patches.Circle((x_circle[i_point], y_circle[i_point]), radius=0.03, color='black', zorder=10)
    ax1.add_patch(circle_plot)

ax1.text(-0.5, 3.2, r'$\textbf{(b)}$', ha='left', fontsize=12, va='center') 
plt.savefig('fig2.png', dpi=600)
# plt.savefig('fig2.pdf')
sys.exit()

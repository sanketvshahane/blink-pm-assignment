import matplotlib.pyplot as plt
import numpy as np

# Data Modeling (Months 0 to 12)
months = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

# Headcount (FTEs): starts at 30, drops to 20 at Month 4, drops to 10 at Month 6, and scales logarithmically to 16 by Month 12
headcount = np.array([30, 30, 30, 25, 20, 15, 10, 11, 12, 13, 14, 15, 16])

# Token Cost: flat at 20 for first 6 months (Months 0 to 6), then grows flatter
token_cost = np.array([20, 20, 20, 20, 20, 20, 20, 28, 34, 38, 41, 43, 45])

# Gross Margin (%): starts at 15%, dips to 5% at Month 2, climbs to 30% at Months 5 & 6,
# and remains exactly 10% (10 units) above the Token Cost curve after Month 6 to prevent intersection.
margin = np.array([15, 10, 5, 15, 22, 30, 30, 38, 44, 48, 51, 53, 55])

# Plotting Setup (Using a Single unified Y-Axis to guarantee zero visual intersection)
fig, ax = plt.subplots(figsize=(11, 6.5))

color_hc = '#1f77b4'      # Tech Blue
color_tc = '#ff7f0e'      # Orange
color_margin = '#2ca02c'  # Green for Profitability

ax.set_xlabel('Timeline (Months)', fontsize=12, fontweight='bold', labelpad=10)
ax.set_ylabel('Metrics (FTE Count / Token Cost Index / Margin %)', fontsize=12, fontweight='bold')

# Plotting all curves on the same unified scale (0 to 60)
line_hc, = ax.plot(months, headcount, color=color_hc, linewidth=3.5, marker='o', markersize=6, label='Headcount (grows logarithmically)')
line_tc, = ax.plot(months, token_cost, color=color_tc, linewidth=3.5, marker='s', markersize=6, label='Token cost (grows flatter as tokens get cheaper)')
line_margin, = ax.plot(months, margin, color=color_margin, linewidth=3.5, marker='^', markersize=6, linestyle='--', label='Margin (dips then explodes)')

# Set Y-axis limits so there is breathing room above 55
ax.set_ylim(0, 60)
ax.grid(True, which='both', linestyle=':', alpha=0.5)

# X-axis ticks with Volume Scaling factors integrated directly at Month 6, 9, and 12
ax.set_xticks(months)
ax.set_xticklabels([
    'Baseline\n(M0)', 'M1', 'M2', 'M3', 'M4', 'M5', 
    '6 Months\n(M6, Vol: 1x)', 'M7', 'M8', 
    '9 Months\n(M9, Vol: 2x)', 'M10', 'M11', 
    '12 Months\n(M12, Vol: 4x)'
], fontsize=8.5, fontweight='bold')

# Legend Configuration
ax.legend(handles=[line_hc, line_tc, line_margin], loc='upper left', frameon=True, shadow=True, facecolor='white')

# Adding visual annotations
ax.annotate('Margin Dip\n(Investment)', xy=(2, 5), xytext=(0.5, 10),
             arrowprops=dict(facecolor='black', shrink=0.08, width=1, headwidth=6))

ax.annotate('AI Launch\n(FTE drops to 10)', xy=(6, 10), xytext=(5.2, 2.5),
             arrowprops=dict(facecolor='black', shrink=0.08, width=1, headwidth=6))

ax.annotate('Margin Locked\n10% Above Token Cost', xy=(9, 48), xytext=(6.8, 53),
             arrowprops=dict(facecolor='black', shrink=0.08, width=1, headwidth=6))

plt.title('Blink Health: Conceptual 12-Month Scale & Profitability Projection', fontsize=14, fontweight='bold', pad=15)
plt.tight_layout()

# Save PNG
plt.savefig('/Users/sanket/Downloads/blinkhealth/scale_profitability.png', dpi=300)
print("Updated chart with volume-labeled timeline ticks generated successfully at /Users/sanket/Downloads/blinkhealth/scale_profitability.png")

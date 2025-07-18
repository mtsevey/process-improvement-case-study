import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.patches as patches

# Load dataset
input_file = 'sales_data.csv'

df = pd.read_csv(input_file)
# Convert date strings to datetime
for col in ['Order Date', 'Ship Date']:
    df[col] = pd.to_datetime(df[col], errors='coerce')

# Compute cycle time (days between order and ship)
df['Cycle_Time'] = (df['Ship Date'] - df['Order Date']).dt.days

# Summary statistics for cycle time
summary = df['Cycle_Time'].describe()
summary.to_csv('cycle_time_summary.csv')

# Average cycle time by region
avg_by_region = df.groupby('Region')['Cycle_Time'].mean().sort_values(ascending=False)
avg_by_region_df = avg_by_region.reset_index().rename(columns={'Cycle_Time': 'Average_Cycle_Time'})
avg_by_region_df.to_csv('average_cycle_time_by_region.csv', index=False)

# Top 5 longest cycle time orders
top5 = df.nlargest(5, 'Cycle_Time')[['Region', 'Country', 'Order Date', 'Ship Date', 'Cycle_Time']]
top5.to_csv('top5_longest_cycle_times.csv', index=False)

# Histogram of cycle times
plt.figure(figsize=(8,5))
sns.histplot(df['Cycle_Time'], bins=10, kde=False, color='#4C72B0')
plt.title('Order Cycle Time Distribution')
plt.xlabel('Cycle Time (days)')
plt.ylabel('Number of Orders')
plt.tight_layout()
plt.savefig('cycle_time_distribution.png')

# Bar chart of average cycle time by region
plt.figure(figsize=(10,6))
ax = sns.barplot(x=avg_by_region.index, y=avg_by_region.values, palette='Blues_d')
ax.set_title('Average Order Cycle Time by Region')
ax.set_xlabel('Region')
ax.set_ylabel('Average Cycle Time (days)')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('average_cycle_time_by_region.png')

# Simple process flow diagram
fig, ax = plt.subplots(figsize=(10,2))
ax.axis('off')
box_width = 0.2
box_height = 0.4
positions = [0.05, 0.4, 0.75]
labels = ['Order Received', 'Order Processed', 'Order Shipped']
for x, label in zip(positions, labels):
    rect = patches.FancyBboxPatch((x, 0.3), box_width, box_height,
                                   boxstyle='round,pad=0.02', linewidth=1,
                                   edgecolor='black', facecolor='#deeaf6')
    ax.add_patch(rect)
    ax.text(x + box_width/2, 0.5, label, ha='center', va='center', fontsize=9)
# Draw arrows between boxes
arrow_props = dict(arrowstyle='->', lw=1)
ax.annotate('', xy=(positions[1], 0.5), xytext=(positions[0] + box_width, 0.5), arrowprops=arrow_props)
ax.annotate('', xy=(positions[2], 0.5), xytext=(positions[1] + box_width, 0.5), arrowprops=arrow_props)
# Title
ax.text(0.5, 0.8, 'Order Fulfillment Process Flow', ha='center', fontsize=12, fontweight='bold')
plt.savefig('process_flow.png', bbox_inches='tight')

print('Analysis complete.')

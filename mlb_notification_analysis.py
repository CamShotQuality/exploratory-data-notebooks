import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

# Data for each day
data = {
    'Date': [
        '2025-06-12',
        '2025-06-13',
        '2025-06-14',
        '2025-06-15',
        '2025-06-16',
        '2025-06-17',
        '2025-06-18'
    ],
    'Total_Games': [8, 15, 15, 15, 7, 15, 11],
    'Total_Pitcher_Changes': [45, 106, 99, 97, 42, 102, 73],
    'Correct_Notifications': [30, 61, 68, 54, 31, 53, 34],
    'Average_Lead_Time': [7.6, 7.9, 5.8, 7.6, 10.0, 7.5, 8.4]
}

# Create DataFrame
df = pd.DataFrame(data)

# Calculate success rate
df['Success_Rate'] = (df['Correct_Notifications'] / df['Total_Pitcher_Changes'] * 100).round(1)

# Set style
plt.style.use('seaborn')
sns.set_palette("husl")

# Create figure with two subplots
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))
fig.suptitle('MLB Pitcher Change Notification Analysis\nJune 12-18, 2025', fontsize=16, y=0.95)

# Plot 1: Success Rate Over Time
sns.lineplot(data=df, x='Date', y='Success_Rate', marker='o', linewidth=2, markersize=10, ax=ax1)
ax1.set_title('Daily Notification Success Rate')
ax1.set_ylabel('Success Rate (%)')
ax1.set_xlabel('')
ax1.grid(True)
ax1.tick_params(axis='x', rotation=45)

# Add value labels on the first plot
for x, y in zip(df['Date'], df['Success_Rate']):
    ax1.annotate(f'{y}%', 
                (x, y),
                textcoords="offset points",
                xytext=(0,10),
                ha='center')

# Plot 2: Daily Metrics Comparison
df_melted = df.melt(id_vars=['Date'], 
                    value_vars=['Total_Games', 'Total_Pitcher_Changes', 'Correct_Notifications'],
                    var_name='Metric', value_name='Count')

sns.barplot(data=df_melted, x='Date', y='Count', hue='Metric', ax=ax2)
ax2.set_title('Daily Game Metrics')
ax2.set_ylabel('Count')
ax2.set_xlabel('Date')
ax2.tick_params(axis='x', rotation=45)
ax2.legend(title='')

# Adjust layout
plt.tight_layout()

# Save the plot
plt.savefig('mlb_notification_analysis.png', dpi=300, bbox_inches='tight')

# Print summary statistics
print("\nSummary Statistics:")
print("-" * 50)
print(f"Overall Success Rate: {(df['Correct_Notifications'].sum() / df['Total_Pitcher_Changes'].sum() * 100):.1f}%")
print(f"Average Lead Time: {df['Average_Lead_Time'].mean():.1f} minutes")
print(f"Total Games: {df['Total_Games'].sum()}")
print(f"Total Pitcher Changes: {df['Total_Pitcher_Changes'].sum()}")
print(f"Total Correct Notifications: {df['Correct_Notifications'].sum()}") 
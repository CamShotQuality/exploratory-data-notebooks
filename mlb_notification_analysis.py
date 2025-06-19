import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

# Data for each day
data = {
    'Date': [
        '2025-06-04',
        '2025-06-05',
        '2025-06-06',
        '2025-06-07',
        '2025-06-08',
        '2025-06-09',
        '2025-06-10',
        '2025-06-11',
        '2025-06-12',
        '2025-06-13',
        '2025-06-14',
        '2025-06-15',
        '2025-06-16',
        '2025-06-17',
        '2025-06-18'
    ],
    'Total_Games': [14, 13, 13, 16, 15, 9, 12, 14, 8, 15, 15, 15, 7, 15, 11],
    'Total_Pitcher_Changes': [87, 82, 89, 102, 96, 69, 74, 80, 45, 106, 99, 97, 42, 102, 73],
    'Correct_Notifications': [61, 52, 56, 57, 64, 40, 42, 57, 30, 61, 68, 54, 31, 53, 34],
    'Average_Lead_Time': [7.0, 8.8, 8.8, 7.0, 10.0, 10.2, 9.4, 7.0, 7.6, 7.9, 5.8, 7.6, 10.0, 7.5, 8.4],
    'Failed_Streams': [0, 0, 3, 4, 1, 1, 2, 0, 0, 0, 0, 0, 0, 0, 5]
}

# Create DataFrame
df = pd.DataFrame(data)

# Calculate success rate
df['Success_Rate'] = (df['Correct_Notifications'] / df['Total_Pitcher_Changes'] * 100).round(1)

# Set style
plt.style.use('seaborn-v0_8')
sns.set_palette("husl")

# Create figure with three subplots
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(12, 15))
fig.suptitle('MLB Pitcher Change Notification Analysis', fontsize=16, y=0.95)

# Plot 1: Success Rate Over Time
sns.lineplot(data=df, x='Date', y='Success_Rate', marker='o', linewidth=2, markersize=10, ax=ax1)
ax1.set_ylabel('Success Rate (%)')
ax1.set_xlabel('')
ax1.grid(True)
ax1.tick_params(axis='x', rotation=45)

# Add vertical lines for implementation dates
implementation_dates = {
    '2025-06-05': 'Automated MLB Scheduling\nimplemented in prod',
    '2025-06-12': 'Automatic retry configuration\nfor failed streams enabled in prod'
}

for date, caption in implementation_dates.items():
    ax1.axvline(x=date, color='blue', linestyle='--', alpha=0.5)
    # Calculate y position for staggered annotations
    y_pos = ax1.get_ylim()[0] + (ax1.get_ylim()[1] - ax1.get_ylim()[0]) * (0.1 if date == '2025-06-05' else 0.2)
    ax1.annotate(caption, 
                xy=(date, ax1.get_ylim()[0]),
                xytext=(10, 20),
                textcoords='offset points',
                ha='left',
                va='bottom',
                bbox=dict(boxstyle='round,pad=0.5', fc='white', alpha=0.8),
                arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0'))

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
ax2.set_xlabel('')
ax2.tick_params(axis='x', rotation=45)
ax2.legend(title='')

# Plot 3: Failed Streams
sns.lineplot(data=df, x='Date', y='Failed_Streams', marker='o', linewidth=2, markersize=10, ax=ax3)
ax3.set_title('Streams Failed in Production')
ax3.set_ylabel('Number of Failed Streams')
ax3.set_xlabel('Date')
ax3.grid(True)
ax3.tick_params(axis='x', rotation=45)

# Add value labels on the third plot
for x, y in zip(df['Date'], df['Failed_Streams']):
    if pd.notna(y):  # Only add label if value is not None
        ax3.annotate(str(int(y)), 
                    (x, y),
                    textcoords="offset points",
                    xytext=(0,10),
                    ha='center')

# Add vertical lines in all plots
for date in implementation_dates.keys():
    ax2.axvline(x=date, color='blue', linestyle='--', alpha=0.5)
    ax3.axvline(x=date, color='blue', linestyle='--', alpha=0.5)

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
print(f"Total Failed Streams: {df['Failed_Streams'].sum()}") 
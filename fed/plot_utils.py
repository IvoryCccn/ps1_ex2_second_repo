import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

plt.style.use('seaborn-v0_8')
sns.set_palette("husl")

def plot_gdp_trends(df, countries=None):
    """Plot GDP trends"""
    if countries is None:
        countries = [col for col in df.columns if col not in ['Year'] and not col.startswith('log_')]
    
    plt.figure(figsize=(12, 6))
    
    for country in countries:
        if country in df.columns:
            plt.plot(df['Year'], df[country], label=country, linewidth=2)
    
    plt.title('GDP Trends by Country (2000-2022)')
    plt.xlabel('Year')
    plt.ylabel('GDP (Current US$)')
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()

def plot_log_gdp_trends(df, countries=None):
    """Plot log-GDP trends"""
    log_cols = [col for col in df.columns if col.startswith('log_')]
    
    if not log_cols:
        return
    
    plt.figure(figsize=(12, 6))
    
    for log_col in log_cols:
        country = log_col.replace('log_', '')
        plt.plot(df['Year'], df[log_col], label=country, linewidth=2)
    
    plt.title('Log GDP Trends by Country (2000-2022)')
    plt.xlabel('Year')
    plt.ylabel('Log GDP (Current US$)')
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()

def plot_growth_rates(df, countries=None):
    """Plot GDP growth rates"""
    if countries is None:
        countries = [col for col in df.columns if col not in ['Year'] and not col.startswith('log_')]
    
    plt.figure(figsize=(12, 6))
    
    for country in countries:
        if country in df.columns:
            growth = df[country].pct_change() * 100
            plt.plot(df['Year'][1:], growth[1:], label=country, linewidth=2)
    
    plt.title('GDP Annual Growth Rates (%)')
    plt.xlabel('Year')
    plt.ylabel('Growth Rate (%)')
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.grid(True, alpha=0.3)
    plt.axhline(y=0, color='red', linestyle='--', alpha=0.5)
    plt.tight_layout()
    plt.show()
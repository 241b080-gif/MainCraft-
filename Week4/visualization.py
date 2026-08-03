
import matplotlib.pyplot as plt
from collections import defaultdict

def generate_charts(expenses):
    cat=defaultdict(float)
    mon=defaultdict(float)
    for e in expenses:
        cat[e["category"]]+=float(e["amount"])
        mon[e["date"][:7]]+=float(e["amount"])

    if not cat:
        print("No data to visualize.")
        return

    plt.figure(figsize=(6,4))
    plt.bar(cat.keys(),cat.values())
    plt.title("Category Spending")
    plt.tight_layout()
    plt.savefig("charts/bar_chart.png")
    plt.close()

    plt.figure(figsize=(5,5))
    plt.pie(cat.values(),labels=cat.keys(),autopct="%1.1f%%")
    plt.title("Category Share")
    plt.savefig("charts/pie_chart.png")
    plt.close()

    months=sorted(mon)
    plt.figure(figsize=(6,4))
    plt.plot(months,[mon[m] for m in months],marker="o")
    plt.title("Monthly Spending")
    plt.tight_layout()
    plt.savefig("charts/monthly_trend.png")
    plt.close()

    print("Charts saved in charts/")

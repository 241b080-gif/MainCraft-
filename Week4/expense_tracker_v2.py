
import csv, os, datetime
from collections import defaultdict
from visualization import generate_charts

CSV_FILE="expenses.csv"
FIELDS=["date","description","category","amount"]

def ensure():
    if not os.path.exists(CSV_FILE):
        with open(CSV_FILE,"w",newline="") as f:
            csv.DictWriter(f,fieldnames=FIELDS).writeheader()

def load():
    ensure()
    with open(CSV_FILE) as f:
        return list(csv.DictReader(f))

def add():
    ensure()
    d=input("Description: ").strip() or "Unnamed"
    while True:
        try:
            a=float(input("Amount: "))
            break
        except:
            print("Invalid amount")
    c=input("Category: ").strip() or "General"
    dt=input("Date YYYY-MM-DD(blank=today): ").strip()
    try:
        dt=(datetime.datetime.strptime(dt,"%Y-%m-%d").date().isoformat() if dt else datetime.date.today().isoformat())
    except:
        dt=datetime.date.today().isoformat()
    with open(CSV_FILE,"a",newline="") as f:
        csv.DictWriter(f,fieldnames=FIELDS).writerow({"date":dt,"description":d,"category":c,"amount":f"{a:.2f}"})

def view():
    ex=load()
    total=0
    for e in ex:
        print(e)
        total+=float(e["amount"])
    print("Total:",round(total,2))

def search():
    ex=load()
    s=input("Category: ").lower()
    t=0
    for e in ex:
        if e["category"].lower()==s:
            print(e)
            t+=float(e["amount"])
    print("Subtotal:",round(t,2))

def monthly():
    d=defaultdict(float)
    for e in load():
        d[e["date"][:7]]+=float(e["amount"])
    for k in sorted(d):
        print(k,d[k])

def summary():
    ex=load()
    d=defaultdict(float)
    total=0
    for e in ex:
        total+=float(e["amount"]); d[e["category"]]+=float(e["amount"])
    print("Entries:",len(ex))
    print("Total:",round(total,2))
    if ex: print("Average:",round(total/len(ex),2))
    for k,v in d.items():
        print(k,v)

def menu():
    while True:
        print("\n1.Add\n2.View\n3.Search\n4.Monthly\n5.Summary\n6.Visualize\n7.Exit")
        c=input("> ")
        if c=="1": add()
        elif c=="2": view()
        elif c=="3": search()
        elif c=="4": monthly()
        elif c=="5": summary()
        elif c=="6": generate_charts(load())
        elif c=="7": break

if __name__=="__main__":
    menu()

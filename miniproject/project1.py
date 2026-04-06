import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = {
    "Name": ["Mysteriousblack", "Pallet pink", "Ghost Green", "Lead Red", "Stealth Silver"],
    "Math": [100, 75, 90, 79, 85],
    "Science": [95, 80, 88, 82, 90],
    "English": [92, 78, 85, 80, 88]
}

df = pd.DataFrame(data)

df['Average'] = df[["Math", "Science", "English"]].mean(axis=1)

topper = df.loc[df['Average'].idxmax()]

subject_avg = df[["Math", "Science", "English"]].mean()
mark_subject = df[["Math","Science","English"]].sum()
weak_subject = subject_avg.min()

print("📊 Student Data: \n", df)
print("\n🏆 Topper: \n", topper)
print("\n📉 Weakest Subject: \n", weak_subject)

plt.figure()
sns.barplot(x = 'Name', y = 'Average', data = df)
plt.title("Average Marks of Students")
plt.show()

df.set_index("Name")[["Math", "Science", "English"]].plot(kind="bar")
plt.title("Subject wise Marks")
plt.ylabel("Marks")
plt.show()

plt.figure()
sns.heatmap(df[["Math", "Science", "English"]].corr(), annot=True, cmap="coolwarm")
plt.title("Marks Heatmap")
plt.show()

plt.figure()
sns.histplot(df["Average"])
plt.title("Average Marks Distribution")
plt.show()


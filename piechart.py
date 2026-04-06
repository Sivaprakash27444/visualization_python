import matplotlib.pyplot as plt

names = ["Python", "Java", "C++", "SQL"]
marks = [80, 90, 75,50]

plt.pie(marks, labels=names)
plt.title("Programming Language Popularity")
plt.show()
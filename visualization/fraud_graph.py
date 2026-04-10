import matplotlib.pyplot as plt

# Fixed values
labels = ["Normal", "Fraud"]
values = [15000, 22000]

plt.figure(figsize=(6,4))
plt.bar(labels, values)

plt.title("Normal vs Fraud Transactions")
plt.xlabel("Transaction Type")
plt.ylabel("Transaction Amount")

plt.show()
import tkinter as tk
from tkinter import messagebox
# import pickle
from sklearn.linear_model import LinearRegression
import numpy as np

# Function to predict sales of next month
def predict_sales():
    # Extracting sales data from entry fields
    sales_data = []
    for entry in entries:
        try:
            sales_data.append(float(entry.get()))
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers for sales data")
            return

    # Checking if exactly 12 months of data are entered
    if len(sales_data) != 12:
        messagebox.showerror("Error", "Please enter sales data for all 12 months")
        return
    X = np.arange(1, 13).reshape(-1, 1)
    y = np.array(sales_data).reshape(-1, 1)

    # Creating and fitting linear regression model
    model = LinearRegression()
    model.fit(X, y)

    # Predicting sales for next month (13th month)
    next_month_sales = model.predict([[13]])

    # Displaying predicted sales
    output_label.config(text="Predicted sales of next month: {:.2f}".format(next_month_sales[0][0]))


# Load the trained model
# with open('gmodel.pkl', 'rb') as f:
#     model = pickle.load(f)

# Create Tkinter window
root = tk.Tk()
root.title("Sales Prediction")

# Configure window size and background color
root.geometry("300x500")    
root.configure(bg="#f0f0f0")

# Create labels and entry fields for 12 months
entries = []
for i in range(12):
    month_label = tk.Label(root, text="Month {}: ".format(i+1), bg="#f0f0f0", font=("Arial", 10))
    month_label.grid(row=i, column=0, padx=5, pady=5, sticky="w")
    entry = tk.Entry(root)
    entry.grid(row=i, column=1, padx=5, pady=5)
    entries.append(entry)

# Create Predict button with styling
predict_button = tk.Button(root, text="Predict", command=predict_sales, bg="#4caf50", fg="white", font=("Arial", 12, "bold"))
predict_button.grid(row=12, columnspan=2, padx=5, pady=10, sticky="we")

# Create label for output with styling
output_label = tk.Label(root, text="", bg="#f0f0f0", font=("Arial", 12, "italic"))
output_label.grid(row=13, columnspan=2, padx=5, pady=5, sticky="w")

# Add padding to all widgets
for child in root.winfo_children():
    child.grid_configure(padx=10, pady=5)

# Start the Tkinter event loop
root.mainloop()

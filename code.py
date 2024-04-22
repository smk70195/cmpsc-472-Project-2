import csv
import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
import matplotlib.pyplot as plt
import seaborn as sns
import io
import base64

class DrugAbuseProject:
    def __init__(self):
        self.data = {}  # You can use this dictionary to store data related to drug abuse and addiction
        self.sodium_to_potassium_ratios = []  # Initialize the list to store ratios
        
    def gather_data(self):
        # Open the CSV file and read data
        with open('drug200.csv', 'r') as file:
            reader = csv.DictReader(file)
            
            # Iterate over each row in the CSV file
            for row in reader:
                # Assuming 'Drug' is the key for drug names and 'Na_to_K' is the key for the sodium to potassium ratio
                drug_name = row['Drug']
                sodium_to_potassium_ratio = float(row['Na_to_K'])
                
                # Add drug name and sodium to potassium ratio to the data dictionary
                self.data[drug_name] = sodium_to_potassium_ratio
                self.sodium_to_potassium_ratios.append(sodium_to_potassium_ratio)
        
    def analyze_data(self):
        # Analyze the gathered data
        if not self.sodium_to_potassium_ratios:
            messagebox.showinfo("No Data", "Please gather data first.")
            return "No data to analyze."
        
        # Calculate average sodium to potassium ratio
        average_ratio = sum(self.sodium_to_potassium_ratios) / len(self.sodium_to_potassium_ratios)
        return f"Average Sodium to Potassium Ratio: {average_ratio:.2f}"
    
    def visualize_data(self):
        # Visualize the analyzed data
        
        if not self.sodium_to_potassium_ratios:
            messagebox.showinfo("No Data", "Please gather data first.")
            return None
        
        # Example 1: Create a histogram of sodium to potassium ratios
        plt.figure(figsize=(8, 6))
        plt.hist(self.sodium_to_potassium_ratios, bins=10, color='skyblue', edgecolor='black')
        plt.title('Distribution of Sodium to Potassium Ratios')
        plt.xlabel('Ratio')
        plt.ylabel('Frequency')
        plt.grid(True)
        
        # Save the plot to a BytesIO object
        buffer = io.BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        
        # Convert the plot to a Tkinter PhotoImage
        img = Image.open(buffer)
        img_tk = ImageTk.PhotoImage(img)
        
        return img_tk
        
    def develop_interface(self):
        # Develop a user-friendly interface using Tkinter
        
        # Create the main window
        root = tk.Tk()
        root.title("Drug Abuse Project Interface")
        root.geometry("400x400")
        
        # Add a label to the window
        label = tk.Label(root, text="Welcome to Drug Abuse Project Interface!", font=("Arial", 14))
        label.pack(pady=20)
        
        # Add a button to gather data
        gather_button = tk.Button(root, text="Gather Data", command=self.gather_data)
        gather_button.pack()
        
        # Add a button to analyze data
        analyze_button = tk.Button(root, text="Analyze Data", command=self.display_analysis)
        analyze_button.pack()
        
        # Add a button to visualize data
        visualize_button = tk.Button(root, text="Visualize Data", command=self.display_visualization)
        visualize_button.pack()
        
        # Label to display analysis result
        self.analysis_label = tk.Label(root, text="", font=("Arial", 12), wraplength=380)
        self.analysis_label.pack(pady=10)
        
        # Label to display visualization
        self.visualization_label = tk.Label(root)
        self.visualization_label.pack(pady=10)
        
        # Run the Tkinter event loop
        root.mainloop()
        
    def display_analysis(self):
        analysis_result = self.analyze_data()
        self.analysis_label.config(text=analysis_result)
        
    def display_visualization(self):
        visualization_img = self.visualize_data()
        if visualization_img:
            self.visualization_label.config(image=visualization_img)
            self.visualization_label.image = visualization_img  # Keep a reference to prevent garbage collection
        
    def collaborate_coding(self):
        # Implement methods to collaborate with team members using version control systems like Git
        # This could involve using Git commands or integrating with Git APIs
        
        # Example: Display a message box with collaboration instructions
        messagebox.showinfo("Collaboration", "Remember to use Git for collaborative coding!")
        
    
if __name__ == "__main__":
    project = DrugAbuseProject()
    project.develop_interface()


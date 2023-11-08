# gui.py
import customtkinter as ctk
import tkinter as tk
from threading import Thread
from main import scrape_deals


app = ctk.CTk()

app.geometry("1000x800")  # Adjust size to accommodate multiple textboxes
app.title("Price Scraper")

# Dictionary to hold textboxes for each store
store_textboxes = {}

def run_scraping():
    deals = scrape_deals()
    display_deals(deals)

def start_scraping():
    scraping_thread = Thread(target=run_scraping)
    scraping_thread.daemon = True
    scraping_thread.start()

def display_deals(deals):
    global store_textboxes
    # Clear previous content and display new deals
    for deal in deals:
        store = deal['store']
        # Create a textbox for the store if it doesn't exist
        if store not in store_textboxes:
            frame = ctk.CTkFrame(app)
            frame.pack(pady=10, padx=10, fill='both', expand=True)
            label = ctk.CTkLabel(frame, text=store, anchor="w", height=25)
            label.pack(fill='x')
            textbox = ctk.CTkTextbox(frame, height=10, width=80)
            textbox.pack(pady=5, fill='both', expand=True)
            store_textboxes[store] = textbox
        # Insert deal into the appropriate textbox
        store_textboxes[store].insert(tk.END, f"{deal['title']} at {deal['price']}\n")

scan_button = ctk.CTkButton(app, text="Scan Prices", command=start_scraping)
scan_button.pack(pady=20)

app.mainloop()

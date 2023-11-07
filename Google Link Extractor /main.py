from googlesearch import search
from tkinter import *

def search_links():
    user_query = query_entry.get()
    num_results = int(num_results_entry.get())

    results = search(user_query, num_results=num_results, lang='en', advanced=True)
    
    # Create a frame to contain the links
    link_frame = Frame(root)
    link_frame.pack()

    # Create a scrollbar
    scrollbar = Scrollbar(link_frame)
    scrollbar.pack(side=RIGHT, fill=Y)

    # Create a listbox to display the links with increased width
    link_listbox = Listbox(link_frame, yscrollcommand=scrollbar.set, width=90, height=20)
    link_listbox.pack(side=LEFT, fill=BOTH, expand=True)

    scrollbar.config(command=link_listbox.yview)

    for link in results:
        link_listbox.insert(END, f"   {link.title} - {link}")

def show_details(link):
    link_details = Toplevel(root)
    link_details.title("Link Details")
    
    link_label = Label(link_details, text=f"Link: {link}")
    link_label.config(font=("Arial", 12))
    link_label.pack()

root = Tk()
root.title("Google Link Extractor")
root.geometry("600x500")

title_label = Label(root, text="Google Link Extractor", font=("Arial", 20))
title_label.pack()

query_label = Label(root, text="Enter your query:")
query_label.config(font=("Arial", 14))
query_label.pack()
query_entry = Entry(root, font=("Arial", 12))
query_entry.pack()

num_results_label = Label(root, text="Number of results:")
num_results_label.config(font=("Arial", 14))
num_results_label.pack()
num_results_entry = Entry(root, font=("Arial", 12))
num_results_entry.pack()

search_button = Button(root, text="Search", command=search_links)
search_button.config(font=("Arial", 14))
search_button.pack()

root.mainloop()

from tkinter import *

def button_click(bus_id):
    print(f"Bus {bus_id} clicked")

def create_table(frame, data):
    for row, (bus_id, operator, bus_type, available_seats, total_seats, fare) in enumerate(data):
        button_text = f"{operator} - {bus_type}"
        button = Button(frame, text=button_text, command=lambda id=bus_id: button_click(id))
        button.grid(row=row, column=0, padx=10, pady=5)

        id_label = Label(frame, text=str(bus_id))
        id_label.grid(row=row, column=1, padx=10, pady=5)

def on_button_click():
    # Replace this list with your data
    data_list = [
        (1, "Operator A", "Sleeper", 20, 50, 500),
        (2, "Operator B", "AC", 15, 30, 800),
        # Add more entries as needed
    ]

    create_table(frame, data_list)

if __name__ == "__main__":
    root = Tk()
    root.title("Bus Information Table")

    frame = Frame(root)
    frame.pack(padx=20, pady=20)

    create_table_button = Button(root, text="Create Table", command=on_button_click)
    create_table_button.pack(pady=10)

    root.mainloop()

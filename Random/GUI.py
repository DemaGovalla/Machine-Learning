import tkinter as tk
from multiprocessing import Queue, Process, freeze_support
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def update_label(queue):
    while True:
        data = queue.get()
        label.config(text=data)

def update_plot(queue):
    fig, ax = plt.subplots()
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.get_tk_widget().pack()

    x_data, y_data = [], []
    line, = ax.plot(x_data, y_data)

    while True:
        data = queue.get()
        x_data.append(len(x_data))
        y_data.append(data)
        line.set_data(x_data, y_data)
        ax.relim()
        ax.autoscale_view()
        canvas.draw()

if __name__ == '__main__':
    freeze_support()

    queue = Queue()

    root = tk.Tk()
    label = tk.Label(root, font=('Arial', 24))
    label.pack()

    p_label = Process(target=update_label, args=(queue,))
    p_label.start()

    p_plot = Process(target=update_plot, args=(queue,))
    p_plot.start()

    root.mainloop()

import tkinter as tk
import webbrowser
root = tk.Tk()

# specify size of window.
root.title("BANK MARKETING ANALYSIS")
root.geometry("700x700") 
root.configure(bg="#333333")

frame1 = tk.Frame(root, bg="#333333")
frame1.pack()



label0 = tk.Label(frame1, text = "BANK MARKETING ANALYSIS", fg = "#00FFFF" ,font=('Aerial', 50, 'bold'), bg = "#333333")
label0.pack(anchor = "center", pady = 100)

label1 = tk.Label(frame1, text="Predicts whether the person will take term deposit or not\n", fg="#FFFFFF", font=('Aerial', 30), bg="#333333")
label1.pack()

new = 1
url = "https://e98e5bf81ef419847b.gradio.live"

def openweb():
    webbrowser.open(url,new=new)

Btn = tk.Button(root, text = "Click here to predict", width = 22, height = 2, command=openweb)
Btn.pack()


root.mainloop()
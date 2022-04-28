from tkinter import (Button, DoubleVar, Entry, IntVar, Label, Radiobutton,
                     StringVar, Tk)


class TipCalulator:
    def __init__(self):
        window = Tk()
        window.title("Tip Calculator App")
        window.configure(background="sky Blue")
        window.geometry("400x300")
        window.resizable(width=False, height=False)

        self.meal_cost = StringVar()
        self.tip_percent = IntVar()
        self.tip = StringVar()
        self.total_cost = StringVar()

        tip_percents = Label(window,
                             text="Tip Percentage",
                             bg="purple",
                             fg="white")
        tip_percents.grid(column=0, row=0, padx=15, pady=15)

        bill_amount = Label(window,
                            text="Total Bill Amount",
                            bg="black",
                            fg="white")
        bill_amount.grid(column=1, row=0, padx=15, pady=15)

        bill_amount_entry = Entry(window,
                                  textvariable=self.meal_cost,
                                  width=14)
        bill_amount_entry.grid(column=2, row=0, padx=15, pady=15)

        five_prcnt_tip = Radiobutton(window,
                                     text="05%",
                                     variable=self.tip_percent,
                                     value=5)
        five_prcnt_tip.grid(column=0, row=1)
        ten_prcnt_tip = Radiobutton(window,
                                    text="10%",
                                    variable=self.tip_percent,
                                    value=10)
        ten_prcnt_tip.grid(column=0, row=2)
        fifteen_prcnt_tip = Radiobutton(window,
                                        text="15%",
                                        variable=self.tip_percent,
                                        value=15)
        fifteen_prcnt_tip.grid(column=0, row=3)
        twenty_prcnt_tip = Radiobutton(window,
                                       text="20%",
                                       variable=self.tip_percent,
                                       value=20)
        twenty_prcnt_tip.grid(column=0, row=4)
        twenty_five_prcnt_tip = Radiobutton(window,
                                            text="25%",
                                            variable=self.tip_percent,
                                            value=25)
        twenty_five_prcnt_tip.grid(column=0, row=5)
        thirty_prcnt_tip = Radiobutton(window,
                                       text="30%",
                                       variable=self.tip_percent,
                                       value=30)
        thirty_prcnt_tip.grid(column=0, row=6)

        tip_amount_lbl = Label(window,
                               text="Tip Amount",
                               bg="brown",
                               fg="white")
        tip_amount_lbl.grid(column=1, row=3, padx=15)
        tip_amount_entry = Entry(window, textvariable=self.tip, width=14)
        tip_amount_entry.grid(column=2, row=3)

        bill_total_lbl = Label(window,
                               text="Bill Total",
                               bg="blue",
                               fg="white")
        bill_total_lbl.grid(column=1, row=5)
        bill_total_entry = Entry(window,
                                 textvariable=self.total_cost,
                                 width=14)
        bill_amount_entry.grid(column=2, row=5)

        window.mainloop()


TipCalulator()

#/usr/bin/env python3

import tkinter as tk
from tkinter import messagebox


class NumberSystemConverterGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Number System Converter")

        self.decimal_label = tk.Label(
            self.master, text="Enter decimal number:")
        self.decimal_label.pack()

        self.decimal_entry = tk.Entry(self.master)
        self.decimal_entry.pack()

        self.binary_label = tk.Label(self.master, text="Enter binary number:")
        self.binary_label.pack()

        self.binary_entry = tk.Entry(self.master)
        self.binary_entry.pack()

        self.octal_label = tk.Label(self.master, text="Enter octal number:")
        self.octal_label.pack()

        self.octal_entry = tk.Entry(self.master)
        self.octal_entry.pack()

        self.hexadecimal_label = tk.Label(
            self.master, text="Enter hexadecimal number:")
        self.hexadecimal_label.pack()

        self.hexadecimal_entry = tk.Entry(self.master)
        self.hexadecimal_entry.pack()

        self.decToBin_button = tk.Button(
            self.master, text="D to B", command=lambda: self.handle_convert(1))
        self.decToBin_button.pack()

        self.decToOct_button = tk.Button(
            self.master, text="D to O", command=lambda: self.handle_convert(2))
        self.decToOct_button.pack()

        self.decToHex_button = tk.Button(
            self.master, text="D to H", command=lambda: self.handle_convert(3))
        self.decToHex_button.pack()

        self.binToDec_button = tk.Button(
            self.master, text="B to D", command=lambda: self.handle_convert(4))
        self.binToDec_button.pack()

        self.binToOct_button = tk.Button(
            self.master, text="B to O", command=lambda: self.handle_convert(5))
        self.binToOct_button.pack()

        self.binToHex_button = tk.Button(
            self.master, text="B to H", command=lambda: self.handle_convert(6))
        self.binToHex_button.pack()

        self.octToDec_button = tk.Button(
            self.master, text="O to D", command=lambda: self.handle_convert(7))
        self.octToDec_button.pack()

        self.octToBin_button = tk.Button(
            self.master, text="O to B", command=lambda: self.handle_convert(8))
        self.octToBin_button.pack()

        self.octToHex_button = tk.Button(
            self.master, text="O to H", command=lambda: self.handle_convert(9))
        self.octToHex_button.pack()

        self.hexToDec_button = tk.Button(
            self.master, text="H to D", command=lambda: self.handle_convert(10))
        self.hexToDec_button.pack()

        self.hexToBin_button = tk.Button(
            self.master, text="H to B", command=lambda: self.handle_convert(11))
        self.hexToBin_button.pack()

        self.hexToOct_button = tk.Button(
            self.master, text="H to O", command=lambda: self.handle_convert(12))
        self.hexToOct_button.pack()

        self.result_label = tk.Label(self.master, text="",font=("Algerian","bold",12))
        self.result_label.pack()

    def decimal_to_binary(self, decimal):
        return bin(decimal)[2:]

    def decimal_to_octal(self, decimal):
        return oct(decimal)[2:]

    def decimal_to_hexadecimal(self, decimal):
        return hex(decimal)[2:]

    def binary_to_decimal(self, binary):
        return int(binary, 2)

    def binary_to_octal(self, binary):
        decimal = self.binary_to_decimal(binary)
        return self.decimal_to_octal(decimal)

    def binary_to_hexadecimal(self, binary):
        decimal = self.binary_to_decimal(binary)
        return self.decimal_to_hexadecimal(decimal)

    def octal_to_decimal(self, octal):
        return int(octal, 8)

    def octal_to_binary(self, octal):
        decimal = self.octal_to_decimal(octal)
        return self.decimal_to_binary(decimal)

    def octal_to_hexadecimal(self, octal):
        decimal = self.octal_to_decimal(octal)
        return self.decimal_to_hexadecimal(decimal)

    def hexadecimal_to_decimal(self, hexadecimal):
        return int(hexadecimal, 16)

    def hexadecimal_to_binary(self, hexadecimal):
        decimal = self.hexadecimal_to_decimal(hexadecimal)
        return self.decimal_to_binary(decimal)

    def hexadecimal_to_octal(self, hexadecimal):
        decimal = self.hexadecimal_to_decimal(hexadecimal)
        return self.decimal_to_octal(decimal)

    def handle_convert(self, choice):
        try:
            if choice == 1:
                decimal = int(self.decimal_entry.get())
                binary = self.decimal_to_binary(decimal)
                self.result_label.config(text="Binary: " + binary)
            elif choice == 2:
                decimal = int(self.decimal_entry.get())
                octal = self.decimal_to_octal(decimal)
                self.result_label.config(text="Octal: " + octal)
            elif choice == 3:
                decimal = int(self.decimal_entry.get())
                hexadecimal = self.decimal_to_hexadecimal(decimal)
                self.result_label.config(text="Hexadecimal: " + hexadecimal)
            elif choice == 4:
                binary = self.binary_entry.get()
                decimal = self.binary_to_decimal(binary)
                self.result_label.config(text="Decimal: " + str(decimal))
            elif choice == 5:
                binary = self.binary_entry.get()
                octal = self.binary_to_octal(binary)
                self.result_label.config(text="Octal: " + octal)
            elif choice == 6:
                binary = self.binary_entry.get()
                hexadecimal = self.binary_to_hexadecimal(binary)
                self.result_label.config(text="Hexadecimal: " + hexadecimal)
            elif choice == 7:
                octal = self.octal_entry.get()
                decimal = self.octal_to_decimal(octal)
                self.result_label.config(text="Decimal: " + str(decimal))
            elif choice == 8:
                octal = self.octal_entry.get()
                binary = self.octal_to_binary(octal)
                self.result_label.config(text="Binary: " + binary)
            elif choice == 9:
                octal = self.octal_entry.get()
                hexadecimal = self.octal_to_hexadecimal(octal)
                self.result_label.config(text="Hexadecimal: " + hexadecimal)
            elif choice == 10:
                hexadecimal = self.hexadecimal_entry.get()
                decimal = self.hexadecimal_to_decimal(hexadecimal)
                self.result_label.config(text="Decimal: " + str(decimal))
            elif choice == 11:
                hexadecimal = self.hexadecimal_entry.get()
                binary = self.hexadecimal_to_binary(hexadecimal)
                self.result_label.config(text="Binary: " + binary)
            elif choice == 12:
                hexadecimal = self.hexadecimal_entry.get()
                octal = self.hexadecimal_to_octal(hexadecimal)
                self.result_label.config(text="Octal: " + octal)
            else:
                raise ValueError("Invalid choice")
        except ValueError as e:
            messagebox.showerror("Error", str(e))


if __name__ == "__main__":
    app = tk.Tk()
    converter_gui = NumberSystemConverterGUI(app)
    app.mainloop()

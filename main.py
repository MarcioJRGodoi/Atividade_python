import tkinter as tk
from tkinter import messagebox

class Conta:
    def __init__(self):
        self.transacoes = []

    def depositar(self, valor):
        self.transacoes.append(valor)

    def sacar(self, valor):
        if valor > sum(self.transacoes):
            return False
        self.transacoes.append(-valor)
        return True

    def extrato(self):
        return self.transacoes

    def saldo(self):
        return sum(self.transacoes)

def depositar():
    valor = float(valor_entry.get())
    conta.depositar(valor)
    atualizar_saldo()
    messagebox.showinfo("Sucesso", f"Depósito de R$ {valor:.2f} realizado com sucesso.")
    valor_entry.delete(0, tk.END)

def sacar():
    valor = float(valor_entry.get())
    if conta.sacar(valor):
        atualizar_saldo()
        messagebox.showinfo("Sucesso", f"Saque de R$ {valor:.2f} realizado com sucesso.")
    else:
        messagebox.showerror("Erro", "Saldo insuficiente para saque.")
    valor_entry.delete(0, tk.END)

def extrato():
    transacoes = conta.extrato()
    extrato_text.delete(1.0, tk.END)
    for transacao in transacoes:
        extrato_text.insert(tk.END, f"R$ {transacao:.2f}\n")

def atualizar_saldo():
    saldo = conta.saldo()
    saldo_label['text'] = f"Saldo atual: R$ {saldo:.2f}"

conta = Conta()

root = tk.Tk()
root.title("Banco")

valor_label = tk.Label(root, text="Valor:")
valor_label.pack()

valor_entry = tk.Entry(root)
valor_entry.pack()

depositar_button = tk.Button(root, text="Depositar", command=depositar)
depositar_button.pack()

sacar_button = tk.Button(root, text="Sacar", command=sacar)
sacar_button.pack()

extrato_button = tk.Button(root, text="Extrato", command=extrato)
extrato_button.pack()

saldo_label = tk.Label(root, text="")
saldo_label.pack()

extrato_text = tk.Text(root)
extrato_text.pack()

root.mainloop()

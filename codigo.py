import tkinter as tk
def calcular():
    # Função para calcular a operação selecionada
    try:
        num1 = float(entrada1.get())
        num2 = float(entrada2.get())
        operacao = operacao_var.get()

        if operacao == "+":
            resultado = num1 + num2
        elif operacao == "-":       
            resultado = num1 - num2
        elif operacao == "*":
            resultado = num1 * num2
        elif operacao == "/":
            if num2 != 0:
                resultado = num1 / num2
            else:
                resultado = "Erro: Divisão por zero"
        else:
            resultado = "Operação inválida"
        resultado_label.config(text="Resultado: " + str(resultado))

    except ValueError:
        resultado_label.config(text="Erro: Insira números válidos.")

# Criação da janela principal
janela = tk.Tk()    
janela.title("Calculadora Simples")

# Rótulos e campos de entrada
label1 = tk.Label(janela, text="Número 1:")
label1.grid(row=0, column=0, padx=10, pady=10)  
entrada1 = tk.Entry(janela)
entrada1.grid(row=0, column=1, padx=10, pady=10)

label2 = tk.Label(janela, text="Número 2:")
label2.grid(row=1, column=0, padx=10, pady=10)
entrada2 = tk.Entry(janela)
entrada2.grid(row=1, column=1, padx=10, pady=10)

# Menu de opções para a operação
operacoes = ["+", "-", "*", "/"]
operacao_var = tk.StringVar(janela)
operacao_var.set(operacoes[0])  # Define a operação padrão
dropdown_operacoes = tk.OptionMenu(janela, operacao_var, *operacoes)
dropdown_operacoes.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

# botao de calcular
botao_calcular = tk.Button(janela, text="Calcular", command=calcular)
botao_calcular.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Rótulo para exibir o resultado
resultado_label = tk.Label(janela, text="Resultado:")
resultado_label.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Inicia o loop principal da interface gráfica
janela.mainloop()
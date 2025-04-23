Explicação do Código:

import tkinter as tk: Importa a biblioteca Tkinter para criar a interface gráfica.
calcular(): Função chamada quando o botão "Calcular" é pressionado.
entrada1.get() e entrada2.get(): Obtêm o texto digitado nos campos de entrada.
float(): Converte o texto para números decimais.
operacao_var.get(): Obtém a operação selecionada no menu dropdown.
Bloco if/elif/else: Realiza a operação matemática correspondente.
resultado_label.config(text=...): Atualiza o texto do rótulo de resultado.
try...except ValueError: Trata erros caso o usuário digite algo que não seja um número.
janela = tk.Tk(): Cria a janela principal da aplicação.
label1, entrada1, etc.: Criam rótulos e campos de entrada de texto.
dropdown_operacoes: Cria um menu dropdown para escolher a operação.
botao_calcular: Cria o botão "Calcular" e associa a função calcular ao seu clique (command=calcular).
resultado_label: Cria um rótulo para exibir o resultado.
.grid(row=..., column=..., ...): Organiza os elementos na janela usando um sistema de grade.
janela.mainloop(): Inicia o loop de eventos do Tkinter, que mantém a janela aberta e responsiva às interações do usuário.

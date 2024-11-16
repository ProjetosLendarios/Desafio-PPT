import tkinter as tk
from tkinter import messagebox
import random
import os
from PIL import Image, ImageTk  # Certifique-se de que está importado corretamente

# Configuração da janela principal
root = tk.Tk()
root.title("Jogo do Pedra, Papel, Tesoura - Desafio PPT")
root.geometry("500x200")
root.configure(bg="#ADD8E6")  # Azul claro para o fundo

# Definir ícone da aplicação
icon_path = os.path.join(os.path.dirname(__file__), "../Docs/icon.ico")
if os.path.exists(icon_path):
    root.iconbitmap(icon_path)
else:
    messagebox.showwarning("Aviso", "Ícone não encontrado. O programa continuará sem o ícone.")

# Caminho absoluto para a pasta de imagens
current_dir = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(current_dir, "imagens")

# Verificar se as imagens existem
if not all(os.path.exists(os.path.join(image_path, img)) for img in ["pedra.png", "papel.png", "tesoura.png"]):
    messagebox.showerror("Erro", "Certifique-se de que as imagens 'pedra.png', 'papel.png' e 'tesoura.png' estão na pasta './imagens/'")
    root.destroy()

# Função para carregar e redimensionar imagens
def carregar_imagem(nome_arquivo, largura, altura):
    try:
        imagem = Image.open(os.path.join(image_path, nome_arquivo))
        imagem = imagem.resize((largura, altura), Image.LANCZOS)  # Redimensionar a imagem com alta qualidade
        return ImageTk.PhotoImage(imagem)
    except Exception as e:
        messagebox.showerror("Erro", f"Falha ao carregar a imagem '{nome_arquivo}': {e}")
        root.destroy()

# Carregar imagens redimensionadas
img_pedra = carregar_imagem("pedra.png", 100, 100)
img_papel = carregar_imagem("papel.png", 100, 100)
img_tesoura = carregar_imagem("tesoura.png", 100, 100)

# Função principal do jogo
def jogar(escolha_utilizador):
    opcoes = ["Pedra", "Papel", "Tesoura"]
    escolha_computador = random.choice(opcoes)

    resultado_texto = f"Computador escolheu: {escolha_computador}\n"
    if escolha_utilizador == escolha_computador:
        resultado_texto += "Empate!"
    elif (escolha_utilizador == "Pedra" and escolha_computador == "Tesoura") or \
         (escolha_utilizador == "Papel" and escolha_computador == "Pedra") or \
         (escolha_utilizador == "Tesoura" and escolha_computador == "Papel"):
        resultado_texto += "Você ganhou!"
    else:
        resultado_texto += "Computador ganhou!"

    messagebox.showinfo("Resultado", resultado_texto)

# Layout da interface
label_instrucao = tk.Label(root, text="Escolha uma opção:", font=("Helvetica", 16), bg="#ADD8E6", fg="#004080")
label_instrucao.pack(pady=10)

frame_opcoes = tk.Frame(root, bg="#ADD8E6")
frame_opcoes.pack(pady=20)

# Botões com imagens redimensionadas
btn_pedra = tk.Button(frame_opcoes, image=img_pedra, command=lambda: jogar("Pedra"), bg="#E6E6FA", activebackground="#D8BFD8")
btn_pedra.grid(row=0, column=0, padx=10)

btn_papel = tk.Button(frame_opcoes, image=img_papel, command=lambda: jogar("Papel"), bg="#E6E6FA", activebackground="#D8BFD8")
btn_papel.grid(row=0, column=1, padx=10)

btn_tesoura = tk.Button(frame_opcoes, image=img_tesoura, command=lambda: jogar("Tesoura"), bg="#E6E6FA", activebackground="#D8BFD8")
btn_tesoura.grid(row=0, column=2, padx=10)

# Iniciar a aplicação
root.mainloop()

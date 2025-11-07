import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import time
import random
import hashlib

class ChatBotSAKY:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("AI SAKY - Login")
        self.root.geometry("400x300")
        self.root.resizable(False, False)
        self.root.configure(bg='#fff0f5')
        
        # Credenciais pré-definidas
        self.credentials = {
            "admin": self.hash_password("admin123"),
            "usuario": self.hash_password("saky2024"),
            "ti": self.hash_password("tecinfo")
        }
        
        # Configurações de tema
        self.dark_mode = False
        self.current_user = None
        
        # Paleta de cores rosa/branco
        self.colors = {
            'light': {
                'bg': '#fff0f5',
                'bg_secondary': '#ffffff',
                'accent': '#ff69b4',
                'accent_light': '#ffb6c1',
                'text': '#333333',
                'text_secondary': '#666666'
            },
            'dark': {
                'bg': '#2d1b2d',
                'bg_secondary': '#3d2b3d',
                'accent': '#ff69b4',
                'accent_light': '#ff85b8',
                'text': '#ffffff',
                'text_secondary': '#cccccc'
            }
        }
        
        self.setup_login_screen()
    
    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()
    
    def setup_login_screen(self):
        # Frame principal
        main_frame = tk.Frame(self.root, bg=self.colors['light']['bg'])
        main_frame.pack(fill='both', expand=True, padx=20, pady=20)
        
        # Logo/Header
        header_frame = tk.Frame(main_frame, bg=self.colors['light']['bg'])
        header_frame.pack(pady=(0, 20))
        
        # Ícone Sakura
        sakura_icon = "🌸"
        icon_label = tk.Label(header_frame, text=sakura_icon, font=('Arial', 24), 
                             bg=self.colors['light']['bg'], fg=self.colors['light']['accent'])
        icon_label.pack()
        
        title_label = tk.Label(header_frame, text="AI SAKY", font=('Arial', 18, 'bold'),
                              bg=self.colors['light']['bg'], fg=self.colors['light']['accent'])
        title_label.pack(pady=(5, 0))
        
        subtitle_label = tk.Label(header_frame, text="Seu Assistente de TI", font=('Arial', 10),
                                 bg=self.colors['light']['bg'], fg=self.colors['light']['text_secondary'])
        subtitle_label.pack()
        
        # Formulário de login
        form_frame = tk.Frame(main_frame, bg=self.colors['light']['bg'])
        form_frame.pack(fill='both', expand=True)
        
        # Campo usuário
        tk.Label(form_frame, text="Usuário:", font=('Arial', 10, 'bold'),
                bg=self.colors['light']['bg'], fg=self.colors['light']['text']).pack(anchor='w', pady=(10, 5))
        
        self.user_entry = tk.Entry(form_frame, font=('Arial', 11), width=25,
                                  bg=self.colors['light']['bg_secondary'], relief='solid', bd=1)
        self.user_entry.pack(fill='x', pady=(0, 10))
        self.user_entry.bind('<Return>', lambda e: self.login())
        
        # Campo senha
        tk.Label(form_frame, text="Senha:", font=('Arial', 10, 'bold'),
                bg=self.colors['light']['bg'], fg=self.colors['light']['text']).pack(anchor='w', pady=(5, 5))
        
        self.pass_entry = tk.Entry(form_frame, font=('Arial', 11), width=25, show='*',
                                  bg=self.colors['light']['bg_secondary'], relief='solid', bd=1)
        self.pass_entry.pack(fill='x', pady=(0, 20))
        self.pass_entry.bind('<Return>', lambda e: self.login())
        
        # Botão de login
        login_btn = tk.Button(form_frame, text="Entrar", font=('Arial', 11, 'bold'),
                             bg=self.colors['light']['accent'], fg='white',
                             activebackground=self.colors['light']['accent_light'],
                             relief='flat', padx=20, pady=8, command=self.login)
        login_btn.pack(pady=10)
        
        # Dicas de login
        tip_frame = tk.Frame(main_frame, bg=self.colors['light']['bg'])
        tip_frame.pack(fill='x')
        
        tip_label = tk.Label(tip_frame, text="Dica: Use 'admin', 'usuario' ou 'ti' como usuário",
                           font=('Arial', 8), bg=self.colors['light']['bg'], 
                           fg=self.colors['light']['text_secondary'])
        tip_label.pack()
    
    def login(self):
        username = self.user_entry.get()
        password = self.pass_entry.get()
        
        if not username or not password:
            messagebox.showerror("Erro", "Por favor, preencha todos os campos!")
            return
        
        hashed_password = self.hash_password(password)
        
        if username in self.credentials and self.credentials[username] == hashed_password:
            self.current_user = username
            self.open_chat_screen()
        else:
            messagebox.showerror("Erro", "Credenciais inválidas!")
    
    def open_chat_screen(self):
        self.root.destroy()
        
        # Nova janela do chat
        self.chat_root = tk.Tk()
        self.chat_root.title(f"AI SAKY - Chat ({self.current_user})")
        self.chat_root.geometry("800x600")
        self.chat_root.configure(bg=self.get_color('bg'))
        
        self.setup_chat_screen()
    
    def setup_chat_screen(self):
        # Header
        header_frame = tk.Frame(self.chat_root, bg=self.get_color('accent'), height=60)
        header_frame.pack(fill='x', side='top')
        header_frame.pack_propagate(False)
        
        # Logo e título no header
        title_frame = tk.Frame(header_frame, bg=self.get_color('accent'))
        title_frame.pack(side='left', padx=15)
        
        sakura_icon = "🌸"
        icon_label = tk.Label(title_frame, text=sakura_icon, font=('Arial', 16),
                             bg=self.get_color('accent'), fg='white')
        icon_label.pack(side='left')
        
        title_label = tk.Label(title_frame, text="AI SAKY", font=('Arial', 14, 'bold'),
                              bg=self.get_color('accent'), fg='white')
        title_label.pack(side='left', padx=(5, 0))
        
        # Botões no header
        btn_frame = tk.Frame(header_frame, bg=self.get_color('accent'))
        btn_frame.pack(side='right', padx=15)
        
        theme_btn = tk.Button(btn_frame, text="🌓 Tema", font=('Arial', 9),
                             bg='white', fg=self.get_color('accent'),
                             command=self.toggle_theme, relief='flat', padx=10)
        theme_btn.pack(side='left', padx=(0, 10))
        
        clear_btn = tk.Button(btn_frame, text="🗑️ Limpar", font=('Arial', 9),
                             bg='white', fg=self.get_color('accent'),
                             command=self.clear_chat, relief='flat', padx=10)
        clear_btn.pack(side='left')
        
        # Área do chat
        self.chat_frame = tk.Frame(self.chat_root, bg=self.get_color('bg'))
        self.chat_frame.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Scrollable text area
        self.chat_area = scrolledtext.ScrolledText(
            self.chat_frame,
            wrap=tk.WORD,
            width=60,
            height=20,
            font=('Arial', 10),
            bg=self.get_color('bg_secondary'),
            fg=self.get_color('text'),
            relief='flat',
            padx=10,
            pady=10
        )
        self.chat_area.pack(fill='both', expand=True)
        self.chat_area.config(state=tk.DISABLED)
        
        # Input area
        input_frame = tk.Frame(self.chat_frame, bg=self.get_color('bg'))
        input_frame.pack(fill='x', pady=(10, 0))
        
        self.input_entry = tk.Entry(
            input_frame,
            font=('Arial', 11),
            bg=self.get_color('bg_secondary'),
            fg=self.get_color('text'),
            relief='solid',
            bd=1
        )
        self.input_entry.pack(side='left', fill='x', expand=True, padx=(0, 10))
        self.input_entry.bind('<Return>', lambda e: self.send_message())
        
        send_btn = tk.Button(
            input_frame,
            text="Enviar",
            font=('Arial', 10, 'bold'),
            bg=self.get_color('accent'),
            fg='white',
            activebackground=self.get_color('accent_light'),
            relief='flat',
            padx=20,
            command=self.send_message
        )
        send_btn.pack(side='right')
        
        # Mensagem de boas-vindas
        self.add_message("AI SAKY", "🌸", "Olá! Sou a SAKY, sua assistente de TI. Como posso ajudar você hoje?", is_user=False)
        
        self.input_entry.focus()
    
    def get_color(self, color_type):
        theme = 'dark' if self.dark_mode else 'light'
        return self.colors[theme][color_type]
    
    def toggle_theme(self):
        self.dark_mode = not self.dark_mode
        self.update_theme()
    
    def update_theme(self):
        # Atualizar cores da interface
        self.chat_root.configure(bg=self.get_color('bg'))
        
        # Atualizar todas as widgets
        for widget in self.chat_root.winfo_children():
            self.update_widget_theme(widget)
    
    def update_widget_theme(self, widget):
        try:
            if isinstance(widget, (tk.Frame, ttk.Frame)):
                widget.configure(bg=self.get_color('bg'))
            elif isinstance(widget, tk.Label):
                if 'accent' in str(widget.cget('bg')):
                    widget.configure(bg=self.get_color('accent'))
                else:
                    widget.configure(bg=self.get_color('bg'), fg=self.get_color('text'))
            elif isinstance(widget, tk.Entry):
                widget.configure(bg=self.get_color('bg_secondary'), fg=self.get_color('text'))
            elif isinstance(widget, tk.Button):
                if widget.cget('text') in ["🌓 Tema", "🗑️ Limpar"]:
                    widget.configure(bg='white', fg=self.get_color('accent'))
                else:
                    widget.configure(bg=self.get_color('accent'), fg='white')
            elif isinstance(widget, scrolledtext.ScrolledText):
                widget.configure(bg=self.get_color('bg_secondary'), fg=self.get_color('text'))
            
            # Atualizar filhos recursivamente
            for child in widget.winfo_children():
                self.update_widget_theme(child)
        except:
            pass
    
    def add_message(self, name, icon, message, is_user=True):
        self.chat_area.config(state=tk.NORMAL)
        
        # Configurar tags para formatação
        self.chat_area.tag_configure('user_name', foreground=self.get_color('accent'), font=('Arial', 9, 'bold'))
        self.chat_area.tag_configure('bot_name', foreground='#2e8b57', font=('Arial', 9, 'bold'))
        self.chat_area.tag_configure('user_msg', foreground=self.get_color('text'), font=('Arial', 10))
        self.chat_area.tag_configure('bot_msg', foreground=self.get_color('text'), font=('Arial', 10))
        self.chat_area.tag_configure('timestamp', foreground=self.get_color('text_secondary'), font=('Arial', 8))
        
        # Adicionar mensagem
        timestamp = time.strftime("%H:%M")
        
        if is_user:
            self.chat_area.insert(tk.END, f"{icon} ", 'user_name')
            self.chat_area.insert(tk.END, f"{name} ", 'user_name')
            self.chat_area.insert(tk.END, f"[{timestamp}]\n", 'timestamp')
            self.chat_area.insert(tk.END, f"{message}\n\n", 'user_msg')
        else:
            self.chat_area.insert(tk.END, f"{icon} ", 'bot_name')
            self.chat_area.insert(tk.END, f"{name} ", 'bot_name')
            self.chat_area.insert(tk.END, f"[{timestamp}]\n", 'timestamp')
            self.chat_area.insert(tk.END, f"{message}\n\n", 'bot_msg')
        
        self.chat_area.config(state=tk.DISABLED)
        self.chat_area.see(tk.END)
    
    def send_message(self):
        message = self.input_entry.get().strip()
        if not message:
            return
        
        # Adicionar mensagem do usuário
        user_icon = "👤"
        self.add_message(self.current_user, user_icon, message, is_user=True)
        
        # Limpar input
        self.input_entry.delete(0, tk.END)
        
        # Simular processamento
        self.chat_root.after(1000, lambda: self.generate_response(message))
    
    def generate_response(self, user_message):
        # IA simulada para assuntos de TI
        response = self.get_ti_response(user_message.lower())
        bot_icon = "🌸"
        self.add_message("AI SAKY", bot_icon, response, is_user=False)
    
    def get_ti_response(self, message):
        # Respostas pré-definidas para assuntos de TI
        responses = {
            'python': "Python é uma linguagem de programação de alto nível, interpretada e de propósito geral. É excelente para automação, análise de dados, IA e desenvolvimento web com frameworks como Django e Flask.",
            
            'javascript': "JavaScript é essencial para desenvolvimento web front-end. Com Node.js também pode ser usado no back-end. Frameworks populares incluem React, Vue e Angular.",
            
            'sql': "SQL (Structured Query Language) é usado para gerenciar bancos de dados relacionais. Comandos básicos: SELECT, INSERT, UPDATE, DELETE. MySQL, PostgreSQL e SQL Server são sistemas populares.",
            
            'html': "HTML é a linguagem de marcação para criar páginas web. A versão mais recente é HTML5, que inclui novos elementos semânticos e APIs multimídia.",
            
            'css': "CSS é usado para estilizar páginas web. CSS3 trouxe recursos como flexbox, grid, animações e responsividade. Frameworks como Bootstrap podem acelerar o desenvolvimento.",
            
            'docker': "Docker é uma plataforma para desenvolver, enviar e executar aplicações em containers. Facilita a implantação e escalabilidade de aplicações.",
            
            'git': "Git é um sistema de controle de versão distribuído. Comandos essenciais: git clone, commit, push, pull, branch. GitHub e GitLab são plataformas populares para hospedagem.",
            
            'api': "API (Application Programming Interface) permite comunicação entre sistemas. REST é um estilo arquitetural comum, usando HTTP com JSON. GraphQL é uma alternativa popular.",
            
            'segurança': "Segurança da informação envolve confidencialidade, integridade e disponibilidade. Práticas importantes: autenticação multifator, criptografia, atualizações regulares e backups.",
            
            'redes': "Redes de computadores permitem comunicação entre dispositivos. Conceitos fundamentais: TCP/IP, DNS, HTTP/HTTPS, roteadores, switches e firewalls.",
            
            'cloud': "Computação em nuvem oferece serviços sob demanda através da internet. Principais provedores: AWS, Azure e Google Cloud. Modelos: IaaS, PaaS e SaaS.",
            
            'linux': "Linux é um sistema operacional open-source. Distribuições populares: Ubuntu, CentOS, Debian. Comandos essenciais: ls, cd, grep, chmod, sudo.",
            
            'banco de dados': "Bancos de dados armazenam e gerenciam dados. Tipos: relacionais (SQL) e não-relacionais (NoSQL). MongoDB, Redis e Cassandra são exemplos de NoSQL.",
            
            'machine learning': "Machine Learning é um subcampo da IA que permite aos sistemas aprenderem com dados. Bibliotecas populares em Python: scikit-learn, TensorFlow, PyTorch.",
            
            'devops': "DevOps integra desenvolvimento e operações para acelerar entrega de software. Ferramentas comuns: Jenkins, Kubernetes, Ansible, Terraform.",
            
            'ia': "Inteligência Artificial simula inteligência humana em máquinas. Inclui machine learning, processamento de linguagem natural, visão computacional e robótica.",
            
            'programação': "Programação envolve escrever instruções para computadores. Boas práticas: código limpo, testes, versionamento e documentação. Algoritmos e estruturas de dados são fundamentais.",
            
            'debug': "Debugging é o processo de encontrar e corrigir erros. Use print statements, debuggers, logs e testes unitários. Entenda a mensagem de erro e reproduza o problema.",
            
            'web': "Desenvolvimento web envolve front-end (interface) e back-end (servidor). Tecnologias modernas incluem PWA, SPAs e arquitetura de microsserviços.",
            
            'mobile': "Desenvolvimento mobile: nativo (Swift/Kotlin) ou cross-platform (React Native, Flutter). Considere experiência do usuário e performance.",
        }
        
        # Encontrar a melhor resposta baseada nas palavras-chave
        for keyword, response in responses.items():
            if keyword in message:
                return response
        
        # Respostas padrão
        default_responses = [
            "Em TI, isso pode envolver várias áreas. Poderia especificar mais? Talvez sobre programação, redes, segurança, banco de dados ou cloud computing?",
            "Interessante! Na área de tecnologia, isso pode ser abordado de diferentes formas. Tem alguma tecnologia específica em mente?",
            "Como assistente de TI, posso ajudar com programação, infraestrutura, segurança, banco de dados e outras áreas de tecnologia. Sobre qual aspecto gostaria de saber mais?",
            "Na computação, esse tópico pode ser complexo. Podemos discutir frameworks específicos, linguagens de programação ou conceitos arquiteturais?",
            "Isso é relevante para o mundo da tecnologia! Posso explicar conceitos de desenvolvimento, operações, análise de dados ou outras áreas de TI."
        ]
        
        return random.choice(default_responses)
    
    def clear_chat(self):
        self.chat_area.config(state=tk.NORMAL)
        self.chat_area.delete(1.0, tk.END)
        self.chat_area.config(state=tk.DISABLED)
        
        # Adicionar mensagem de boas-vindas novamente
        self.add_message("AI SAKY", "🌸", "Olá! Sou a SAKY, sua assistente de TI. Como posso ajudar você hoje?", is_user=False)
    
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = ChatBotSAKY()
    app.run()
from tkinter import *
from tkinter import ttk


class PayrollApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Aplicación de gestión nóminas")
        self.master.geometry("900x700")
        self.master.configure(background='white')
        
        # Configuración de estilo
        self.style = ttk.Style()
        self.setup_styles()
        
        
        # Crear interfaz
        self.create_interface()
    
    def setup_styles(self):
        # Estilos de botones
        self.style.configure('Blue.TButton', 
            font=('Arial', 12, 'bold'),
            background='#2196F3',  # Azul
            foreground='white',
            padding=10
        )
        
        self.style.map('Blue.TButton',
            background=[('active', '#1976D2'), ('pressed', '#0D47A1')],
            foreground=[('active', 'white')]
        )
        
        self.style.configure('White.TButton', 
            font=('Arial', 12, 'bold'),
            background='white',
            foreground='#2196F3',
            padding=10
        )
        
        self.style.map('White.TButton',
            background=[('active', '#E3F2FD'), ('pressed', '#BBDEFB')],
            foreground=[('active', '#1976D2')]
        )
        
        self.style.configure('Red.TButton', 
            font=('Arial', 12, 'bold'),
            background='#F44336',  # Rojo
            foreground='white',
            padding=10
        )
        
        self.style.map('Red.TButton',
            background=[('active', '#D32F2F'), ('pressed', '#B71C1C')],
            foreground=[('active', 'white')]
        )
    
    def create_interface(self):
        # Marco principal
        main_frame = Frame(self.master, bg='white')
        main_frame.pack(expand=True, fill=BOTH, padx=20, pady=20)
        
        # Título
        title_label = Label(main_frame, 
                            text="Gestión de Nóminas", 
                            font=("Arial", 24, "bold"), 
                            fg='#2196F3', 
                            bg='white')
        title_label.pack(pady=20)
        
        # Imagen
        image = PhotoImage(file="img/nomina.png").subsample(2, 2)
        image_label = Label(main_frame, image=image, bg='white')
        image_label.image = image  # Guardar referencia
        image_label.pack(pady=10)
        
        # Marco de botones
        button_frame = Frame(main_frame, bg='white')
        button_frame.pack(pady=20)
        
        # Definir botones con diferentes estilos
        buttons_config = [
            ("Bajas", self.bajas, 'Red.TButton'),
            ("Altas", self.altas, 'Blue.TButton'),
            ("Informes", self.informes, 'White.TButton'),
            ("Nóminas", self.nominas, 'Blue.TButton')
        ]
        
        # Crear cuadrícula de botones
        for i, (text, command, style) in enumerate(buttons_config):
            btn = ttk.Button(button_frame, 
                             text=text, 
                             command=command, 
                             style=style, 
                             width=20)
            btn.grid(row=i//2, column=i%2, padx=10, pady=10)
    
    def bajas(self):
        print("bajas")
    
    def altas(self):
        print("bajas")
    
    def informes(self):
        print("bajas")
    
    def nominas(self):
        print("bajas")
        
# Iniciar aplicación
if __name__ == "__main__":
    root = Tk()
    app = PayrollApp(root)
    root.mainloop()
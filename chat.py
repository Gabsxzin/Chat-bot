from tkinter import scrolledtext
from tkinter import filedialog
from selenium import webdriver
import customtkinter as CTk 
import time
import wget # type: ignore

class ChatBotApp:
    def __init__(self, master):
        self.master = master
        master.title("Chat Bot")
        self.chat_box = scrolledtext.ScrolledText(master, wrap=CTk.WORD, width=70, height=20)
        self.chat_box.pack(expand=True, fill="both")
        self.user_input = CTk.CTkEntry(master, width=140 , height=20 )
        self.user_input.pack(pady=5)
        self.send_button = CTk.CTkButton(master, text="Enviar", command=self.send_message) 
        self.send_button.pack()
        self.add_message('''                                            
╔══════════════════════════════════════╗
║        Gabriel Natan Andrade         ║
║     Computer Engineering Student     ║
╚══════════════════════════════════════╝

Welcome to my interactive portfolio!

1 • About Me
2 • Resume (CV)
3 • Technical Skills
4 • GitHub

Type a number and press Enter. ''')
                        

    def send_message(self):
        user_message = self.user_input.get()
        self.user_input.delete(0, CTk.END)
        bot_response = self.generate_bot_response(user_message)
        self.add_message(f"You: {user_message}")
        self.add_message( f'''
bot:  {bot_response}''')

    def generate_bot_response(self, user_message):
            
            if "1" in user_message.lower():
                return '''                       
        𝐌𝐲 𝐧𝐚𝐦𝐞 𝐢𝐬 𝐆𝐚𝐛𝐫𝐢𝐞𝐥 𝐍𝐚𝐭𝐚𝐧 𝐝𝐞 𝐀𝐧𝐝𝐫𝐚𝐝𝐞, 𝐈'𝐦 21 𝐲𝐞𝐚𝐫𝐬 𝐨𝐥𝐝 𝐚𝐧𝐝 𝐈'𝐦 𝐠𝐫𝐚𝐝𝐮𝐚𝐭𝐢𝐧𝐠 𝐢𝐧
        𝐂𝐨𝐦𝐩𝐮𝐭𝐞𝐫 𝐄𝐧𝐠𝐢𝐧𝐞𝐞𝐫𝐢𝐧𝐠, 𝐈 𝐡𝐚𝐯𝐞 𝐬𝐤𝐢𝐥𝐥𝐬 𝐢𝐧 𝐛𝐚𝐜𝐤-𝐞𝐧𝐝, 𝐟𝐫𝐨𝐧𝐭-𝐞𝐧𝐝 𝐚𝐧𝐝 𝐡𝐚𝐫𝐝𝐰𝐚𝐫𝐞,
        𝐖𝐢𝐭𝐡 𝐜𝐫𝐢𝐭𝐢𝐜𝐚𝐥 𝐚𝐧𝐝 𝐚𝐧𝐚𝐥𝐲𝐭𝐢𝐜𝐚𝐥 𝐭𝐡𝐢𝐧𝐤𝐢𝐧𝐠, 𝐰𝐢𝐭𝐡 𝐚 𝐛𝐚𝐬𝐞 𝐢𝐧 𝐝𝐚𝐭𝐚 𝐬𝐭𝐫𝐮𝐜𝐭𝐮𝐫𝐞,
        𝐀𝐥𝐰𝐚𝐲𝐬 𝐥𝐨𝐨𝐤𝐢𝐧𝐠 𝐟𝐨𝐫 𝐜𝐨𝐧𝐭𝐢𝐧𝐮𝐨𝐮𝐬 𝐢𝐦𝐩𝐫𝐨𝐯𝐞𝐦𝐞𝐧𝐭 .'''
            elif "2" in user_message.lower():
            
                file_id = '19a0FXQXcvs1228TKl1LwtvYWblAe8swD'
                url = f'https://drive.google.com/uc?id={file_id}'
                filename = filedialog.askdirectory()
                wget.download(url, out=filename)
                return 'Donwload concluido'
            elif '3'in user_message.lower():
                return '''
𝙿𝚢𝚝𝚑𝚘𝚗, 𝚓𝚊𝚟𝚊, 𝚓𝚊𝚟𝚊𝚜𝚌𝚛𝚒𝚙𝚝, 𝚑𝚝𝚖𝚕, 𝚌𝚜𝚜, 𝚛𝚎𝚊𝚌𝚝, 𝚖𝚢𝚜𝚚𝚕, 𝚌, 𝚌++
'''
            elif '4' in user_message.lower():
                navegador = webdriver.Chrome()
                time.sleep(1)
                navegador.get("https://github.com/Gabsxzin")
                time.sleep(100000000000)
                return ChatBotApp
            else:
            
                return "Desculpe, selecione uma opção não reconhecida."

    def add_message(self, message):
        self.chat_box.insert(CTk.END, message + "\n")
        self.chat_box.see(CTk.END)
        self.chat_box.config(background='#1C1C1C',font='Luminari',foreground='white')
        
if __name__ == "__main__":
    root = CTk.CTk()
    CTk.set_appearance_mode('dark')
    CTk.set_default_color_theme('dark-blue')
    app = ChatBotApp(root)
    root.mainloop()




from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import random
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from qa import IT_Fundamentals_MCQs

class QuizApp:
    def __init__(self, root,user_info):
        self.root = root
        self.user_info = user_info
        self.root.title("IT QUIZ-WIZZ")

        self.bg_image = Image.open("5096154.jpg")  
        self.bg_image = ImageTk.PhotoImage(self.bg_image)

        self.canvas = Canvas(root, width=self.bg_image.width(), height=self.bg_image.height())
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_image(0, 0, image=self.bg_image, anchor="nw")
        
        self.score = 0
        self.question_number = 0
        self.questions = random.sample(IT_Fundamentals_MCQs, 5)

        self.question_label = Label(root, text="", wraplength=400, font=("Arial", 14), bg="white")
        self.canvas.create_window(400, 100, window=self.question_label)

        self.var = StringVar()
        self.vars = [IntVar() for _ in range(4)]
        self.options = []

        self.submit_button = Button(root, text="Submit", command=self.check_answer, font=("Arial", 12), padx=20, pady=10)
        self.canvas.create_window(800, 200, window=self.submit_button)

        self.next_button = Button(root, text="Next Question", command=self.next_question, font=("Arial", 12), padx=20, pady=10)
        self.canvas.create_window(800, 250, window=self.next_button)
        
        self.clear_button = Button(root, text="Clear", command=self.clear_selection, font=("Arial", 12), padx=20, pady=10)
        self.canvas.create_window(800, 300, window=self.clear_button)
        
        self.display_question()

    def display_question(self):
        if self.question_number < len(self.questions):
            current_question = self.questions[self.question_number]
            self.question_label.config(text=current_question["question"])

            for option in self.options:
                option.destroy()
            self.options.clear()

            is_multiple = current_question.get("multiple", False)

            if is_multiple:
                for i, option_text in enumerate(current_question["options"]):
                    option = Checkbutton(self.root, text=option_text, variable=self.vars[i], onvalue=1, offvalue=0, font=("Arial", 12), padx=20, pady=10, width=30, height=2)
                    self.options.append(option)
                    self.canvas.create_window(400, 200 + i * 50, window=option)
            else:
                self.var.set(None)  # Deselect all options
                for i, option_text in enumerate(current_question["options"]):
                    option = Radiobutton(self.root, text=option_text, variable=self.var, value=option_text, font=("Arial", 12), padx=20, pady=10, width=30, height=2)
                    self.options.append(option)
                    self.canvas.create_window(400, 200 + i * 50, window=option)
        else:
            self.end_quiz()

    def check_answer(self):
        current_question = self.questions[self.question_number]
        is_multiple = current_question.get("multiple", False)
        
        if is_multiple:
            selected_answers = [self.options[i].cget('text') for i, var in enumerate(self.vars) if var.get() == 1]
            if set(selected_answers) == set(current_question["answer"]):
                self.score += 1
        else:
            selected_answer = self.var.get()
            if selected_answer in current_question["answer"]:
                self.score += 1

        self.question_number += 1
        self.display_question()

    def next_question(self):
        self.question_number += 1
        self.display_question()

    def clear_selection(self):
        for var in self.vars:
            var.set(0)
        self.var.set(None)

    def end_quiz(self):
        user_info_str = (f"Name: {self.user_info['name']}\n"
                        f"Roll No: {self.user_info['roll_no']}\n"
                        f"Email ID: {self.user_info['email']}")
        messagebox.showinfo("Quiz Completed", f"{user_info_str}\nYour score is {self.score}/{len(self.questions)}")
        self.send_email(self.user_info['email'], self.user_info['name'], self.user_info['roll_no'], self.score)
        self.root.destroy()

    def send_email(self, recipient_email, name, roll_no, score):
        sender_email = "asishpradhan943@gmail.com"
        sender_password = "qtnz sefg xkli yhxd"
        subject = "Quiz Results"
        body = f"Name: {name}\nRoll No: {roll_no}\nScore: {score}/{len(self.questions)}"
        
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))
        
        try:
            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server.login(sender_email, sender_password)
            text = msg.as_string()
            server.sendmail(sender_email, recipient_email, text)
            server.close()
            print("Email sent successfully")
        except Exception as e:
            print(f"Failed to send email: {e}")
        
    
class LoginApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")

        self.bg_image = Image.open("8275340.jpg") 
        self.bg_image = ImageTk.PhotoImage(self.bg_image)

       
        self.canvas = Canvas(root, width=self.bg_image.width(), height=self.bg_image.height())
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_image(0, 0, image=self.bg_image, anchor="nw")

        
        self.name_label = Label(root, text="Name", font=("Arial", 12), bg="white")
        self.name_entry = Entry(root, font=("Arial", 12), width=30)
        self.roll_no_label = Label(root, text="Roll No", font=("Arial", 12), bg="white")
        self.roll_no_entry = Entry(root, font=("Arial", 12), width=30)
        self.email_label = Label(root, text="Email ID", font=("Arial", 12), bg="white")
        self.email_entry = Entry(root, font=("Arial", 12), width=30)
        self.login_button = Button(root, text="Login", command=self.login, font=("Arial", 12), padx=20, pady=10)

        
        self.canvas.create_window(200, 150, window=self.name_label)
        self.canvas.create_window(400, 150, window=self.name_entry)
        self.canvas.create_window(200, 200, window=self.roll_no_label)
        self.canvas.create_window(400, 200, window=self.roll_no_entry)
        self.canvas.create_window(200, 250, window=self.email_label)
        self.canvas.create_window(400, 250, window=self.email_entry)
        self.canvas.create_window(300, 300, window=self.login_button)

    def login(self):
        user_info = {
            "name": self.name_entry.get(),
            "roll_no": self.roll_no_entry.get(),
            "email": self.email_entry.get(),
        }

        if all(user_info.values()): 
            self.root.destroy()
            main_app(user_info)
        else:
            messagebox.showerror("Error", "All fields are required")

def main_app(user_info):
    root = Tk()
    app = QuizApp(root, user_info)
    root.mainloop()

if __name__ == "__main__":
    root = Tk()
    app = LoginApp(root)
    root.mainloop()
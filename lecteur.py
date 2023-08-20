from colorama import init, Fore, Style

# Initialise la coloration de la console
init(autoreset=True)

# Saisie du nom du fichier quizz
file = input("Entrez le nom du fichier quizz : ")

class Quizz:
    def __init__(self, filename):
        self.questions = []
        self.load_quizz(filename)
    
    def load_quizz(self, filename):
        with open(filename, 'r') as file:
            lines = file.readlines()
            question_data = []
            for line in lines:
                line = line.strip()
                if line.startswith("## Question"):
                    if question_data:
                        self.questions.append(question_data)
                    question_data = [line]
                elif line.startswith("-"):
                    question_data.append(line[2:])
                elif line and question_data:
                    question_data[-1] += "\n" + line
            if question_data:
                self.questions.append(question_data)
    
    def run_quizz(self):
        total_questions = len(self.questions)
        correct_answers = 0
        
        for question_data in self.questions:
            print(Fore.CYAN + question_data[0])
            for i, answer in enumerate(question_data[1:], start=1):
                answer_text = answer
                if answer_text.endswith("(Correcte)"):
                    answer_text = answer_text[:-11]
                print(f"{Fore.YELLOW}{i}. {answer_text}")
            
            user_choice = input(Fore.GREEN + "Votre réponse (1, 2, 3, 4) : ")
            if user_choice.isdigit() and 1 <= int(user_choice) <= len(question_data) - 1:
                if question_data[int(user_choice)][-10:] == "(Correcte)":
                    print(Fore.GREEN + "Correct !")
                    correct_answers += 1
                else:
                    print(Fore.RED + "Incorrect.")
            else:
                print(Fore.RED + "Choix invalide.")
        
        score = (correct_answers / total_questions) * 100
        print(Style.RESET_ALL + "\n---- Résultats ----")
        print(f"Nombre total de questions : {total_questions}")
        print(f"Nombre de réponses correctes : {correct_answers}")
        print(f"Score : {score:.2f}%")

if __name__ == "__main__":
    quizz = Quizz(file)
    quizz.run_quizz()
                  

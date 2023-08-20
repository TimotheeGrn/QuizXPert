def create_quizz_file():
    quizz_title = input("Entrez le titre du quizz : ")
    num_questions = int(input("Combien de questions voulez-vous ajouter ? "))
    
    filename = f"{quizz_title.lower().replace(' ', '_')}.quizz"
    
    with open(filename, "w") as file:
        file.write(f"# {quizz_title}\n\n")
        
        for i in range(1, num_questions + 1):
            question = input(f"Question {i} : ")
            
            num_answers = int(input("Combien de réponses possibles pour cette question ? "))
            answers = []
            for j in range(num_answers):
                answer = input(f"Réponse {j+1} : ")
                answers.append(answer)
            
            correct_answer_index = int(input("Indice de la réponse correcte (1, 2, 3, ...) : "))
            
            file.write(f"\n## Question {i}:\n{question}\n")
            for idx, answer in enumerate(answers):
                if idx + 1 == correct_answer_index:
                    file.write(f"- Réponse {chr(65 + idx)}: {answer} (Correcte)\n")
                else:
                    file.write(f"- Réponse {chr(65 + idx)}: {answer}\n")
    
    print(f"Le fichier {filename} a été généré avec succès.")

if __name__ == "__main__":
    create_quizz_file()
  

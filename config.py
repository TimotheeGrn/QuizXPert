try:
    import colorama
except ImportError:
    print("Colorama n'est pas installé. Vous pouvez l'installer avec la commande :")
    print("pip install colorama")
    exit(1)

def print_tutorial():
    print("Bienvenue dans le tutoriel d'utilisation de QuizXpert !")
    print("Suivez ces étapes pour tirer le meilleur parti de l'outil :")
    print()

    input("Appuyez sur Entrée pour continuer à l'étape 1...")
    step_1()

def step_1():
    print("1. Utilisation du Lecteur de Quizz (lecteur.py) :")
    print("   - Assurez-vous d'avoir un fichier .quizz prêt.")
    print("   - Exécutez le script lecteur.py.")
    print("   - Suivez les instructions pour répondre aux questions.")
    print("   - Obtenez instantanément vos résultats et votre score.")
    print()

    input("Appuyez sur Entrée pour passer à l'étape 2...")
    step_2()

def step_2():
    print("2. Création de Fichiers de Quizz (create_quiz.py) :")
    print("   - Exécutez le script create_quiz.py.")
    print("   - Suivez les étapes pour créer un nouveau fichier .quizz.")
    print("   - Entrez le titre du quizz et le nombre de questions.")
    print("   - Ajoutez des questions, réponses et indiquez la réponse correcte.")
    print("   - Le fichier .quizz sera généré pour vous.")
    print()

    input("Appuyez sur Entrée pour passer à l'étape 3...")
    step_3()

def step_3():
    print("3. Exemple de Fichier de Quizz (example.quizz) :")
    print("   - Vous pouvez étudier le contenu de ce fichier pour comprendre le format.")
    print("   - Il contient des exemples de questions, réponses et réponses correctes.")
    print()

    print("C'est tout ! Profitez de QuizXpert pour créer et répondre à des quizz captivants.")
    print("N'oubliez pas de consulter le README pour plus d'informations et de détails.")
    print("Amusez-vous bien et bon quizzing !")

if __name__ == "__main__":
    print_tutorial()
  

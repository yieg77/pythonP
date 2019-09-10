import pickle
import quiz_9_class as cm

# === main =================================================================
cl_Quiz = cm.TypingGame()

number = 0
while 1:
    cl_Quiz.showList()
    cl_Quiz.showMenu()

    number = input()
    if (number=='1') or (number=='2') : cl_Quiz.get_list(number)
    elif number=='3': cl_Quiz.add_word()
    elif number=='4': cl_Quiz.saveAsTxtFile()
    elif number=='5': cl_Quiz.saveAsPickle()
    elif number=='6': cl_Quiz.getPickle()
    elif number=='7': cl_Quiz.game()
    elif number=='8': cl_Quiz.showRecord()
    elif number=='0': break

import pickle

rank = {}

def rankLoad():
    #with open("./basic/quiz_9_typing_game_pickle.pkl", 'rb') as f:
    with open("./basic/quiz_9_typing_game_record.pkl", 'rb') as f:
        rank = pickle.load(f)
    return rank

rank = rankLoad()
print(rank)



import pickle

with open("model/class_names.pkl", "rb") as f:
    class_names = pickle.load(f)

print(len(class_names))
print(class_names)
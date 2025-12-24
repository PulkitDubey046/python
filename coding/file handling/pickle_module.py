import pickle

# Example data
data = {
    'name': 'John',
    'age': 30,
    'hobbies': ['reading', 'coding', 'gaming']
}

# Serialize (pickle) the data to a file
with open('data.pkl', 'wb') as file:
    pickle.dump(data, file)

# Deserialize (unpickle) the data from a file
with open('data.pkl', 'rb') as file:
    loaded_data = pickle.load(file)

print(loaded_data)

# You can also serialize to bytes directly
pickled_bytes = pickle.dumps(data)
unpickled_data = pickle.loads(pickled_bytes)
print(unpickled_data)
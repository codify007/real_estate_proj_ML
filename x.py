import pickle 
import numpy as np
import json
import sklearn


with open('public/final.pickle', 'rb') as f:
    model=pickle.load(f)




with open('public/columns.json', 'r') as f:
  data_columns=json.load(f)['data_columns']


def get_predicted_price(location,sqft,bhk,bath):
    try:
        loc_index = data_columns.index(location.lower())
    except:
        loc_index = -1

    x = np.zeros(len(data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index>=0:
        x[loc_index] = 1

    return round(model.predict([x])[0],2)

print(str(get_predicted_price('Whitefield',1000, 3, 3)) + " lakh")

# import pickle
# import sklearn

# # Load the pickle file
# with open('public/final.pickle', 'rb') as file:
#     model = pickle.load(file)

# # Get the protocol version used to save the pickle file
# pickle_protocol = model.__getstate__()[-1]

# # Get the version of scikit-learn
# sklearn_version = sklearn.__version__

# # Compare the versions
# if pickle_protocol == sklearn.version_info.major:
#     print(f"Pickle file and scikit-learn versions match: {sklearn_version}")
# else:
#     print(f"Pickle file and scikit-learn versions do not match. Pickle file protocol: {pickle_protocol}, scikit-learn version: {sklearn_version}")
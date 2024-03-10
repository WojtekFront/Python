#before begin project install Pandas. Write in console "pip install pandas"
import pandas as pd
import numpy as np

dictionary_object = pd.DataFrame(
    {"A": 1,
     "B": pd.Timestamp("20130102"),
     "C": pd.Series([1,2,3,4], index=list(range(4)), dtype="float32"),
     "D": np.array([3,5,2.2,1], dtype="int32"),
     "E": pd.Categorical(["test1", "test2", "test3", "test4"]),
     "F": np.array(["aa", "bb", "cc", "dd"], dtype="str")
    })

# print(dictionary_object.index)
# print(dictionary_object.columns)
# print(dictionary_object.to_numpy())
# print(dictionary_object.describe())
# print(dictionary_object.T)
# print(dictionary_object.sort_index(axis=1, ascending=False))
print(dictionary_object.sort_values(axis=0, by="D"))
print("\n--------------------------------\n")


print(dictionary_object)
# print(dictionary_object.head(1))
# print(dictionary_object.tail(1))
# print(dictionary_object.copy())
# print(dictionary_object.dtypes)
     
     
     
     
     










# new_project = pd.DataFrame({"Name": ["Jan", "Leo", "Bob"]})
# print(new_project)

# new_s = pd.Series([1, 3, 5, None, 6, 8])
# print(new_s)

# dates = pd.date_range("20230101", periods=24)
# print(dates)

# dates_with_values = pd.DataFrame(np.random.randn(24, 5), index=dates, columns = list("ABCDE"))
# print(dates_with_values)

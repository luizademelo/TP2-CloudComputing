from mlxtend.frequent_patterns import fpgrowth
from mlxtend.frequent_patterns import association_rules
from mlxtend.preprocessing import TransactionEncoder
import pandas as pd
import pickle


def compute_rules(): 
    df = pd.read_csv("../data/2023_spotify_ds1.csv")

    df.drop(['track_uri', 'album_name', 'album_uri', 'artist_name', 'artist_uri', 'duration_ms'], axis=1, inplace=True)

    transactions = df.groupby('pid')['track_name'].apply(list)

    transaction_list = transactions.tolist()

    te = TransactionEncoder()
    te_ary = te.fit(transaction_list).transform(transaction_list)

    encoded_df = pd.DataFrame(te_ary, columns=te.columns_)

    frequent_itemsets = fpgrowth(encoded_df, min_support=0.05, use_colnames=True)

    # print(frequent_itemsets)
    print("frequent itemsets computed")

    rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.6, num_itemsets=2)
    print("association rules computed")
    rules['antecedents'] = rules['antecedents'].apply(list)
    rules['consequents'] = rules['consequents'].apply(list)



    pickle.dump(rules, open("rules.pickle", "wb"))
    # print(rules)
    # return rules
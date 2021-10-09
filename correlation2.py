#-*- coding: utf-8 -*-
"""
@author: leolqli
@create time： 20200827
@function: calculate conference
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def sns_heatmap(data, column_lst, date):
    fig = plt.figure(figsize=(15, 13))
    ax = fig.add_subplot(111)

    ax.set_yticks(range(len(column_lst)))
    ax.set_yticklabels(column_lst, fontsize=10)
    ax.set_xticks(range(len(column_lst)))
    ax.set_xticklabels(column_lst, fontsize=10, rotation=30)

    sns.heatmap(data, linewidths=0.05, ax=ax, cmap='YlGnBu')
    
    plt.title("Device correlation", fontsize=20)
    plt.savefig("./2.result/" + date + "_corr_heatmap.png")
    # plt.show()

def as_int(data_x, column_names):
    data = data_x.copy()
    data.loc[data[column_names[0]] == "\\N", column_names[-1]] = 0
    data = data.replace("\\N", 0)
    for column_name in column_names:
        data[column_name] = data[column_name].astype(int)
    return data

def feature_cnt(data_x, column_names, date):
    save_dict = {}
    for column_name in column_names:
        res_cnt = data_x[data_x[column_name] > 0][column_name].mean()
        save_dict[str(column_name)] = [res_cnt]
    save_df = pd.DataFrame(save_dict)
    print(save_dict)
    save_df.to_csv("./2.result/" + date + "_feature_cnt.csv", index=None)

def feature_frequency(data_x, column_name):
    y = data_x[data_x[column_name] > 0].groupby(column_name)[column_name].count()
    with open("./2.result/feature_frequency.txt", "w") as f:
        for i, v in y.iteritems():
            f.write(str(i) + "|" + str(v) + "\n")

    y = list(data_x[data_x[column_name] > 0][column_name])
    # sns.barplot(x=list(range(len(y))), y=y)
    # plt.hist(y, bins=[1, 50, 100, max(y)], cumulative=True) 
    # plt.bar(list(range(len(y))), y)
    # plt.show()

if __name__ == "__main__":
    # origin_user_file = "/data2/leolqli/86266/20200824.txt"
    date = "20200826"
    origin_user_file = "./2.result/" + date + ".txt"

    origin_user_data = pd.read_csv(origin_user_file, sep="|", error_bad_lines=True, header=None)

    # replace "\\N"
    user_feature = list(range(2, 65)) + ["is_join"]
    origin_user_data["is_join"] = 1
    origin_user_data = as_int(origin_user_data[user_feature], user_feature)

    feature_cnt(origin_user_data, user_feature, date)

    # correlation matrix
    user_feature = list(range(2, 65)) + ["is_join"]
    cor_user = origin_user_data[user_feature].corr()
    print("user cor:")
    print(cor_user)

    # sns_heatmap(cor_user, user_feature, date)

    feature_frequency(origin_user_data, 4)


    origin_user_data[(origin_user_data[28]>=1595779200) & (origin_user_data[8]>=50) \
        &(origin_user_data[30]<=6) & (origin_user_data[27]<=2) & \
        (origin_user_data[14]<=6) & (origin_user_data[4]<=1000)]


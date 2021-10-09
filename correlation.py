#-*- coding: utf-8 -*-
"""
@author: leolqli
@create time： 20200814
@function: calculate conference
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def sns_heatmap(data, column_lst):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111)

    ax.set_yticks(range(len(column_lst)))
    ax.set_yticklabels(column_lst, fontsize=10)
    ax.set_xticks(range(len(column_lst)))
    ax.set_xticklabels(column_lst, fontsize=10, rotation=30)

    sns.heatmap(data, annot=True, fmt="0.3f", linewidths=0.05, ax=ax, cmap='YlGnBu')
    
    plt.title("Device correlation", fontsize=20)
    plt.savefig('./result/corr_heatmap.png')
    # plt.show()

def as_int(data, column_names):
    data.loc[data[column_names[0]] == "\\N", column_names[-1]] = 0
    data = data.replace("\\N", 0)
    for column_name in column_names:
        data[column_name] = data[column_name].astype(int)
    return data

if __name__ == "__main__":
    origin_device_file = "/data2/leolqli/85631/device.txt"
    # origin_user_file = "/data2/leolqli/85631/user.txt"
    # origin_user_file = "./user.txt"

    origin_device_data = pd.read_csv(origin_device_file, sep="|", error_bad_lines=True)
    # origin_user_data = pd.read_csv(origin_user_file, sep="|", error_bad_lines=True)

    origin_device_data.columns = ["deviceid", "allblue_partition_field", "deviceid_rename", "punish_feature", \
                                    "low_value_feature", "register_feature", "plugin_punish_feature", "other_feature_1"]
    device_feature = ["punish_feature", "low_value_feature", "register_feature", "plugin_punish_feature", "openid_worldid"]
    origin_device_data["openid_worldid"] = 1
    origin_device_data = as_int(origin_device_data[device_feature], device_feature)

    # user_columns = ["openid_", "world_id_", "allblue_partition_field", "vopen_zonearea_id", "punish_feature", \
    #                 "low_value_feature", "register_feature", "train_account_feature", "address_tran_feature", \
    #                 "abnormal_behaviour_feature", "other_feature_1", "other_feature_2", "other_feature_3", \
    #                 "other_feature_4", "vopenid", "zoneareaid"]
    # origin_user_data.columns = user_columns
    # origin_user_data["openid_worldid"] = 1
    # user_feature = ["punish_feature", "low_value_feature", "register_feature", "train_account_feature", "openid_worldid"]
    # origin_user_data = as_int(origin_user_data[user_feature], user_feature)

    cor_device = origin_device_data.corr() # 计算相关系数，得到一个矩阵
    # cor_user = origin_user_data.corr()
    print("device cor:")
    print(cor_device)
    # print("user cor:")
    # print(cor_user)

    # sns_heatmap(cor_user, user_feature)

    sns_heatmap(cor_device, device_feature)
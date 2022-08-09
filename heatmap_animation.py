    # 动态画图
    import matplotlib.pyplot as plt
    import matplotlib.pylab as mpl
    import matplotlib.animation as animation
    import seaborn as sns
    import numpy as np

    mpl.rcParams['font.sans-serif'] = ['FangSong']  # 指定默认字体
    mpl.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题



    fig = plt.figure(figsize=(10, 10))
    
    all_risk_numpy_defogging = np.random.normal(size=[20, 2, 4])
    all_risk_numpy_fogging = np.random.normal(size=[20, 2, 4])

    sub_risk_numpy = abs(all_risk_numpy_defogging - all_risk_numpy_fogging)
    sub_risk_numpy = np.reshape(sub_risk_numpy, [20, -1])

    def init_heatmap():
        ax1 = fig.add_subplot(111)
        mask = np.ones_like(sub_risk_numpy)
        sns.heatmap(sub_risk_numpy, linewidths=0.05, mask=mask, ax=ax1, cmap='RdBu_r', annot=True)

        plt.xlabel("risk area", fontsize=15)
        plt.ylabel("seconds", fontsize=15)
        plt.title("8 Risk area in Piece", fontsize=15)

    def update_heatmap(t, sub_risk_numpy):
        fig.clear()
        ax1 = fig.add_subplot(111)

        mask = np.ones_like(sub_risk_numpy)
        mask[:t+1] = 0

        sns.heatmap(sub_risk_numpy, linewidths=0.05, mask=mask, ax=ax1, cmap='RdBu_r', annot=True)

        plt.xlabel("risk area", fontsize=15)
        plt.ylabel("seconds", fontsize=15)
        plt.title("8 Risk area in Piece", fontsize=15)

    # sns.heatmap(np.reshape(sub_risk_numpy, [20, -1]), linewidths=0.05, ax=ax1, cmap='RdBu_r', annot=True)

    ani = animation.FuncAnimation(fig, update_heatmap, init_func=init_heatmap, fargs=[sub_risk_numpy], frames=20, repeat=True, interval=1550)
    ani.save('./pic/volback_heatmap_test.gif', writer='pillow')
    plt.show()
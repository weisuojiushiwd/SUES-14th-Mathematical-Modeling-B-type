# SUES 14th Mathematical Modeling B type
 SUES校数学建模竞赛B题解题思路
# 问题1：
 由于电子信号序列可能很长或者不同的被检测者检测时间长度不同，所以电子信号长短可能不同，选取你们认为的足够长度的电子信号序列对现有电子信号序列进行聚类分析，并对每一个聚类分析其电子信号序列的特征及相应生命体征生命体征的特征。
解析：
 题目已经给出具体做法，首先对呼吸、体动、心率这三者进行皮尔逊相关性分析。对电子信号序列进行聚类分析，这里基于引文的方法，使用K-means，簇的选择一开始是5，后发现两簇数据的方差近似，最终合并，选择簇数为4。
 再对电子信号"opticalpower"数组进行频谱分析，分别使用傅里叶变换和小波变换。
 
 ![image](https://github.com/weisuojiushiwd/SUES-14th-Mathematical-Modeling-B-type/assets/121271836/6ad383f9-0dc5-4dcd-9e0e-2a173edbde54)
 
“平均”傅里叶频谱流程图 

 ![image](https://github.com/weisuojiushiwd/SUES-14th-Mathematical-Modeling-B-type/assets/121271836/85a25bde-dc0d-4493-a570-76d0a68d88b0)
 
 “平均”小波频谱流程图
 
发现不同簇内的信号，经过小波变换后每簇数据有明显差异性。
再对聚类后呼吸、心率、体动三种生命特征进行基础的数值分析，分析各簇平均值、方差和分布。
观察到呼吸和心率样本在不同簇内的分布有相似性，通过拟合概率密度函数得到了信号的特征分布。

# 问题2：
监测仪器可以随时监测到被监测者的电子信号，需要将电子信号“翻译”为被监测者能理解的生命体征数据，请建立通过电子信号估计生命体征数据的数学模型。
解析：
拆分为根据电子信号估计单一生命体征数据的模型，首先对"opticalpower"和"breath"进行建模。
判断任务为：回归任务。
回归任务常用：线性回归、支持向量机、随机森林、逻辑回归、XGBoost。
其中逻辑回归一般用于二分类问题，这里并不适用。
建立模型后发现随机森林对于此问题性能最优。

![image](https://github.com/weisuojiushiwd/SUES-14th-Mathematical-Modeling-B-type/assets/121271836/a977f887-b430-40b1-a0b2-db7c0f2cf71d)

基于第一问的结论，再对心率和体动进行相同的建模，发现Random Forest对于心率和呼吸模型的性能表现最优，但是对于体动预测，性能低。

![image](https://github.com/weisuojiushiwd/SUES-14th-Mathematical-Modeling-B-type/assets/121271836/fd66d01f-4d22-49a7-acef-3952933f7d36)

![image](https://github.com/weisuojiushiwd/SUES-14th-Mathematical-Modeling-B-type/assets/121271836/95c2a8f5-748b-4a14-849d-f491fa6187d2)

这里作者添加了一个

![image](https://github.com/weisuojiushiwd/SUES-14th-Mathematical-Modeling-B-type/assets/121271836/d9c7a1b7-f40f-41cc-9133-b5301189c908)

这个模型思路，但是做出来效果并不好。

# 问题3：就某一类疾病，比如阻塞性睡眠呼吸暂停、打鼾，请查阅资料了解其生命体征，进而分析其电子信号序列的特征。
解析：自行选择了“不安腿综合征”，这里当然是选择一个较好分析的疾病来进行解释。但是作者在这里变成了预测某病患为不安腿综合征，跑题了。

不安腿综合征对应的是体动值，根据第一部分的数值分析，发现第四簇的体动值平均值大，方差也大，说明“活动”幅度较大，且次数多，这里假设第四簇中有不安腿综合征来进行分析，实属跑题。
分析发现“异常”数据均为第28号患者。用第二章中求分布的方法对第28号目标的体动值数据进行独立分析，分析得图。
![image](https://github.com/weisuojiushiwd/SUES-14th-Mathematical-Modeling-B-type/assets/121271836/0c88a7d1-f415-40c9-a0d7-8acfe3f3cd97)

在28号目标的体动值中，33和48都属于出现频率较低的体动值，我们可以认为当28号目标的体动值超过33时，28号表现出有“活动”的趋势，可以认为是不宁腿综合征的发病。

# 问题4：除了该企业目前关注的 3 个生命体征，你们小组认为还有哪些生命体征应该受到关注？
解析：顺理成章即可，体温，血压等等都可以，写入引文就行。

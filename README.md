# PMF
复现论文《Probabilistic Matrix Factorization》
1.引言
PMF项目复现了论文《Probabilistic Matrix Factorization》，其中包含了数据预处理、PMF模型、评估以及一个main文件这四个模块。
2.说明
1）在编写PMF模型时，主要参考了论文以及课堂PPT对U、V进行了更新并计算了loss。
U、V更新：
∂E/(∂U_i )=(R_(i,j)-U_i^T V_j ) V_j-λ_U U_i
∂E/(∂V_j )=(R_(i,j)-U_i^T V_j ) U_i-λ_V V_j
U_i=U_i+α ∂E/(∂U_i )
V_j=V_j+α ∂E/(∂V_j )

loss计算：
 
prediction：
X_nm=u_n^T v_m
2）该项目的训练策略参考了论文中的训练策略：max_iterations=100，K=10，λ_U=0.1，λ_V =0.1。
3）论文中使用了RMSE对模型进行评估，这里也使用RMSE来评价模型。当训练集 : 测试集=7 : 3时，可得到最终的RMSE为0.9345左右。RMSE曲线如下图所示：
 
4）运行结果截图：
 
5）学生信息：学号-2020223040055，姓名-袁晨晨

# PMF 

1.引言  
--

PMF项目复现了论文《Probabilistic Matrix Factorization》，其中包含了数据预处理、PMF模型、评估以及main这四个模块。 
  
2.说明 
-- 

2.1 在编写PMF模型时，主要参考了论文以及课堂PPT对U、V进行了更新并计算了loss。最后，对指定的用户（user_id）进行了top 5的电影推荐。  

1\) U、V更新：  

![update.png](readme_imgs//update.png) 

2\) loss计算：  

![loss.png](readme_imgs//loss.png)  

3\) prediction： 

![prediction.png](readme_imgs//prediction.png)    

2.2 该项目的训练策略参考了论文中的训练策略：max_iterations=100，K=10，lamda_U=0.1，lamda_V=0.1。  

2.3 论文中使用了RMSE对模型进行评估，这里也使用RMSE来评价模型。当训练集 : 测试集=7 : 3时，可得到最终的RMSE为0.93左右。RMSE曲线如下图所示：  

![curve.png](readme_imgs//curve.png)  

2.4 运行结果截图：  
  
1\) train process:  

![train_process.png](readme_imgs//train_process.png)  

2\) top 5:  

![recommendation.png](readme_imgs//recommendation.png)  


3.学生信息  
--

学号-2020223040055，姓名-袁晨晨  

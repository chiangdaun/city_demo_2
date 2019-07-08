城市的二级级联，省份是一级，地级市是二级，一级省份在forms.py中写死的。

![](https://ws1.sinaimg.cn/large/e9cd5756gy1g4su4xy72hj20i606ut8l.jpg)

二级地级市使用ajax动态获取(暂时写死在html文件中)

![](https://ws1.sinaimg.cn/large/e9cd5756gy1g4su5iqo08j20ae05x3yc.jpg)

![](https://ws1.sinaimg.cn/large/e9cd5756gy1g4su67k6w3j20nn0dlgm2.jpg)

页面效果如下:

![](https://ws1.sinaimg.cn/large/e9cd5756gy1g4su6r67ojj205i04wwe9.jpg) 

![](https://ws1.sinaimg.cn/large/e9cd5756gy1g4su79evwgj205k09d3yb.jpg) 

但是当表单提交**二级地级市总是报错:Not a valid choice**
而且在表单验证之前可以打印form.data可以获取选中的值。

问题发现:
1.表单提交后，二级下拉框变为初始状态

![](https://ws1.sinaimg.cn/large/e9cd5756gy1g4su84y95sj205905it8h.jpg)

2.在表单验证函数中输出

![](https://ws1.sinaimg.cn/large/e9cd5756gy1g4su8sxwy7j20gt053glh.jpg) 

结果为:

![](https://ws1.sinaimg.cn/large/e9cd5756gy1g4su9ca8egj20jv02sgle.jpg)
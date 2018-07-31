import tushare as ts

tf = ts.get_stock_basics("2018-07-31")
print(tf)

# 每次调试都要重新拿一次数据，还是在Jupyter Notebook上调试吧
# IDE还是只用来看源代码好了

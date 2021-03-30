from pyecharts import options as opts
from pyecharts.charts import Bar

bar = (
  Bar()
  .add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
  .add_yaxis("商家A", [5, 20, 36, 10, 75, 90])
  .add_yaxis("商家B", [15, 10, 26, 20, 35, 30])
)
# bar.render_notebook()
bar.render()

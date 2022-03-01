import pygal
from pygal.style import Style
custom_style = Style(
    colors=("#E80080", "#404040", "#B69420"))
b_chart = pygal.Bar(style=custom_style)
b_chart.title= "Destiny k/d ratio"
b_chart.add("Dijiphos", [0.94])
b_chart.add("Punisherdork", [1.05])
b_chart.add("Musclemuffins20", [1.10])
b_chart.render_in_browser()
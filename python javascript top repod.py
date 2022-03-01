import requests
import pygal
from pygal.style import Style
py_url = "https://api.github.com/search/repositories?q=language:python&sort=stars"
js_url = "https://api.github.com/search/repositories?q=language:javascript&sort=stars"

response = requests.get(py_url)
response_js = requests.get(js_url)

print("Status code: ", response.status_code)
response_dict = response.json()
response_dict_js = response_js.json()

print("Total repositories: ", response_dict["total_count"])
repo_dicts = response_dict["items"]
repo_dicts_js = response_dict_js["items"]

print("Repositories returned: ", len(repo_dicts))
py_names = []
py_stars = []

js_names = []
js_stars = []
i = 0
for repo in repo_dicts:
    py_names.append(repo_dicts[i]["name"])
    py_stars.append(repo_dicts[i]["stargazers_count"])
    i += 1
i = 0
for repo in repo_dicts_js:
    js_names.append(repo_dicts_js[i]["name"])
    js_stars.append(repo_dicts_js[i]["stargazers_count"])
    i += 1
my_style = Style(color = "B69420")
my_config = pygal.Config()
chart = pygal.Bar(style = my_style, x_label_rotation = 70, show_legend = True)
chart.title = "Most-Starred Python and JavaScript Projects on GitHub"
chart.add("JavaScript", js_stars)
chart.add("Python", py_stars)
chart.render_in_browser()

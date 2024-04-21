from jinja2 import Template


name = 'Bill'
age = 28


tm = Template('User name: {{ name }}, age: {{ age }}')
msg = tm.render(name=name, age=age)


print(msg)
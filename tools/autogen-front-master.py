import os
import time
import re

header = '---\ntitle: %s\ndate: "%s"\ntags: ["%s"]\ncolumns: ["%s"]\ncategories: ["%s"]\ncategories_weight: %s\n---\n'

ROOT = os.path.join('D:\Projects\personal-site\content', 'documents','columns')
remove_existing_front_matter = False
tag = 'database'
categories = '24讲吃透分布式数据库'
categories_weight = 1
path = os.path.join(ROOT, tag, categories)

for file in os.listdir(path):
    print('handle file: %s' % file)
    if file.endswith('.md.md'):
        os.rename(os.path.join(path, file), os.path.join(path, file[:-3]))
        file = file[:-3]
    title = file[:-3]
    date = time.strftime(r"%Y-%m-%dT%H:%M:%S+08:00", time.localtime(time.time()))

    front_matter = header % (title, date, tag, categories, categories, categories_weight)
    categories_weight = categories_weight + 1

    time.sleep(1)
    with open(os.path.join(path, file), 'r+', encoding='UTF-8') as f:
        content = f.read()
        if remove_existing_front_matter:
            content = re.sub('^---[\s\S]*?---', '', content)
        if content.startswith('---'):
            print('skip file: %s' % f.name)
            continue
        f.seek(0, 0)
        f.write(front_matter + content)
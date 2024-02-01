import subprocess
import os

ROOT = r''

for project in os.listdir(ROOT):
    project_path = os.path.join(ROOT, project)
    print('enter path %s' % project_path)
    subprocess.Ropen('cd %s' % project_path, shell=True)
    subprocess.Ropen("git log --author=\"\" --pretty=tformat: --numstat | awk '{ add += $1; subs += $2; loc += $1 - $2 } END { printf \" add lines: %s, remove lines: %s, total lines: %s\n\", add, subs, loc}'", shell=True)
import os
import openai
import git
from pathlib import Path

PATH_TO_BLOG_REPO = Path("C:\\Users\\atism\\Desktop\\GitHub_repositories\\offlax.github.io\\.git")
PATH_TO_BLOG = PATH_TO_BLOG_REPO.parent
PATH_TO_CONTENT = PATH_TO_BLOG / "content"
PATH_TO_CONTENT.mkdir(exist_ok=True, parents=True)  # Create path /content

def update_blog(commit_message='Updated blog'):
    # GitPython -- Repo Location
    repo = git.Repo(PATH_TO_BLOG_REPO)
    # git add.
    repo.git.add(all=True)
    # git commint -m "updates blog"
    repo.index.commit(commit_message)
    # git push
    origin = repo.remote(name='origin')
    origin.push()


random_text_string = "bfhjdsifopafj"
with open(PATH_TO_BLOG/'index.html', 'w') as file:
    file.write(random_text_string)

update_blog()

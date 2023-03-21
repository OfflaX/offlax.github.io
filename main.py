import os
import openai
import git
from pathlib import Path
import shutil

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


def create_new_blog(title, content, cover_image):
    cover_image = Path(cover_image)

    files = len(list(PATH_TO_CONTENT.glob("*html")))
    new_title = f"{files+1}.html"
    path_to_new_content = PATH_TO_CONTENT/new_title

    shutil.copy(cover_image, PATH_TO_CONTENT)

    if not os.path.exists(path_to_new_content):
        # WRITE A NEW HTML FILE
        with open(path_to_new_content, 'w') as file:
            file.write('<!DOCTYPE HTML>\n')
            file.write("<html>\n")
            file.write("<head>\n")
            file.write(f"<title> {title} </title>\n")
            file.write("</head>\n")

            file.write("<body>\n")
            file.write(f"<img src='{cover_image} alt='Cover Image'><br>\n")
            file.write(f"<h1>{title}<h1>")
            # OpenAI --> Completion GPT --> "hello\nblog_post\n"
            file.write(content.replace('\n', "<br />\n"))
            file.write("</body>\n")
            file.write("</html>\n")
            print("Blog Created")
            return path_to_new_content
    else:
        raise FileExistsError("File already exists, please check again your name! Aborting!")

# path_to_new_content = create_new_blog('Test_title', 'ghjk', 'PATH')

# Index.html --> BLog post
from bs4 import BeautifulSoup as Soup
with open(PATH_TO_BLOG/'index.html') as index:
    soup = Soup(index.read())
print(str(soup))
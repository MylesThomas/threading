# Threading

## Project Setup

Open VSCode terminal or a command prompt in Windows.

Setup the local project directory:

```sh
mkdir threading
cd threading
```

Head to github.com and create a new repository named threading.

After completing that, create a new repository on the command line:

```sh
echo "# threading" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/MylesThomas/threading.git
git push -u origin main
```

Save this markdown file into directory `threading` as `threading-notes.md`, then open up a new VSCode instance and Open folder > `threading`.

Setup a virtual Python environment:

```sh
cd threading
py -m venv env
```

You should now see a folder 'env' with a python.exe program in the /Scripts directory.

Create a .gitignore file for the Python project and save it in the root directory `threading`:

```sh
cd threading
echo > .gitignore
```

Code for .gitignore: [Link to file](https://github.com/github/gitignore/blob/main/Python.gitignore)

Activate the virtual environment in the terminal:

```sh
where python
.\env\Scripts\activate

python.exe -m pip install --upgrade pip
pip list
```

Note: You can leave the virtual environment with this call:

```sh
deactivate
```

Save these files and update git before beginning the project:

```sh
cd threading
git status
git add .
git commit -m "Completed project setup"
git push -u origin main
git status
git log --oneline
q
```

## Tech With Tim - Threading Explained

### Threading Tutorial #1 - Concurrency, Threading and Parallelism Explained

### Threading Tutorial #2 - Implementing Threading in Python 3 (Examples)

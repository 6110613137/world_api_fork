# Task 5_2

## Tasks for Collaborator A

### Add development branch

1. Make sure you are in your **`world_api_fork`** directory.

   **RUN:**

   ```console
   cd /d/working/world_api_fork
   ```

2. Create a new local branch called **`dev`** and change into the new branch.

   **RUN:**

   ```console
   git branch dev
   git switch dev
   ```

   **OUTPUT:**

   ```console
   Switched to branch 'dev'
   ```

   Or create a new branch and change into the branch in one command.

   **RUN:**

   ```console
   git switch -c dev
   ```

### Add path parameter endpoint "/world/city/{name}"

1. Copy **`db/world_table_city.csv`** from assignment repo, e.g. **`/d/working/A06`**, into this directory.

   **RUN:**

   ```console
   cp /d/working/A06/db/world_table_city.csv .
   ```

   Note the dot **`.`** at the end of the command

2. Add the file and make a commit to the repo.

   ```console
   git add world_table_city.csv
   git commit -m "Add world_table_city.csv"
   ```

   **OUTPUT:**

   ```console
   [dev cbea692a] Add world_table_city.csv
    1 file changed, 4080 insertions(+)
    create mode 100644 world_table_city.csv
   ```

3. Modify **`main.py`** such that its current content is the same as the following code:

   ```python
   import csv

   # For tutorial on FastAPI
   # See https://fastapi.tiangolo.com/tutorial/first-steps/
   from fastapi import FastAPI

   # get city data from csv file
   filename = "world_table_city.csv"
   with open(filename, "r") as csv_file:
       csv_reader = csv.reader(csv_file)
       headers = next(csv_reader)
       data_country = [{k: v for (k, v) in zip(headers, row)} for row in csv_reader]

   # create an instance of class FastAPI named "app"
   app = FastAPI()

   # define function that handles "GET" request with endpoint "/"
   @app.get("/")
   async def read_root() -> dict:
       return {"message": "Hello there"}

   # define function that handles "GET" request with endpoint "/world/city/{name}"
   # "/world/city/{name}" is a "path paramter" endpoint
   @app.get("/world/city/{name}")
   async def read_city(name: str) -> dict:
       for row in data_city:
           if row["Name"].lower() == name.lower():
               return {"result": row}
       return {"result": {}}

   ```

4. Check status.

   **RUN:**

   ```console
   git status
   ```

   **OUTPUT:**

   ```console
   On branch dev
   Changes not staged for commit:
     (use "git add <file>..." to update what will be committed)
     (use "git restore <file>..." to discard changes in working directory)
      modified:   main.py

   no changes added to commit (use "git add" and/or "git commit -a")
   ```

5. Add the change and make a commit (current branch is **`dev`**).

   **RUN:**

   ```console
   git add main.py
   git commit -m "Add endpoint /world/city/{name}"
   ```

   **OUTPUT:**

   ```console
   [dev 99a41d49] Add endpoint /world/city/{name}
    1 file changed, 18 insertions(+)
   ```

6. Check log.

   **RUN:**

   ```console
   git log --oneline --graph --all
   ```

   **OUTPUT:**

   ```console
   * 99a41d49 (HEAD -> dev) Add endpoint /world/city/{name}
   * cbea692a Add world_table_city.csv
   * 2d169e14 (upstream/main, main) Add initial requirements.txt
   * 0ced441a (origin/main, origin/HEAD) Initial commit
   ```

### Get any new commit from **`upstream`**

1. Before merging any local commit to **`main`** branch, **always** get any new commit from **`upstream`** (if the repos has an upstream).

   **RUN:**

   ```console
   git fetch upstream
   ```

   **OUTPUT:**

   ```console
   remote: Enumerating objects: 8, done.
   remote: Counting objects: 100% (8/8), done.
   remote: Compressing objects: 100% (4/4), done.
   remote: Total 6 (delta 2), reused 6 (delta 2), pack-reused 0
   Unpacking objects: 100% (6/6), 13.72 KiB | 1.25 MiB/s, done.
   From https://github.com/xxxxxxxxxx/world_api
      2d169e14..0ea39e5d  main       -> upstream/main
   ```

2. Change to local branch **`main`**.

   **RUN:**

   ```console
   git switch main
   ```

   **OUTPUT:**

   ```console
   Switched to branch 'main'
   Your branch is ahead of 'origin/main' by 1 commit.
     (use "git push" to publish your local commits)
   ```

3. Merge new commits from **`upstream`** on to **`main`**.

   **RUN:**

   ```console
   git merge upstream/main
   ```

   **OUTPUT:**

   ```console
   Updating 2d169e14..0ea39e5d
   Fast-forward
    main.py                 |  16 ++++++
    world_table_country.csv | 240 ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    2 files changed, 256 insertions(+)
    create mode 100644 world_table_country.csv
   ```

4. Check status.

   **RUN:**

   ```console
   git status
   ```

   **OUTPUT:**

   ```console
   On branch main
   Your branch is ahead of 'origin/main' by 3 commits.
     (use "git push" to publish your local commits)

   nothing to commit, working tree clean
   ```

5. Check log.

   **RUN:**

   ```console
   git log --oneline --graph --all
   ```

   **OUTPUT:**

   ```console
   * 99a41d49 (dev) Add endpoint /world/city/{name}
   * cbea692a Add world_table_city.csv
   | * 0ea39e5d (HEAD -> main, upstream/main) Add endpoint /world
   | * b3cd5997 Add world_table_country.csv
   |/
   * 2d169e14 Add initial requirements.txt
   * 0ced441a (origin/main, origin/HEAD) Initial commit
   ```

### Update local branch **`dev`** from **`main`**

1. Change to branch **`dev`**.

   **RUN:**

   ```console
   git switch dev
   ```

   **OUTPUT:**

   ```console
   Switched to branch 'dev'
   ```

2. Rebase onto branch **`main`**.

   **RUN:**

   ```console
   git rebase main
   ```

   **OUTPUT:**

      ```console
   Auto-merging main.py
   CONFLICT (content): Merge conflict in main.py
   error: could not apply 99a41d49... Add endpoint /world/city/{name}
   hint: Resolve all conflicts manually, mark them as resolved with
   hint: "git add/rm <conflicted_files>", then run "git rebase --continue".
   hint: You can instead skip this commit: run "git rebase --skip".
   hint: To abort and get back to the state before "git rebase", run "git rebase --abort".
   Could not apply 99a41d49... Add endpoint /world/city/{name}
   ```

3. Check status.

   **RUN:**

   ```console
   git status
   ```

   **OUTPUT:**

   ```console
   interactive rebase in progress; onto 0ea39e5d
   Last commands done (2 commands done):
      pick cbea692a Add world_table_city.csv
      pick 99a41d49 Add endpoint /world/city/{name}
   No commands remaining.
   You are currently rebasing branch 'dev' on '0ea39e5d'.
     (fix conflicts and then run "git rebase --continue")
     (use "git rebase --skip" to skip this patch)
     (use "git rebase --abort" to check out the original branch)

   Unmerged paths:
     (use "git restore --staged <file>..." to unstage)
     (use "git add <file>..." to mark resolution)
      both modified:   main.py
   ```

4. Resolve conflicts in **`main.py`**.

   (Accept both changes with some line rearrangement).

   Modify the file **`main.py`** such that its current content is the same as the following code:

   ```python
   import csv

   # For tutorial on FastAPI
   # See https://fastapi.tiangolo.com/tutorial/first-steps/
   from fastapi import FastAPI

   # get country data from csv file
   filename = "world_table_country.csv"
   with open(filename, "r") as csv_file:
       csv_reader = csv.reader(csv_file)
       headers = next(csv_reader)
       data_country = [{k: v for (k, v) in zip(headers, row)} for row in csv_reader]

   # get city data from csv file
   filename = "world_table_city.csv"
   with open(filename, "r") as csv_file:
       csv_reader = csv.reader(csv_file)
       headers = next(csv_reader)
       data_city = [{k: v for (k, v) in zip(headers, row)} for row in csv_reader]

   # create an instance of class FastAPI named "app"
   app = FastAPI()

   # define function that handles "GET" request with endpoint "/"
   @app.get("/")
   async def read_root() -> dict:
       return {"message": "Hello there"}


   # define function that handles "GET" request with endpoint "/world"
   # list all countries
   @app.get("/world")
   async def read_countries() -> dict:
       return {"result": data_country}


   # define function that handles "GET" request with endpoint "/world/city/{name}"
   # "/world/city/{name}" is a "path paramter" endpoint
   @app.get("/world/city/{name}")
   async def read_city(name: str) -> dict:
       for row in data_city:
           if row["Name"].lower() == name.lower():
               return {"result": row}
       return {"result": {}}

   ```

5. Mark conflict as resolved by adding the change in **`main.py`**.

   **RUN:**

   ```console
   git add main.py
   ```

6. Continue the **rebase** process.

   **RUN:**

   ```console
   git rebase --continue
   ```

   If an editor opened for file **`main.py`**, just accept the default commit message by closing the editor.

   **OUTPUT:**

   ```console
   [detached HEAD 11b91ef5] Add endpoint /world/city/{name}
    1 file changed, 18 insertions(+), 1 deletion(-)
   Successfully rebased and updated refs/heads/dev.
   ```

7. Check log.

   **RUN:**

   ```console
   git log --oneline --graph --all
   ```

   **OUTPUT:**

   ```console
   * 11b91ef5 (HEAD -> dev) Add endpoint /world/city/{name}
   * c9eb6db4 Add world_table_city.csv
   * 0ea39e5d (upstream/main, main) Add endpoint /world
   * b3cd5997 Add world_table_country.csv
   * 2d169e14 Add initial requirements.txt
   * 0ced441a (origin/main, origin/HEAD) Initial commit
   ```

### Test endpoint `/world/city/{name}`

1. Make sure you are running in virtual environment.

   For Linux/MacOS:

   **RUN:**

   ```console
   . ./venv/bin/activate
   ```

   For Windows:

   **RUN:**

   ```console
   . ./venv/Scripts/activate
   ```

2. Run the application

   **RUN:**

   ```console
   uvicorn main:app --port 9000 --reload
   ```

   **OUTPUT:**

   ```console
   INFO:     Will watch for changes in these directories: ['/d/working/world_api_fork']
   INFO:     Uvicorn running on http://127.0.0.1:9000 (Press CTRL+C to quit)
   INFO:     Started reloader process [10114] using StatReload
   INFO:     Started server process [10116]
   INFO:     Waiting for application startup.
   INFO:     Application startup complete.
   ```

3. Test the endpoint using browser.

   Open URL: <http://127.0.0.1:9000/world/city/Bangkok>.

   You should see a JSON object with a long list of objects.

   **OUTPUT:**

   ```console
   {"result":{"ID":"3320","Name":"Bangkok","CountryCode":"THA","District":"Bangkok","Population":"6320174"}}
   ```

4. Stop the appication.

   Press **`Ctrl+C`** to stop the appication

### Merge new commits to branch **`main`**

1. Change to branch main.

   **RUN:**

   ```console
   git switch main
   ```

   **OUTPUT:**

   ```console
   Switched to branch 'main'
   Your branch is ahead of 'origin/main' by 3 commits.
     (use "git push" to publish your local commits)
   ```

2. Merge new commits from branch **`dev`**.

   **RUN:**

   ```console
   git merge dev
   ```

   **OUTPUT:**

   ```console
   Updating 0ea39e5d..11b91ef5
   Fast-forward
    main.py              |   19 +-
    world_table_city.csv | 4080 ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    2 files changed, 4098 insertions(+), 1 deletion(-)
    create mode 100644 world_table_city.csv
   ```

3. Check status.

   **RUN:**

   ```console
   git status
   ```

   **OUTPUT:**

   ```console
   On branch main
   Your branch is ahead of 'origin/main' by 5 commits.
     (use "git push" to publish your local commits)

   nothing to commit, working tree clean
   ```

4. Check log.

   **RUN:**

   ```console
   git log --oneline --graph --all
   ```

   **OUTPUT:**

   ```console
   * 11b91ef5 (HEAD -> main, dev) Add endpoint /world/city/{name}
   * c9eb6db4 Add world_table_city.csv
   * 0ea39e5d (upstream/main) Add endpoint /world
   * b3cd5997 Add world_table_country.csv
   * 2d169e14 Add initial requirements.txt
   * 0ced441a (origin/main, origin/HEAD) Initial commit
   ```

5. Update new commit on branch **`main`** to remote **`origin/main`**.

   **RUN:**

   ```console
   git push
   ```

   **OUTPUT:**

   ```console
   Enumerating objects: 8, done.
   Counting objects: 100% (8/8), done.
   Delta compression using up to 4 threads
   Compressing objects: 100% (6/6), done.
   Writing objects: 100% (6/6), 60.79 KiB | 4.34 MiB/s, done.
   Total 6 (delta 3), reused 0 (delta 0), pack-reused 0
   remote: Resolving deltas: 100% (3/3), completed with 2 local objects.
   To https://github.com/aaaaaaaaaa/world_api_fork.git
      0ced441a..11b91ef5  main -> main
   ```

6. Check log.

   **RUN:**

   ```console
   git log --oneline --graph --all
   ```

   **OUTPUT:**

   ```console
   * 11b91ef5 (HEAD -> main, origin/main, origin/HEAD, dev) Add endpoint /world/city/{name}
   * c9eb6db4 Add world_table_city.csv
   * 0ea39e5d (upstream/main) Add endpoint /world
   * b3cd5997 Add world_table_country.csv
   * 2d169e14 Add initial requirements.txt
   * 0ced441a Initial commit
   ```

7. Check branch.

   **RUN:**

   ```console
   git branch -avv
   ```

   **OUTPUT:**

   ```console
     dev                   11b91ef5 Add endpoint /world/city/{name}
   * main                  11b91ef5 [origin/main] Add endpoint /world/city/{name}
     remotes/origin/HEAD   -> origin/main
     remotes/origin/main   11b91ef5 Add endpoint /world/city/{name}
     remotes/upstream/main 0ea39e5d Add endpoint /world
   ```

### Check Point: Task 5_2

#### For Collaborator

In repository **`/d/working/world_api_fork`**, there should be:

- **4 new commit**
- current total commits: **6**
- local branches: **2**
- remote branches: **2**
- remote tracking branch: **1**

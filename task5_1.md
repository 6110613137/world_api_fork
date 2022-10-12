# Task 5_1

## Tasks for Maintainer

### Add development branch

1. Make sure you are in your **`world_api`** directory.

   **RUN:**

   ```console
   cd /d/working/world_api
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

### Add endpoint `/world`

1. Copy **`db/world_table_country.csv`** from assignment repo, e.g. **`/d/working/A06`**, into this directory.

   **RUN:**

   ```console
   cp /d/working/A06/db/world_table_country.csv .
   ```

   Note the dot **`.`** at the end of the command

2. Add the file and make a commit to the repo.

   ```console
   git add world_table_country.csv
   git commit -m "Add world_table_country.csv"
   ```

   **OUTPUT:**

   ```console
   [dev b3cd5997] Add world_table_country.csv
    1 file changed, 240 insertions(+)
    create mode 100644 world_table_country.csv
   ```

3. Modify **`main.py`** such that its current content is the same as the following code:

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
   git commit -m "Add endpoint /world"
   ```

   **OUTPUT:**

   ```console
   [dev 0ea39e5d] Add endpoint /world
    1 file changed, 16 insertions(+)
   ```

6. Check log.

   **RUN:**

   ```console
   git log --oneline --graph --all
   ```

   **OUTPUT:**

   ```console
   * 0ea39e5d (HEAD -> dev) Add endpoint /world
   * b3cd5997 Add world_table_country.csv
   * 2d169e14 (origin/main, main) Add initial requirements.txt
   * 0ced441a Initial commit
   ```

### Test endpoint `/world`

1. Make sure you are running in virtual environment.

   For Linux/MacOS:

   **RUN:**

   ```console
   python3 -m venv venv
   ```

   For Windows:

   **RUN:**

   ```console
   python -m venv venv
   ```

2. Run the application

   **RUN:**

   ```console
   uvicorn main:app --port 9000 --reload
   ```

   **OUTPUT:**

   ```console
   INFO:     Will watch for changes in these directories: ['/d/working/world_api']
   INFO:     Uvicorn running on http://127.0.0.1:9000 (Press CTRL+C to quit)
   INFO:     Started reloader process [10114] using StatReload
   INFO:     Started server process [10116]
   INFO:     Waiting for application startup.
   INFO:     Application startup complete.
   ```

3. Test the endpoint using browser.

   Open URL: <http://127.0.0.1:9000/world>.

   You should see a JSON object with a long list of objects.

   **OUTPUT:**

   ```console
   {
      result: [
         {
            Code: "ABW",
            Name: "Aruba",
            Continent: "North America",
            Region: "Caribbean",
            SurfaceArea: "193.00",
            IndepYear: "NULL",
            Population: "103000",
            LifeExpectancy: "78.4",
            GNP: "828.00",
            GNPOld: "793.00",
            LocalName: "Aruba",
            GovernmentForm: "Nonmetropolitan Territory of The Netherlands",
            HeadOfState: "Beatrix",
            Capital: "129",
            Code2: "AW"
         },
         {
            ...
         },
         {
            ...
         },
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
   Your branch is up to date with 'origin/main'.
   ```

2. Merge new commits from branch **`dev`**.

   **RUN:**

   ```console
   git merge dev
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

3. Update new commit on branch **`main`** to remote **`origin/main`**.

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
   Writing objects: 100% (6/6), 13.74 KiB | 1.06 MiB/s, done.
   Total 6 (delta 2), reused 0 (delta 0), pack-reused 0
   remote: Resolving deltas: 100% (2/2), completed with 1 local object.
   To https://github.com/xxxxxxxxxx/world_api.git
      2d169e14..0ea39e5d  main -> main
   ```

   **NOTE:**

   - this is a short version of `git push origin main`
     - default remote repo is **`origin`**
     - default remote branch is the remote tracking branch **`origin/main`** for current local branch (**`main`**)

4. Check log.

   **RUN:**

   ```console
   git log --oneline --graph --all
   ```

   **OUTPUT:**

   ```console
   * 0ea39e5d (HEAD -> main, origin/main, dev) Add endpoint /world
   * b3cd5997 Add world_table_country.csv
   * 2d169e14 Add initial requirements.txt
   * 0ced441a Initial commit
   ```

5. Check branch.

   **RUN:**

   ```console
   git branch -avv
   ```

   **OUTPUT:**

   ```console
     dev                 0ea39e5d Add endpoint /world
   * main                0ea39e5d [origin/main] Add endpoint /world
     remotes/origin/main 0ea39e5d Add endpoint /world
   ```

### Check Point: Task 5_1

#### For Maintainer

In repository **`/d/working/world_api`**, there should be:

- **2 new commits**
- current total commits: **4**
- local branches: **2**
- remote branches: **1**
- remote tracking branch: **1**

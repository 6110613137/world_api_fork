# Task 4_1

## Tasks for Maintainer

### Create depndencies for this application

1. Install dependencies for this **`world_api`** application.

   **RUN:**

   ```console
   pip install fastapi uvicorn
   ```

   **NOTE:**

   - this will install all dependencies (packages) required by this application

2. Run initial application

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

   **NOTE:**

   - **`main`** refers to the module name from `main.py`
   - **`app`** refers to an instance of an application object (from class `FastAPI`)  created in file `main.py`
   - option **`--port`** specifies port number to use, i.e. argument `9000`
   - option **`reload`** allows automatic reloading when there is a change in `main.py`
  
3. Test application using browser.

   Open URL: <http://127.0.0.1:9000>.

   You should see a JSON object.

   **OUTPUT:**

   ```console
   {
       message: "Hello there"
   }
   ```

4. Stop the appication.

   Press **`Ctrl+C`** to stop the appication

### Create a commit for dependencies

1. Create a **`requirements.txt`** file.

   **RUN:**

   ```console
   pip freeze > requirements.txt
   ```

2. Add **`requirements.txt`** to the repo.

   **RUN:**

   ```console
   git add requirements.txt
   ```

3. Create a commit.

   **RUN:**

   ```console
   git commit -m "Add initial requirements.txt"
   ```

   **OUTPUT:**

   ```console
   [main 2d169e14] Add initial requirements.txt
    1 file changed, 10 insertions(+)
    create mode 100644 requirements.txt
   ```

4. Push local change to remote repository **`origin`**.

   **RUN:**

   ```console
   git push
   ```

   **OUTPUT:**

   ```console
   Enumerating objects: 4, done.
   Counting objects: 100% (4/4), done.
   Delta compression using up to 4 threads
   Compressing objects: 100% (3/3), done.
   Writing objects: 100% (3/3), 395 bytes | 395.00 KiB/s, done.
   Total 3 (delta 1), reused 0 (delta 0), pack-reused 0
   remote: Resolving deltas: 100% (1/1), completed with 1 local object.
   To https://github.com/xxxxxxxxxx/world_api.git
      0ced441a..2d169e14  main -> main
   ```

5. Check log.

   **RUN:**

   ```console
   git log --oneline --graph --all
   ```

   **OUTPUT:**

   ```console
   * 2d169e14 (HEAD -> main, origin/main) Add initial requirements.txt
   * 0ced441a Initial commit
   ```

6. Check branch.

   **RUN:**

   ```console
   git branch -avv
   ```

   **OUTPUT:**

   ```console
   * main                2d169e14 [origin/main] Add initial requirements.txt
     remotes/origin/main 2d169e14 Add initial requirements.txt
   ```

#### Check Point: Task 4_1

#### For Maintainer

In repository **`/d/working/world_api`**, there should be:

- **1 new commit**
- current total commits: **2**
- local branches: **1**
- remote branches: **1**
- remote tracking branch: **1**

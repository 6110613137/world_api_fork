# Task 4_2

## Tasks for Collaborator(s)

For simplified workflow with predictable commit sequence, wait until Maintainer has completed tasks in `task4_1.md`.

### Get any update from **`upstream`**

1. Get any update from **`upstream`**.

   **RUN:**

   ```console
   git fetch upstream
   ```

   **OUTPUT:**

   ```console
   remote: Enumerating objects: 4, done.
   remote: Counting objects: 100% (4/4), done.
   remote: Compressing objects: 100% (2/2), done.
   remote: Total 3 (delta 1), reused 3 (delta 1), pack-reused 0
   Unpacking objects: 100% (3/3), 375 bytes | 375.00 KiB/s, done.
   From https://github.com/cn10xy/world_api
      0ced441a..2d169e14  main       -> upstream/main
   ```

2. Check for any new commit.

   **RUN:**

   ```console
   git log --oneline --graph --all
   ```

   **OUTPUT:**

   ```console
   * 2d169e14 (upstream/main) Add initial requirements.txt
   * 0ced441a (HEAD -> main, origin/main, origin/HEAD) Initial commit
   ```

### Merge any new commit from **`upstream`**

1. Make sure you are on local branch **`main`**

   **RUN:**

   ```console
   git switch main
   ```

   **OUTPUT:**

   ```console
   Already on 'main'
   Your branch is up to date with 'origin/main'
   ```

2. Merge any change from **`upstream`** to local branch **`main`**

   **RUN:**

   ```console
   git merge upstream/main
   ```

   **OUTPUT:**

   ```console
   Updating 0ced441a..2d169e14
   Fast-forward
    requirements.txt | 10 ++++++++++
    1 file changed, 10 insertions(+)
    create mode 100644 requirements.txt
   ```

   **NOTE:**

   - this is a simple **fast-forward** merge

### Install depndencies for this application

1. Install dependencies for this **`world_api_fork`** application.

   **RUN:**

   ```console
   pip install -r requirements.txt
   ```

   **NOTE:**

   - option **`-r`** spefifies requirement file to use
   - this will install all dependencies (packages) required by this application

2. Run initial application

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

### Push local change to **`origin`**

1. Check current status.

   **RUN:**

   ```console
   git status
   ```

   ***OUTPUT:**

   ```console
   On branch main
   Your branch is ahead of 'origin/main' by 1 commit.
     (use "git push" to publish your local commits)
   
   nothing to commit, working tree clean
   ```

2. Check log.

   **RUN:**

   ```console
   git log --oneline --graph --all
   ```

   **OUTPUT:**

   ```console
   * 23aa196f (HEAD -> main, upstream/main) Add initial requirements.txt
   * 5b25c744 (origin/main, origin/HEAD) Initial commit
   ```

3. Push local commits to **`origin`**

   **RUN:**

   ```console
   git push
   ```

   **OUTPUT:**

   ```console
   Total 0 (delta 0), reused 0 (delta 0), pack-reused 0
   To github.com:cn20xy/world_api_fork.git
      5b25c744..23aa196f  main -> main
   ```

4. Check current status again.

   **RUN:**

   ```console
   git status
   ```

   ***OUTPUT:**

   ```console
   On branch main
   Your branch is up to date with 'origin/main'.
   
   nothing to commit, working tree clean
   ```

5. Check log again.

   **RUN:**

   ```console
   git log --oneline --graph --all
   ```

   **OUTPUT:**

   ```console
   * 2d169e14 (HEAD -> main, upstream/main) Add initial requirements.txt
   * 0ced441a (origin/main, origin/HEAD) Initial commit
   ```

6. Check branch.

   **RUN:**

   ```console
   git branch -avv
   ```

   **OUTPUT:**

   ```console
   * main                  2d169e14 [origin/main: ahead 1] Add initial requirements.txt
     remotes/origin/HEAD   -> origin/main
     remotes/origin/main   0ced441a Initial commit
     remotes/upstream/main 2d169e14 Add initial requirements.txt
   ```

#### Check Point: Task 4_2

#### For Collaborator

In repository **`/d/working/world_api_fork`**, there should be:

- **0 new commit**
- current total commits: **2**
- local branches: **1**
- remote branches: **2**
- remote tracking branch: **1**

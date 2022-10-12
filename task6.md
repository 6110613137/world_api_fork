# Task 6

## Submit Repository

### Submit repository `world_api` or `world_api_fork`

1. Change into a directory containing your repository

   - for Maintaniner - **`world_api`**, e.g. **`/d/working`**
   - for Collaborators - **`world_api_fork`**, e.g. **`/d/working`**

   **RUN:**

   ```console
   cd /d/working
   ```

2. Compress the directory.

   - for Maintaniner -  **`world_api`** as **`world_api.zip`**
   - for Collaborators -  **`world_api_fork`** as **`world_api_fork.zip`**

   Using `zip`:

   **RUN:**

   ```console
   zip -r world_api.zip world_api -x '*/venv*' -x '*__pycache__*'
   # or
   zip -r world_api_fork.zip world_api_fork -x '*/venv*' -x '*__pycache__*'
   ```

   Using `7-zip`:

   **RUN:**

   ```console
   7z a world_api.zip world_api -xr'!venv' -xr'!__pycache__'
   # or
   7z a world_api_fork.zip world_api_fork -xr'!venv' -xr'!__pycache__'
   ```

   You can use other tools to compress the directory without using the command line.

3. Copy **`world_api.zip`** or **`world_api_fork.zip`** into your repository (**`/d/working/A06`**).

   ```console
   cp world_api.zip /d/working/A06/
   # or
   cp world_api_fork.zip /d/working/A06/
   ```

4. Add and commit **`world_api.zip`** or **`world_api_fork.zip`** to the repository.

   **RUN:**

   ```console
   git add world_api.zip
   # or
   git add world_api_fork.zip

   git commit -m "Complete Task 6"
   ```

**NOTE:**

- For your repository (**`/d/working/A06`**), there should be 3 commits with messages:

1. "Complete Task 1"
2. "Complete Task 2"
3. "Complete Task 6"

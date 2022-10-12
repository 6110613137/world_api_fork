# Task 4

## Prepare and Run Initial API

### Create virtual environment

1. For each member on their local repository:

   - for maintainer - e.g. go to direcotry **`/d/working/world_api`**
   - for collaborators - e.g. go to directory **`/d/working/world_api_fork`**

   For maintainer:

   **RUN:**

   ```console
   cd /d/working/world_api
   ```

   For collaborator(s):

   **RUN:**

   ```console
   cd /d/working/world_api_fork
   ```

2. Create a **virtual environment** inside the directory **`world_api`** or **`world_api_fork`**.

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

   **NOTE:**

   - option **`-m`** with argument (first) **`venv`** is to use module `venv`suppress
   - the (second) **`venv`** argument is the name of directory for new virtual environment

3. Activate the created virtual environment.

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

   **NOTE:**

   - note the `.` (dot) at begining of the command
   - your prompt should now start with **`(venv)`**

For Maintainer, continute to complete tasks in [task4_1.md](task4_1.md)
For Collaborator, continue to complete tasks in [task4_2.md](task4_2.md)

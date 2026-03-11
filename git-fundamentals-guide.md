# Git Fundamentals
### A Practical Guide for Beginners
*From Download to Pull Request — with Real Code Examples*

---

## Table of Contents

- [Part 1 — Setting Up Your Project](#part-1--setting-up-your-project)
  - [1.1 Download the Repository as a ZIP](#11-download-the-repository-as-a-zip)
  - [1.2 Unzip and Clean the src Folder](#12-unzip-and-clean-the-src-folder)
  - [1.3 Initialise a Git Repository](#13-initialise-a-git-repository)
  - [1.4 Add README.md and .gitignore](#14-add-readmemd-and-gitignore)
  - [1.5 Publish to GitHub with VS Code](#15-publish-to-github-with-vs-code)
- [Part 2 — Feature Branches and Pull Requests](#part-2--feature-branches-and-pull-requests)
  - [2.1 Create a Feature Branch](#21-create-a-feature-branch)
  - [2.2 Write Code — BMI Calculator](#22-write-code--bmi-calculator)
  - [2.3 Test the Code Locally](#23-test-the-code-locally)
  - [2.4 Commit and Push the Branch](#24-commit-and-push-the-branch)
  - [2.5 Create a Pull Request and Merge](#25-create-a-pull-request-and-merge)
- [Part 3 — Introducing a Bug (Intentionally)](#part-3--introducing-a-bug-intentionally)
- [Part 4 — Fetching and Pulling Changes](#part-4--fetching-and-pulling-changes)
- [Part 5 — Rolling Back with git revert and git reset](#part-5--rolling-back-with-git-revert-and-git-reset)
- [Part 6 — Tagging Releases with git tag](#part-6--tagging-releases-with-git-tag)
- [Quick Reference Cheat Sheet](#quick-reference-cheat-sheet)

---

## Part 1 — Setting Up Your Project

### 1.1 Download the Repository as a ZIP

If you don't have git installed yet, you can still download a copy of any GitHub repository as a plain ZIP file.

1. Open the repository page on GitHub in your browser.
2. Click the green **Code** button near the top-right of the file list.
3. Select **Download ZIP** from the dropdown menu.
4. Save the ZIP file to a convenient location (e.g. your Desktop or Downloads folder).

> 💡 **Tip:** You won't have any git history in this downloaded copy — that is intentional. You will create a fresh git repository in the next steps.

---

### 1.2 Unzip and Clean the src Folder

After extracting the archive you need to remove all files inside the `src` folder so you can start with a clean slate.

#### On Windows (File Explorer)

1. Right-click the ZIP file and choose **Extract All…**
2. Choose a destination folder and click **Extract**.
3. Open the extracted folder, navigate into `src`, select all files (`Ctrl+A`) and press `Delete`.

#### On macOS / Linux (Terminal)

```bash
# Unzip the archive
unzip repo-main.zip -d my-project

# Navigate into the project
cd my-project

# Remove everything inside src (keep the folder itself)
rm -rf src/*
```

---

### 1.3 Initialise a Git Repository

Open a terminal (or Git Bash on Windows), navigate to your project root, and run:

```bash
# Make sure you are in the project root
cd path/to/my-project

# Initialise git
git init

# Expected output:
# Initialized empty Git repository in .../my-project/.git/
```

> 📝 **Note:** `git init` creates a hidden `.git` folder. This folder stores every version of your project — do not delete it.

---

### 1.4 Add README.md and .gitignore

Two files every project should have from day one.

#### README.md

```bash
# Create a minimal README
echo "# My Project" > README.md
echo "" >> README.md
echo "A beginner Git practice project." >> README.md
```

#### .gitignore

The `.gitignore` file tells git which files to ignore (e.g. generated files, secrets, virtual environments).

```bash
cat > .gitignore << 'EOF'
__pycache__/
*.py[cod]
*.pyo
.env
.venv/
venv/
dist/
build/
*.egg-info/
.DS_Store
Thumbs.db
EOF
```

Stage and commit these two files:

```bash
git add README.md .gitignore
git commit -m "chore: add README and .gitignore"
```

---

### 1.5 Publish to GitHub with VS Code

VS Code has built-in git and GitHub integration — no CLI needed for this step.

1. Open the project folder in VS Code (**File → Open Folder…**).
2. Click the **Source Control** icon in the left sidebar (the branch icon).
3. Click **Publish to GitHub** at the top of the Source Control panel.
4. Sign in with your GitHub account if prompted.
5. Choose a repository name and visibility (public or private).
6. VS Code pushes your initial commit and opens the repository page in your browser.

> 💡 **Tip:** If you don't see 'Publish to GitHub', make sure the **GitHub Pull Requests and Issues** extension is installed.

---

## Part 2 — Feature Branches and Pull Requests

### 2.1 Create a Feature Branch

Always develop new features on a separate branch — never directly on `main`.

#### Modern command: `git switch`

Git 2.23 (released 2019) introduced `git switch` as a clearer, more focused replacement for `git checkout` when working with branches. Prefer it for all branch operations going forward.

```bash
# Create a new branch and switch to it immediately
git switch -c feature/bmi-calculator

# Equivalent old command (still works, but less clear):
# git checkout -b feature/bmi-calculator

# Verify you are on the new branch
git branch
# * feature/bmi-calculator
#   main
```

| Command | What it does |
|---|---|
| `git switch -c <name>` | Create a new branch and switch to it |
| `git switch <name>` | Switch to an existing branch |
| `git switch -` | Switch back to the previous branch |
| `git switch main` | Switch to the main branch |
| `git branch` | List all local branches |
| `git branch -d <name>` | Delete a local branch (safe — warns if unmerged) |

> 📝 **Note:** `git switch` only handles branch switching. Use `git restore` (also introduced in 2.23) to discard file changes instead of the old `git checkout -- <file>`.

---

### 2.2 Write Code — BMI Calculator

Create the file `src/main.py` with the following content:

```python
# src/main.py

def calculate_bmi(weight_kg: float, height_m: float) -> float:
    """
    Calculate Body Mass Index (BMI).

    Args:
        weight_kg: Weight in kilograms.
        height_m:  Height in metres.

    Returns:
        BMI as a float rounded to 2 decimal places.
    """
    if height_m <= 0:
        raise ValueError("Height must be greater than zero.")
    if weight_kg <= 0:
        raise ValueError("Weight must be greater than zero.")
    bmi = weight_kg / (height_m ** 2)
    return round(bmi, 2)


def bmi_category(bmi: float) -> str:
    """Return the WHO BMI category label."""
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25.0:
        return "Normal weight"
    elif bmi < 30.0:
        return "Overweight"
    else:
        return "Obese"


if __name__ == "__main__":
    weight = float(input("Enter your weight in kg: "))
    height = float(input("Enter your height in metres: "))
    bmi = calculate_bmi(weight, height)
    print(f"Your BMI is {bmi} — {bmi_category(bmi)}")
```

---

### 2.3 Test the Code Locally

Before committing, make sure everything works:

```bash
# Run the script interactively
python src/main.py

# Quick sanity check from the terminal
python -c "from src.main import calculate_bmi; print(calculate_bmi(70, 1.75))"
# Expected: 22.86

# Create and run tests with pytest
cat > src/test_main.py << 'EOF'
from main import calculate_bmi, bmi_category

def test_normal_bmi():
    assert calculate_bmi(70, 1.75) == 22.86

def test_category_normal():
    assert bmi_category(22.86) == "Normal weight"
EOF

cd src && python -m pytest test_main.py -v
```

---

### 2.4 Commit and Push the Branch

```bash
# Stage the new files
git add src/main.py src/test_main.py

# Commit with a descriptive message
git commit -m "feat: add BMI calculator with category labels"

# Push the branch to GitHub
git push -u origin feature/bmi-calculator

# -u sets the upstream so future pushes only need: git push
```

---

### 2.5 Create a Pull Request and Merge

1. Go to your GitHub repository in the browser.
2. You will see a banner: *"feature/bmi-calculator had recent pushes"*. Click **Compare & pull request**.
3. Add a clear title (e.g. `feat: BMI calculator`) and a brief description of your changes.
4. Click **Create pull request**.
5. Review the diff, then click **Merge pull request → Confirm merge**.
6. Click **Delete branch** to clean up the remote branch.

Sync your local repo:

```bash
# Switch back to main using the modern command
git switch main

# Pull the merged changes
git pull origin main

# Delete the local branch
git branch -d feature/bmi-calculator
```

---

## Part 3 — Introducing a Bug (Intentionally)

This section demonstrates a common real-world mistake: code that passes all tests but produces wrong results because the test cases were also wrong.

### 3.1 Create a Bug Branch

```bash
git switch -c feature/bmi-imperial-input
```

### 3.2 Add the Buggy Code

Replace the contents of `src/main.py` with the version below. The user enters weight in pounds, but the conversion to kilograms is **missing** — so the formula silently receives the wrong value.

```python
# src/main.py  ← BUGGY VERSION

def calculate_bmi(weight_lb: float, height_m: float) -> float:
    """
    Calculate BMI from weight in POUNDS and height in metres.
    BUG: weight is never converted from lb to kg!
    """
    # Missing: weight_kg = weight_lb * 0.453592
    bmi = weight_lb / (height_m ** 2)   # ← uses lb directly — WRONG
    return round(bmi, 2)


def bmi_category(bmi: float) -> str:
    if bmi < 18.5:   return "Underweight"
    elif bmi < 25.0: return "Normal weight"
    elif bmi < 30.0: return "Overweight"
    else:            return "Obese"


if __name__ == "__main__":
    weight = float(input("Enter your weight in pounds: "))
    height = float(input("Enter your height in metres: "))
    bmi = calculate_bmi(weight, height)
    print(f"Your BMI is {bmi} — {bmi_category(bmi)}")
```

### 3.3 The Misleading Test

The test below **passes** because the expected value was calculated using the same buggy formula:

```python
# src/test_main.py  ← TESTS THAT PASS BUT ARE WRONG

from main import calculate_bmi

def test_bmi_with_pounds():
    # 154 lb, 1.75 m → correct BMI should be 22.86
    # But this test expects the wrong (buggy) result
    assert calculate_bmi(154, 1.75) == 50.32   # 154 / 1.75² = 50.32 — WRONG

# pytest passes ✓ … but 50.32 is wildly incorrect for someone 154 lb / 1.75 m
```

> ⚠️ **Warning:** Tests that pass are not proof of correctness — the test data must also be verified against real-world expectations.

### 3.4 Push, PR, Merge, and Delete

```bash
git add src/main.py src/test_main.py
git commit -m "feat: accept weight in pounds (WIP)"
git push -u origin feature/bmi-imperial-input
```

Then on GitHub: open a PR, merge into `main`, delete the remote branch, and sync locally as shown in section 2.5.

---

## Part 4 — Fetching and Pulling Changes

This is one of the most important distinctions to understand in Git. There are three similar-looking commands that behave very differently.

### The Three Commands Compared

```bash
git pull                  # (1) fetch + merge in one step
git fetch origin main     # (2) download only — don't touch your branches
git fetch origin main:main  # (3) download AND update your local main branch
```

---

### `git pull`

`git pull` is shorthand for two operations: **fetch** then **merge** (or rebase, depending on config). It downloads new commits from the remote **and immediately merges them into your current branch**.

```bash
git switch main
git pull

# Equivalent to:
git fetch origin
git merge origin/main
```

**When to use it:** When you're on a branch and want to bring it up to date with the remote in one step. This is the most common daily command.

**Potential downside:** If you have local uncommitted changes or unpushed commits, the automatic merge can create merge commits or conflicts. Some teams prefer `git fetch` + manual `git merge` for more control.

---

### `git fetch origin main`

`git fetch origin main` downloads commits from the remote `main` branch into a **remote-tracking reference** called `origin/main`. It does **not** touch your local `main` branch or your working directory at all.

```bash
git fetch origin main

# Your local `main` is unchanged.
# But origin/main is now up to date.

# You can inspect what was fetched before merging:
git log main..origin/main          # commits on remote not yet in local main
git diff main origin/main          # see what changed

# Then merge manually when you're ready:
git merge origin/main
```

**When to use it:** When you want to **see what changed** on the remote without affecting your local work. Safe to run at any time.

---

### `git fetch origin main:main`

`git fetch origin main:main` downloads commits from the remote `main` **and also fast-forwards your local `main` branch** to match — but only if you are **not** currently on `main`.

```bash
# You are on a feature branch
git switch feature/bmi-calculator

# This updates local main without switching branches
git fetch origin main:main

# Now local main is up to date — and you never left your feature branch!
# You can now rebase your feature branch onto the updated main:
git rebase main
```

**When to use it:** When you're working on a feature branch and want to update `main` in the background without switching to it. This is particularly useful before rebasing.

> ⚠️ **Warning:** This command will **fail** if you are currently checked out on `main`, because Git won't update a branch you have checked out via a fetch. Use `git pull` instead in that case.

---

### Side-by-Side Summary

| Command | Downloads new commits | Updates `origin/main` ref | Updates local `main` branch | Merges into current branch |
|---|---|---|---|---|
| `git pull` | ✅ | ✅ | ✅ (if on main) | ✅ automatic |
| `git fetch origin main` | ✅ | ✅ | ❌ | ❌ manual |
| `git fetch origin main:main` | ✅ | ✅ | ✅ (if NOT on main) | ❌ manual |

---

### Practical Workflow Example

```bash
# You're deep in a feature branch and hear that main has been updated.
# You want to rebase your feature on the latest main — without switching branches.

git switch feature/bmi-calculator    # you're here

git fetch origin main:main           # update local main silently

git rebase main                      # rebase feature onto updated main

git push --force-with-lease          # push the rebased branch
```

---

## Part 5 — Rolling Back with git revert and git reset

### 5.1 View Your Commit History

```bash
git log --oneline

# Example output:
# a3f2c1d (HEAD -> main) feat: accept weight in pounds (WIP)
# 7b9e4a2 feat: add BMI calculator with category labels
# 1d0c8f3 chore: add README and .gitignore
```

---

### 5.2 git revert — Safe Undo (Recommended)

`git revert` creates a **new commit** that undoes the changes from a specific commit. This is the safest approach because it preserves the full history and is safe on shared branches.

```bash
# Revert the most recent commit
git revert HEAD

# Revert a specific commit by hash
git revert a3f2c1d

# Revert without opening an editor (uses default commit message)
git revert HEAD --no-edit

# Push the revert
git push
```

> 📝 **Note:** After reverting, `git log` will show both the original commit and the new `Revert "..."` commit. The buggy code is gone from the working tree but still visible in history.

---

### 5.3 git reset — Rewrite History (Use with Caution)

`git reset` moves the branch pointer backwards. Use this **only** on commits that have **not** been pushed, or with extreme care on unshared branches.

```bash
# --soft  →  undo commit, keep changes staged
git reset --soft HEAD~1

# --mixed (default)  →  undo commit, keep changes in working directory (unstaged)
git reset HEAD~1

# --hard  →  DISCARD all changes (cannot be undone easily)
git reset --hard HEAD~1

# After a hard reset on a pushed branch you must force-push
# ⚠️  Never force-push to shared branches!
git push --force-with-lease
```

| Mode | What happens to your changes |
|---|---|
| `--soft` | Kept staged — ready to recommit |
| `--mixed` | Kept but unstaged — review before re-staging |
| `--hard` | Permanently discarded — cannot be recovered easily |

> ⚠️ **Warning:** Avoid `git reset --hard` on commits that teammates have already pulled. Use `git revert` for shared branches.

---

### 5.4 git restore — Discard File Changes (Modern Command)

For discarding changes to individual files, use `git restore` instead of the old `git checkout -- <file>`:

```bash
# Discard unstaged changes to a single file
git restore src/main.py

# Discard all unstaged changes in the working directory
git restore .

# Unstage a file (remove from staging area, keep changes in working dir)
git restore --staged src/main.py

# Old equivalents (still work, but less clear):
# git checkout -- src/main.py
# git reset HEAD src/main.py
```

---

## Part 6 — Tagging Releases with git tag

### 6.1 Why Tags?

Tags mark specific commits as meaningful milestones (`v1.0`, `v2.0-beta`, etc.). Unlike branches, tags do not move when new commits are added — they are **permanent pointers** to a snapshot.

---

### 6.2 Creating Tags

```bash
# Lightweight tag (just a name, no message)
git tag v1.0

# Annotated tag (recommended — includes author, date, message)
git tag -a v1.0 -m "Release v1.0: working BMI calculator with kg input"

# Tag a specific past commit
git tag -a v0.1 7b9e4a2 -m "Initial BMI implementation"

# List all tags
git tag

# Show tag details
git show v1.0
```

---

### 6.3 Push Tags to GitHub

```bash
# Push a single tag
git push origin v1.0

# Push ALL tags at once
git push origin --tags
```

> 📝 **Note:** Tags pushed to GitHub automatically appear under **Releases** on the repository page.

---

### 6.4 Creating a GitHub Release from a Tag

1. Go to your repository on GitHub.
2. Click the **Releases** link in the right sidebar (or the Releases tab).
3. Click **Draft a new release**.
4. Select the tag you just pushed from the dropdown.
5. Add release notes and click **Publish release**.

---

### 6.5 Revert to a Previous Release

To restore your project to the state it was in at a tagged release:

```bash
# Option A: Check out the tag in 'detached HEAD' state (read-only look)
git switch --detach v1.0
# Old equivalent: git checkout v1.0

# Option B: Create a new branch FROM the tag and continue working there (recommended)
git switch -c hotfix/v1.0-patch v1.0
# Old equivalent: git checkout -b hotfix/v1.0-patch v1.0

# Option C: Hard reset main to the tag (rewrites history — be careful!)
git switch main
git reset --hard v1.0
git push --force-with-lease
```

> 💡 **Tip:** Option B is usually the safest choice: you get a full working branch based on the stable release, without destroying the buggy history.

| Goal | Recommended command |
|---|---|
| Undo last commit (keep history) | `git revert HEAD` |
| View repo at old release | `git switch --detach v1.0` |
| Start a hotfix from stable release | `git switch -c hotfix/v1.0-patch v1.0` |
| Permanently roll back main (danger!) | `git reset --hard v1.0` + force push |

---

## Quick Reference Cheat Sheet

### Repository Setup

| Command | Description |
|---|---|
| `git init` | Initialise a new local repository |
| `git clone <url>` | Clone an existing remote repository |
| `git remote add origin <url>` | Link local repo to a remote |
| `git remote -v` | Show remote connections |

---

### Everyday Workflow

| Command | Description |
|---|---|
| `git status` | Show staged/unstaged changes |
| `git add <file>` | Stage a file for commit |
| `git add .` | Stage all changes |
| `git commit -m 'msg'` | Commit staged changes |
| `git push` | Push to remote branch |
| `git pull` | Fetch and merge from remote |
| `git fetch origin main` | Download remote changes, don't merge |
| `git fetch origin main:main` | Update local main while on another branch |
| `git log --oneline` | Compact commit history |

---

### Branches (Modern Commands)

| Command | Description |
|---|---|
| `git switch -c <name>` | Create and switch to new branch |
| `git switch <name>` | Switch to existing branch |
| `git switch -` | Switch back to previous branch |
| `git switch --detach <tag>` | Check out a tag or commit in detached HEAD |
| `git merge <name>` | Merge branch into current |
| `git branch -d <name>` | Delete local branch |
| `git push origin --delete <name>` | Delete remote branch |

---

### Discarding Changes (Modern Commands)

| Command | Description |
|---|---|
| `git restore <file>` | Discard unstaged changes to a file |
| `git restore .` | Discard all unstaged changes |
| `git restore --staged <file>` | Unstage a file |

---

### Undo / History

| Command | Description |
|---|---|
| `git revert HEAD` | Safe undo of last commit (keeps history) |
| `git reset --soft HEAD~1` | Undo commit, keep changes staged |
| `git reset --hard HEAD~1` | Undo commit, discard changes |
| `git diff` | Show unstaged differences |
| `git diff HEAD` | Show all uncommitted changes |

---

### Tags

| Command | Description |
|---|---|
| `git tag -a v1.0 -m 'msg'` | Create annotated tag |
| `git tag` | List all tags |
| `git push origin --tags` | Push all tags to remote |
| `git switch --detach v1.0` | Check out code at a tag |
| `git show v1.0` | Display tag details |

---

### Old vs Modern Command Reference

| Old command | Modern equivalent | Notes |
|---|---|---|
| `git checkout -b <name>` | `git switch -c <name>` | Create and switch branch |
| `git checkout <name>` | `git switch <name>` | Switch branch |
| `git checkout <tag>` | `git switch --detach <tag>` | Detached HEAD |
| `git checkout -- <file>` | `git restore <file>` | Discard file changes |
| `git reset HEAD <file>` | `git restore --staged <file>` | Unstage a file |

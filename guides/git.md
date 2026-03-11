# 📘 The Modern Git & Open Source Guide (2026)
*A comprehensive guide to modern commands, rebasing, and the forking workflow.*

---

## 1. Project Initialization & Setup
| Command | Action |
| :--- | :--- |
| `git init` | Start a new local repository. |
| `git clone <url>` | Clone a remote repository. |
| `git config --global pull.rebase true` | **Best Practice:** Sets rebase as the default for all pulls. |

---

## 2. Modern Branching (The `switch` Command)
Git now uses `switch` instead of `checkout` for moving between branches to avoid confusion.

* **Create and jump to a branch:** `git switch -c feature-name`
* **Switch back to main:** `git switch main`
* **Toggle to previous branch:** `git switch -`



---

## 3. Undoing Mistakes Gracefully
Use `restore` instead of the old `reset` or `checkout` methods for files.

* **Discard unstaged changes:** `git restore <filename>`
* **Unstage a file (keep your code):** `git restore --staged <filename>`
* **The "Clean Slate":** `git reset --hard HEAD` (Wipes all changes since last commit).
* **Delete junk files/folders:** `git clean -fd`

---

## 4. Resolving Merge Conflicts
Conflicts happen when Git doesn't know which version of a line to keep.

### The Workflow:
1.  **Locate the markers:** Look for `<<<<<<< HEAD`, `=======`, and `>>>>>>>`.
    * Everything between `HEAD` and `====` is **your** change.
    * Everything between `====` and the branch name is the **incoming** change.
2.  **Edit the file:** Manually delete the markers and keep the version of the code you want (or combine them).
3.  **Stage it:** `git add <filename>`
4.  **Finish it:**
    * If merging: `git commit`
    * If rebasing: `git rebase --continue`

---

## 5. The Forking Workflow (Working on Open Source)
When you don't have "Write" access to a project, you **Fork** it. This creates your own copy on GitHub.

### Setup (Only do this once):
1.  **Clone your fork:** `git clone <your-fork-url>`
2.  **Add the original repo as "Upstream":**
    `git remote add upstream <original-project-url>`
3.  **Verify:** `git remote -v` (You should see `origin` as yours and `upstream` as the original).



---

## 6. Syncing your Fork
If the original project (`upstream`) adds new features, you need to bring them into your fork (`origin`).

### The Modern Way (Rebase):
1.  **Fetch the latest:** `git fetch upstream`
2.  **Move your work on top:** `git rebase upstream/main`
3.  **Update your GitHub:** `git push origin main --force-with-lease`
    * *Note: Use `--force-with-lease` after rebasing a branch that you've already pushed.*



---

## 7. Conflicts During a Fork Sync
If you edited a line in your fork that was also changed in the `upstream` project, a rebase will pause.

1.  Git will say: *"CONFLICT (content): Merge conflict in <filename>"*.
2.  Open the file and resolve the conflict manually.
3.  Run `git add <filename>`.
4.  Run `git rebase --continue`.
5.  Repeat if necessary, then push: `git push origin HEAD --force-with-lease`.

---

## 8. 🚀 Ultimate Quick-Reference Cheat Sheet

| Category | Task | Command |
| :--- | :--- | :--- |
| **Setup** | Set name/email | `git config --global user.name "Your Name"` |
| **Branching** | Create & move | `git switch -c <name>` |
| **Branching** | Delete branch | `git branch -d <name>` |
| **Saving** | Stage all | `git add .` |
| **Saving** | Commit | `git commit -m "Message"` |
| **Syncing** | Pull latest | `git pull --rebase origin main` |
| **Syncing** | Push to cloud | `git push origin HEAD` |
| **Undo** | Discard edits | `git restore <file>` |
| **Undo** | Unstage file | `git restore --staged <file>` |
| **Open Source** | Link original | `git remote add upstream <url>` |
| **Open Source** | Sync original | `git fetch upstream && git rebase upstream/main` |

---

## ⚠️ The Golden Rule
**Only rebase branches you own (local feature branches).** Never rebase a public branch like `main` if other people are using it, as it will break their history and cause massive conflicts for the team.
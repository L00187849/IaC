# Git Command Cheat Sheet

---

##  Setup 

```bash
git --version
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
git config --global init.defaultBranch main
git config --global core.editor "code --wait"   # VS Code as editor
git config --list
```
Show where a setting comes from:
```bash
git config --show-origin --get user.email
```

---

##  Repos

```bash
git init                         # start a new repo in the current folder
git clone <url>                  # clone existing repo
git status                       # what changed?
git log --oneline --graph --decorate --all   # nice history view
git show <rev>                   # show a commit or object details
git diff                         # unstaged changes
git diff --staged                # staged changes
```

---

##  Staging & Committing

```bash
git add <file>                   # stage file
git add .                        # stage all tracked/untracked changes
git restore --staged <file>      # unstage
git commit -m "message"          # commit staged changes
git commit --amend               # edit last commit (message/contents)
```

---

##  Branching 

```bash
git branch                       # list branches
git branch <name>                # create branch
```

---

## 5) GIT Pull and Git Push

```bash
git remote -v
git remote add origin <url>
git fetch origin                 # download refs, not merge
git pull                         # fetch + merge (uses tracking branch)
git pull --rebase                # fetch + rebase (clean history)
git push -u origin main          # first push; set upstream
git push                         # push current branch
git push --force-with-lease      # safe force-push when necessary
```

**Common URLs**
- SSH: `git@github.com:user/repo.git`  
- HTTPS: `https://github.com/user/repo.git`



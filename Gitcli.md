## git 笔记 



git init——初始化仓库

git status——查看仓库的状态

git add——向暂存区中添加文件 (如何清空暂存区呢)

git commit——保存仓库的历史记录

git commit -am --改动文件而没有新建文件的时候合并提交

git commit --amend——修改提交信息

git log——查看提交日志

git log --graph——以图表形式查看分支

git reflog命令，查看当前仓库的操作日志

git diff——查看更改前后的差别

git branch——显示分支一览表

git checkout -b——创建、切换分支

git checkout - 切换回上一个分支

git merge——合并分支

git reset——回溯历史版本

```
git rest --hard hash
```

git rebase -i HEAD~n ——压缩历史  (多个commit压缩成一个)pick -> fixup

git remote add——添加远程仓库

git push——推送至远程仓库

```
git push -u origin master
```

git pull

```
git pull origin dev
```

### notes:

Pro Git

LearnGitBranching

tryGit



### tricks:

```
git checkout -b branch-name origin/branch-name
```


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


### 新建git仓库的命令说明

##### Git global setup

```shell
git config --global user.name "username"
git config --global user.email your-email
```


在Git中，用`HEAD`表示当前版本，也就是最新的提交`1094adb...`，上一个版本就是`HEAD^`，上上一个版本就是`HEAD^^`，当然往上100个版本写100个`^`比较容易数不过来，所以写成`HEAD~100`

`git reset --hard HEAD^`  	回退到上次提交

`git reset --hard HEAD^^` 	回退到上上次提交

`git reset --hard HEAD~n` 	回退到上n次提交

`git reset --hard commit_id`	回退到指定id

`git reflog` 用来记录每一次命令

`git diff HEAD -- filename` 查看工作区和版本库里面最新版本的区别



撤销操作：

工作区： `git checkout -- filename`  撤销工作区

暂存区：`git reset HEAD <file>`  撤销暂存区,重新放回工作区

已经commit的时候使用reset



删除操作：

暂存区删除： `git rm `

误删除恢复：git checkout -- file （等于撤销工作区的操作）



`git stash`  `git stash list`

`git stash apply`不删除stash，需要使用`git stash drop` （`git stash apply stash@{0}`）

`git stash pop`	恢复的同时删除删除stash

`git cherry-pick `命令，把bug提交的修改“复制”到当前分支，避免重复劳动






##### Create a new repository

```shell
git clone git@xxxx.git
cd test
touch README.md
git add README.md
git commit -m "add README"
```



##### Push an existing folder

```shell
cd existing_folder
git init
# 关联远程仓库命名为origin， 可以使用git remote rm origin删除
git remote add origin git@xxxx.git
git add .
git commit -m "Initial commit"
```

##### Push an existing Git repository

```shell
cd existing_repo
# git仓库迁移
git remote rename origin old-origin
git remote add origin git@xxxx.git
```



------
`git remote -v`  查看关联远程仓库

git push -u origin master  默认把mater分支提交到origin远程，之后只要git push就行了





Github和gitee双向同步

```
$ git remote set-url --add origin git@xxxx.git
```

git push 就会同时同步github和gitee了，如果分别拉取和推送的话同**Push an existing Git repository**

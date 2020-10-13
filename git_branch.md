## git 如何管理远程仓库

https://docs.github.com/cn/free-pro-team@latest/github/using-git/managing-remote-repositories



远程仓库有https协议和ssh 协议的两种，一般的来说，一个本地仓库对应一个远程仓库，当然也有对应多个的时候，比如说git仓库迁移又不想丢失原来的commit信息，这个时候就可以对应原来的远程分支（origin）和新的远程（new）

```
https://github.com/user/repo.git
git@github.com:user/repo.git
```

有关这些 URL 之间差异的信息，请参阅“[我应使用哪种远程 URL？](https://docs.github.com/cn/free-pro-team@latest/articles/which-remote-url-should-i-use)”

### 创建远程

使用 `git remote add` 命令将远程 URL 与名称匹配。 例如，在命令行中输入以下命令：

```shell
git remote add origin  <REMOTE_URL> 
```

这会将名称 `origin` 与 `REMOTE_URL` 关联。

您可以使用命令 `git remote set-url` 来[更改远程 URL](https://docs.github.com/cn/free-pro-team@latest/articles/changing-a-remote-s-url)。

### 添加远程

`git remote add` 命令使用两个参数：

- 远程命令，如 `origin`
- 远程 URL，如 `https://github.com/user/repo.git`

```shell
$ git remote add origin https://github.com/user/repo.git
# Set a new remote

$ git remote -v
# Verify new remote
> origin  https://github.com/user/repo.git (fetch)
> origin  https://github.com/user/repo.git (push)
```

### 更改远程

`git remote set-url` 命令可更改现有远程仓库的 URL。

```shell
$ git remote set-url origin https://github.com/USERNAME/REPOSITORY.git
$ git remote set-url origin git@github.com:USERNAME/REPOSITORY.git
```

### 重命名远程

使用 `git remote rename` 命令可重命名现有的远程。

```shell
$ git remote -v
# 查看现有远程
> origin  https://github.com/OWNER/REPOSITORY.git (fetch)
> origin  https://github.com/OWNER/REPOSITORY.git (push)

$ git remote rename origin destination
# 将远程名称从 'origin' 更改为 'destination'

$ git remote -v
# 验证远程的新名称
> destination  https://github.com/OWNER/REPOSITORY.git (fetch)
> destination  https://github.com/OWNER/REPOSITORY.git (push)
```

### 删除远程

使用 `git remote rm` 命令可从仓库中删除远程 URL。

`git remote rm` 命令使用一个参数：

- 远程名称，例如 `destination`

```shell
$ git remote -v
# 查看当前远程
> origin  https://github.com/OWNER/REPOSITORY.git (fetch)
> origin  https://github.com/OWNER/REPOSITORY.git (push)
> destination  https://github.com/FORKER/REPOSITORY.git (fetch)
> destination  https://github.com/FORKER/REPOSITORY.git (push)

$ git remote rm destination
# 删除远程
$ git remote -v
# 验证其已删除
> origin  https://github.com/OWNER/REPOSITORY.git (fetch)
> origin  https://github.com/OWNER/REPOSITORY.git (push)
```

> `git remote rm` 不会从服务器中删除远程仓库。 它只是从本地仓库中删除远程及其引用。

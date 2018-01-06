# git使用

## 协作开发

> 很重要的一点，如何让其他的小伙伴提交代码到我的仓库
权限问题，不能随便让别人动自己的项目，一般流程：`fork -> pull -> request -> merge`

1、让他fork一份你的项目，改好了再pull request，你测试没问题后merge。
2、你在项目`settings`的`Collaborators`这里，把他的github账号加入Collaborators。

> 别人git提交了代码，我怎么更新代码

1、让别人 git commit push。我这边 先做一个 git rebase 或者 merge
2、可以先在我的本地做一个 git stash 放到栈中，然后 git pull下来，检查是否有冲突
3、最简单的应该是自己再建一个分支，然后pull下来看看代码是否有问题，做相关的处理后再merge到自己的开发分支上

4、使用 git fetch upstream 拉取原作者的仓库更新
  git checkout master 切换到自己的主分支上
  git merge upstream/master ，这里merge或者rebase都行，到自己的主分支上，这样就完成了更新

### fork 和 clone 的区别

1、fork：在github页面，点击fork按钮。将别人的仓库复制一份到自己的仓库
2、clone：将github中的仓库克隆到自己本地电脑中

## git commit -m 和 git commit -am "" 的却别

1、git commit -m 用于提交暂存区的文件    | 如果`add`过的文件修改，直接使用这句，不会提交修改后的内容-- 因为新增的内容没有提交到暂存区
2、git commit -am 用于提交跟踪过的文件  | 就是如果`add`过的文件修改了，那么这是可以将修改过的内容一起提交
总结：使用git commit -am可以省略使用git add命令将已跟踪文件放到暂存区的功能

## git add -A和 git add .   git add -u

    git add . ：他会监控工作区的状态树，使用它会把工作时的所有变化提交到暂存区，包括文件内容修改(modified)以及新文件(new)，但不包括被删除的文件。

    git add -u ：他仅监控已经被add的文件（即tracked file），他会将被修改的文件提交到暂存区。add -u 不会提交新文件（untracked file）。（git add --update的缩写）

    git add -A ：提交所有变化;是上面两个功能的合集（git add --all的缩写）

## 分支

> 一般建这么几个分支 `master | dev | bug | feature`

1、新建分支
    git checkout -b branchame
2、切换分支
    git checkout branchname
3、合并分支
    git checkout master  |  git merge branchname
4、获取分支
    git branch
5、删除分支
    git branch -D branchname
6、合并分支时产生冲突
    git status  |  git mergetool  |  手动解决冲突地方  |  git status  |  git merge branchname

## 创建&删除远程分支

1、git push origin master:branch-name
2、git push origin :branch-name

### 下载指定分支

1、使用Git下载指定分支命令为：git clone -b 分支名仓库地址

### 在本地奖励和远程分支对应的分支

1、git checkout -b branch-name origin/branch-name

## 标签

    tag就像是一个里程碑一个标志一个点，branch是一个新的征程一条线；
    tag是静态的，branch要向前走；
      * git tag分为两种类型：轻量tag 和 附注tag。轻量tag是指向提交对象的引用，附注tag则是仓库中的一个独立的对象  |  建议使用附注Tag
1、新建tag
    git tag v0.1.1  |  不需要传递参数
    git tag -a v0.1.2 -m '0.1.2版本'  |  需指定tag类型
2、切换标签
    git checkout tagname
3、查看tag
    git show tagname
    git tag
4、删除tag
    git tag -d tagname
5、给指定的commit打tag
    git tag -a v0.1.1 9fbc360
6、tag推送到服务器
    git push origin tagname
    git push --tags

## 删除文件&文件夹

1、删除raindow文件夹及其下所有的文件
    git rm raindow -r -f |
2、删除 index.html 文件
    git rm index.html

## git pull | fetch

1、git fetch：相当于是从远程获取最新版本到本地，不会自动merge

```js
git fetch origin master
git log -p master..origin/master
git merge origin/master

首先从远程的origin的master主分支下载最新的版本到origin/master分支上
   然后比较本地的master分支和origin/master分支的差别
   最后进行合并

git fetch origin master:tmp
git diff tmp
git merge tmp
```

2、git pull：相当于是从远程获取最新版本并merge到本地

```js
git pull origin master

上述命令其实相当于git fetch 和 git merge
```

3、在实际使用中，`git fetch + merge` 更安全一些
因为在merge前，我们可以查看更新情况，然后再决定是否合并

4、如果提示`no tracking information`，则说明本地分支和远程分支的链接关系还没有创建，用命令解决
`git branch --set-upstream branch-name origin/branch-name`

5、git merge 和 rebase 的区别

1、git merge 会生成一个新的合并节点。而rebase不会

## 版本回退

1、git log   |  git log --pretty=online
2、git reflog
3、git reset --hard commit_id
4、git reset --hard HEAD^
5、git revert HEAD | git revert HEAD~0、1/2

## window下git使用问题

在windows中使用git签出项目的时候

warning: Your console font probably doesn't support Unicode. If you experience strange characters in the output, consider switching to a TrueType font such as Lucida Console!

应该是字符不对，所以在粘贴之前先修改一下字符，

用这个命令：$ git config --global core.autocrlf true，完了就可以下载成功

## git项目中存在子项目 不能提交的问题

    例如：github pages hexo next 主题不能提交到 github 对应的博客项目里面
    造成的问题：next 主题里面的一些配置不能同步提交到 github。如果将本地项目删除了，主体又做了很多的修改，无法通过
    远程仓库恢复，再配置就比较麻烦

## 如何检测 当前分支与远程分支存在追踪关系

    如何查看当前分支如temp，track到的是远程代码库的哪个分支呀？
    git config -l | grep 'branch\.temp'
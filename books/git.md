# git使用

## git commit -m 和 git commit -am "" 的却别
1、git commit -m 用于提交暂存区的文件    | 如果`add`过的文件修改，直接使用这句，不会提交修改后的内容-- 因为新增的内容没有提交到暂存区
2、git commit -am 用于提交跟踪过的文件  | 就是如果`add`过的文件修改了，那么这是可以将修改过的内容一起提交
总结：使用git commit -am可以省略使用git add命令将已跟踪文件放到暂存区的功能


## git add -A和 git add .   git add -u
    git add . ：他会监控工作区的状态树，使用它会把工作时的所有变化提交到暂存区，包括文件内容修改(modified)以及新文件(new)，但不包括被删除的文件。

    git add -u ：他仅监控已经被add的文件（即tracked file），他会将被修改的文件提交到暂存区。add -u 不会提交新文件（untracked file）。（git add --update的缩写）

    git add -A ：提交所有变化;是上面两个功能的合集（git add --all的缩写）

## 分支
1、新建分支
    git checkout -b branchame
2、切换分支
    git checkout branchname
3、合并分支
    git checkout master  |  git merge branchname
4、获取分支
    git branch
5、删除分支
    git checkout -d branchname
6、合并分支时产生冲突
    git status  |  git mergetool  |  手动解决冲突地方  |  git status  |  git merge branchname
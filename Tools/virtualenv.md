在开发Python应用程序的时候，系统安装的Python3只有一个版本。所有第三方的包都会被pip安装到Python3的site-packages目录下.

然而一台服务器上可能运行好几个项目，而不同项目所用的需求文件版本不一定一样，甚至python的版本都不同。

这种情况下，每个应用可能需要各自拥有一套“独立”的Python运行环境。virtualenv就是用来为一个应用创建一套“隔离”的Python运行环境。

安装virtualenv:  
```$ pip3 install virtualenv```

创建一个独立的Python运行环境,命名为venv, 在项目根目录运行:  
```$ virtualenv --no-site-packages venv```

其中, `--no-site-pacakages`会禁止将已经安装到系统Python环境中的第三方包复制过来, 这样会获得一个不带任何第三方包的“干净”的Python运行环境.

进入virtualenv提供的虚拟环境:  
bash: `source venv/bin/activate`  
cmd:`venv/Scripts/activate`

注意到命令提示符变了，有个(venv)前缀，表示当前环境是一个名为venv的Python环境.  
```
c:\code\python\diet-pal>venv\Scripts\activate
(venv) c:\code\python\diet-pal>
```  

要退出, 输入`deactivate`即可.  

要给服务器搭建同样的环境, 先导出本地环境, 在本地执行:  
```pip freeze > \requirement.txt```

然后进入服务器, 创建虚拟环境并进入, 上传requirement.txt, 然后执行:
```pip install -r requirements.txt```

pip会自动读取项目根目录下的需求文件，并且安装里面记录的包。这样，开发环境就复制到服务器了。而且环境只在你创建的虚拟环境中，不会和外部环境冲突。
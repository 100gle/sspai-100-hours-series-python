# 《100 小时后请叫我程序员》教程源码使用说明

本仓库为少数派平台 [《100 小时后请叫我程序员》](https://sspai.com/series/271) 教程内容的相关源码、以及素材仓库，教程内的大部分示例代码都可通过对应的目录找到。

在使用过程中如有任何问题欢迎在少数派私信我（推荐方式），或者在本仓库上面的 Issues 页面中提问。

在使用前需要将本仓库的项目下载后再通过 IDE 打开。

> 注：如果是通过 ZIP 下载方式下载本项目，默认会选择主干分支（master branch），解压之后得到的目录名称会带有 `-master` 后缀，此时最好是将该后缀去掉，重名命为 `sspai-100-hours-series-python`，以便和本文中的示例代码保持一致。

## 环境依赖安装

参照教程内容安装好 Python 解释器、镜像配置以及设置相关的 IDE 之后，进入到该项目路径下，使用对应 Python 解释器的 `pip` 命令来进行安装 `requirements.txt` 文件中的依赖。

### 查看当前 Python 解释器路径

Windows：

```powershell
where.exe python3
# or where.exe python
```

macOS：

```bash
which python3
# or which python
```

### 运行 pip 命令

方式一（推荐）：通过指定 Python 解释器来运行

```bash
cd ./sspai-100-hours-series-python
python3 -m pip install -r ./requirements.txt
```

方式二：

```bash
pip install -r ./requirements.txt
```

## 项目使用

教程内容中所涉及到的 `.ipynb` 结尾的 Notebook 文件需要通过 Jupyter Notebook 打开，即在当前目录下运行如下代码启动 Jupyter 服务，然后在当中以 REPL 方式使用：

```bash
cd ./sspai-100-hours-series-python
python3 -m jupyter notebook .
# or jupyter notebook .
```

除此之外，如果是以 `.py` 结尾的 Python 代码文件，则可以直接通过 IDE 进行运行。

## LICENSE

```plain
MIT License

Copyright (c) 2022-present 100gle

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

# 《100 小时后请叫我程序员》教程源码使用说明

本仓库为少数派平台 [《100 小时后请叫我程序员》](https://sspai.com/series/271) 教程内容的相关源码、以及素材仓库，教程内的大部分示例代码都可通过对应的目录找到。

仓库地址：

- [Gitee](https://gitee.com/tinybot/sspai-100-hours-series-python)（国内）
- [Github](https://github.com/100gle/sspai-100-hours-series-python)

在使用过程中如有任何问题欢迎在少数派私信我（推荐方式），或者在本仓库上面的 Issues 页面中提问。

在使用前需要将本仓库的项目下载后再通过 IDE 打开。

## 项目下载方式

方式一：**压缩包下载**。

这种方式对于没有 Git 基础的新手而言比较方便，与环境搭建视频的操作一致。

> 注：如果是通过 ZIP 下载方式下载本项目，默认会选择主干分支（master branch），解压之后得到的目录名称会带有 `-master` 后缀，此时最好是将该后缀去掉，重名命为 `sspai-100-hours-series-python`，以便和本文中的示例代码保持一致。

缺点：无法实时获取到最新代码，如果项目有更新的地方可能需要随时重新下载。

方式二：**通过 Git 或进行仓库 Fork 之后再拉取**。

这种方式可以随时通过拉取保持与本仓库项目代码的一致，无需手动重复下载。

缺点：该方式只适用于有 Git 操作经验的读者使用。

## 关于爬虫项目的说明

教程的有两章内容涉及到爬虫：

1. 第一章：[《从一个例子开始了解编程》](https://sspai.com/post/72756)
2. 实践案例：[《使用 Scrapy 爬虫框架获取数据（下）：实战案例》](https://sspai.com/post/74246)

上述两章主要以 B 站为目标站点进行展开，但爬虫代码可能会因网站内容变动而**随时失效**，因此本人**不确保代码能一直正常运行**；而源码主要仅供读者了解思路以及相关用法的学习，望读者知悉。

**2023-01-05 更新说明**：有读者反映已无法直接运行并获取到 B 站数据，排查之后可以肯定两章内容中的 API 接口目前均已被 B 站限制访问，**所以目前代码已经失效**；如果想要代码成功运行，需要读者自行用浏览器登录 B 站之后复制 **Cookie** 信息并在请求时一同发送，第一章的示例只需要在 `HEADERS` 字典里加上即可，而 Scrapy 的综合案例需要自行编写中间件代码，可参考：<https://docs.scrapy.org/en/latest/_modules/scrapy/downloadermiddlewares/cookies.html>

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

# User Manual for "Call Me a Programmer After 100 Hours" Tutorial Source Code

This repository contains the relevant source code and assets for the [《100 小时后请叫我程序员》](https://sspai.com/series/271) (Call Me a Programmer After 100 Hours) tutorial on the sspai platform. Most of the example code from the tutorial can be found in the corresponding directories.

Repository Addresses:

- [Gitee](https://gitee.com/tinybot/sspai-100-hours-series-python) (Mainland China)
- [Github](https://github.com/100gle/sspai-100-hours-series-python)

If you encounter any problems during use, feel free to DM me on sspai (recommended) or ask questions in the Issues page of this repository.

Before use, please download the project from this repository and open it via an IDE.

## How to Download the Project

Method 1: **ZIP Download**.

This method is convenient for beginners without Git basics and is consistent with the operations in the environment setup video.

> Note: If you download this project via ZIP, the master branch is selected by default. The resulting directory name after extraction will have a `-master` suffix. It is best to remove this suffix and rename it to `sspai-100-hours-series-python` to maintain consistency with the example code in this document.

Disadvantage: You cannot get the latest code in real-time; if the project is updated, you may need to re-download it.

Method 2: **Via Git or by Forking and Pulling**.

This method allows you to maintain consistency with the repository code at any time via pulling, without the need for manual repeated downloads.

Disadvantage: This method is only suitable for readers with Git experience.

## Note Regarding Web Scraping Projects

Two chapters of the tutorial involve web scraping:

1. Chapter 1: [《Getting Started with Programming through an Example》](https://sspai.com/post/72756)
2. Practical Case: [《Using the Scrapy Framework to Get Data (Part 2): Practical Case》](https://sspai.com/post/74246)

The two chapters above primarily use Bilibili as the target site. However, scraping code may **fail at any time** due to changes in website content; therefore, I **do not guarantee that the code will always run normally**. The source code is provided primarily for readers to understand the logic and learn relevant usage.

**2023-01-05 Update**: Some readers have reported that Bilibili data can no longer be retrieved directly. After investigation, it is confirmed that the API interfaces in both chapters are currently restricted by Bilibili, **so the code is currently invalid**. To make the code run successfully, readers need to log into Bilibili via a browser, copy the **Cookie** information, and send it with the request. For the Chapter 1 example, simply add it to the `HEADERS` dictionary; for the Scrapy comprehensive case, you need to write middleware code yourself. Refer to: <https://docs.scrapy.org/en/latest/_modules/scrapy/downloadermiddlewares/cookies.html>

## Installing Environment Dependencies

After installing the Python interpreter, configuring the mirror, and setting up the relevant IDE as described in the tutorial, enter the project path and use the `pip` command of the corresponding Python interpreter to install the dependencies listed in the `requirements.txt` file.

### Check Current Python Interpreter Path

Windows:

```powershell
where.exe python3
# or where.exe python
```

macOS:

```bash
which python3
# or which python
```

### Running pip Command

Method 1 (Recommended): Run by specifying the Python interpreter

```bash
cd ./sspai-100-hours-series-python
python3 -m pip install -r ./requirements.txt
```

Method 2:

```bash
pip install -r ./requirements.txt
```

## Project Usage

Notebook files ending in `.ipynb` mentioned in the tutorial need to be opened via Jupyter Notebook. Run the following code in the current directory to start the Jupyter service, then use it in REPL mode:

```bash
cd ./sspai-100-hours-series-python
python3 -m jupyter notebook .
# or jupyter notebook .
```

Other than that, Python code files ending in `.py` can be run directly through your IDE.

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

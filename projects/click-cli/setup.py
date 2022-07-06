from setuptools import find_packages, setup

setup(
    name="watermark",
    version="0.1",
    author="100gle",
    py_modules=["watermark"],
    packages=find_packages(),
    install_requires=[
        "Click",
        "pillow",
    ],
    entry_points={
        "console_scripts": [
            "watermark=watermark.main:cli",
        ]
    },
)

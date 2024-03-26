from setuptools import setup

setup(
    name="kptgraphs",
    version="0.1",
    py_modules=["kptgraphs"],
    install_requires=[
        "matplotlib >= 3.8.3",
        "seaborn >= 0.13.2",
        "pandas >= 2.2.0",
        "numpy >= 1.26.3",
    ],
)

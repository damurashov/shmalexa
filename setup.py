from setuptools import setup
import logging

# TODO
project_name="shmalexa"
requirements = list()
description="wat?"
author="What's your name"
long_description=""
url="example.com"

with open('requirements.txt', 'r') as f:
    requirements = list(filter(lambda i: len(i) > 0, map(lambda i: i.strip(), f.readlines())))

print(f"requirements: {requirements}")

with open("README.md", 'r', encoding='utf-8') as f:
    long_description = f.read()


setup(
    name=project_name,
    packages=[
    	"shmalexa",
        "shmalexa.models",
        "shmalexa.voice",
    ],
    package_data = {
        "shmalexa.models": [
			"vosk-model-small-en-us-0.15/graph",
			"vosk-model-small-en-us-0.15/graph/disambig_tid.int",
			"vosk-model-small-en-us-0.15/graph/phones",
			"vosk-model-small-en-us-0.15/graph/phones/word_boundary.int",
			"vosk-model-small-en-us-0.15/graph/HCLr.fst",
			"vosk-model-small-en-us-0.15/graph/Gr.fst",
			"vosk-model-small-en-us-0.15/ivector",
			"vosk-model-small-en-us-0.15/ivector/global_cmvn.stats",
			"vosk-model-small-en-us-0.15/ivector/online_cmvn.conf",
			"vosk-model-small-en-us-0.15/ivector/final.mat",
			"vosk-model-small-en-us-0.15/ivector/splice.conf",
			"vosk-model-small-en-us-0.15/ivector/final.ie",
			"vosk-model-small-en-us-0.15/ivector/final.dubm",
			"vosk-model-small-en-us-0.15/README",
			"vosk-model-small-en-us-0.15/conf",
			"vosk-model-small-en-us-0.15/conf/mfcc.conf",
			"vosk-model-small-en-us-0.15/conf/model.conf",
			"vosk-model-small-en-us-0.15/am",
			"vosk-model-small-en-us-0.15/am/final.mdl",
        ],
        "shmalexa.voice": ["*.mp3"],
    },
    include_package_data=True,
    license="MIT",
    description=description,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=url,
    author=author,
    setup_requires=["wheel"],
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    version="0.0.1",
    entry_points=f"""
        [console_scripts]
        {project_name} = {project_name}.main:main
    """
)


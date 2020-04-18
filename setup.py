import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="denga",
    version="0.0.1",
    author="ankitshaw",
    author_email="ankit.india14@gmail.com",
    description="Data Augmentation for NLP Dataset using Thesaurus",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ankitshaw/DenGa",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
)

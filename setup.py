from setuptools import setup, find_packages

setup(
    name="Chat-RPG-Game",
    version="0.1.0",
    packages=find_packages(),
    author="Necraatall",
    author_email="seyuki.yamamoro@gmail.com",
    license="BEERWARE",
    install_requires=[
        "fastapi",
        "graphene",
        "graphene-sqlalchemy",
        "psycopg2-binary",
        "sqlalchemy",
        "python-dotenv"
    ],
    extras_require={
        "dev": [
            "pytest",
            "pytest-cov"
        ]
    }
)

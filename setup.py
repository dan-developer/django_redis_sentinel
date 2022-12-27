from setuptools import setup

from django_redis_sentinel import __version__

description = """
Full featured redis cache backend for Django for Sentinel Redis Clusters.
"""

setup(
    name="django-redis-sentinel-redux",
    url="https://github.com/danigosa/django-redis-sentinel-redux",
    author="Dani Gonzalez @danigosa",
    author_email="danigosa@gmail.com",
    version=__version__,
    packages=[
        "django_redis_sentinel",
        "django_redis_sentinel.client"
    ],
    description=description.strip(),
    install_requires=[
        "django-redis==4.5.0",
    ],
    zip_safe=False,
    classifiers=[
        "Development Status :: 1 - Release",
        "Environment :: Web Environment",
        "Framework :: Django :: 3.0",
        "Framework :: Django :: 4.0",
        "Framework :: Django",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Software Development :: Libraries",
        "Topic :: Utilities",
    ],
)

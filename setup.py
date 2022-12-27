from setuptools import setup

from django_redis_sentinel import __version__

description = """
Full featured redis cache backend for Django for Sentinel Redis Clusters.
"""

setup(
    name="django_redis_sentinel",
    url="https://github.com/dan-developer/django_redis_sentinel",
    author="Dan Developer",
    author_email="and.dan19@gmail.com",
    version=__version__,
    packages=[
        "django_redis_sentinel",
        "django_redis_sentinel.client"
    ],
    description=description.strip(),
    install_requires=[
        "django-redis~=5.2.0",
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

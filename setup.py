from setuptools import setup, find_packages
import pathlib
import pkg_resources

# automatically parse requirements.txt and use as install_requires
with pathlib.Path('requirements.txt').open() as requirements_txt:
    install_requires = [
        str(requirement)
        for requirement
        in pkg_resources.parse_requirements(requirements_txt)
    ]

setup(
    name='deformable-detr',
    version='1.0.0',
    packages=find_packages(),
    install_requires=install_requires,
)
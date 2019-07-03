from setuptools import setup, find_packages

setup(
    name='fundos_cvm',
    version='0.0.1',
    description='Fetch and structure fund data from CVM.',
    url='https://github.com/carlosbettin/fundos_cvm',
    author='Carlos Bettin',
    author_email='carlosalexandrebcar@gmail.com',
    license='MIT',
    packages=find_packages(
        exclude=[
            "*.tests", "*.tests.*", "tests.*", "tests",
            "*.raw", "*.raw.*", "raw.*", "raw"
            ]),
)

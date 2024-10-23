from setuptools import setup, find_packages

setup(
    name='monkey_generator',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    package_data={
        'monkey_generator': ['assets/*.svg'],  # Include SVG file
    },
    description='A simple Python package example',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Your Name',
    author_email='your_email@example.com',
    url='https://github.com/yourusername/my_python_package',  # Your repo URL
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)

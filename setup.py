from setuptools import setup, find_packages

setup(
    name='temp_tiktok',
    version='0.1',
    packages=find_packages("Components"),
    install_requires=[
        # Add your project dependencies here
    ],
    entry_points={
        'console_scripts': [
            # Add command line scripts here
        ],
    },
    author='danvt',
    author_email='nguyenvanthanhdat1810@gmail.com',
    # description='A simple description of your project',
    url='https://github.com/yourusername/temp_tiktok',
    classifiers=[
        # 'Programming Language :: Python :: 3',
        # 'License :: OSI Approved :: MIT License',
        # 'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
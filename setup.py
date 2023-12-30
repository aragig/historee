from setuptools import setup, find_packages
setup(
    name='historee',
    version='0.1.1',
    packages=find_packages(),
    description='アクション履歴を管理するPythonパッケージ',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Toshihiko Arai',
    author_email='i.officearai@gmail.com',
    license='MIT',
    url='https://github.com/aragig/historee',
    install_requires=[
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.9',
)

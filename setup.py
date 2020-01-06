from setuptools import setup, find_packages
from os.path import join, dirname


setup(
    name='gtrans',
    version='0.1',
    description='Free Google Translate API service',
    keywords='google translate api free python gtrans',
    url='https://github.com/sergei4e/gtrans',
    author='Luis Monteiro',
    author_email='monteiro.lcm@gmail.com',
    license='MIT',
    # classifiers=[
    #     'License :: OSI Approved :: MIT License',
    #     'Intended Audience :: Developers',
    #     'Programming Language :: Python :: 3.6',
    #     'Environment :: Web Environment',
    #     'Development Status :: 3 - Alpha',
    # ],
    packages=find_packages(),
    #long_description=open(join(dirname(__file__), 'README.rst')).read(),
    install_requires=[
         'selenium'
    ],
    include_package_data=True,
)

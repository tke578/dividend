from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='dividend',
	    packages=['dividend', 'dividend.parsers'],
      version='1.0.0',
      description='The Unofficial API for Dividend.com',
      long_description=long_description,
      long_description_content_type="text/markdown",
      url='http://github.com/tke578/dividend',
      author='Andrew Garcia',
      author_email='tke578@gmail.com',
      keywords = ['dividend', 'api', 'screener', 'dividend api'],
      license='MIT',
      install_requires=[
          'requests',
          'aiohttp',
      ],
      test_suite='nose.collector',
      tests_require=['nose'],
      zip_safe=False)
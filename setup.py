from setuptools import setup

setup(name='dividend',
	  packages=['dividend', 'dividend.parsers'],
      version='0.1',
      description='Unofficail API for Dividend.com',
      url='http://github.com/storborg/funniest',
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
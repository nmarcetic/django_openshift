from setuptools import setup

setup(name='django_openshift',
      version='1.0',
      description='My django app flying on openshift ',
      author='Nikola Marcetic',
      author_email='nikola.marcetic@ntsystems.rs',
      url='http://djangoapp-nmarcetic.rhcloud.com/',
      ### We must define all requirements to install_requires ###
      # My base app prod requirements!
      install_requires=['Django>=1.6.2','Markdown>=2.4','South>=0.8.4','django-appconf>=0.6','django-classy-tags>=0.4',
	  'django-compressor>=1.3','django-filter>=0.7','django-sekizai==0.7','djangorestframework==2.3.12','psycopg2==2.5.2',
      'six==1.5.2','sqlparse==0.1.11','wsgiref==0.1.2'],
     )

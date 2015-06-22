# Публикация python-пакета в PYPI.

*Подробная, пошаговая документация содержится [по этой ссылке](https://packaging.python.org/en/latest/distributing.html).*

Ниже минимально необхожимый перечень шагов, для создания пакета python и публикации его в PYPI с возможностью установки через пакетный менеджер pip.

1. Создаем проект с примерной структурой:
--------
        myapp
          |
          |-- setup.py
          |-- LICENSE
          |-- README.md  
          |-- requirements.pip
          |-- .gitignore
          |__ app
          |     |
          |     |-- __init__.py
          |     |-- ..
          |     |-- .
  
2. Пример файла setup.py:
--------

        from setuptools import setup, find_packages

        setup(
            name='myapp',
            version='0.0.1',
            url='https://github.com/path/to/project',
            license='MIT',
            author='Name',
            author_email='Email',
            description='Description',
            long_description='Description',
            platforms='any',
            packages=find_packages(),
            install_requires=[
                'some-required-lib',
                ...
            ],
            keywords='myapp, ...',
        )

3. Пример файла .gitignore:
--------

        *.py[cod]
        *.egg-info/        
        dist/
        build/

4. Создаем пакет:
--------
 
        $ pip install whell twine
        $ cp ~/path/to/root_of_project
        $ mkdir dist
        $ python setup.py sdist bdist_wheel

5. Создать аккаунт на сайте [PYPI](https://pypi.python.org/pypi).
--------


6. Создать файл ~/.pypirc:
--------

        [distutils]
           index-servers =
           pypi
        
        [pypi]
           username:<PYPI username>
           password:<PYPI password>
7. Загрузка пакета в PYPI:
--------

*Следующие команды могут предложить ввести логин и пароль, если вы не создавали файл ~/.pypirc, или создать пользователя, если у Вас еще нет аккаунта на PYPI.*

        $ python setup.py register
        $ twine upload dist/*  # или указать архив пакета с конкретной версией
        
8. Если ошибок не возникло, то можно проверить процесс установки пакета в пустом виртуальном окружении:
--------

       $ virtualenv .ve  # или воспользоваться virtualenvwrapper: mkvirtualenv test
       $ source .ve/bin/activate
       $ pip install myapp
       $ pip freeze
         myapp==0.0.1
         some-required-lib==2.7.0
         wheel==0.24.0
         
  Теперь можно запустить интерпретатор и импортировать Вашу библиотеку для использования.
   
9. Через некоторое время, когда PYPI проиндексирует Ваш новый пакет, он будет доступен для поиска:
--------

        $ pip search myapp
          myapp - Description.

10. Пример проекта:
--------
[python-ponominalu](https://github.com/abogoyavlensky/python-ponominalu)

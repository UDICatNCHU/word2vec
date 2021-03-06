from distutils.core import setup

setup(
    name = 'kem',
    packages=['kem'],
    package_dir={'kem':'kem'},
    package_data={'kem':['management/commands/*']},
    version = '4.5',
    description = 'A django App for kem',
    author = ['davidtnfsh', 'theshaneyu'],
    author_email = 'davidtnfsh@gmail.com',
    url = 'https://github.com/udicatnchu/kem',
    download_url = 'https://github.com/udicatnchu/kem/archive/v4.5.tar.gz',
    keywords = ['kem', 'gensim'],
    classifiers = [],
    license='GPL3.0',
    install_requires=[
        'simplejson',
        'gensim',
        'ngram',
        'nltk'
    ],
    zip_safe=True,
)

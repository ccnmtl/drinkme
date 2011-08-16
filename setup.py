from setuptools import setup, find_packages

setup(
    name="drinkme",
    version="0.1",
    install_requires = [
    "selector >= 0.8.11",
    "PasteScript > 0.9.7",
    "Paste > 0.9.7",
    "PasteDeploy > 0.9.7",
    ],
    zip_safe=True,
    packages=find_packages(),
    keywords = [     ],
    entry_points="""
    [paste.app_factory]
    main=drinkme.wsgiapp
    """
    )

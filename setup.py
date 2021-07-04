from distutils.core import setup

setup(
    name='i3-workflow',
    packages=['i3-workflow'],  # Chose the same as "name"
    version='1.0',  # Start with a small number and increase it with every change you make
    license='MIT',  # Chose a license from here: https://help.github.com/articles/licensing-a-repository
    description='An application to group different application together in i3wm and start them together to fasten your workflow.',  # Give a short description about your library
    author='Lukas van den Berk',  # Type in your name
    author_email='lukasvdberk@gmail.com',  # Type in your E-Mail
    url='https://github.com/lukasvdberk/i3-workflow',  # Provide either the link to your github or to your website
    download_url='https://github.com/lukasvdberk/i3-workflow/archive/refs/tags/1.0.tar.gz',  # I explain this later on
    keywords=['tool', 'window-manager', 'i3', 'i3wm'],  # Keywords that define your package best
    install_requires=[  # I get to this in a second
        'pick',
    ],
    classifiers=[
        'Development Status :: 1 - Finale',
        # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'License :: OSI Approved :: MIT License',  # Again, pick a license
        'Programming Language :: Python :: 3.9',  # Specify which python versions that you want to support
    ],
)

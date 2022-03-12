from setuptools import setup

setup(
    name='outlook',
    version='1.0.1',
    author='Tiancheng Jiao',
    author_email='jtc1246@outlook.com',
    url='https://github.com/jtc1246/outlook',
    description='A simple email sender for Outlook',
    packages=['outlook'],
    install_requires=['myHttp','mySecrets','msal'],
    python_requires='>=3',
    platforms=["all"],
    license='GPL-2.0 License',
    entry_points={
        'console_scripts': [
            'setAccount=outlook:setAccount',
            'sendEmail=outlook:sendEmail'
        ]
    }
)

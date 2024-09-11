from setuptools import find_packages, setup
 
setup(
    name='MCQGEN',
    version='0.1',
    description='Sample Python package for AI Chatbot',
    author='Akhil Passi',
    author_email='akhilpassi@gmail.com',
    # packages=['SFMC_Chatbot'],
    install_requires=[ 'langchain',
                        'langchain_huggingface',
                        'python-dotenv',
                        'streamlit'],
    packages= find_packages()
)
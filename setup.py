from setuptools import setup, find_packages

install_requires = [
    'aiohttp==3.9.5',
    'aiosignal==1.3.1',
    'annotated-types==0.7.0',
    'anyio==4.4.0',
    'asttokens==2.4.1',
    'async-timeout==4.0.3',
    'attrs==23.2.0',
    'backcall==0.2.0',
    'beautifulsoup4==4.12.3',
    'bleach==6.1.0',
    'blinker==1.8.2',
    'cachetools==5.4.0',
    'certifi==2024.7.4',
    'charset-normalizer==3.3.2',
    'click==8.1.7',
    'dataclasses-json==0.6.7',
    'decorator==5.1.1',
    'defusedxml==0.7.1',
    'distro==1.9.0',
    'docopt==0.6.2',
    'docstring_parser==0.16',
    'exceptiongroup==1.2.2',
    'executing==2.0.1',
    'fastjsonschema==2.20.0',
    'filelock==3.15.4',
    'Flask==3.0.3',
    'frozenlist==1.4.1',
    'fsspec==2024.6.1',
    'google-ai-generativelanguage==0.6.6',
    'google-api-core==2.19.1',
    'google-api-python-client==2.138.0',
    'google-auth==2.32.0',
    'google-auth-httplib2==0.2.0',
    'google-cloud-aiplatform==1.60.0',
    'google-cloud-bigquery==3.25.0',
    'google-cloud-core==2.4.1',
    'google-cloud-resource-manager==1.12.4',
    'google-cloud-storage==2.18.0',
    'google-crc32c==1.5.0',
    'google-generativeai==0.7.2',
    'google-resumable-media==2.7.1',
    'googleapis-common-protos==1.63.2',
    'greenlet==3.0.3',
    'grpc-google-iam-v1==0.13.1',
    'grpcio==1.65.1',
    'grpcio-status==1.62.2',
    'h11==0.14.0',
    'httpcore==1.0.5',
    'httplib2==0.22.0',
    'httpx==0.27.0',
    'httpx-sse==0.4.0',
    'huggingface-hub==0.24.2',
    'idna==3.7',
    'ipython==8.12.3',
    'itsdangerous==2.2.0',
    'jedi==0.19.1',
    'Jinja2==3.1.4',
    'jsonpatch==1.33',
    'jsonpickle==3.2.2',
    'jsonpointer==3.0.0',
    'jsonschema==4.23.0',
    'jsonschema-specifications==2023.12.1',
    'jupyter_client==8.6.2',
    'jupyter_core==5.7.2',
    'jupyterlab_pygments==0.3.0',
    'kafka-python==2.0.2',
    'langchain==0.2.11',
    'langchain-community==0.2.10',
    'langchain-core==0.2.23',
    'langchain-google-vertexai==1.0.7',
    'langchain-mistralai==0.1.10',
    'langchain-openai==0.1.17',
    'langchain-text-splitters==0.2.2',
    'langsmith==0.1.93',
    'MarkupSafe==2.1.5',
    'marshmallow==3.21.3',
    'matplotlib-inline==0.1.7',
    'mistune==3.0.2',
    'multidict==6.0.5',
    'mypy-extensions==1.0.0',
    'nbclient==0.10.0',
    'nbconvert==7.16.4',
    'nbformat==5.10.4',
    'numpy==1.26.4',
    'openai==1.37.1',
    'orjson==3.10.6',
    'packaging==24.1',
    'pandocfilters==1.5.1',
    'parso==0.8.4',
    'pexpect==4.9.0',
    'pickleshare==0.7.5',
    'pipreqs==0.5.0',
    'platformdirs==4.2.2',
    'prompt_toolkit==3.0.47',
    'proto-plus==1.24.0',
    'protobuf==4.25.4',
    'ptyprocess==0.7.0',
    'pure_eval==0.2.3',
    'pyasn1==0.6.0',
    'pyasn1_modules==0.4.0',
    'pydantic==2.8.2',
    'pydantic_core==2.20.1',
    'Pygments==2.18.0',
    'pyparsing==3.1.2',
    'python-dateutil==2.9.0.post0',
    'python-dotenv==1.0.1',
    'PyYAML==6.0.1',
    'pyzmq==26.0.3',
    'referencing==0.35.1',
    'regex==2024.7.24',
    'requests==2.32.3',
    'rpds-py==0.19.1',
    'rsa==4.9',
    'shapely==2.0.5',
    'six==1.16.0',
    'sniffio==1.3.1',
    'soupsieve==2.5',
    'SQLAlchemy==2.0.31',
    'stack-data==0.6.3',
    'tenacity==8.5.0',
    'tiktoken==0.7.0',
    'tinycss2==1.3.0',
    'tokenizers==0.19.1',
    'tornado==6.4.1',
    'tqdm==4.66.4',
    'traitlets==5.14.3',
    'typing-inspect==0.9.0',
    'typing_extensions==4.12.2',
    'uritemplate==4.1.1',
    'urllib3==2.2.2',
    'wcwidth==0.2.13',
    'webencodings==0.5.1',
    'Werkzeug==3.0.3',
    'yarg==0.1.9',
    'yarl==1.9.4'
]


setup(
    name='ds-service',
    version='1.0',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    install_requires=install_requires
)
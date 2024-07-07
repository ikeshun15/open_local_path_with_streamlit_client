# Open Local File with Streamlit (Client)
Please use with a [streamlit server](https://github.com/ikeshun15/open_local_path_with_streamlit_server).

## Create environment and executable file (Miniconda)
```bash
conda create --name python311_open_local_path_with_streamlit_client python=3.11
```

```bash
conda activate python311_open_local_path_with_streamlit_client
```

```bash
pip install -r requirements.txt
```

```bash
pyinstaller --onefile client_server.py
```
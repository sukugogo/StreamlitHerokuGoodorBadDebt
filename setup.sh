mkdir -p ~/.streamlit/
echo "\
[general]\n\
email = \"sukumar_gogoi@yahoo.com\"\n\
" > ~/.streamlit/credentials.toml
echo "\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\
" > ~/.streamlit/config.toml
/home/appuser/venv/bin/python -m pip install --upgrade pip

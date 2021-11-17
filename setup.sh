mkdir -p ~/.streamlit/

echo "[theme]
primaryColor = '#ff4b4b'
backgroundColor = '#000000'
secondaryBackgroundColor = '#11264c'
textColor= '#ffffff'
font = 'sans serif'
[server]
headless = true
port = $PORT
enableCORS = false
" > ~/.streamlit/config.toml
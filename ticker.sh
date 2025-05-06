python3.11 -m venv venv

source venv/bin/activate

pip install -r requirements.txt

while true; do
    clear;
    python portfolio.py
    sleep 30s;
done

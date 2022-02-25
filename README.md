# ADF-2.0 COMMAND UPDATE NOW
pkg update upgrade

pkg install git -y  python -y

pip install requests mechanize futures bs4

rm -rf ADF

git clone https://github.com/ADF1337/ADF-2.0

cd ADF-2.0

git pull

python Adf.py

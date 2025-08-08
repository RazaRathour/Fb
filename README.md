pkg update && pkg upgrade -y

pkg install git python -y

git clone https://github.com/RazaRathour/Fb.git

cd Fb

python verify.py

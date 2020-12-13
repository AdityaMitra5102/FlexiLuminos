echo "Updating apt"
sudo apt-get update
sudo apt-get upgrade
echo "Installing dependencies for Discord bot"
sudo pip3 install discord.py
echo "Installing dependencies for Telegram bot"
sudo pip3 install python-telegram-bot
echo "Installing npm"
sudo pip install npm
echo "Installing LocalTunnel"
sudo npm install -g localtunnel
echo "Installing Apache"
sudo apt install apache2 -y
echo "Starting Apache"
sudo service apache2 start
echo "Copying server files"
sudo cp -r ./html /var/www/
echo "Installing Remote SSH"
curl -s https://www.dataplicity.com/ujue6mq4.py | sudo python
echo "Compiling files"
javac Test.java
javac Server.java
javac Main.java
echo "Making executable"
sudo chmod +x run.sh
sudo chmod +x runweb.sh
sudo chmod +x main.sh
echo "Making run at startup"
sudo echo "@lxterminal --working-directory=$(pwd) -e ./main.sh" >> /etc/xdg/lxsession/LXDE-pi/autostart
sudo echo "chromium-browser -noerrors --disable-session-crashed-bubble --disable-restore-session-state --disable-insfobars localhost" >> /etc/xdg/lxsession/LXDE-pi/autostart
echo "Rebooting Device"
sudo reboot

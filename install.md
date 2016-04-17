# CARA INSTALASI

Silahkan untuk mengikuti langkah-langkah berikut ini secara berurutan :

1. install [python] (https://www.python.org), `gunakan versi 2.7.x`
2. install [python-pip] (https://pip.pypa.io/en/stable/installing/)
3. install [RPi-GPIO](http://www.raspberrypi-spy.co.uk/2012/05/install-rpi-gpio-python-library/) pada raspberry pi, untuk development windows/mac saat ini ditulis belum ada versinya (linux belum coba)
4. install modul requests (diperlukan diproject), dengan mengetikkan perintah ```pip install requests```
5. install [mongodb](https://mongodb.org) , untuk raspberry silahkan ikuti [langkah-langkah ini.](http://c-mobberley.com/
wordpress/2013/10/14/raspberry-pi-mongodb-installation-the-working-guide/), setelah instalasi di terminal silahkan jalankan perintah ```mongo```, apabila belum bisa silahkan jalankan perintah ini ```export PATH=$PATH:/opt/mongo/bin``` (sesuaikan pathnya, gunakan ```whereis mongo``` untuk mengetahui path mongo)
6. install [PyMongo](https://docs.mongodb.org/getting-started/python/client/) ```pip install pymongo```
7. jalankan ``` python install.py ```
8. install gpio library, dengan mengetikkan perintah ```pip install RPi.GPIO```
9. install [C++ Distribute Package](https://www.microsoft.com/en-us/download/details.aspx?id=44266) (windows)

# Python ICS and VspyX installation

## Install ICS software on pi

### About

This is a shell script that will install the following:

1. ICS python library: [python-ics docs](https://python-ics.readthedocs.io/en/master/)
2. VspyX python library: [vspyx docs](https://docs.intrepidcs.net/vspyx/release/intro.html)
3. All required dependencies for controlling the membrane using python: [membrane example for python](../control-membrane-leds-and-trigger-button.md)

### Running the install script

#### 1. Download the install\_script.zip file attached and unzip it in the PI's home directory.

Run `ls` in your home directory to make sure you can see `install_ics.sh` and `requirements.txt`

{% file src="../.gitbook/assets/install_script.zip" %}

#### 2. Run the install script

In your terminal window run the following 2 commands:

```
sudo chmod +x $HOME/install_ics.sh
./install_ics.sh
```

It could take up to 20 minutes to complete.

If you see `"Licensing error! Please place a valid license in /home/pi/.vspyx/Licenses"` then the install was successful.

### Usage

There are two ways of using the environment. First one is to activate it with pyenv:

```
pyenv activate vspyx_env
```

Then just use `python myscript.py`.

The second way to use it without activating the environment but still using it:

```
sudo $HOME/.pyenv/versions/vspyx_env/bin/python myscript.py
```

To use VspyX you will need a valid licence from ICS, so if you do not have one please contact [ICS support](mailto:icssupport@intrepidcs.com).

ICS-python is free to use without any licenses.

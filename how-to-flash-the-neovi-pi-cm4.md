# How to flash the neoVI PI CM4

### 4. How to flash the neoVI PI CM4

This step by step guide will walk you through how to flash the CM4, overclock and run supertuxkart on it. Steps 1 - 4 are flashing and programming the CM4. Steps 5 and 6 are installing supertuxkart.

**Step 1. Getting the Hardware Ready**

The first thing we need to do is prepare the neoVI-Pi for flashing. Plug in a CM4 module underneath the motherboard. Make sure the holes line up because you can plug them in backwards. Press hard so that both connectors make a distinct click sound. The metal standoffs on the motherboard should look like they are touching the CM4. Then we need to flip it back over and turn switch number 5 on the dip switch to the “ON” position. See image below.

{% hint style="info" %}
#### **Note:** Connect the IO board to the RPI using the microUSB cable. This step is only necessary if you have purchased the IO board and RPI separately. If you have purchased the entire package, skip to step 2
{% endhint %}

**Step 2. Installing Necessary Software**

If you already have the required software, then skip this step and move to step 3. We need to install 2 programs onto whatever computer you are using to flash the PI. The first program is RPIboot.exe. This program is needed to tell windows that we want to use the Pi as a storage device. The Second program we need to install is RPI Imager. This is where we chose an OS, and set the settings on our PI. Links to software below.

RPIboot.exe: [https://www.raspberrypi.com/documentation/computers/compute-module.html](https://www.raspberrypi.com/documentation/computers/compute-module.html)

{% hint style="info" %}
#### Note: If you are having trouble with your keyboard and mouse not working during the setup process, this may be because the microUSB port being used by the RPI is disabling the USB 2.0 ports that are used to connect your peripherals. To fix this issue, connect your keyboard and mouse to the USB 3.0 ports instead.
{% endhint %}

**Windows Installer**

For those who just want to enable the Compute Module eMMC as a mass storage device under Windows, the stand-alone installer is the recommended option. This installer has been tested on Windows 10 32-bit and 64-bit, and Windows XP 32-bit.

Please ensure you are not writing to any USB devices whilst the installer is running.

1. Download and run the [Windows installer](https://github.com/raspberrypi/usbboot/raw/master/win32/rpiboot\_setup.exe) to install the drivers and boot tool.
2. Plug your **host PC USB** into the **USB SLAVE port**, making sure you have setup the board as described above.
3. Apply power to the board; Windows should now find the hardware and install the driver.
4. Once the driver installation is complete, run the `RPiBoot.exe` tool that was previously installed.
5. After a few seconds, the Compute Module eMMC will pop up under Windows as a disk (USB mass storage device).

Raspberry Pi Imager: [https://www.raspberrypi.com/software/](https://www.raspberrypi.com/software/)

**Step 3. Flashing the Raspberry Pi.**

Once you have the software installed, flashing the PI is easy. Take a USB cable and plug in neoVI-Pi to your computer via its micro usb port. Plug in DC power to the barrel jack as well. Once it's plugged in, run RPIboot.exe. The CMD terminal will come up and run a script. Once it's done it will close (only a few seconds). Once the terminal closes the Pi will look like a storage device on windows. Then, we want to open up the Raspberry Pi Imager to flash the OS. For the operating system, we want Raspberry Pi OS (64 bit). This OS can be found in the “Other” dropdown menu. In the “Storage” option click on your raspberry pi. Then the last thing is settings (Gear Icon). This is where you can set local passwords and permissions. This can be left alone. Once all of that is set, you can click “Write” and the computer will start flashing the OS onto Pi. This will take a while.

<figure><img src=".gitbook/assets/md-bfd602be71b2c1099b91877aed3b41f0.png" alt=""><figcaption></figcaption></figure>

**Step 4. Enabling USB ports and Overclocking**

By default, the CM4 has the USB ports disabled, so we need to enable them. Once the CM4 is done flashing, it will automatically eject. Don't worry if you get any weird errors from windows saying the device needs to be formatted. Don’t format it, just click OK or the red X. Since it ejects, we need to unplug and plug it back in (power or USB, doesn't matter). Since we unplugged it though we need to run RPIBoot.exe again. After we run RPIboot, go into file explorer and find the CM4. Inside the CM4 find the file named “config.txt”. To enable USB ports, copy and paste the following line into the file:

dtoverlay=dwc2,dr\_mode=host

To overclock the PI (Do this if running supertuxkart) paste these lines into the same file:

arm\_freq=2040&#x20;

gpu\_freq=750&#x20;

over\_voltage=6

It doesn't matter where you paste them in the file so long as it's a new line. I personally like to paste them in the “Additional Overlays” section to stay organized. Once you’ve pasted what you needed to, save the file and eject the PI.

**Step 5. Connect Pi to Wifi**

Some CM4’s have the ability to connect to wifi without needing to do anything, some do not. If you have a wireless CM4 you can pair it to wifi like any other device. If your CM4 is not wireless you can use a USB wifi adapter or plug into it via ethernet.

**Step 6. Installing supertuxkart**

Open the pi terminal and run this series of commands. Once you are done supertuxkart will be installed.

```bash
sudo apt update
sudo apt install snapd
```

```bash
sudo reboot
```

```bash
sudo snap install core
```

```bash
sudo snap install supertuxkart
```

Restart the Pi again after supertuxkart installs.

**Step 7. GPU Memory dedication**

Since we want the game to run as smoothly as possible, we want to dedicate memory to the GPU. To do this, go into the Pi terminal and type the command: sudo raspi-config. It will bring you to a blue menu that is navigable with the arrow keys. Go to performance options and the GPU memory. Delete 64 and put 1024. Then finish and reboot.

**Notes for Supertuxkart:**

* In the graphics tab in settings turn graphics down all the way, and geometry detail to disabled.&#x20;
* Turn full screen on&#x20;
* Avoid fish level&#x20;
* Avoid levels with detail
* Don’t need to make an online account to play together over Meteors or LAN. Just need to enable internet connection in the game’s settings. (It's just a checkbox)

# Control membrane LEDs and Trigger Button

### 7. Control membrane LEDs and Trigger Button

<figure><img src=".gitbook/assets/Image_20230713_153642_753.jpeg" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
**Note -** (if you have followed the [Software setup](software-setup/) page you can skip this step)
{% endhint %}

Before you can address the membrane, you will need to activate the `i2c_vc` interface. To do that you need to run the following command:

<pre class="language-sh" data-overflow="wrap"><code class="lang-sh"><strong>echo "dtparam=i2c_vc=on" | sudo tee -a /boot/config.txt
</strong></code></pre>

After this you need to reboot the pi, `sudo reboot` will do the job.

#### Download the below file to control membrane LEDs and trigger buttons.

{% file src=".gitbook/assets/membrane.py" %}

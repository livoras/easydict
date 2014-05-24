easydict
========

The simplest dictionary on Linux, only for Chinese so far. 

It actually looks up dictionary of [Youdao](http://www.youdao.com/) which is a widely used online dictionary and application for desktop as well(for Chinese). 

There is a similar application called [openyoudao](https://github.com/justzx2011/openyoudao/) for linux which as well depends on youdao's resources and provides much more funtionalites. If you want more fancy abilities, I strongly recommand you to use it althought I failed to install it on my system so made me come up with this `easydict` idea.

For it was my first trial on GUI application of Linux. I have tried hard to make it work and bug free. But eventually I made it work but not bug free. But its codes are will structed, you can learn something from codes (if you are a pyhon programmer), instead of the benifits to which it originally aim at delivering.

I make no attempts to maintain it anymore. Maybe the excitements, if any, coming up again, will make me continue to enhance it. 

## Installation

Easydict depends on `Xlib` for interaction with X system of linux and on `GTK` for GUI supports. So, at first, you need to install thrid libraries of both of them in python, throught `apt-get` and `pip`.

```
  sudo apt-get install python-xlib && sudo pip install pygtk
```

If pip is not installed on your system you have to install it first.

```
  sudo apt-get install pip
```

After those preparetions, now, install `easydict`.

```
  git clone git@github.com:livoras/easydict.git
  cd easydist
  sudo python setup.py install
```

You can run it using `easydict`.

```
  easydict
```

## TODOS

* Make it bug free
* Enhance user experience.
* Translate 2 spaces to 4 spaces.
* Fill codes with commenets!

## License
GPL v2

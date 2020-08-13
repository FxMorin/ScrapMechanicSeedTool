![GUI](https://github.com/fxmorin/ScrapMechanicSeedTool/blob/master/icon.ico)

# ScrapMechanicSeedTool

This tool was designed for scrap mechanic v0.4.0+ (Tested on v0.4.0-v0.4.7)
So that we could easily share good map seeds by allowing others to view/modify map seeds.
**This is untested with creative saves, tool was created for survival saves**

---

### GUI
The seed tool has a graphical user interface, so that people without any programming knowledge can easily modify save seed's!


![GUI](https://github.com/fxmorin/ScrapMechanicSeedTool/blob/master/img/GUI.PNG)

---

### How to use SMST

Download the ScrapMechanicSeedTool.py
Then run python3 ScrapMechanicSeedTool.py

---

### Options

**Current Seed** - This is the seed that will be used for all other options

**Seed to use / Set seed** - This is where you can change the current seed manually

**Extract seed from save file** - This option will prompt you to choose a save file so that it can set the current seed to the seed of the map

**Modify world gen seed to be constant** - This options sets the seed of ALL newly generated worlds to the Current Seed. Use this option to create a world with a specific seed!!

**Reset world gen to default** - This option will reverse the effects of modifying the world gen seed, so that it will no longer be constant.

**Inject seed into save file** - This option allows you to modify the seed of a save file. I added this features since dev tools give you the /recreate command which resets the world. I believe the seed is still being used for that command, I will attempt to try a bunch of different ideas. I would like to mention that I have no idea if changing the seed of the world after its already been generated works, this was added as an extra feature for testing purposes.

---

##### Hope you all enjoy this very small tool

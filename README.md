# Forbidden Advantage

ZMK config for [my hand-wired Kinesis Advantage 2 using a subset of the
keys](https://resolved.ch/projects/forbidden_advantage.html) and a RP2040
microcontroller. 

## Building

The Elite-Pi is compatible with the Sparkfun Pro Micro RP2040. To locally build
it:

``` sh
west build -s zmk/app -b sparkfun_pro_micro_rp2040 -- -DZMK_CONFIG=/home/pascal/git/forbidden-advantage/config/ -DSHIELD="forbidden_advantage"
```

## Flashing

Put the elite-pi into bootloader, mount it and copy the uf1 file
(`build/zephyr/zmk.uf2`) onto it.

## Ideas

 - double tap shift for all_caps word [Caps Word](https://zmk.dev/docs/behaviors/caps-word)


## Resources

 - [Callum's layout](https://github.com/callum-oakley/keymap)
 - [AlaaSaadAbdo's config](https://github.com/AlaaSaadAbdo/zmk-config)
 - [rafaelromao keymap](https://github.com/rafaelromao/keyboards)



#!/usr/bin/env python

# Este script es sólo un esqueleto y necesita muchas muchas modificaciones para funcionar.
# Lo tengo sólo como ejemplo.

import usb.core
import usb.util

# Encuentra el Vorago MO-404
dev = usb.core.find(idVendor=0x1d57, idProduct=0xfa0a)

# Desconecta del kernel
dev.detach_kernel_driver(1)
usb.util.claim_interface(dev,1)
dev.set_interface_altsetting(interface=1,alternate_setting=0)

# Blink on/off
blink = [0x00, 0x00, 0xFF]

# concatenate the colours into the expected 8 bytes
data = [0x07, 0x0a, 0x01, 0x00] + colors + [0x00]

# send the data to the mouse
dev.ctrl_transfer(bmRequestType=0x21, bRequest=0x09, wValue=0x0307, wIndex=0x0001, data_or_wLength=data,timeout=1000)

# reclaim the device
usb.util.release_interface(dev,1)
dev.attach_kernel_driver(1)

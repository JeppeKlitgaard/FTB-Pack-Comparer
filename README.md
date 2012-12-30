FTB-Pack-Comparer
=================

Generates an CSV file for importing to Google Docs containing a comparison of the different FTB packs.


"Official" google docs page: https://docs.google.com/spreadsheet/pub?key=0AoBvEi8Kl59JdDN4SFdIS3ZJNDAtekZPWEYxU083RGc&single=true&gid=0&output=html


Setup
=====
* Generate a csv file by executing `python compare.py`
* Go to docs.google.com, create a new spreadsheet. With seperator: "_"
* Select all the fields (press the little square between "1" and "a" field.)
* Set font size to 18.
* Right click -> Conditional formatting
* Make 2 rules, they have to be exactly "YES" and "NO", "YES" should have green color, "NO" should have red color.
* Profit.

This tutorial is extremely sloppy, but I don't expect anyone to use this except me, so that's fine!

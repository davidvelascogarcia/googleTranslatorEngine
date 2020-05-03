[![googleTranslatorEngine Homepage](https://img.shields.io/badge/googleTranslatorEngine-develop-orange.svg)](https://github.com/davidvelascogarcia/googleTranslatorEngine/tree/develop/programs) [![Latest Release](https://img.shields.io/github/tag/davidvelascogarcia/googleTranslatorEngine.svg?label=Latest%20Release)](https://github.com/davidvelascogarcia/googleTranslatorEngine/tags) [![Build Status](https://travis-ci.org/davidvelascogarcia/googleTranslatorEngine.svg?branch=develop)](https://travis-ci.org/davidvelascogarcia/googleTranslatorEngine)

# Google Translator Engine: googleTranslatorEngine (Python API)

- [Introduction](#introduction)
- [Running Software](#running-software)
- [Requirements](#requirements)
- [Status](#status)
- [Related projects](#related-projects)


## Introduction

`googleTranslatorEngine` module use `Google Translator` API in `python`. This module receive text to translate with `YARP` port, send request to `Google Translator` server and publish results with `YARP` port.


## Running Software

`googleTranslatorEngine` requires text like input.
The process to running the program:

1. Execute [programs/googleTranslatorEngine.py](./programs), to start de program.
```python
python googleTranslatorEngine.py
```
2. Connect data source.
```bash
yarp connect /yourport/data:o /googleTranslatorEngine/data:i
```

NOTE:

- Data results are published on `/googleTranslatorEngine/data:o`

## Requirements

`googleTranslatorEngine` requires:

* [Install YARP 2.3.XX+](https://github.com/roboticslab-uc3m/installation-guides/blob/master/install-yarp.md)
* [Install pip](https://github.com/roboticslab-uc3m/installation-guides/blob/master/install-pip.md)
* Install Google Translator:
```bash
pip install googletrans
```

Tested on: `windows 10`, `ubuntu 14.04`, `ubuntu 16.04`, `ubuntu 18.04`, `lubuntu 18.04` and `raspbian`.


## Status

[![Build Status](https://travis-ci.org/davidvelascogarcia/googleTranslatorEngine.svg?branch=develop)](https://travis-ci.org/davidvelascogarcia/googleTranslatorEngine)

[![Issues](https://img.shields.io/github/issues/davidvelascogarcia/googleTranslatorEngine.svg?label=Issues)](https://github.com/davidvelascogarcia/googleTranslatorEngine/issues)

## Related projects

* [Googletrans: docs](https://pypi.org/project/googletrans/)


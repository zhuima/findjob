#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import ConfigParser

work_dir = os.path.dirname(os.path.realpath(__file__))


def get_config(section=''):
    config = ConfigParser.ConfigParser()
    service_conf= os.path.join(work_dir, 'config/myservice.conf')
    config.read(service_conf)

    conf_items = dict(config.items('common')) if config.has_section('common') else {}
    if section and config.has_section(section):
        conf_items.update(config.items(section))
    return conf_items


if __name__ == "__main__":
    print get_config('common')

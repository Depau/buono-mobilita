#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from multiprocessing import Pool
from datetime import datetime

import pytz

tz = pytz.timezone("Europe/Rome")


def parallel_convert(line: str) -> str:
    tstamp, val = line.strip().split(",")
    return ",".join([datetime.fromtimestamp(float(tstamp), tz).isoformat(), val]) + '\n'


if __name__ == "__main__":
    pool = Pool(12)
    with open("bonus_mobilita_raw.csv") as raw:
        with open("bonus_mobilita.csv", "w") as iso:
            iso.writelines(pool.imap(parallel_convert, raw.readlines(), 1024))

# !/usr/bin/env bash

# TL;DR
# This script was created because the "standard" parsing in shcmd-arguments.sh fails with globbing.
# i.e if I want to pass a glob pattern as argument, shcmd-arguments.sh will expand the pattern before
# it reaches the case statement

# Moreover, the following code is both compact and more predictable
# Notes:
# 1. shlex.quote(str) returns a valid shell string (i.e. escapes " and ' in the string")
# 2. vars(type) returns type.__dict__. the latter contains the public args of type.

set -Ee
if (( "${BASH_VERSINFO[0]}" > 3 )); then
    set -o pipefail
fi

eval "$(python - "$@" << 'PY'
import argparse
import shlex

apsr = argparse.ArgumentParser()
apsr.add_argument("--profile-path", "-p", type=str)
args = apsr.parse_args()

assignments = [f"{name}={shlex.quote(value or '')}" for name, value in vars(args).items()]
print(*assignments, sep=" ")
PY
)"


# args are herein available as env variables
python << PY
import json
import yaml
from vscode_settings import utilities as utl

with open("$profile_path") as fd:
    res = json.load(fd)
    print(
        yaml.dump(
            [json.loads(res[key], cls=utl.MyDecoder) for key in res.keys()], 
            Dumper=utl.LiteralDumper
        )
    )

PY
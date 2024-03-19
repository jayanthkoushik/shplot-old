#!/usr/bin/env python3

import subprocess
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("-r", "--release-version", nargs="?", type=str)
parser.add_argument("-p", "--pre-release", type=str, choices=["true", "false"])
parser.add_argument("-t", "--pre-release-tag", nargs="?", type=str)
parser.add_argument("--dry-run", action="store_true")
args = parser.parse_args()

cmd_version_args = []
if args.release_version:
    cmd_version_args = ["-r", args.release_version]

pre_release_args = []
if args.pre_release == "true":
    pre_release_args = ["-p"]
    if args.pre_release_tag:
        pre_release_args.append(args.pre_release_tag)

dry_run_args = []
if args.dry_run:
    dry_run_args = ["--dry-run"]

cmd = [
    "npx",
    "commit-and-tag-version",
    *cmd_version_args,
    *pre_release_args,
    *dry_run_args,
]
print(f"+ {' '.join(cmd)}")
subprocess.run(cmd, check=True)

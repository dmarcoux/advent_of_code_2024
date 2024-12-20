# <a href="https://github.com/dmarcoux/advent_of_code_2024">dmarcoux/advent_of_code_2024</a>

Solving the problems from [Advent of Code 2024](https://adventofcode.com/2024)
with [Python](https://www.python.org/).

## Python Development Environment with Nix Flakes

Reproducible development environment for Python projects which relies on
[Nix](https://github.com/NixOS/nix) [Flakes](https://nixos.wiki/wiki/Flakes),
a purely functional and cross-platform package manager.

In addition, it is optional, but _highly recommended_ to install
[direnv](https://direnv.net/) and [setup its shell
hook](https://direnv.net/docs/hook.html) to automatically enable the development
environment when navigating to this project's root directory.

Refer to the [Makefile](./Makefile) to see various commands, like starting the
development environment or formatting the code.

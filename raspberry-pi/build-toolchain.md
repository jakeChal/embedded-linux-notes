# Building a RPi toolchain with crosstool-ng

For more high-level instructions on toolchains and for the `crosstool-ng` installation steps, go [here](../toolchains/README.md).

This guide is for Raspberry Pi 4, but you can get the gist of how to set it up for older/newer (?) raspberry boards.

- `cd` in the (already configured) crosstool-ng repo
- We're gonna use this configuration `aarch64-rpi4-linux-gnu`. To check which version of which component it has:
    ```
    $ ./ct-ng show-aarch64-rpi4-linux-gnu
    Languages       : C,C++
    OS              : linux-6.4
    Binutils        : binutils-2.40
    Compiler        : gcc-13.2.0
    C library       : glibc-2.38
    Debug tools     : gdb-13.2
    Companion libs  : expat-2.5.0 gettext-0.21 gmp-6.2.1 isl-0.26 libiconv-1.16 mpc-1.2.1 mpfr-4.2.1 ncurses-6.4 zlib-1.2.13 zstd-1.5.5
    Companion tools :
    ```
- Select it as a baselinen configuration:
    ```
    $ ./ct-ng aarch64-rpi3-linux-gnu
    ```

- Customize the configuration with `menuconfig` menu and save it:

    ```
    $ ./ct-ng menuconfig
    ```

    - Allow extending the toolchain after it is created (by default, it is created as read-only):  
    `Paths and misc options -> Render the toolchain read-only ->false`

- Build the toolchain (NOTE: this can easily take 30 minutes - depends how powerful your machine is):
    ```
    $ ./ct-ng build
    ```

- Add the toolchain to your PATH:
    ```
    $ PATH=$PATH:~/x-tools/aarch64-rpi4-linux-gnu/bin
    ```
- Test it! Compile a simple program with your freshly baked toolchain:

    ``` c
    #include <stdio.h>

    int main() {

        printf("Hello world \n");
        return 0;
    }
    ```

    ```
    $ aarch64-rpi4-linux-gnu-g++ hello_world.cpp -o hello_world
    ```
    and copy it to the board (e.g. via `scp`)
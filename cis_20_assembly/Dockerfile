FROM arm32v7/debian:bullseye

# Tools for building & debugging
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential gdb make ca-certificates \
 && rm -rf /var/lib/apt/lists/*

WORKDIR /work

COPY ./lab_1/helloWorldMain.s /work/

# defaults for Raspberry Pi 2/3/4 (ARMv7, hard-float)
ENV CFLAGS="-O2 -march=armv7-a -mfpu=neon-vfpv4 -mfloat-abi=hard" \
    CC="gcc"

# Compile at build time
RUN $CC $CFLAGS helloWorldMain.s -o helloWorld

# Drop into a shell by default
CMD ["bash"]

# ============================================
# 1. line 10: Change file name and path
# 2. line 17: Change file and executable name

# Build the image
# docker build -t arm-assembly .

# Run the program in the container
# docker run --rm arm-assembly ./helloWorld
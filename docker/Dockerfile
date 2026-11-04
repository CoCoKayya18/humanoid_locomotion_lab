FROM osrf/ros:jazzy-desktop

ENV DEBIAN_FRONTEND=noninteractive
ENV ROS_DISTRO=jazzy
WORKDIR /workspace
SHELL ["/bin/bash", "-lc"]

RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
    build-essential \
    cmake \
    git \
    libgl1 \
    libgl1-mesa-dev \
    libglu1-mesa \
    libosmesa6 \
    pkg-config \
    python3 \
    python3-dev \
    python3-venv \
    python3-pip \
    python3-colcon-common-extensions \
    python3-empy \
    python3-numpy \
    python3-vcstool \
    vim \
    wget \
    xvfb \
    && rm -rf /var/lib/apt/lists/*

RUN python3 -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
RUN pip install --no-cache-dir --upgrade pip setuptools wheel && \
    pip install --no-cache-dir mujoco mujoco-menagerie

COPY docker/entrypoint.sh /usr/local/bin/entrypoint.sh
RUN chmod +x /usr/local/bin/entrypoint.sh

ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]
CMD ["bash"]

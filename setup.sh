#!/bin/sh

yum -y install https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm
yum -y localinstall \
    --nogpgcheck \
    https://download1.rpmfusion.org/free/el/rpmfusion-free-release-7.noarch.rpm \
    https://download1.rpmfusion.org/nonfree/el/rpmfusion-nonfree-release-7.noarch.rpm
yum -y update

yum -y groupinstall 'Development Tools'
yum -y install \
    libcurl-devel \
    openssl-devel \
    python34 \
    python34-devel \
    python34-numpy \
    python34-pip \
    python34-pycurl \
    cmake \
    gtk2-devel \
    libdc1394-devel \
    libv4l-devel \
    ffmpeg-devel \
    gstreamer-plugins-base-devel \
    lippng-devel \
    libjpeg-turbo-devel \
    jasper-devel \
    openexr-devel \
    libtiff-devel \
    libwebp-devel \
    tbb-devel \
    eigen3-devel \
    && echo all done!

######UNCOMMENT IF YOU WANT TO COMPILE ON YOUR SERVER OR LOCAL MACHINE#########
#if test ! -f /tmp/opencv.zip
#then
#    curl -LSso /tmp/opencv.zip https://github.com/opencv/opencv/archive/3.4.3.zip
#    cd /tmp
#    unzip opencv.zip
#fi
#cd /tmp/opencv-3.4.3
#mkdir -p build
#cd build
#cmake \
#    -D CMAKE_BUILD_TYPE=RELEASE \
#    -D CMAKE_INSTALL_PREFIX=/usr/local \
#    ..
#make
#make install


cd /home/centos/Videosearch-Python

pip3 install --upgrade pip
pip3 install -r requirements.txt

mv lib64/* /usr/local/lib64/

echo 'export PYTHONPATH=/usr/local/lib/python3.4/site-packages' > /etc/profile.d/opencv.sh

# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.box = "centos/7"

  config.vm.provision "shell", inline: <<-SHELL
    set -ex
    yum -y install epel-release
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

#    if test ! -f /tmp/opencv.zip
#    then
#      curl -LSso /tmp/opencv.zip https://github.com/opencv/opencv/archive/3.4.3.zip
#      cd /tmp
#      unzip opencv.zip
#    fi
#    cd /tmp/opencv-3.4.3
#    mkdir -p build
#    cd build
#    cmake \
#      -D CMAKE_BUILD_TYPE=RELEASE \
#      -D CMAKE_INSTALL_PREFIX=/usr/local \
#      ..
#    make
#    make install
#    echo 'export PYTHONPATH=/usr/local/lib/python3.4/site-packages' > /etc/profile.d/opencv.sh

    pip3 install --upgrade pip

    cd /vagrant
    pip3 install -r requirements.txt
  SHELL
end

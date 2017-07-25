Name:           ros-jade-grid-map-core
Version:        1.5.2
Release:        0%{?dist}
Summary:        ROS grid_map_core package

Group:          Development/Libraries
License:        BSD
URL:            http://github.com/ethz-asl/grid_map
Source0:        %{name}-%{version}.tar.gz

Requires:       eigen3-devel
BuildRequires:  eigen3-devel
BuildRequires:  ros-jade-catkin

%description
Universal grid map library to manage two-dimensional grid maps with multiple
data layers.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/jade" \
        -DCMAKE_PREFIX_PATH="/opt/ros/jade" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/jade

%changelog
* Tue Jul 25 2017 Péter Fankhauser <pfankhauser@ethz.ch> - 1.5.2-0
- Autogenerated by Bloom

* Tue Jul 25 2017 Péter Fankhauser <pfankhauser@ethz.ch> - 1.5.1-0
- Autogenerated by Bloom

* Tue Jul 18 2017 Péter Fankhauser <pfankhauser@ethz.ch> - 1.5.0-0
- Autogenerated by Bloom

* Tue Jan 24 2017 Péter Fankhauser <pfankhauser@ethz.ch> - 1.4.2-0
- Autogenerated by Bloom

* Sun Oct 23 2016 Péter Fankhauser <pfankhauser@ethz.ch> - 1.4.1-0
- Autogenerated by Bloom

* Mon Aug 22 2016 Péter Fankhauser <pfankhauser@ethz.ch> - 1.4.0-0
- Autogenerated by Bloom

* Tue May 10 2016 Péter Fankhauser <pfankhauser@ethz.ch> - 1.3.1-0
- Autogenerated by Bloom

* Tue Apr 26 2016 Péter Fankhauser <pfankhauser@ethz.ch> - 1.3.0-0
- Autogenerated by Bloom

* Thu Mar 03 2016 Péter Fankhauser <pfankhauser@ethz.ch> - 1.2.0-0
- Autogenerated by Bloom

* Mon Jan 11 2016 Péter Fankhauser <pfankhauser@ethz.ch> - 1.1.3-0
- Autogenerated by Bloom

* Mon Jan 11 2016 Péter Fankhauser <pfankhauser@ethz.ch> - 1.1.2-0
- Autogenerated by Bloom

* Mon Jan 11 2016 Péter Fankhauser <pfankhauser@ethz.ch> - 1.1.1-0
- Autogenerated by Bloom

* Fri Jan 08 2016 Péter Fankhauser <pfankhauser@ethz.ch> - 1.1.0-0
- Autogenerated by Bloom


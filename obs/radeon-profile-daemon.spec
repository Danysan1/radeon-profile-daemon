Name: radeon-profile-daemon
Url: https://github.com/marazmista/radeon-profile-daemon
License: GPLv2+
Group: System/Monitoring
AutoReqProv: on
Version: 1
Release: 2%{?dist}
Summary: Systemd service for radeon-profile
Source0: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-build

%if 0%{?suse_version}
BuildRequires: libqt5-qtbase-devel
Requires: libqt5-qtbase
%else
BuildRequires: qt5-qtbase-devel
Requires: qt5-qtbase
%endif

BuildRequires: make
BuildRequires: gcc-c++

Requires: radeon-profile

%description
System daemon for reading info about GPU clocks and volts and pass this data to radeon-profile so the GUI application can be run as normal user.

%prep
%setup -q

%build
CFLAGS="%{optflags}"
CXXFLAGS="%{optflags}"
mkdir -p build
cd build
qmake-qt5 ../radeon-profile-daemon
make

%install
install -Dm755 "build/radeon-profile-daemon" "%{buildroot}%{_bindir}/radeon-profile-daemon"
install -Dm644 "radeon-profile-daemon/extra/radeon-profile-daemon.service" "%{buildroot}%{_unitdir}/radeon-profile-daemon.service"

%post -p /sbin/ldconfig  
   
%postun -p /sbin/ldconfig  

%files
%{_bindir}/radeon-profile-daemon
%{_unitdir}/radeon-profile-daemon.service

%changelog
* Fri Jan 29 2016 danysan95@gmail.com
- Port of package to OBS

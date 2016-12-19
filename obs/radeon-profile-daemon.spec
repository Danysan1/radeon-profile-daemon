Name: radeon-profile-daemon
Url: https://github.com/marazmista/radeon-profile-daemon
License: GPL-2.0
Group: System/Monitoring
AutoReqProv: on
Version: 1
Release: 2%{?dist}
Summary: Systemd service for radeon-profile
Source0: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-build

%if 0%{?rhel}
BuildRequires: libjpeg-turbo-devel qt-devel
Requires: qt4
%else

%if 0%{?suse_version}
BuildRequires: libqt5-qtbase-devel
Requires: libqt5-qtbase

%if 0%{?suse_version} >= 1210
BuildRequires: systemd-rpm-macros
%endif

%else
BuildRequires: qt5-qtbase-devel
Requires: qt5-qtbase
%endif

%endif

BuildRequires: make
BuildRequires: gcc-c++

Requires: radeon-profile
%{?systemd_requires}

%description
System daemon for reading info about GPU clocks and volts and pass this data to radeon-profile so the GUI application can be run as normal user.

%prep
%setup -q

%build
cd radeon-profile-daemon
# https://en.opensuse.org/openSUSE:Build_system_recipes#qmake
qmake-qt5 radeon-profile-daemon.pro QMAKE_CXXFLAGS+="%optflags" QMAKE_STRIP="/bin/true" || qmake-qt4 radeon-profile-daemon.pro QMAKE_CXXFLAGS+="%optflags" QMAKE_STRIP="/bin/true"
make

%install
cd radeon-profile-daemon
install -Dm755 "radeon-profile-daemon" "%{buildroot}%{_bindir}/radeon-profile-daemon"
install -Dm644 "extra/radeon-profile-daemon.service" "%{buildroot}%{_unitdir}/radeon-profile-daemon.service"

# https://en.opensuse.org/openSUSE:Systemd_packaging_guidelines#Register_systemd_unit_files_in_install_scripts
# These macros seem to be creating problems to Fedora installation

#%pre
#%service_add_pre radeon-profile-daemon.service

#%post
#%service_add_post radeon-profile-daemon.service

#%preun
#%service_del_preun radeon-profile-daemon.service

#%postun
#%service_del_postun radeon-profile-daemon.service

%files
%{_bindir}/radeon-profile-daemon
%{_unitdir}/radeon-profile-daemon.service

%changelog
* Fri Jan 29 2016 danysan95@gmail.com
- Port of package to OBS

* Wed May 14 2014 marazmista@gmail.com
- Initial commit

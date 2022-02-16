%global debug_package %{nil}

Name: hwdata
Epoch: 100
Version: 0.359
Release: 1%{?dist}
Summary: Hardware identification and configuration data
License: GPL-2.0-or-later
URL: https://github.com/vcrhonek/hwdata/tag
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: make

%description
hwdata contains various hardware identification and configuration data,
such as the pci.ids and usb.ids databases.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%configure

%install
%make_install libdir=%{_prefix}/lib

%files
%license COPYING
%dir %{_datadir}/hwdata
%{_datadir}/hwdata/*
%{_prefix}/lib/modprobe.d/dist-blacklist.conf

%changelog

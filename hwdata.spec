# Copyright 2024 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

%global source_date_epoch_from_changelog 0

Name: hwdata
Epoch: 100
Version: 0.377
Release: 1%{?dist}
Summary: Hardware identification and configuration data
License: GPL-2.0-or-later
URL: https://github.com/vcrhonek/hwdata/tags
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
%{_datadir}/pkgconfig/hwdata.pc
%{_prefix}/lib/modprobe.d/dist-blacklist.conf

%changelog

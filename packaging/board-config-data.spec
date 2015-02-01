Name:       board-config-data
Summary:    Board specific configuration information package
Version:    0.0.4
Release:    2
Group:      TO_BE/FILLED_IN
License:    Apache-2.0
BuildArch:  noarch
Source0:    board-config-%{version}.tar.gz
Requires(post): coreutils

%description
Board specific configuration data package

%package redwood
Summary: Board specific configuration data package for redwood
Group: TO_BE/FILLED_IN
License:    Apache-2.0

%description redwood
Board specific configuration data package for redwood

%package B2
Summary: Board specific configuration data package for B2
Group: TO_BE/FILLED_IN
License:    Apache-2.0

%description B2
Board specific configuration data package for B2

%package slp_pq
Summary: Board specific configuration data package for slp_pq
Group: TO_BE/FILLED_IN
License:    Apache-2.0

%description slp_pq 
Board specific configuration data package for slp_pq

%prep
%setup -q -n %{name}-%{version}

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/etc/config
cp -arf data/* %{buildroot}/etc/config
mkdir -p %{buildroot}/usr/share/license
cp -a LICENSE %{buildroot}/usr/share/license/%{name}-B2


%files redwood
%manifest board-config-data.manifest
%defattr(-,root,root,-)
/etc/config/*-SLP_PQ.xml

%files B2
%manifest board-config-data.manifest
%defattr(-,root,root,-)
/etc/config/*-B2.xml
/usr/share/license/%{name}-B2

%files slp_pq
%manifest board-config-data.manifest
%defattr(-,root,root,-)
/etc/config/*-SLP_PQ.xml

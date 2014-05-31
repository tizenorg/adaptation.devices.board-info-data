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


%package redwood45
Summary: Board specific configuration data package for redwood45
Group: TO_BE/FILLED_IN
License:    Apache-2.0

%description redwood45
Board specific configuration data package for redwood45


%package redwood45_lte
Summary: Board specific configuration data package for redwood45_lte
Group: TO_BE/FILLED_IN
License:    Apache-2.0

%description redwood45_lte
Board specific configuration data package for redwood45_lte


%package redwood45_lte_jpn
Summary: Board specific configuration data package for redwood45_lte_jpn
Group: TO_BE/FILLED_IN
License:    Apache-2.0

%description redwood45_lte_jpn
Board specific configuration data package for redwood45_lte_jpn


%package baltic
Summary: Board specific configuration data package for baltic
Group: TO_BE/FILLED_IN
License:    Apache-2.0

%description baltic
Board speicific configuration data package for baltic


%package redwood_msm8974
Summary: Board specific configuration data package for RedwoodLTE_MSM_EUR
Group: TO_BE/FILLED_IN
License:    Apache-2.0

%description redwood_msm8974
Board specific configuration data package for RedwoodLTE_MSM_EUR


%package redwood8974_n099
Summary: Board specific configuration data package for RedwoodLTE_MSM_JPN
Group: TO_BE/FILLED_IN
License:    Apache-2.0

%description redwood8974_n099
Board specific configuration data package for RedwoodLTE_MSM_JPN


%package msm8x10
Summary: Board specific configuration data package for TIZEN_MSM8X10
Group: TO_BE/FILLED_IN
License:    Apache-2.0

%description msm8x10
Board specific configuration data package for TIZEN_MSM8X10


%package B2
Summary: Board specific configuration data package for B2
Group: TO_BE/FILLED_IN
License:    Apache-2.0

%description B2
Board specific configuration data package for B2


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
/etc/config/*-REDWOOD.xml

%files redwood45
%manifest board-config-data.manifest
%defattr(-,root,root,-)
/etc/config/*-REDWOOD45.xml

%files redwood45_lte
%manifest board-config-data.manifest
%defattr(-,root,root,-)
/etc/config/*-REDWOOD45_LTE.xml

%files redwood45_lte_jpn
%manifest board-config-data.manifest
%defattr(-,root,root,-)
/etc/config/*-REDWOOD45_LTE_JPN.xml

%files baltic
%manifest board-config-data.manifest
%defattr(-,root,root,-)
/etc/config/*-EXPRESS.xml

%files redwood_msm8974
%manifest board-config-data.manifest
%defattr(-,root,root,-)
/etc/config/*-REDWOOD_MSM8974.xml
/etc/config/*-RedwoodLTE_MSM_EUR.xml
/etc/config/*-RedwoodLTE_MSM_JPN.xml

%files redwood8974_n099
%manifest board-config-data.manifest
%defattr(-,root,root,-)
/etc/config/*-RedwoodLTE_MSM_JPN.xml
/etc/config/*-RedwoodLTE_MSM_EUR.xml

%files msm8x10
%manifest board-config-data.manifest
%defattr(-,root,root,-)
/etc/config/*-TIZEN_MSM8X10.xml

%files B2
%manifest board-config-data.manifest
%defattr(-,root,root,-)
/etc/config/*-B2.xml
/usr/share/license/%{name}-B2

%global commit 870a9231cd451b24d876097166e95ab4a55122ce
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global owner seandepagnier
%global plugin watchdog

Name: opencpn-plugin-watchdog
Summary: Watchdog plugin for OpenCPN
Version: 0.0
Release: 0.1.%{shortcommit}%{?dist}
License: GPLv2+

Source0: https://github.com/%{owner}/%{plugin}_pi/archive/%{commit}/%{name}-%{shortcommit}.tar.gz

BuildRequires: bzip2-devel
BuildRequires: cmake
BuildRequires: gettext
BuildRequires: tinyxml-devel
BuildRequires: wxGTK3-devel
BuildRequires: zlib-devel

Requires: opencpn%{_isa}
Supplements: opencpn%{_isa}
Requires: opencpn-plugin-draw%{_isa}

%description
The Watchdog plugin for OpenCPN implements various configurable alarms
alerting the user about the changing conditions around the boat. Also
implements an improved anchor alarm.

%prep
%autosetup -n %{plugin}_pi-%{commit}

sed -i -e s'/SET(PREFIX_LIB lib)/SET(PREFIX_LIB %{_lib})/' cmake/PluginInstall.cmake

mkdir build

%build

cd build
%cmake -DBUILD_SHARED_LIBS:BOOL=OFF ..
%make_build

%install

cd build
mkdir -p %{buildroot}%{_bindir}
%make_install

%find_lang opencpn-%{plugin}_pi

%files -f build/opencpn-%{plugin}_pi.lang

%{_libdir}/opencpn/lib%{plugin}_pi.so

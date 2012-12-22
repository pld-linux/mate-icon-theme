Summary:	Icon theme for MATE Desktop
Name:		mate-icon-theme
Version:	1.5.0
Release:	1
License:	GPLv2+ and LGPLv2+
Group:		Themes
URL:		http://mate-desktop.org/
Source0:	http://pub.mate-desktop.org/releases/1.5/%{name}-%{version}.tar.xz
# Source0-md5:	6ae1369e21371f7517e4523750443df9
BuildRequires:	icon-naming-utils >= 0.8.7
BuildRequires:	mate-common
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	gtk-update-icon-cache
Obsoletes:	mate-icon-theme-legacy < 1.5.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Icon theme for MATE Desktop.

%package devel
Summary:	Development files for mate-icon-theme
Group:		Development/Libraries

%description devel
Development files for mate-icon-theme

%prep
%setup -q

%build
NOCONFIGURE=1 ./autogen.sh
%configure \
	--enable-icon-mapping \
	--disable-static
%{__make} \
	V=1

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	install_sh="install -p" \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache mate

%postun
%update_icon_cache mate

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%{_iconsdir}/mate

%files devel
%defattr(644,root,root,755)
%{_npkgconfigdir}/mate-icon-theme.pc

Summary:	Icon theme for MATE Desktop
Name:		mate-icon-theme
Version:	1.5.0
Release:	1
License:	GPL v2+ and LGPL v2+
Group:		Themes
Source0:	http://pub.mate-desktop.org/releases/1.5/%{name}-%{version}.tar.xz
# Source0-md5:	6ae1369e21371f7517e4523750443df9
URL:		http://wiki.mate-desktop.org/mate-icon-theme
BuildRequires:	icon-naming-utils >= 0.8.7
BuildRequires:	intltool >= 0.40.0
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
Development files for mate-icon-theme.

%prep
%setup -q

%build
NOCONFIGURE=1 ./autogen.sh
%configure \
	--enable-icon-mapping
%{__make} \
	V=1

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	install_sh="install -p" \
	DESTDIR=$RPM_BUILD_ROOT

> $RPM_BUILD_ROOT%{_iconsdir}/mate/icon-theme.cache

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache mate

%postun
%update_icon_cache mate

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%dir %{_iconsdir}/mate
%{_iconsdir}/mate/index.theme
%{_iconsdir}/mate/[0-9]*x*
%ghost %{_iconsdir}/mate/icon-theme.cache

%files devel
%defattr(644,root,root,755)
%{_npkgconfigdir}/mate-icon-theme.pc

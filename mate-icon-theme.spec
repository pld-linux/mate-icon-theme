Summary:	Icon theme for MATE Desktop
Name:		mate-icon-theme
Version:	1.6.1
Release:	1
License:	GPL v2+ and LGPL v2+
Group:		Themes
Source0:	http://pub.mate-desktop.org/releases/1.6/%{name}-%{version}.tar.xz
# Source0-md5:	6dfe141cec1e2727f36314657c7ad0ae
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

%package menta
Summary:	Menta Icon theme for MATE Desktop
Group:		Themes
Requires:	%{name} = %{version}-%{release}

%description menta
Menta Icon theme for MATE Desktop.

%package devel
Summary:	Development files for mate-icon-theme
Group:		Development/Libraries

%description devel
Development files for mate-icon-theme.

%prep
%setup -q

%build
%configure \
	--disable-silent-rules \
	--enable-icon-mapping
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	install_sh="install -p" \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_datadir}/icons/mate/scalable/{actions,apps,status}
> $RPM_BUILD_ROOT%{_iconsdir}/mate/icon-theme.cache
> $RPM_BUILD_ROOT%{_iconsdir}/menta/icon-theme.cache

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache mate

%postun
%update_icon_cache mate

%post menta
%update_icon_cache menta

%postun menta
%update_icon_cache menta

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%dir %{_iconsdir}/mate
%{_iconsdir}/mate/index.theme
%{_iconsdir}/mate/[0-9]*x*
%ghost %{_iconsdir}/mate/icon-theme.cache
%dir %{_iconsdir}/mate/scalable
%dir %{_iconsdir}/mate/scalable/actions
%dir %{_iconsdir}/mate/scalable/apps
%dir %{_iconsdir}/mate/scalable/status

%files menta
%defattr(644,root,root,755)
%dir %{_iconsdir}/menta
%{_iconsdir}/menta/[0-9]*x*
%{_iconsdir}/menta/scalable
%{_iconsdir}/menta/index.theme
%ghost %{_iconsdir}/menta/icon-theme.cache

%files devel
%defattr(644,root,root,755)
%{_npkgconfigdir}/mate-icon-theme.pc

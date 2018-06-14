Summary:	Icon theme for MATE Desktop
Summary(pl.UTF-8):	Motyw ikon dla środowiska MATE Desktop
Name:		mate-icon-theme
Version:	1.20.1
Release:	1
License:	LGPL v3 or CC-BY-SA v3.0
Group:		Themes
Source0:	http://pub.mate-desktop.org/releases/1.20/%{name}-%{version}.tar.xz
# Source0-md5:	f9eb68003cf79e269ab65c604caddc21
URL:		http://wiki.mate-desktop.org/mate-icon-theme
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake >= 1:1.9
BuildRequires:	icon-naming-utils >= 0.8.7
BuildRequires:	intltool >= 0.40.0
BuildRequires:	mate-common
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	gtk-update-icon-cache
Obsoletes:	mate-icon-theme-devel < 1.12.0
Obsoletes:	mate-icon-theme-legacy < 1.5.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Icon theme for MATE Desktop.

%description -l pl.UTF-8
Motyw ikon dla środowiska MATE Desktop.

%package menta
Summary:	Menta Icon theme for MATE Desktop
Summary(pl.UTF-8):	Motyw ikon Menta dla środowiska MATE Desktop
Group:		Themes
Requires:	%{name} = %{version}-%{release}
Provides:	make-icon-theme-menta = 1.6.0-2
Obsoletes:	make-icon-theme-menta

%description menta
Menta Icon theme for MATE Desktop.

%description menta -l pl.UTF-8
Motyw ikon Menta dla środowiska MATE Desktop.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__automake}
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
%doc AUTHORS COPYING ChangeLog README TODO
%dir %{_iconsdir}/mate
%{_iconsdir}/mate/index.theme
%{_iconsdir}/mate/[0-9]*x[0-9]*
%{_iconsdir}/mate/scalable
%{_iconsdir}/mate/scalable-up-to-32
%ghost %{_iconsdir}/mate/icon-theme.cache

%files menta
%defattr(644,root,root,755)
%dir %{_iconsdir}/menta
%{_iconsdir}/menta/index.theme
%{_iconsdir}/menta/[0-9]*x[0-9]*
%ghost %{_iconsdir}/menta/icon-theme.cache

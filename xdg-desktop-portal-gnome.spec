Summary:	GNOME Desktop Portal
Summary(pl.UTF-8):	Implementacja XDG Desktop Portal dla GNOME
Name:		xdg-desktop-portal-gnome
Version:	46.2
Release:	1
License:	LGPL v2+
Group:		X11/Applications
Source0:	https://download.gnome.org/sources/xdg-desktop-portal-gnome/46/%{name}-%{version}.tar.xz
# Source0-md5:	a57a52d9488463277445bac40507487e
URL:		https://gitlab.gnome.org/GNOME/xdg-desktop-portal-gnome
BuildRequires:	fontconfig-devel
BuildRequires:	glib2-devel >= 1:2.62
BuildRequires:	gnome-desktop4-devel >= 4
BuildRequires:	gsettings-desktop-schemas-devel
BuildRequires:	gtk4-devel >= 4.0
BuildRequires:	libadwaita-devel >= 1.4.0
BuildRequires:	meson >= 0.59.0
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	tar >= 1:1.22
BuildRequires:	xdg-desktop-portal-devel >= 1.17.0
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xz
Requires:	glib2 >= 1:2.62
Requires:	gsettings-desktop-schemas
Requires:	gtk4 >= 4.0
Requires:	libadwaita >= 1.4.0
Requires:	systemd-units >= 1:242
Requires:	xdg-desktop-portal >= 1.17.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XDG Desktop Portal implementation for GNOME. It uses GNOME-specific
APIs and components, such as GNOME Shell, Mutter, and GNOME Settings
Daemon, to provide various portal features.

%description -l pl.UTF-8
Implementacja XDG Desktop Portal dla GNOME. Wykorzystuje API i
komponenty specyficzne dla GNOME, takie jak GNOME Shell, Mutter czy
GNOME Settings Daemon, aby zapewnić różne funkcje portalu.

%prep
%setup -q

%build
%meson build \
	-Dsystemduserunitdir=%{systemduserunitdir}

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

# not supported by glibc (as of 2.37)
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/ie

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%glib_compile_schemas

%postun
%glib_compile_schemas

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc NEWS README.md
%attr(755,root,root) %{_libexecdir}/xdg-desktop-portal-gnome
%{systemduserunitdir}/xdg-desktop-portal-gnome.service
%{_datadir}/dbus-1/services/org.freedesktop.impl.portal.desktop.gnome.service
%{_datadir}/glib-2.0/schemas/xdg-desktop-portal-gnome.gschema.xml
%{_datadir}/xdg-desktop-portal
%{_desktopdir}/xdg-desktop-portal-gnome.desktop

%define	_beta	beta1
Summary:	Curses client for Music Player Daemon
Summary(pl.UTF-8):	Klient curses dla demona MPD
Name:		ncmpc
Version:	0.12
Release:	0.%{_beta}.1
License:	GPL v2+
Group:		Applications/Sound
Source0:	http://dl.sourceforge.net/musicpd/%{name}-%{version}_%{_beta}.tar.bz2
# Source0-md5:	e7372dccb7707a1247c98606e95a5370
Patch0:		%{name}-configure.patch
URL:		http://hem.bredband.net/kaw/ncmpc/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glib2-devel
BuildRequires:	libtool
BuildRequires:	ncurses-ext-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ncmpc is a curses client for the Music Player Daemon (MPD). ncmpc
connects to a MPD running on a machine on the local network, and
controls this with an interface inspired by cplay. If ncmpc is used
with lirc and irpty it can be used to manage playlists and control MPD
with a remote control.

%description -l pl.UTF-8
ncmpc to klient curses dla demona MPD (Music Player Daemon). ncmpc
łączy się z MPD działającym na maszynie w sieci lokalnej i
steruje nim przy użyciu interfejsu zainspirowanego programem cplay.
Jeśli ncmpc jest używany z lircem lub irpty, można go używać do
zarządzania playlistami i sterowania MPD za pomocą pilota.

%prep
%setup -q -n %{name}-%{version}~%{_beta}
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}

%configure \
	CPPFLAGS="-I/usr/include/ncurses"
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -rf $RPM_BUILD_ROOT%{_docdir}/%{name}

%find_lang ncmpc

%clean
rm -rf $RPM_BUILD_ROOT

%files -f ncmpc.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*

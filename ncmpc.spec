Summary:	Curses client for Music Player Daemon
Summary(pl.UTF-8):	Klient curses dla demona MPD
Name:		ncmpc
Version:	0.16.1
Release:	1
License:	GPL v2+
Group:		Applications/Sound
Source0:	http://downloads.sourceforge.net/musicpd/%{name}-%{version}.tar.bz2
# Source0-md5:	f3e53a379bd0bc82d315aa111bfdd17a
URL:		http://mpd.wikia.com/wiki/Client:Ncmpc
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel
BuildRequires:	libmpdclient-devel
BuildRequires:	libtool
BuildRequires:	ncurses-ext-devel
BuildRequires:	pkgconfig
BuildRequires:	rpm-pythonprov
Suggests:	mpd
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ncmpc is a curses client for the Music Player Daemon (MPD). ncmpc
connects to a MPD running on a machine on the local network, and
controls this with an interface inspired by cplay. If ncmpc is used
with lirc and irpty it can be used to manage playlists and control MPD
with a remote control.

%description -l pl.UTF-8
ncmpc to klient curses dla demona MPD (Music Player Daemon). ncmpc
łączy się z MPD działającym na maszynie w sieci lokalnej i steruje nim
przy użyciu interfejsu zainspirowanego programem cplay. Jeśli ncmpc
jest używany z lircem lub irpty, można go używać do zarządzania
playlistami i sterowania MPD za pomocą pilota.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}

%configure \
	CPPFLAGS="-I/usr/include/ncurses" \
	--enable-lyrics-screen \
	--with-lyrics-plugin-dir=%{_libdir}/ncmpc/lyrics
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
%doc AUTHORS NEWS README doc/*.sample doc/ncmpc.lirc
%attr(755,root,root) %{_bindir}/*
%dir %{_libdir}/ncmpc
%dir %{_libdir}/ncmpc/lyrics
%attr(755,root,root) %{_libdir}/ncmpc/lyrics/*
%{_mandir}/man1/ncmpc.*

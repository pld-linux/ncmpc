Summary:	Curses client for Music Player Daemon
Summary(pl.UTF-8):	Klient curses dla demona MPD
Name:		ncmpc
Version:	0.24
Release:	1
License:	GPL v2+
Group:		Applications/Sound
Source0:	http://www.musicpd.org/download/ncmpc/0/%{name}-%{version}.tar.xz
# Source0-md5:	0717193f38446780372f2a8907316362
Source1:	ax_require_defined.m4
URL:		http://mpd.wikia.com/wiki/Client:Ncmpc
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake >= 1:1.11
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.14
BuildRequires:	libmpdclient-devel >= 2.5
BuildRequires:	ncurses-devel
BuildRequires:	pkgconfig
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
%{__cp} %{SOURCE1} m4

%build
%{__glib_gettextize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}

%configure \
	--enable-artist-screen \
	--enable-chat-screen \
	--enable-colors \
	--enable-help-screen \
	--enable-key-screen \
	--enable-locale \
	--enable-lyrics-screen \
	--enable-mouse \
	--enable-outputs-screen \
	--enable-search-screen \
	--enable-song-screen \
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

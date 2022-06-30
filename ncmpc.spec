Summary:	Curses client for Music Player Daemon
Summary(pl.UTF-8):	Klient curses dla demona MPD
Name:		ncmpc
Version:	0.47
Release:	1
License:	GPL v2+
Group:		Applications/Sound
Source0:	https://www.musicpd.org/download/ncmpc/0/%{name}-%{version}.tar.xz
# Source0-md5:	388bbf3eed9a845e8e97d7afa2c2d596
URL:		http://mpd.wikia.com/wiki/Client:Ncmpc
BuildRequires:	gcc-c++ >= 6:8
BuildRequires:	gettext-tools
BuildRequires:	libmpdclient-devel >= 2.17
BuildRequires:	libstdc++-devel
BuildRequires:	meson >= 0.49
BuildRequires:	ncurses-devel
BuildRequires:	ninja
BuildRequires:	pcre2-8-devel
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	sphinx-pdg
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	libmpdclient >= 2.17
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
%meson build \
	-Dchat_screen=true \
	-Dcolors=true \
	-Ddocumentation=enabled \
	-Dhelp_screen=true \
	-Dkey_screen=true \
	-Dlocale=enabled \
	-Dlyrics_screen=true \
	-Dmanual=true \
	-Dmouse=enabled \
	-Doutputs_screen=true \
	-Dsearch_screen=true \
	-Dsong_screen=true \
	-Dlirc=disabled

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -j1 -C build

rm -r $RPM_BUILD_ROOT%{_docdir}/%{name}

%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/ie

%find_lang ncmpc

%clean
rm -rf $RPM_BUILD_ROOT

%files -f ncmpc.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README.rst doc/*.sample doc/ncmpc.lirc
%attr(755,root,root) %{_bindir}/*
%dir %{_libdir}/ncmpc
%dir %{_libdir}/ncmpc/lyrics
%attr(755,root,root) %{_libdir}/ncmpc/lyrics/*
%{_mandir}/man1/ncmpc.*

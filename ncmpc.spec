Summary:	Curses client for Music Player Daemon
Summary(pl):	Klient curses dla demona MPD
Name:		ncmpc
Version:	0.11.1
Release:	1
License:	GPL
Group:		Applications/Sound
Source0:	http://hem.bredband.net/kaw/ncmpc/files/%{name}-%{version}.tar.gz
# Source0-md5:	c90668b12f3676c73913a863482ec405
URL:		http://hem.bredband.net/kaw/ncmpc/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel
BuildRequires:	ncurses-ext-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ncmpc is a curses client for the Music Player Daemon (MPD). ncmpc
connects to a MPD running on a machine on the local network, and
controls this with an interface inspired by cplay. If ncmpc is used
with lirc and irpty it can be used to manage playlists and control MPD
with a remote control.

%description -l pl
ncmpc to klient curses dla demona MPD (Music Player Daemon). ncmpc
³±czy siê z MPD dzia³aj±cym na maszynie w sieci lokalnej i steruje nim
przy u¿yciu interfejsu zainspirowanego programem cplay. Je¶li ncmpc
jest u¿ywany z lircem lub irpty, mo¿na go u¿ywaæ do zarz±dzania
playlistami i sterowania MPD za pomoc± pilota.

%prep
%setup -q

%build
#%%{__gettextize}
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
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*

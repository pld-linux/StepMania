# TODO - add br, does not build
Summary:	Rhythm game
Summary(pl.UTF-8):	Gra rytmu
Name:		StepMania
Version:	3.9
Release:	0.1
License:	BSD/Custom, see Copying.txt
Group:		Applications
Source0:	http://dl.sourceforge.net/stepmania/%{name}-%{version}-src.tar.gz
# Source0-md5:	28bbbc985788bc990fa7042e2d7320b8
Patch0:		%{name}-3.9-64bits.patch
Patch1:		%{name}-3.9-alsa.patch
Patch2:		%{name}-3.9-ffmpeg.patch
Patch3:		%{name}-3.9-gcc41.patch
Patch4:		%{name}-3.9-sdl.patch
Patch5:		%{name}-3.9-vorbis.patch
Patch6:		%{name}-lua.patch
URL:		http://www.stepmania.com/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	lua50-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Rhythm game.

%description -l pl.UTF-8
Gra rytmu.

%prep
%setup -q -n %{name}-%{version}-src
%patch -P0 -p0
%patch -P1 -p0
%patch -P2 -p0
%patch -P3 -p0
%patch -P4 -p0
%patch -P5 -p0
%patch -P6 -p1

%build
%{__aclocal} -I autoconf/m4
%{__autoconf}
%{__automake}
%configure
%{__make}


%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/stepmania

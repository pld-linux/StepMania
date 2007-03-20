# TODO - add br, does not build
Summary:	Rhythm game 
Summary(pl):	Gra rytmu
Name:		StepMania
Version:	3.9
Release:	0.1
License:	BSD/Custom, see Copying.txt
Group:		Applications
Source0:	http://dl.sourceforge.net/sourceforge/stepmania/%{name}-%{version}-src.tar.gz
# Source0-md5:	28bbbc985788bc990fa7042e2d7320b8
Patch0:		StepMania-3.9-64bits.patch
Patch1:		StepMania-3.9-alsa.patch
Patch2:		StepMania-3.9-ffmpeg.patch
Patch3:		StepMania-3.9-gcc41.patch
Patch4:		StepMania-3.9-sdl.patch
Patch5:		StepMania-3.9-vorbis.patch
URL:		http://www.stepmania.com
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	lua50-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
TODO

%prep
%setup -q -n %{name}-%{version}-src
%patch0 -p0
%patch1 -p0
%patch2 -p0
%patch3 -p0
%patch4 -p0
%patch5 -p0

%build
%{__aclocal} -I autoconf/m4
%{__autoconf}
%{__automake}
%configure
%{__make}


%install
rm -rf $RPM_BUILD_ROOT
# create directories if necessary
#install -d $RPM_BUILD_ROOT
#install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(644,root,root,755)
%doc AUTHORS CREDITS ChangeLog NEWS README THANKS TODO

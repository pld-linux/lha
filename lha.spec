Summary:	An archiving and compression utility for LHarc format archives.
Name:		lha
Version:	1.00
Release:	12
Copyright:	freeware
Group:		Applications/Archiving
Source:		ftp://sunsite.unc.edu/pub/Linux/utils/compress/%{name}-%{version}.tar.Z
Patch:		lha-1.00-fsstnd.patch
BuildRoot:	/tmp/%{name}-%{version}-root

%description
LHA is an archiving and compression utility for LHarc format archives.
LHA is mostly used in the DOS world, but can be used under Linux to
extract DOS files from LHA archives.

Install the lha package if you need to extract DOS files from LHA archives.

%prep
%setup -q
%patch -p1

%build
make CFLAGS="-DEUC -DSYSV_SYSTEM_DIR -DSYSTIME_HAS_NO_TM -DMKTIME $RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install -s src/lha $RPM_BUILD_ROOT%{_bindir}

gzip -9nf README.Linux

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc	README.Linux.gz
%attr(755,root,root) %{_bindir}/lha

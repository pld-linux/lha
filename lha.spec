Summary: An archiving and compression utility for LHarc format archives.
Name: lha
Version: 1.00
Release: 11
Copyright: freeware
Group: Applications/Archiving
Source: ftp://sunsite.unc.edu/pub/Linux/utils/compress/lha-1.00.tar.Z
Patch: lha-1.00-fsstnd.patch
BuildRoot: /var/tmp/lha-root

%description
LHA is an archiving and compression utility for LHarc format archives.
LHA is mostly used in the DOS world, but can be used under Linux to
extract DOS files from LHA archives.

Install the lha package if you need to extract DOS files from LHA archives.

%prep
%setup -q
%patch -p1

%build
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/bin

install -m755 -s src/lha $RPM_BUILD_ROOT/usr/bin

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc	README.Linux
/usr/bin/lha

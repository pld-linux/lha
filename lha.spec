Summary:	An archiving and compression utility for LHarc format archives.
Summary(de):	erstellt und erweitert Archive im lharc-Format 
Summary(fr):	cr�e et d�compresse des archives au format lharc
Summary(tr):	lharc bi�imindeki ar�ivleri yarat�r ve geni�letir
Name:		lha
Version:	1.00
Release:	12
Copyright:	freeware
Group:		Applications/Archiving
Source:		ftp://sunsite.unc.edu/pub/Linux/utils/compress/%{name}-%{version}.tar.Z
Patch:		lha-fsstnd.patch
BuildRoot:	/tmp/%{name}-%{version}-root

%description
LHA is an archiving and compression utility for LHarc format archives.
LHA is mostly used in the DOS world, but can be used under Linux to
extract DOS files from LHA archives.

Install the lha package if you need to extract DOS files from LHA archives.

%description -l de
Dies ist ein Archivierungs- und Komprimierungsdienstprogramm.
Es wird �berwiegend unter DOS verwendet, kann aber auch unter Linux
eingesetzt werden, um DOS-Dateien aus LHA-Archiven zu extrahieren.

%description -l fr
Un utilitaire d'archivage et de compression. il est surtout utilis� dans
le monde DOS, mais peut �tre utilis� sous Linux pour extraire des fichiers
dans des archives LHA.

%description -l tr
Bu bir dosya ar�ivleme ve s�k��t�rma program�d�r. Genelde DOS d�nyas�nda
kullan�lmakla birlikte LHA ar�ivlerinden DOS dosyalar�n� a�mak i�in Linux
alt�nda da kullan�labilir.

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

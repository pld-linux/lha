Summary:	An archiving and compression utility for LHarc format archives
Summary(de):	erstellt und erweitert Archive im lharc-Format 
Summary(fr):	cr�e et d�compresse des archives au format lharc
Summary(pl):	Program archiwizuj�cy i kompresuj�cy, u�ywaj�cy formatu archiw�w LHarc
Summary(tr):	lharc bi�imindeki ar�ivleri yarat�r ve geni�letir
Name:		lha
Version:	1.14f
Release:	1
Copyright:	freeware
Group:		Applications/Archiving
Group(de):	Applikationen/Archivierung
Group(pl):	Aplikacje/Archiwizacja
Source0:	http://www2m.biglobe.ne.jp/~dolphin/lha/prog/%{name}-114f.tar.gz
Source1:	%{name}.1
Patch0:		%{name}-ext.patch
Patch1:		%{name}-make.patch
URL:		http://www2m.meshnet.or.jp/~dolphin/lha/lha-unix.htm
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LHA is an archiving and compression utility for LHarc format archives.
LHA is mostly used in the DOS world, but can be used under Linux to
extract DOS files from LHA archives.

Install the lha package if you need to extract DOS files from LHA
archives.

%description -l de
Dies ist ein Archivierungs- und Komprimierungsdienstprogramm. Es wird
�berwiegend unter DOS verwendet, kann aber auch unter Linux eingesetzt
werden, um DOS-Dateien aus LHA-Archiven zu extrahieren.

%description -l fr
Un utilitaire d'archivage et de compression. il est surtout utilis�
dans le monde DOS, mais peut �tre utilis� sous Linux pour extraire des
fichiers dans des archives LHA.

%description -l pl
LHA jest programem archiwizuj�cym i kompresuj�cym dla archiw�w w
formacie LHarc. By� u�ywany g��wnie w �rodowisku DOS, pod Linuksem
mo�e by� u�yty do rozpakowania archiw�w LHA.

%description -l tr
Bu bir dosya ar�ivleme ve s�k��t�rma program�d�r. Genelde DOS
d�nyas�nda kullan�lmakla birlikte LHA ar�ivlerinden DOS dosyalar�n�
a�mak i�in Linux alt�nda da kullan�labilir.

%prep
%setup  -q -n %{name}-114f
%patch0 -p1
%patch1 -p1

%build
%{__make} OPTIMIZE="%{rpmcflags} -DSUPPORT_LH6"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/{man1,ja/man1}}

install src/lha $RPM_BUILD_ROOT%{_bindir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_mandir}/man1
install man/lha.man $RPM_BUILD_ROOT%{_mandir}/ja/man1

gzip -9nf change-114e.txt {CHANGES,PROBLEMS,README}.euc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc change-114e.txt.gz
%lang(ja) %doc {CHANGES,PROBLEMS,README}.euc.gz
%attr(755,root,root) %{_bindir}/lha
%{_mandir}/man1/*
%lang(ja) %{_mandir}/ja/man1/*

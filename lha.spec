Summary:	An archiving and compression utility for LHarc format archives
Summary(es):	Crea y expande archivos en formato lharc
Summary(de):	erstellt und erweitert Archive im lharc-Format
Summary(fr):	crée et décompresse des archives au format lharc
Summary(ja):	¹â°µ½Ì¥¢¡¼¥«¥¤¥Ð
Summary(pl):	Program archiwizuj±cy i kompresuj±cy, u¿ywaj±cy formatu archiwów LHarc
Summary(pt_BR):	Cria e expande arquivos no formato lharc
Summary(tr):	lharc biçimindeki arþivleri yaratýr ve geniþletir
Name:		lha
Version:	1.14i
Release:	0.1
License:	Freeware
Group:		Applications/Archiving
Source0:	http://www2m.biglobe.ne.jp/~dolphin/lha/prog/%{name}-114i.tar.gz
# Source0-md5:	5225884d557b91f04124693e2c5c9e94
Source1:	%{name}.1
Patch0:		%{name}-ext.patch
Patch1:		%{name}-time.patch
Patch2:		%{name}-sec.patch
Patch3:		%{name}-symlink.patch
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
überwiegend unter DOS verwendet, kann aber auch unter Linux eingesetzt
werden, um DOS-Dateien aus LHA-Archiven zu extrahieren.

%description -l es
Éste es un utilitario de almacenaje y compresión. Es más utilizado en
el mundo Amiga, pero puede ser usado en Linux para extraer archivos.

%description -l fr
Un utilitaire d'archivage et de compression. il est surtout utilisé
dans le monde DOS, mais peut être utilisé sous Linux pour extraire des
fichiers dans des archives LHA.

%description
LHa ¤Ï¸úÎ¨¤Î¹â¤¤°µ½Ìµ¡Ç½¤ò»ý¤Ä¥Õ¥¡¥¤¥ë¥¢¡¼¥«¥¤¥Ð¤Ç¤¹¡£

¤³¤ì¤Ï -lh5-, -lh6- °µ½Ì·Á¼°¤Ç¤Î°µ½Ì/Å¸³«¤¬²ÄÇ½¤Ê¥¢¡¼¥«¥¤¥Ð
LHa ¤Î UNIX ÈÇ¤ÎÈóÀµ¼° ¥Ð¡¼¥¸¥ç¥ó¥¢¥Ã¥×ÈÇ¤Ç¤¹¡£

%description -l pl
LHA jest programem archiwizuj±cym i kompresuj±cym dla archiwów w
formacie LHarc. By³ u¿ywany g³ównie w ¶rodowisku DOS, pod Linuksem
mo¿e byæ u¿yty do rozpakowania archiwów LHA.

%description -l pt_BR
Este é um utilitário de armazenamento e compressão. Ele é mais
utilizado no mundo Amiga, mas pode ser usado no Linux para extrair
arquivos.

%description -l tr
Bu bir dosya arþivleme ve sýkýþtýrma programýdýr. Genelde DOS
dünyasýnda kullanýlmakla birlikte LHA arþivlerinden DOS dosyalarýný
açmak için Linux altýnda da kullanýlabilir.

%prep
%setup  -q -n %{name}-114i
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%{__make} \
	OPTIMIZE="%{rpmcflags} -DSUPPORT_LH7 -DMKSTEMP" \
	MACHINE="-DEUC -DSYSV_SYSTEM_DIR -DTZSET -DARCHIVENAME_EXTENTION=\".lha\" -DBACKUPNAME_EXTENTION=\".bak\" -DSUPPORT_LH7" \
	BINDIR=%{_bindir} \
	MANDIR=%{_mandir} \
	MANSECT=1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/{man1,ja/man1}}

install src/lha $RPM_BUILD_ROOT%{_bindir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_mandir}/man1
install man/lha.man $RPM_BUILD_ROOT%{_mandir}/ja/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc change-*.txt
%lang(ja) %doc {CHANGES,PROBLEMS,README}.euc
%attr(755,root,root) %{_bindir}/lha
%{_mandir}/man1/*
%lang(ja) %{_mandir}/ja/man1/*

Summary:	An archiving and compression utility for LHarc format archives
Summary(es.UTF-8):	Crea y expande archivos en formato lharc
Summary(de.UTF-8):	erstellt und erweitert Archive im lharc-Format
Summary(fr.UTF-8):	crée et décompresse des archives au format lharc
Summary(ja.UTF-8):	高圧縮アーカイバ
Summary(pl.UTF-8):	Program archiwizujący i kompresujący, używający formatu archiwów LHarc
Summary(pt_BR.UTF-8):	Cria e expande arquivos no formato lharc
Summary(tr.UTF-8):	lharc biçimindeki arşivleri yaratır ve genişletir
Name:		lha
Version:	1.14i
Release:	17
License:	Freeware
Group:		Applications/Archiving
Source0:	http://www2m.biglobe.ne.jp/~dolphin/lha/prog/%{name}-114i.tar.gz
# Source0-md5:	5225884d557b91f04124693e2c5c9e94
Source1:	%{name}.1
Patch0:		%{name}-ext.patch
Patch1:		%{name}-time.patch
Patch2:		%{name}-sec.patch
Patch3:		%{name}-symlink.patch
Patch4:		%{name}-dir_length_bounds_check.patch
Patch5:		%{name}-security_fixes.patch
URL:		http://www2m.biglobe.ne.jp/~dolphin/lha/lha-unix.htm
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LHA is an archiving and compression utility for LHarc format archives.
LHA is mostly used in the DOS world, but can be used under Linux to
extract DOS files from LHA archives.

Install the lha package if you need to extract DOS files from LHA
archives.

%description -l de.UTF-8
Dies ist ein Archivierungs- und Komprimierungsdienstprogramm. Es wird
überwiegend unter DOS verwendet, kann aber auch unter Linux eingesetzt
werden, um DOS-Dateien aus LHA-Archiven zu extrahieren.

%description -l es.UTF-8
LHA es un utilitario de almacenaje y compresión. Es más utilizado en
el mundo Amiga, pero puede ser usado en Linux para extraer archivos.

%description -l fr.UTF-8
Un utilitaire d'archivage et de compression. il est surtout utilisé
dans le monde DOS, mais peut être utilisé sous Linux pour extraire des
fichiers dans des archives LHA.

%description -l ja.UTF-8
LHa は効率の高い圧縮機能を持つファイルアーカイバです。

これは -lh5-, -lh6- 圧縮形式での圧縮/展開が可能なアーカイバ
LHa の UNIX 版の非正式 バージョンアップ版です。

%description -l pl.UTF-8
LHA jest programem archiwizującym i kompresującym dla archiwów w
formacie LHarc. Był używany głównie w środowisku DOS, pod Linuksem
może być użyty do rozpakowania archiwów LHA.

%description -l pt_BR.UTF-8
Este é um utilitário de armazenamento e compressão. Ele é mais
utilizado no mundo Amiga, mas pode ser usado no Linux para extrair
arquivos.

%description -l tr.UTF-8
Bu bir dosya arşivleme ve sıkıştırma programıdır. Genelde DOS
dünyasında kullanılmakla birlikte LHA arşivlerinden DOS dosyalarını
açmak için Linux altında da kullanılabilir.

%prep
%setup  -q -n %{name}-114i
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p0
%patch5 -p1

%build
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags} -DSUPPORT_LH7 -DMKSTEMP" \
	MACHINE='-DEUC -DSYSV_SYSTEM_DIR -DTZSET -DARCHIVENAME_EXTENTION=\".lha\" -DBACKUPNAME_EXTENTION=\".bak\" -DSUPPORT_LH7' \
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

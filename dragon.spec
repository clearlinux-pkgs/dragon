#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v21
# autospec commit: fbbd4e3
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : dragon
Version  : 24.12.3
Release  : 82
URL      : https://download.kde.org/stable/release-service/24.12.3/src/dragon-24.12.3.tar.xz
Source0  : https://download.kde.org/stable/release-service/24.12.3/src/dragon-24.12.3.tar.xz
Source1  : https://download.kde.org/stable/release-service/24.12.3/src/dragon-24.12.3.tar.xz.sig
Source2  : BB463350D6EF31EF.pkey
Summary  : No detailed summary available
Group    : Development/Tools
License  : CC0-1.0 GFDL-1.2 GPL-2.0 GPL-3.0
Requires: dragon-bin = %{version}-%{release}
Requires: dragon-data = %{version}-%{release}
Requires: dragon-lib = %{version}-%{release}
Requires: dragon-license = %{version}-%{release}
Requires: dragon-locales = %{version}-%{release}
Requires: dragon-man = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : gnupg
BuildRequires : kconfig-dev
BuildRequires : kcoreaddons-dev
BuildRequires : kcrash-dev
BuildRequires : kdbusaddons-dev
BuildRequires : ki18n-dev
BuildRequires : kio-dev
BuildRequires : kjobwidgets-dev
BuildRequires : phonon-dev
BuildRequires : qt6base-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
No detailed description available

%package bin
Summary: bin components for the dragon package.
Group: Binaries
Requires: dragon-data = %{version}-%{release}
Requires: dragon-license = %{version}-%{release}

%description bin
bin components for the dragon package.


%package data
Summary: data components for the dragon package.
Group: Data

%description data
data components for the dragon package.


%package doc
Summary: doc components for the dragon package.
Group: Documentation
Requires: dragon-man = %{version}-%{release}

%description doc
doc components for the dragon package.


%package lib
Summary: lib components for the dragon package.
Group: Libraries
Requires: dragon-data = %{version}-%{release}
Requires: dragon-license = %{version}-%{release}

%description lib
lib components for the dragon package.


%package license
Summary: license components for the dragon package.
Group: Default

%description license
license components for the dragon package.


%package locales
Summary: locales components for the dragon package.
Group: Default

%description locales
locales components for the dragon package.


%package man
Summary: man components for the dragon package.
Group: Default

%description man
man components for the dragon package.


%prep
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE2}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE1} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) BB463350D6EF31EF' gpg.status
%setup -q -n dragon-24.12.3
cd %{_builddir}/dragon-24.12.3
pushd ..
cp -a dragon-24.12.3 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1742457844
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake .. -DQT_MAJOR_VERSION=6  -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
pushd ../buildavx2/
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
%cmake .. -DQT_MAJOR_VERSION=6  -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1742457844
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/dragon
cp %{_builddir}/dragon-%{version}/.flatpak-manifest.json.license %{buildroot}/usr/share/package-licenses/dragon/864bc0eb28c73bd997ac19ff91935ab771846615 || :
cp %{_builddir}/dragon-%{version}/LICENSES/GFDL-1.2-or-later.txt %{buildroot}/usr/share/package-licenses/dragon/7697008f58568e61e7598e796eafc2a997503fde || :
cp %{_builddir}/dragon-%{version}/LICENSES/GPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/dragon/2a638514c87c4923c0570c55822620fad56f2a33 || :
cp %{_builddir}/dragon-%{version}/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/dragon/e712eadfab0d2357c0f50f599ef35ee0d87534cb || :
cp %{_builddir}/dragon-%{version}/LICENSES/GPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/dragon/6091db0aead0d90182b93d3c0d09ba93d188f907 || :
cp %{_builddir}/dragon-%{version}/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/dragon/7d9831e05094ce723947d729c2a46a09d6e90275 || :
cp %{_builddir}/dragon-%{version}/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/dragon/7d9831e05094ce723947d729c2a46a09d6e90275 || :
export GOAMD64=v2
pushd ../buildavx2/
GOAMD64=v3
pushd clr-build-avx2
%make_install_v3  || :
popd
popd
GOAMD64=v2
pushd clr-build
%make_install
popd
%find_lang dragonplayer
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/dragon
/usr/bin/dragon

%files data
%defattr(-,root,root,-)
/usr/share/applications/org.kde.dragonplayer.desktop
/usr/share/icons/hicolor/128x128/apps/dragonplayer.png
/usr/share/icons/hicolor/16x16/apps/dragonplayer.png
/usr/share/icons/hicolor/22x22/apps/dragonplayer.png
/usr/share/icons/hicolor/32x32/apps/dragonplayer.png
/usr/share/icons/hicolor/48x48/apps/dragonplayer.png
/usr/share/icons/hicolor/64x64/apps/dragonplayer.png
/usr/share/icons/hicolor/scalable/apps/dragonplayer.svgz
/usr/share/icons/oxygen/16x16/actions/player-volume-muted.png
/usr/share/icons/oxygen/22x22/actions/player-volume-muted.png
/usr/share/icons/oxygen/32x32/actions/player-volume-muted.png
/usr/share/icons/oxygen/48x48/actions/player-volume-muted.png
/usr/share/icons/oxygen/scalable/actions/player-volume-muted.svgz
/usr/share/kio/servicemenus/dragonplayer_play_dvd.desktop
/usr/share/metainfo/org.kde.dragonplayer.appdata.xml
/usr/share/solid/actions/dragonplayer-openaudiocd.desktop
/usr/share/solid/actions/dragonplayer-opendvd.desktop
/usr/share/xdg/dragonplayerrc

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/HTML/ca/dragonplayer/index.cache.bz2
/usr/share/doc/HTML/ca/dragonplayer/index.docbook
/usr/share/doc/HTML/de/dragonplayer/index.cache.bz2
/usr/share/doc/HTML/de/dragonplayer/index.docbook
/usr/share/doc/HTML/de/dragonplayer/main.png
/usr/share/doc/HTML/en/dragonplayer/index.cache.bz2
/usr/share/doc/HTML/en/dragonplayer/index.docbook
/usr/share/doc/HTML/en/dragonplayer/main.png
/usr/share/doc/HTML/en/dragonplayer/playmedia.png
/usr/share/doc/HTML/es/dragonplayer/index.cache.bz2
/usr/share/doc/HTML/es/dragonplayer/index.docbook
/usr/share/doc/HTML/es/dragonplayer/main.png
/usr/share/doc/HTML/et/dragonplayer/index.cache.bz2
/usr/share/doc/HTML/et/dragonplayer/index.docbook
/usr/share/doc/HTML/fr/dragonplayer/index.cache.bz2
/usr/share/doc/HTML/fr/dragonplayer/index.docbook
/usr/share/doc/HTML/gl/dragonplayer/index.cache.bz2
/usr/share/doc/HTML/gl/dragonplayer/index.docbook
/usr/share/doc/HTML/id/dragonplayer/index.cache.bz2
/usr/share/doc/HTML/id/dragonplayer/index.docbook
/usr/share/doc/HTML/it/dragonplayer/index.cache.bz2
/usr/share/doc/HTML/it/dragonplayer/index.docbook
/usr/share/doc/HTML/it/dragonplayer/main.png
/usr/share/doc/HTML/it/dragonplayer/playmedia.png
/usr/share/doc/HTML/nl/dragonplayer/index.cache.bz2
/usr/share/doc/HTML/nl/dragonplayer/index.docbook
/usr/share/doc/HTML/pl/dragonplayer/index.cache.bz2
/usr/share/doc/HTML/pl/dragonplayer/index.docbook
/usr/share/doc/HTML/pl/dragonplayer/main.png
/usr/share/doc/HTML/pt/dragonplayer/index.cache.bz2
/usr/share/doc/HTML/pt/dragonplayer/index.docbook
/usr/share/doc/HTML/pt_BR/dragonplayer/index.cache.bz2
/usr/share/doc/HTML/pt_BR/dragonplayer/index.docbook
/usr/share/doc/HTML/pt_BR/dragonplayer/main.png
/usr/share/doc/HTML/ru/dragonplayer/index.cache.bz2
/usr/share/doc/HTML/ru/dragonplayer/index.docbook
/usr/share/doc/HTML/sl/dragonplayer/index.cache.bz2
/usr/share/doc/HTML/sl/dragonplayer/index.docbook
/usr/share/doc/HTML/sr/dragonplayer/index.cache.bz2
/usr/share/doc/HTML/sr/dragonplayer/index.docbook
/usr/share/doc/HTML/sr@latin/dragonplayer/index.cache.bz2
/usr/share/doc/HTML/sr@latin/dragonplayer/index.docbook
/usr/share/doc/HTML/sv/dragonplayer/index.cache.bz2
/usr/share/doc/HTML/sv/dragonplayer/index.docbook
/usr/share/doc/HTML/sv/dragonplayer/main.png
/usr/share/doc/HTML/tr/dragonplayer/index.cache.bz2
/usr/share/doc/HTML/tr/dragonplayer/index.docbook
/usr/share/doc/HTML/tr/dragonplayer/main.png
/usr/share/doc/HTML/tr/dragonplayer/playmedia.png
/usr/share/doc/HTML/uk/dragonplayer/index.cache.bz2
/usr/share/doc/HTML/uk/dragonplayer/index.docbook
/usr/share/doc/HTML/uk/dragonplayer/main.png
/usr/share/doc/HTML/uk/dragonplayer/playmedia.png

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/qt6/plugins/kf6/parts/dragonpart.so
/usr/lib64/qt6/plugins/kf6/parts/dragonpart.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/dragon/2a638514c87c4923c0570c55822620fad56f2a33
/usr/share/package-licenses/dragon/6091db0aead0d90182b93d3c0d09ba93d188f907
/usr/share/package-licenses/dragon/7697008f58568e61e7598e796eafc2a997503fde
/usr/share/package-licenses/dragon/7d9831e05094ce723947d729c2a46a09d6e90275
/usr/share/package-licenses/dragon/864bc0eb28c73bd997ac19ff91935ab771846615
/usr/share/package-licenses/dragon/e712eadfab0d2357c0f50f599ef35ee0d87534cb

%files man
%defattr(0644,root,root,0755)
/usr/share/man/ca/man1/dragon.1
/usr/share/man/de/man1/dragon.1
/usr/share/man/es/man1/dragon.1
/usr/share/man/et/man1/dragon.1
/usr/share/man/fr/man1/dragon.1
/usr/share/man/it/man1/dragon.1
/usr/share/man/man1/dragon.1
/usr/share/man/nl/man1/dragon.1
/usr/share/man/pt/man1/dragon.1
/usr/share/man/pt_BR/man1/dragon.1
/usr/share/man/sl/man1/dragon.1
/usr/share/man/sr/man1/dragon.1
/usr/share/man/sr@latin/man1/dragon.1
/usr/share/man/sv/man1/dragon.1
/usr/share/man/tr/man1/dragon.1
/usr/share/man/uk/man1/dragon.1

%files locales -f dragonplayer.lang
%defattr(-,root,root,-)


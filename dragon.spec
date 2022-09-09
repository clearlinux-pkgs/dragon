#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : dragon
Version  : 22.08.1
Release  : 45
URL      : https://download.kde.org/stable/release-service/22.08.1/src/dragon-22.08.1.tar.xz
Source0  : https://download.kde.org/stable/release-service/22.08.1/src/dragon-22.08.1.tar.xz
Source1  : https://download.kde.org/stable/release-service/22.08.1/src/dragon-22.08.1.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : GFDL-1.2 GPL-2.0 GPL-3.0
Requires: dragon-bin = %{version}-%{release}
Requires: dragon-data = %{version}-%{release}
Requires: dragon-lib = %{version}-%{release}
Requires: dragon-license = %{version}-%{release}
Requires: dragon-locales = %{version}-%{release}
Requires: dragon-man = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : phonon-dev

%description
INTRODUCTION
Dragon Player is a very simple Phonon-based media player. It was originally
developed by Max Howell and called Codeine. I ported it to KDE 4.0 and on
Max's suggestion renamed it to Video Player (probably, I might still
rename it.)

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
%setup -q -n dragon-22.08.1
cd %{_builddir}/dragon-22.08.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1662766468
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1662766468
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/dragon
cp %{_builddir}/dragon-%{version}/LICENSES/GFDL-1.2-or-later.txt %{buildroot}/usr/share/package-licenses/dragon/7697008f58568e61e7598e796eafc2a997503fde || :
cp %{_builddir}/dragon-%{version}/LICENSES/GPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/dragon/2a638514c87c4923c0570c55822620fad56f2a33 || :
cp %{_builddir}/dragon-%{version}/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/dragon/e712eadfab0d2357c0f50f599ef35ee0d87534cb || :
cp %{_builddir}/dragon-%{version}/LICENSES/GPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/dragon/6091db0aead0d90182b93d3c0d09ba93d188f907 || :
cp %{_builddir}/dragon-%{version}/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/dragon/7d9831e05094ce723947d729c2a46a09d6e90275 || :
cp %{_builddir}/dragon-%{version}/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/dragon/7d9831e05094ce723947d729c2a46a09d6e90275 || :
pushd clr-build
%make_install
popd
%find_lang dragonplayer

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
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
/usr/share/kservices5/ServiceMenus/dragonplayer_play_dvd.desktop
/usr/share/kservices5/dragonplayer_part.desktop
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
/usr/share/doc/HTML/sr/dragonplayer/index.cache.bz2
/usr/share/doc/HTML/sr/dragonplayer/index.docbook
/usr/share/doc/HTML/sv/dragonplayer/index.cache.bz2
/usr/share/doc/HTML/sv/dragonplayer/index.docbook
/usr/share/doc/HTML/sv/dragonplayer/main.png
/usr/share/doc/HTML/tr/dragonplayer/index.cache.bz2
/usr/share/doc/HTML/tr/dragonplayer/index.docbook
/usr/share/doc/HTML/uk/dragonplayer/index.cache.bz2
/usr/share/doc/HTML/uk/dragonplayer/index.docbook
/usr/share/doc/HTML/uk/dragonplayer/main.png
/usr/share/doc/HTML/uk/dragonplayer/playmedia.png

%files lib
%defattr(-,root,root,-)
/usr/lib64/qt5/plugins/kf5/parts/dragonpart.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/dragon/2a638514c87c4923c0570c55822620fad56f2a33
/usr/share/package-licenses/dragon/6091db0aead0d90182b93d3c0d09ba93d188f907
/usr/share/package-licenses/dragon/7697008f58568e61e7598e796eafc2a997503fde
/usr/share/package-licenses/dragon/7d9831e05094ce723947d729c2a46a09d6e90275
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
/usr/share/man/sr/man1/dragon.1
/usr/share/man/sv/man1/dragon.1
/usr/share/man/tr/man1/dragon.1
/usr/share/man/uk/man1/dragon.1

%files locales -f dragonplayer.lang
%defattr(-,root,root,-)


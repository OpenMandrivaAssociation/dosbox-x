# dosbox-x has its own autogen.sh script that differs a little
%define _disable_rebuild_configure 1

Name: dosbox-x
Version: 2023.10.06
Release: 1
Source0: https://github.com/joncampbell123/dosbox-x/archive/refs/tags/dosbox-x-v%{version}.tar.gz
Summary: DOS Emulator
URL: https://dosbox-x.com/
License: GPLv2+
Group: Emulators
BuildRequires: autoconf automake
BuildRequires: pkgconfig(opusfile)
BuildRequires: pkgconfig(sdl2)
BuildRequires: pkgconfig(SDL2_net)
BuildRequires: pkgconfig(SDL2_image)
BuildRequires: pkgconfig(slirp) >= 4.6.1
BuildRequires: pkgconfig(gl)
BuildRequires: pkgconfig(fluidsynth)
BuildRequires: pkgconfig(mt32emu)
BuildRequires: pkgconfig(libpng)
BuildRequires: pkgconfig(alsa)
BuildRequires: pkgconfig(gtest)
BuildRequires: pkgconfig(gmock)
BuildRequires: pkgconfig(iir)
BuildRequires: pkgconfig(speexdsp)
BuildRequires: atomic-devel
Obsoletes: dosbox < %{EVRD}

%description
DOSBox is a DOS emulator, emulating 286/386 CPUs, filesystems,
XMS/EMS, various graphics cards and sound cards.

DOSBox-x is a fork of DOSBox that tries to modernize the codebase
and add new features.

%prep
%autosetup -p1 -n %{name}-%{name}-v%{version}
./autogen.sh || :

%configure \
	--enable-sdl2

%build
%make_build

%install
%make_install

%files
%{_bindir}/dosbox-x
%{_datadir}/bash-completion/completions/dosbox-x
%{_datadir}/icons/hicolor/*/apps/dosbox-x.*
%{_datadir}/applications/com.dosbox_x.DOSBox-X.desktop
%{_datadir}/metainfo/com.dosbox_x.DOSBox-X.metainfo.xml
%{_datadir}/dosbox-x
%{_mandir}/man1/dosbox-x.1*

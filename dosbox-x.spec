# dosbox-x has its own autogen.sh script that differs a little
%global _disable_rebuild_configure 1

Summary: DOS Emulator
Name: dosbox-x
Version: 2026.03.29
License: GPLv2+
Group: Emulators
Release: 1
Url: https://dosbox-x.com
Source0: https://github.com/joncampbell123/dosbox-x/archive/refs/tags/dosbox-x-v%{version}.tar.gz
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: chrpath
BuildRequires: libtool-base
BuildRequires: m4
BuildRequires: make
BuildRequires: slibtool
BuildRequires: atomic-devel
BuildRequires: pkgconfig(alsa)
BuildRequires: pkgconfig(fluidsynth)
BuildRequires: pkgconfig(gl)
BuildRequires: pkgconfig(gtest)
BuildRequires: pkgconfig(gmock)
BuildRequires: pkgconfig(iir)
BuildRequires: pkgconfig(libpng)
BuildRequires: pkgconfig(mt32emu)
BuildRequires: pkgconfig(opusfile)
BuildRequires: pkgconfig(sdl2)
BuildRequires: pkgconfig(SDL2_net)
BuildRequires: pkgconfig(SDL2_image)
BuildRequires: pkgconfig(slirp) >= 4.6.1
BuildRequires: pkgconfig(speexdsp)
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(xrandr)
Obsoletes: dosbox < %{EVRD}

%description
This is a DOS emulator, emulating 286/386 CPUs, filesystems, XMS/EMS, various
graphics cards and sound cards. It is a fork of DOSBox that tries to modernize
the codebase and add new features.

%files
%license COPYING
%doc CHANGELOG README.*
%{_bindir}/%{name}
%{_datadir}/bash-completion/completions/%{name}
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%{_datadir}/applications/com.dosbox_x.DOSBox-X.desktop
%{_datadir}/metainfo/com.dosbox_x.DOSBox-X.metainfo.xml
%{_datadir}/%{name}
%{_mandir}/man1/%{name}.1*

#-----------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{name}-%{name}-v%{version}
# Remove deprecated entries in configure.ac
autoupdate
./autogen.sh || :

%configure \
	--enable-sdl2


%build
%make_build


%install
%make_install

# Fix chrpath
chrpath -d %{buildroot}%{_bindir}/%{name}

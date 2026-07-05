# dosbox-x has its own autogen.sh script that differs a little
%global _disable_rebuild_configure 1

Summary: DOS Emulator
Name: dosbox-x
Version: 2026.07.02
License: GPLv2+
Group: Emulators
Release: 1
Url: https://dosbox-x.com
Source0: https://github.com/joncampbell123/dosbox-x/archive/refs/tags/%{name}-%{name}-v%{version}.tar.gz
Patch0:	dosbox-x-2026.07.02-fix-FSF-address.patch
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: chrpath
BuildRequires: dos2unix
BuildRequires: libtool-base
BuildRequires: m4
BuildRequires: make
BuildRequires: nasm
BuildRequires: slibtool
BuildRequires: atomic-devel
BuildRequires: SDL_sound-devel
BuildRequires: pkgconfig(alsa)
BuildRequires: pkgconfig(fluidsynth)
BuildRequires: pkgconfig(freetype2)
BuildRequires: pkgconfig(gl)
BuildRequires: pkgconfig(gtest)
BuildRequires: pkgconfig(gmock)
BuildRequires: pkgconfig(iir)
BuildRequires: pkgconfig(libavcodec)
BuildRequires: pkgconfig(libpcap)
BuildRequires: pkgconfig(libpng)
BuildRequires: pkgconfig(mt32emu)
BuildRequires: pkgconfig(ncurses)
BuildRequires: pkgconfig(opusfile)
BuildRequires: pkgconfig(sdl2)
#BuildRequires: pkgconfig(sdl3)
BuildRequires: pkgconfig(SDL2_net)
BuildRequires: pkgconfig(SDL2_image)
BuildRequires: pkgconfig(slirp) >= 4.6.1
BuildRequires: pkgconfig(speexdsp)
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(xrandr)
BuildRequires: pkgconfig(zlib)
%rename dosbox

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

# Fix EOL
dos2unix CHANGELOG
dos2unix README.video
dos2unix README.md


%build
# Remove deprecated entries in configure.ac
autoupdate
./autogen.sh || :

# Using SDL3 disables some things  (gamelink support, internal modem and IPX support)
# and  makes the build fail because of a missing include... stay on SDL2 for now
%configure \
		--enable-sdl2 \
		--enable-avcodec

%make_build


%install
%make_install

# Fix rpath
chrpath -d %{buildroot}%{_bindir}/%{name}

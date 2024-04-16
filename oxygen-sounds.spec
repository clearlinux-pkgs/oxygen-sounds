#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v10
# autospec commit: 5905be9
#
# Source0 file verified with key 0xD7574483BB57B18D (jr@jriddell.org)
#
Name     : oxygen-sounds
Version  : 6.0.4
Release  : 11
URL      : https://download.kde.org/stable/plasma/6.0.4/oxygen-sounds-6.0.4.tar.xz
Source0  : https://download.kde.org/stable/plasma/6.0.4/oxygen-sounds-6.0.4.tar.xz
Source1  : https://download.kde.org/stable/plasma/6.0.4/oxygen-sounds-6.0.4.tar.xz.sig
Source2  : D7574483BB57B18D.pkey
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-2-Clause CC0-1.0 LGPL-3.0
Requires: oxygen-sounds-data = %{version}-%{release}
Requires: oxygen-sounds-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : gnupg
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
No detailed description available

%package data
Summary: data components for the oxygen-sounds package.
Group: Data

%description data
data components for the oxygen-sounds package.


%package license
Summary: license components for the oxygen-sounds package.
Group: Default

%description license
license components for the oxygen-sounds package.


%prep
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE2}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE1} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) D7574483BB57B18D' gpg.status
%setup -q -n oxygen-sounds-6.0.4
cd %{_builddir}/oxygen-sounds-6.0.4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1713299928
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
%cmake ..
make  %{?_smp_mflags}
popd
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
%cmake ..
make  %{?_smp_mflags}
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
export SOURCE_DATE_EPOCH=1713299928
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/oxygen-sounds
cp %{_builddir}/oxygen-sounds-%{version}/LICENSES/BSD-2-Clause.txt %{buildroot}/usr/share/package-licenses/oxygen-sounds/a17e788a7f1bf9b9c02eb6431ffc2b8002aae4f2 || :
cp %{_builddir}/oxygen-sounds-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/oxygen-sounds/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0 || :
cp %{_builddir}/oxygen-sounds-%{version}/LICENSES/LGPL-3.0-or-later.txt %{buildroot}/usr/share/package-licenses/oxygen-sounds/f45ee1c765646813b442ca58de72e20a64a7ddba || :
cp %{_builddir}/oxygen-sounds-%{version}/sounds/oxygen/index.theme.license %{buildroot}/usr/share/package-licenses/oxygen-sounds/34611dc636e0a6ded585c6625380c58367d02e2a || :
cp %{_builddir}/oxygen-sounds-%{version}/sounds/oxygen/stereo/complete-media-burn.ogg.license %{buildroot}/usr/share/package-licenses/oxygen-sounds/34611dc636e0a6ded585c6625380c58367d02e2a || :
cp %{_builddir}/oxygen-sounds-%{version}/sounds/oxygen/stereo/complete-media-error.ogg.license %{buildroot}/usr/share/package-licenses/oxygen-sounds/34611dc636e0a6ded585c6625380c58367d02e2a || :
cp %{_builddir}/oxygen-sounds-%{version}/sounds/oxygen/stereo/completion-fail.ogg.license %{buildroot}/usr/share/package-licenses/oxygen-sounds/34611dc636e0a6ded585c6625380c58367d02e2a || :
cp %{_builddir}/oxygen-sounds-%{version}/sounds/oxygen/stereo/completion-rotation.ogg.license %{buildroot}/usr/share/package-licenses/oxygen-sounds/34611dc636e0a6ded585c6625380c58367d02e2a || :
cp %{_builddir}/oxygen-sounds-%{version}/sounds/oxygen/stereo/completion-success.ogg.license %{buildroot}/usr/share/package-licenses/oxygen-sounds/34611dc636e0a6ded585c6625380c58367d02e2a || :
cp %{_builddir}/oxygen-sounds-%{version}/sounds/oxygen/stereo/desktop-login-long.ogg.license %{buildroot}/usr/share/package-licenses/oxygen-sounds/34611dc636e0a6ded585c6625380c58367d02e2a || :
cp %{_builddir}/oxygen-sounds-%{version}/sounds/oxygen/stereo/desktop-login-short.ogg.license %{buildroot}/usr/share/package-licenses/oxygen-sounds/34611dc636e0a6ded585c6625380c58367d02e2a || :
cp %{_builddir}/oxygen-sounds-%{version}/sounds/oxygen/stereo/desktop-login.ogg.license %{buildroot}/usr/share/package-licenses/oxygen-sounds/34611dc636e0a6ded585c6625380c58367d02e2a || :
cp %{_builddir}/oxygen-sounds-%{version}/sounds/oxygen/stereo/desktop-logout.ogg.license %{buildroot}/usr/share/package-licenses/oxygen-sounds/34611dc636e0a6ded585c6625380c58367d02e2a || :
cp %{_builddir}/oxygen-sounds-%{version}/sounds/oxygen/stereo/device-added.ogg.license %{buildroot}/usr/share/package-licenses/oxygen-sounds/34611dc636e0a6ded585c6625380c58367d02e2a || :
cp %{_builddir}/oxygen-sounds-%{version}/sounds/oxygen/stereo/dialog-error-critical.ogg.license %{buildroot}/usr/share/package-licenses/oxygen-sounds/34611dc636e0a6ded585c6625380c58367d02e2a || :
cp %{_builddir}/oxygen-sounds-%{version}/sounds/oxygen/stereo/dialog-error-serious.ogg.license %{buildroot}/usr/share/package-licenses/oxygen-sounds/34611dc636e0a6ded585c6625380c58367d02e2a || :
cp %{_builddir}/oxygen-sounds-%{version}/sounds/oxygen/stereo/dialog-error-veryserious.ogg.license %{buildroot}/usr/share/package-licenses/oxygen-sounds/34611dc636e0a6ded585c6625380c58367d02e2a || :
cp %{_builddir}/oxygen-sounds-%{version}/sounds/oxygen/stereo/dialog-error.ogg.license %{buildroot}/usr/share/package-licenses/oxygen-sounds/34611dc636e0a6ded585c6625380c58367d02e2a || :
cp %{_builddir}/oxygen-sounds-%{version}/sounds/oxygen/stereo/dialog-information.ogg.license %{buildroot}/usr/share/package-licenses/oxygen-sounds/34611dc636e0a6ded585c6625380c58367d02e2a || :
cp %{_builddir}/oxygen-sounds-%{version}/sounds/oxygen/stereo/dialog-question.ogg.license %{buildroot}/usr/share/package-licenses/oxygen-sounds/34611dc636e0a6ded585c6625380c58367d02e2a || :
cp %{_builddir}/oxygen-sounds-%{version}/sounds/oxygen/stereo/dialog-special.ogg.license %{buildroot}/usr/share/package-licenses/oxygen-sounds/34611dc636e0a6ded585c6625380c58367d02e2a || :
cp %{_builddir}/oxygen-sounds-%{version}/sounds/oxygen/stereo/dialog-warning.ogg.license %{buildroot}/usr/share/package-licenses/oxygen-sounds/34611dc636e0a6ded585c6625380c58367d02e2a || :
cp %{_builddir}/oxygen-sounds-%{version}/sounds/oxygen/stereo/file-error.ogg.license %{buildroot}/usr/share/package-licenses/oxygen-sounds/34611dc636e0a6ded585c6625380c58367d02e2a || :
cp %{_builddir}/oxygen-sounds-%{version}/sounds/oxygen/stereo/message-attention.ogg.license %{buildroot}/usr/share/package-licenses/oxygen-sounds/34611dc636e0a6ded585c6625380c58367d02e2a || :
cp %{_builddir}/oxygen-sounds-%{version}/sounds/oxygen/stereo/message-conectivity-problem.ogg.license %{buildroot}/usr/share/package-licenses/oxygen-sounds/34611dc636e0a6ded585c6625380c58367d02e2a || :
cp %{_builddir}/oxygen-sounds-%{version}/sounds/oxygen/stereo/message-connectivity-error-serious.ogg.license %{buildroot}/usr/share/package-licenses/oxygen-sounds/34611dc636e0a6ded585c6625380c58367d02e2a || :
cp %{_builddir}/oxygen-sounds-%{version}/sounds/oxygen/stereo/message-connectivity-error.ogg.license %{buildroot}/usr/share/package-licenses/oxygen-sounds/34611dc636e0a6ded585c6625380c58367d02e2a || :
cp %{_builddir}/oxygen-sounds-%{version}/sounds/oxygen/stereo/message-connectivity-lost.ogg.license %{buildroot}/usr/share/package-licenses/oxygen-sounds/34611dc636e0a6ded585c6625380c58367d02e2a || :
cp %{_builddir}/oxygen-sounds-%{version}/sounds/oxygen/stereo/message-contact-in.ogg.license %{buildroot}/usr/share/package-licenses/oxygen-sounds/34611dc636e0a6ded585c6625380c58367d02e2a || :
cp %{_builddir}/oxygen-sounds-%{version}/sounds/oxygen/stereo/message-contact-out.ogg.license %{buildroot}/usr/share/package-licenses/oxygen-sounds/34611dc636e0a6ded585c6625380c58367d02e2a || :
cp %{_builddir}/oxygen-sounds-%{version}/sounds/oxygen/stereo/message-error.ogg.license %{buildroot}/usr/share/package-licenses/oxygen-sounds/34611dc636e0a6ded585c6625380c58367d02e2a || :
cp %{_builddir}/oxygen-sounds-%{version}/sounds/oxygen/stereo/message-highlight.ogg.license %{buildroot}/usr/share/package-licenses/oxygen-sounds/34611dc636e0a6ded585c6625380c58367d02e2a || :
cp %{_builddir}/oxygen-sounds-%{version}/sounds/oxygen/stereo/message-irc-event.ogg.license %{buildroot}/usr/share/package-licenses/oxygen-sounds/34611dc636e0a6ded585c6625380c58367d02e2a || :
cp %{_builddir}/oxygen-sounds-%{version}/sounds/oxygen/stereo/message-lowpriority.ogg.license %{buildroot}/usr/share/package-licenses/oxygen-sounds/34611dc636e0a6ded585c6625380c58367d02e2a || :
cp %{_builddir}/oxygen-sounds-%{version}/sounds/oxygen/stereo/message-new-email.ogg.license %{buildroot}/usr/share/package-licenses/oxygen-sounds/34611dc636e0a6ded585c6625380c58367d02e2a || :
cp %{_builddir}/oxygen-sounds-%{version}/sounds/oxygen/stereo/message-new-instant.ogg.license %{buildroot}/usr/share/package-licenses/oxygen-sounds/34611dc636e0a6ded585c6625380c58367d02e2a || :
cp %{_builddir}/oxygen-sounds-%{version}/sounds/oxygen/stereo/message-new-sms.ogg.license %{buildroot}/usr/share/package-licenses/oxygen-sounds/34611dc636e0a6ded585c6625380c58367d02e2a || :
cp %{_builddir}/oxygen-sounds-%{version}/sounds/oxygen/stereo/message-sent-instant.ogg.license %{buildroot}/usr/share/package-licenses/oxygen-sounds/34611dc636e0a6ded585c6625380c58367d02e2a || :
cp %{_builddir}/oxygen-sounds-%{version}/sounds/oxygen/stereo/outcome-failure.ogg.license %{buildroot}/usr/share/package-licenses/oxygen-sounds/34611dc636e0a6ded585c6625380c58367d02e2a || :
cp %{_builddir}/oxygen-sounds-%{version}/sounds/oxygen/stereo/outcome-success.ogg.license %{buildroot}/usr/share/package-licenses/oxygen-sounds/34611dc636e0a6ded585c6625380c58367d02e2a || :
cp %{_builddir}/oxygen-sounds-%{version}/sounds/oxygen/stereo/phone-incoming-call.ogg.license %{buildroot}/usr/share/package-licenses/oxygen-sounds/34611dc636e0a6ded585c6625380c58367d02e2a || :
cp %{_builddir}/oxygen-sounds-%{version}/sounds/oxygen/stereo/print-error.ogg.license %{buildroot}/usr/share/package-licenses/oxygen-sounds/34611dc636e0a6ded585c6625380c58367d02e2a || :
cp %{_builddir}/oxygen-sounds-%{version}/sounds/oxygen/stereo/service-login.ogg.license %{buildroot}/usr/share/package-licenses/oxygen-sounds/34611dc636e0a6ded585c6625380c58367d02e2a || :
cp %{_builddir}/oxygen-sounds-%{version}/sounds/oxygen/stereo/service-logout.ogg.license %{buildroot}/usr/share/package-licenses/oxygen-sounds/34611dc636e0a6ded585c6625380c58367d02e2a || :
cp %{_builddir}/oxygen-sounds-%{version}/sounds/oxygen/stereo/trash-empty.ogg.license %{buildroot}/usr/share/package-licenses/oxygen-sounds/34611dc636e0a6ded585c6625380c58367d02e2a || :
cp %{_builddir}/oxygen-sounds-%{version}/sounds/oxygen/stereo/window-close.ogg.license %{buildroot}/usr/share/package-licenses/oxygen-sounds/34611dc636e0a6ded585c6625380c58367d02e2a || :
cp %{_builddir}/oxygen-sounds-%{version}/sounds/oxygen/stereo/window-maximized.ogg.license %{buildroot}/usr/share/package-licenses/oxygen-sounds/34611dc636e0a6ded585c6625380c58367d02e2a || :
cp %{_builddir}/oxygen-sounds-%{version}/sounds/oxygen/stereo/window-minimized.ogg.license %{buildroot}/usr/share/package-licenses/oxygen-sounds/34611dc636e0a6ded585c6625380c58367d02e2a || :
cp %{_builddir}/oxygen-sounds-%{version}/sounds/oxygen/stereo/window-move-end.ogg.license %{buildroot}/usr/share/package-licenses/oxygen-sounds/34611dc636e0a6ded585c6625380c58367d02e2a || :
cp %{_builddir}/oxygen-sounds-%{version}/sounds/oxygen/stereo/window-move-start.ogg.license %{buildroot}/usr/share/package-licenses/oxygen-sounds/34611dc636e0a6ded585c6625380c58367d02e2a || :
cp %{_builddir}/oxygen-sounds-%{version}/sounds/oxygen/stereo/window-pin.ogg.license %{buildroot}/usr/share/package-licenses/oxygen-sounds/34611dc636e0a6ded585c6625380c58367d02e2a || :
cp %{_builddir}/oxygen-sounds-%{version}/sounds/oxygen/stereo/window-shaded.ogg.license %{buildroot}/usr/share/package-licenses/oxygen-sounds/34611dc636e0a6ded585c6625380c58367d02e2a || :
cp %{_builddir}/oxygen-sounds-%{version}/sounds/oxygen/stereo/window-unpin.ogg.license %{buildroot}/usr/share/package-licenses/oxygen-sounds/34611dc636e0a6ded585c6625380c58367d02e2a || :
cp %{_builddir}/oxygen-sounds-%{version}/sounds/oxygen/stereo/window-unshaded.ogg.license %{buildroot}/usr/share/package-licenses/oxygen-sounds/34611dc636e0a6ded585c6625380c58367d02e2a || :
export GOAMD64=v2
GOAMD64=v3
pushd clr-build-avx2
%make_install_v3  || :
popd
GOAMD64=v2
pushd clr-build
%make_install
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/sounds/Oxygen-Im-Cant-Connect.ogg
/usr/share/sounds/Oxygen-Im-Connection-Lost.ogg
/usr/share/sounds/Oxygen-Im-Contact-In.ogg
/usr/share/sounds/Oxygen-Im-Contact-Out.ogg
/usr/share/sounds/Oxygen-Im-Error-On-Connection.ogg
/usr/share/sounds/Oxygen-Im-Highlight-Msg.ogg
/usr/share/sounds/Oxygen-Im-Internal-Error.ogg
/usr/share/sounds/Oxygen-Im-Irc-Event.ogg
/usr/share/sounds/Oxygen-Im-Low-Priority-Message.ogg
/usr/share/sounds/Oxygen-Im-Message-In.ogg
/usr/share/sounds/Oxygen-Im-Message-Out.ogg
/usr/share/sounds/Oxygen-Im-Network-Problems.ogg
/usr/share/sounds/Oxygen-Im-New-Mail.ogg
/usr/share/sounds/Oxygen-Im-Nudge.ogg
/usr/share/sounds/Oxygen-Im-Phone-Ring.ogg
/usr/share/sounds/Oxygen-Im-Sms.ogg
/usr/share/sounds/Oxygen-Im-User-Auth.ogg
/usr/share/sounds/Oxygen-K3B-Finish-Error.ogg
/usr/share/sounds/Oxygen-K3B-Finish-Success.ogg
/usr/share/sounds/Oxygen-K3B-Insert-Medium.ogg
/usr/share/sounds/Oxygen-Sys-App-Error-Critical.ogg
/usr/share/sounds/Oxygen-Sys-App-Error-Serious-Very.ogg
/usr/share/sounds/Oxygen-Sys-App-Error-Serious.ogg
/usr/share/sounds/Oxygen-Sys-App-Error.ogg
/usr/share/sounds/Oxygen-Sys-App-Message.ogg
/usr/share/sounds/Oxygen-Sys-App-Negative.ogg
/usr/share/sounds/Oxygen-Sys-App-Positive.ogg
/usr/share/sounds/Oxygen-Sys-Error-Printing.ogg
/usr/share/sounds/Oxygen-Sys-File-Open-Foes.ogg
/usr/share/sounds/Oxygen-Sys-List-End.ogg
/usr/share/sounds/Oxygen-Sys-List-Match-Multiple.ogg
/usr/share/sounds/Oxygen-Sys-List-Match-No.ogg
/usr/share/sounds/Oxygen-Sys-Log-In-Long.ogg
/usr/share/sounds/Oxygen-Sys-Log-In-Short.ogg
/usr/share/sounds/Oxygen-Sys-Log-In.ogg
/usr/share/sounds/Oxygen-Sys-Log-Out-Long.ogg
/usr/share/sounds/Oxygen-Sys-Log-Out.ogg
/usr/share/sounds/Oxygen-Sys-Question.ogg
/usr/share/sounds/Oxygen-Sys-Special.ogg
/usr/share/sounds/Oxygen-Sys-Trash-Emptied.ogg
/usr/share/sounds/Oxygen-Sys-Warning.ogg
/usr/share/sounds/Oxygen-Window-All-Desktops-Not.ogg
/usr/share/sounds/Oxygen-Window-All-Desktops.ogg
/usr/share/sounds/Oxygen-Window-Close.ogg
/usr/share/sounds/Oxygen-Window-Maximize.ogg
/usr/share/sounds/Oxygen-Window-Minimize.ogg
/usr/share/sounds/Oxygen-Window-Move-Stop.ogg
/usr/share/sounds/Oxygen-Window-Move.ogg
/usr/share/sounds/Oxygen-Window-Shade-Down.ogg
/usr/share/sounds/Oxygen-Window-Shade-Up.ogg
/usr/share/sounds/oxygen/index.theme
/usr/share/sounds/oxygen/stereo/alarm-clock-elapsed.ogg
/usr/share/sounds/oxygen/stereo/battery-caution.ogg
/usr/share/sounds/oxygen/stereo/battery-full.ogg
/usr/share/sounds/oxygen/stereo/battery-low.ogg
/usr/share/sounds/oxygen/stereo/bell-window-system.ogg
/usr/share/sounds/oxygen/stereo/camera-shutter.wav
/usr/share/sounds/oxygen/stereo/complete-media-burn.ogg
/usr/share/sounds/oxygen/stereo/complete-media-error.ogg
/usr/share/sounds/oxygen/stereo/completion-fail.ogg
/usr/share/sounds/oxygen/stereo/completion-rotation.ogg
/usr/share/sounds/oxygen/stereo/completion-success.ogg
/usr/share/sounds/oxygen/stereo/desktop-login-long.ogg
/usr/share/sounds/oxygen/stereo/desktop-login-short.ogg
/usr/share/sounds/oxygen/stereo/desktop-login.ogg
/usr/share/sounds/oxygen/stereo/desktop-logout.ogg
/usr/share/sounds/oxygen/stereo/device-added.ogg
/usr/share/sounds/oxygen/stereo/device-removed.ogg
/usr/share/sounds/oxygen/stereo/dialog-error-critical.ogg
/usr/share/sounds/oxygen/stereo/dialog-error-serious.ogg
/usr/share/sounds/oxygen/stereo/dialog-error-veryserious.ogg
/usr/share/sounds/oxygen/stereo/dialog-error.ogg
/usr/share/sounds/oxygen/stereo/dialog-information.ogg
/usr/share/sounds/oxygen/stereo/dialog-question.ogg
/usr/share/sounds/oxygen/stereo/dialog-special.ogg
/usr/share/sounds/oxygen/stereo/dialog-warning.ogg
/usr/share/sounds/oxygen/stereo/file-error.ogg
/usr/share/sounds/oxygen/stereo/game-over-loser.ogg
/usr/share/sounds/oxygen/stereo/game-over-winner.ogg
/usr/share/sounds/oxygen/stereo/media-insert-request.ogg
/usr/share/sounds/oxygen/stereo/message-attention.ogg
/usr/share/sounds/oxygen/stereo/message-conectivity-problem.ogg
/usr/share/sounds/oxygen/stereo/message-connectivity-error-serious.ogg
/usr/share/sounds/oxygen/stereo/message-connectivity-error.ogg
/usr/share/sounds/oxygen/stereo/message-connectivity-lost.ogg
/usr/share/sounds/oxygen/stereo/message-contact-in.ogg
/usr/share/sounds/oxygen/stereo/message-contact-out.ogg
/usr/share/sounds/oxygen/stereo/message-error.ogg
/usr/share/sounds/oxygen/stereo/message-highlight.ogg
/usr/share/sounds/oxygen/stereo/message-irc-event.ogg
/usr/share/sounds/oxygen/stereo/message-lowpriority.ogg
/usr/share/sounds/oxygen/stereo/message-new-email.ogg
/usr/share/sounds/oxygen/stereo/message-new-instant.ogg
/usr/share/sounds/oxygen/stereo/message-new-sms.ogg
/usr/share/sounds/oxygen/stereo/message-sent-instant.ogg
/usr/share/sounds/oxygen/stereo/outcome-failure.ogg
/usr/share/sounds/oxygen/stereo/outcome-success.ogg
/usr/share/sounds/oxygen/stereo/phone-incoming-call.ogg
/usr/share/sounds/oxygen/stereo/power-plug.ogg
/usr/share/sounds/oxygen/stereo/power-unplug.ogg
/usr/share/sounds/oxygen/stereo/print-error.ogg
/usr/share/sounds/oxygen/stereo/service-login.ogg
/usr/share/sounds/oxygen/stereo/service-logout.ogg
/usr/share/sounds/oxygen/stereo/theme-demo.ogg
/usr/share/sounds/oxygen/stereo/trash-empty.ogg
/usr/share/sounds/oxygen/stereo/window-close.ogg
/usr/share/sounds/oxygen/stereo/window-maximized.ogg
/usr/share/sounds/oxygen/stereo/window-minimized.ogg
/usr/share/sounds/oxygen/stereo/window-move-end.ogg
/usr/share/sounds/oxygen/stereo/window-move-start.ogg
/usr/share/sounds/oxygen/stereo/window-pin.ogg
/usr/share/sounds/oxygen/stereo/window-shaded.ogg
/usr/share/sounds/oxygen/stereo/window-unpin.ogg
/usr/share/sounds/oxygen/stereo/window-unshaded.ogg

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/oxygen-sounds/34611dc636e0a6ded585c6625380c58367d02e2a
/usr/share/package-licenses/oxygen-sounds/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0
/usr/share/package-licenses/oxygen-sounds/a17e788a7f1bf9b9c02eb6431ffc2b8002aae4f2
/usr/share/package-licenses/oxygen-sounds/f45ee1c765646813b442ca58de72e20a64a7ddba

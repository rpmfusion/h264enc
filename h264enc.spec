Name:           h264enc
Version:        8.7.2
Release:        1%{?dist}
Summary:        An interactive menu-driven frontend for mencoder
Group:          Applications/Multimedia
License:        GPLv2+
URL:            http://h264enc.sourceforge.net/
Source0:        http://internap.dl.sourceforge.net/sourceforge/h264enc/h264enc-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:       mencoder
BuildArch:      noarch


%description
h264enc is an advanced and powerful interactive menu-driven shell
script written for the GNU/Linux operating system which can help you
to encode a DVD, a video file, a directory with video files or a (S)VCD
to the H.264/MPEG-4 Part 10/AVC video format using the MEncoder encoder
from the MPlayer project and the libx264 library. It supports muxing
the final encode from AVI to Matroska, from AVI to OGM, from AVI to TS
and from AVI to the MP4 container.


%prep
%setup -q
sed -i -e "s|^PREFIX=.*$||" \
  -e "s|^DOCDIR=.*$|DOCDIR=./installed-docs|" \
  -e 's|^MANDIR=.*$|MANDIR=$PREFIX/share/man/man1|' \
  ./install

sed -i -e "s|\r$||" matrices/eqm_avc_hr_matrix
sed -i -e "s|/usr/local|%{_prefix}|" doc/README.matrices


%build
# Entire program is shell script, no compilation needed


%install
rm -rf $RPM_BUILD_ROOT
PREFIX="$RPM_BUILD_ROOT%{_prefix}" ./install
rm ./installed-docs/uninstall


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc ./installed-docs/*
%{_bindir}/h264enc
%{_mandir}/man1/h264enc.1*


%changelog
* Sun Feb 22 2009 Conrad Meyer <konrad@tylerc.org> - 8.7.2-1
- Fix license, sed /usr/local to prefix.
- Bump to 8.7.2.

* Mon Feb 2 2009 Conrad Meyer <konrad@tylerc.org> - 8.7.0-1
- Initial package.

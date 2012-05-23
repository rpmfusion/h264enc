Name:           h264enc
Version:        9.4.6
Release:        1%{?dist}
# Epoch is 1 in F-13, so we need 1 here to keep upgrade path:
Epoch:          1
Summary:        An interactive menu-driven frontend for mencoder
Group:          Applications/Multimedia
License:        GPLv2+
URL:            http://h264enc.sourceforge.net/
Source0:        http://downloads.sourceforge.net/project/h264enc/h264enc/h264enc-%{version}.tar.gz
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
* Tue May 22 2012 Conrad Meyer <konrad@tylerc.org> - 1:9.4.6-1
- Bump to version 9.4.6 (2012-04-16)
- Current rawhide mplayer is 2012-02-05; F-16 is 2011-09-25. This version
  seems to work with F-16's mplayer, at least.

* Wed Feb 08 2012 Nicolas Chauvet <kwizart@gmail.com> - 1:9.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Sep 28 2010 Conrad Meyer <konrad@tylerc.org> - 1:9.2.4-1
- Bump to version 9.2.4, released 2010-07-21 (hopefully compatible
  with mplayer 20100703 in rpmfusion rawhide).
- Bump epoch to keep upgrade path from F-13.
  
* Tue Dec 8 2009 Conrad Meyer <konrad@tylerc.org> - 9.1.0-1
- Bump version to 9.1.0.

* Thu Aug 13 2009 Conrad Meyer <konrad@tylerc.org> - 8.9.9-1
- Bump version to 8.9.9.

* Fri May 22 2009 Conrad Meyer <konrad@tylerc.org> - 8.8.0-1
- Bump version to 8.8.0.

* Sun Mar 29 2009 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 8.7.2-2
- rebuild for new F11 features

* Sun Feb 22 2009 Conrad Meyer <konrad@tylerc.org> - 8.7.2-1
- Fix license, sed /usr/local to prefix.
- Bump to 8.7.2.

* Mon Feb 2 2009 Conrad Meyer <konrad@tylerc.org> - 8.7.0-1
- Initial package.

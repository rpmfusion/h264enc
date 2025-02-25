Name:           h264enc
Version:        10.4.7
Release:        18%{?dist}
# Epoch is 1 in F-13, so we need 1 here to keep upgrade path:
Epoch:          1
Summary:        An interactive menu-driven frontend for mencoder
License:        GPLv2+
URL:            http://h264enc.sourceforge.net/
Source0:        http://downloads.sourceforge.net/project/h264enc/h264enc/h264enc-%{version}.tar.gz
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
sed -i -e "s|\r$||" matrices/eqm_avc_hr_matrix
sed -i -e "s|/usr/local|%{_prefix}|" doc/README.matrices

%build

%install
# binary
install -D -m 755 h264enc %{buildroot}/%{_bindir}/h264enc
# man
install -D -m 644 man/h264enc.1 %{buildroot}/%{_mandir}/man1/h264enc.1
# move license
mv doc/LICENSE .

%files
%doc doc/* matrices/
%license LICENSE
%{_bindir}/h264enc
%{_mandir}/man1/h264enc.1*


%changelog
* Tue Jan 28 2025 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1:10.4.7-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Aug 02 2024 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1:10.4.7-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Feb 03 2024 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1:10.4.7-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Aug 02 2023 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1:10.4.7-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun Aug 07 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1:10.4.7-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild and ffmpeg
  5.1

* Wed Feb 09 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1:10.4.7-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Aug 02 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1:10.4.7-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Feb 03 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1:10.4.7-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Aug 18 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1:10.4.7-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Feb 04 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1:10.4.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Aug 13 2019 Leigh Scott <leigh123linux@gmail.com> - 1:10.4.7-8
- Clean up spec file and improve packaging

* Fri Aug 09 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1:10.4.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Mar 04 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1:10.4.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 26 2018 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1:10.4.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar 01 2018 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 1:10.4.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 31 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 1:10.4.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Mar 19 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 1:10.4.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Feb 23 2016 Sérgio Basto <sergio@serjux.com> - 1:10.4.7-1
- Update to 10.4.7

* Sun Aug 31 2014 Sérgio Basto <sergio@serjux.com> - 1:9.4.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon May 27 2013 Nicolas Chauvet <kwizart@gmail.com> - 1:9.4.6-3
- Rebuilt for x264/FFmpeg

* Sun Mar 03 2013 Nicolas Chauvet <kwizart@gmail.com> - 1:9.4.6-2
- Mass rebuilt for Fedora 19 Features

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

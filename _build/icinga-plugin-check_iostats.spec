#
# spec file for package icinga_check_iostats
#

Name:           icinga-plugin-check_iostats
Version:        %{version}
Release:        %{release}
Summary:        Check disk IO usage
License:        MIT
Group:          System/Monitoring
Url:            https://github.com/joernott/icinga-plugin-check_iostats
Source0:        icinga-plugin-check_iostats-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl
Requires:       sysstat
Provides:       check_iostats

%description
This plugin shows the I/O usage of the specified disk, using the iostat
external program. It prints three statistics: Transactions per second (tps),
Kilobytes per second read from the disk (KB_read/s) and and written to the disk
(KB_written/s)

%prep
%setup -q -n icinga-plugin-check_iostats-%{version}

%install
rm -rf "$RPM_BUILD_ROOT"
mkdir -p "$RPM_BUILD_ROOT/usr/lib64/nagios/plugins"
cp check_iostats "$RPM_BUILD_ROOT/usr/lib64/nagios/plugins/"

%files
%defattr(-,root,root,755)
%attr(0755,root,root) /usr/lib64/nagios/plugins/check_iostats

%changelog
* Wed Apr 26 2022 Joern Ott <joern.ott@ott-consult.de>
- Initial version



%define		pkg	nagtrap
%define		php_min_version 5.0.0
Summary:	NagTrap picks the snmptraps from the database of SNMPTT
Name:		nagios-%{pkg}
Version:	0.1.3
Release:	0.4
License:	GPL v2
Group:		Applications/WWW
Source0:	http://downloads.sourceforge.net/nagtrap/nagtrap-%{version}.tar.gz
# Source0-md5:	430a41a4455fbfe3ec5471eab691386e
Source1:	README
Patch0:		config.patch
URL:		http://www.nagtrap.org/doku.php/en:start
Requires:	nagios-cgi
Requires:	php-common >= 4:%{php_min_version}
Requires:	php-mysql
Requires:	php-xml
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_webapps	/etc/webapps
%define		_sysconfdir	%{_webapps}/nagios
%define		_appdir		%{_datadir}/nagios/%{pkg}

%description
NagTrap is a webinterface written in PHP for Nagios. You can manage
and administrate recipient snmptraps from SNMPTT.

%prep
%setup -q -n %{pkg}-%{version}
%patch0 -p1

mv %{pkg}/etc config-sample
cp -p %{SOURCE1} .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{_appdir}}
cp -a %{pkg}/* /$RPM_BUILD_ROOT%{_appdir}
cp -a db /$RPM_BUILD_ROOT%{_appdir}
cp -p config-sample/config.ini.php-dist $RPM_BUILD_ROOT%{_sysconfdir}/%{pkg}.php

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog THANKS README
%attr(640,root,http) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{pkg}.php
%{_appdir}

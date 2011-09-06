%define		plugin	appear
Summary:	jQuery plugin to call a function when an element becomes visible
Name:		jquery-%{plugin}
Version:	1.1.1
Release:	1
License:	MIT
Group:		Applications/WWW
Source0:	https://jquery-appear.googlecode.com/files/jquery.appear-%{version}.js
# Source0-md5:	bf16fff99021a0ad3696e2659b69de75
Source1:	https://jquery-appear.googlecode.com/files/jquery.appear-%{version}.min.js
# Source1-md5:	72e1d93fddec7a7150ae9de2b334a1cd
URL:		https://code.google.com/p/jquery-appear/
BuildRequires:	rpmbuild(macros) > 1.268
Requires:	jquery >= 1.3.2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir	%{_datadir}/jquery/%{plugin}

%description
Mimics a custom "appear" event, which fires when an element scrolls
into view or otherwise becomes visible to the user.

This plugin can be used to prevent unnecessary requests for content
that's hidden or outside the viewable area.

%prep
%setup -qcT

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_appdir}
cp -p %{SOURCE0} $RPM_BUILD_ROOT%{_appdir}/%{plugin}.src.js
cp -p %{SOURCE1} $RPM_BUILD_ROOT%{_appdir}/%{plugin}.min.js
ln -s %{plugin}.min.js $RPM_BUILD_ROOT%{_appdir}/%{plugin}.js

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_appdir}

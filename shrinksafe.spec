Summary:	Dojo toolkit's JavaScript compressor
Name:		shrinksafe
Version:	0
Release:	0.1
License:	AFL 2.1 or BSD
Group:		Applications
Source0:	http://svn.dojotoolkit.org/dojo/trunk/buildscripts/lib/custom_rhino.jar
# Source0-md5:	260f96b8e030ed1cb5ce08ceb4a72b81
URL:		http://dojotoolkit.org/docs/shrinksafe
BuildRequires:	rpm-javaprov
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	jre >= 1.4
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Dojo toolkit's JavaScript compressor.

%prep
%setup -qcT
cat <<'EOF' >> %{name}
#!/bin/sh
exec java -jar %{_javadir}/%{name}_rhino.jar -c "$@"
EOF

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_javadir}}
install %{name} $RPM_BUILD_ROOT%{_bindir}/%{name}
install %{SOURCE0} $RPM_BUILD_ROOT%{_javadir}/%{name}_rhino.jar

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/shrinksafe
%{_javadir}/shrinksafe_rhino.jar

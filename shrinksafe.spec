%include	/usr/lib/rpm/macros.java
Summary:	Dojo toolkit's JavaScript compressor
Summary(pl.UTF-8):	Kompresor JavaScriptu z zestawu narzędzi Dojo
Name:		shrinksafe
Version:	1.2.2
Release:	2
License:	MPL 1.1
Group:		Applications
Source0:	http://download.dojotoolkit.org/release-1.2.2/dojo-release-%{version}-%{name}.tar.gz
# Source0-md5:	db5314f7cf08be30a6a1da46196b793a
Source1:	http://ftp.mozilla.org/pub/mozilla.org/js/rhino1_6R7.zip
# Source1-md5:	7be259ae496aae78feaafe7099e09897
Source2:	http://java.sun.com/products/jfc/tsc/articles/treetable2/downloads/src.zip
# Source2-md5:	ab016c8f81812bb930fc0f7a69e053c5
Patch0:		custom_rhino.diff
URL:		http://dojotoolkit.org/docs/shrinksafe
BuildRequires:	ant
BuildRequires:	jaxp_parser_impl
BuildRequires:	jpackage-utils
BuildRequires:	rpm-javaprov
BuildRequires:	rpmbuild(macros) >= 1.300
BuildRequires:	unzip
BuildRequires:	xml-commons-apis
Requires:	jpackage-utils
Requires:	jre >= 1.4
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The premier JavaScript compression engine.

%description -l pl.UTF-8
Kompresor JavaScriptu z zestawu narzędzi Dojo.

%prep
%setup -q -n dojo-release-%{version}-%{name} -a1
cat <<'EOF' >> %{name}
#!/bin/sh
exec java -jar %{_javadir}/%{name}_rhino.jar "$@"
EOF

mv rhino{*,}
cd rhino
%patch0 -p0
cd -

%build
cd rhino
cat <<'EOF' >> build.properties
# use local path
swing-ex-url=file:%{SOURCE2}
EOF
%ant -Ddebug=off -Dno-e4x=true -Dno-xmlbeans=true jar

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_javadir}}
install %{name} $RPM_BUILD_ROOT%{_bindir}/%{name}
install rhino/build/rhino*/*js.jar $RPM_BUILD_ROOT%{_javadir}/%{name}_rhino.jar

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/shrinksafe
%{_javadir}/shrinksafe_rhino.jar

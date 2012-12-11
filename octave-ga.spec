%define	pkgname ga
%define name	octave-%{pkgname}
%define version 0.9.8

Summary:	Genetic optimization tools for Octave
Name:		%{name}
Version:	%{version}
Release:        2
Source0:	%{pkgname}-%{version}.tar.gz
License:	GPLv2+
Group:		Sciences/Mathematics
Url:		http://octave.sourceforge.net/ga/
Conflicts:	octave-forge <= 20090607
Requires:	octave >= 2.9.7
Requires:	octave-communications >= 1.0.0
BuildRequires:  octave-devel >= 2.9.9
BuildRequires:  mesagl-devel
BuildRequires:  mesaglu-devel
BuildArch:	noarch

%description
Genetic optimization tools for Octave.

%prep
%setup -q -c %{pkgname}-%{version}
cp %SOURCE0 .

%install
%__install -m 755 -d %{buildroot}%{_datadir}/octave/packages/
export OCT_PREFIX=%{buildroot}%{_datadir}/octave/packages
octave -q --eval "pkg prefix $OCT_PREFIX; pkg install -verbose -nodeps -local %{pkgname}-%{version}.tar.gz"

tar zxf %SOURCE0 
mv %{pkgname}/COPYING .
mv %{pkgname}/DESCRIPTION .

%clean

%post
%{_bindir}/test -x %{_bindir}/octave && %{_bindir}/octave -q -H --no-site-file --eval "pkg('rebuild');" || :

%postun
%{_bindir}/test -x %{_bindir}/octave && %{_bindir}/octave -q -H --no-site-file --eval "pkg('rebuild');" || :

%files
%defattr(-,root,root)
%doc COPYING DESCRIPTION
%{_datadir}/octave/packages/%{pkgname}-%{version}


%changelog
* Tue Jun 28 2011 Lev Givon <lev@mandriva.org> 0.9.8-1mdv2011.0
+ Revision: 687920
- import octave-ga



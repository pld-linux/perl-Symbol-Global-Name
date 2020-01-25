#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define	pdir	Symbol
%define	pnam	Global-Name
Summary:	Symbol::Global::Name - finds name and type of a global variable
#Summary(pl.UTF-8):
Name:		perl-Symbol-Global-Name
Version:	0.05
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Symbol/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	95e374d0f0df78d593de208f651391d6
URL:		http://search.cpan.org/dist/Symbol-Global-Name/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Symbol::Global::Name - Lookups symbol table to find an element by
reference..

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%dir %{perl_vendorlib}/Symbol/Global
%{perl_vendorlib}/Symbol/Global/Name.pm
%{_mandir}/man3/*

#
# Conditional build:
%bcond_without	tests # do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Math
%define		pnam	Business-BlackScholes
Summary:	Math::Business::BlackScholes - Black-Scholes option price model functions
Summary(pl):	Math::Business::BlackScholes - funkcje modelu cenowego Black-Scholes
Name:		perl-Math-Business-BlackScholes
Version:	0.06
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	d49d2e8231b0ed36c6fd17fc31e4b7a5
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	perl-Math-CDF >= 0.1
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Math::Business::BlackScholes estimates the fair market price of a
European stock option according to the Black-Scholes model.

%description -l pl
Math::Business::BlackScholes estymuje wolnorynkow� cen� europejskich
opcji na akcje zgodnie z modelem Black-Scholes.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_vendorlib}/Math/Business/BlackScholes.pm
%{_mandir}/man3/*

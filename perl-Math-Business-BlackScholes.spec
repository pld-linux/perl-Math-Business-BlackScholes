#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Math
%define		pnam	Business-BlackScholes
Summary:	Math::Business::BlackScholes - Black-Scholes option price model functions
Summary(pl):	Math::Business::BlackScholes - funkcje modelu cenowego Black-Scholes
Name:		perl-Math-Business-BlackScholes
Version:	0.03
Release:	1
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	perl-Math-CDF >= 0.1
BuildRequires:	rpm-perlprov >= 4.0.2-104
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Math::Business::BlackScholes estimates the fair market price of a
European stock option according to the Black-Scholes model.

%description -l pl
Math::Business::BlackScholes estymuje wolnorynkow± cenê europejskich
opcji na akcje zgodnie z modelem Black-Scholes.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL
%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_sitelib}/Math/Business/BlackScholes.pm
%{_mandir}/man3/*

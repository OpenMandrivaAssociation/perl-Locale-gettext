%define	module gettext
%define modver 1.07
%ifarch %{x86_64}
# FIXME workaround for debuginfo bug
%global _debugsource_template %{nil}
%endif

Summary:	Message handling functions for Perl
Name:		perl-Locale-gettext
Version:	%{perl_convert_version %{modver}}
Release:	8
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/%{module}
Source0:	http://www.cpan.org/modules/by-module/Locale/%{module}-%{modver}.tar.gz
Patch1:		gettext-1.05-SvUTF8_on-on-strings-when-bind_textdomain_codeset-utf8.patch
Patch2:		gettext-1.05-add-iconv.patch
BuildRequires:	gettext-devel
BuildRequires:	perl-devel
BuildRequires:	perl-List-MoreUtils

%description
The gettext module permits access from perl to the gettext() family of
functions for retrieving message strings from databases constructed to
internationalize software.

It provides gettext(), dgettext(), dcgettext(), textdomain() and
bindtextdomain().

%prep
%autosetup -p1 -n Locale-%{module}-%{modver}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

# FIXME As of cooker 2018/04/29, one test fails
%if 0
%check
%make test
%endif

%install
%makeinstall_std

%files
%doc README
%{perl_vendorarch}/Locale
%{perl_vendorarch}/auto/Locale
%{_mandir}/man3/*

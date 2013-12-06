%define	module	gettext
%define modver	1.05

Summary:	Message handling functions for Perl
Name:		perl-Locale-gettext
Version:	%{perl_convert_version %{modver}}
Release:	15
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{module}
Source0:	http://www.cpan.org/modules/by-module/Locale/%{module}-%{modver}.tar.bz2
Patch1:		gettext-1.05-SvUTF8_on-on-strings-when-bind_textdomain_codeset-utf8.patch
Patch2:		gettext-1.05-add-iconv.patch
Patch3:		compatibility-with-POSIX-module.diff
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
%setup -qn %{module}-%{modver}
%apply_patches

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc README
%{perl_vendorarch}/Locale
%{perl_vendorarch}/auto/Locale
%{_mandir}/man3/*


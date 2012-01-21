%define upstream_name gettext
%define upstream_version 1.05

Name:       perl-Locale-gettext
Version:    %perl_convert_version %{upstream_version}
Release:    9

Summary:	Message handling functions for Perl
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Locale/%{upstream_name}-%{upstream_version}.tar.bz2
Patch1:		gettext-1.05-SvUTF8_on-on-strings-when-bind_textdomain_codeset-utf8.patch
Patch2:		gettext-1.05-add-iconv.patch
Patch3:		compatibility-with-POSIX-module.diff

BuildRequires:	gettext-devel
BuildRequires:	perl-devel >= 2:5.14
BuildRequires:	perl-List-MoreUtils >= 0.320.0-4

Conflicts:	drakfloppy <= 0.43-10mdk
Conflicts:	nlpr <= 0.0.1-2mdk
Conflicts:	urpmi <= 3.6-4mdk

%description
The gettext module permits access from perl to the gettext() family of
functions for retrieving message strings from databases constructed to
internationalize software.

It provides gettext(), dgettext(), dcgettext(), textdomain() and
bindtextdomain().

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%{__make}

%check
%{__make} test

%install
%{__rm} -rf %{buildroot}
%makeinstall_std

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README
%{perl_vendorarch}/Locale
%{perl_vendorarch}/auto/Locale
%{_mandir}/*/*

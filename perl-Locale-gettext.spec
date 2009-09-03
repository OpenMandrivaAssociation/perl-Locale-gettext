%define name perl-Locale-gettext
%define real_name gettext
%define version 1.05
%define release %mkrel 10

Name:		%{name}
Version:	%{version}
Release:	%{release}
Group:		Development/Perl
License:	GPL or Artistic
URL:		http://search.cpan.org/dist/%{real_name}
Source:		http://www.cpan.org/modules/by-module/Locale/%{real_name}-%{version}.tar.bz2
Patch1:		gettext-1.05-SvUTF8_on-on-strings-when-bind_textdomain_codeset-utf8.patch
Patch2:		gettext-1.05-add-iconv.patch
Patch3:		compatibility-with-POSIX-module.diff
Summary:	Message handling functions for Perl
BuildRequires:	gettext-devel perl-devel
BuildRoot:	%{_tmppath}/%{name}-root
Conflicts:	nlpr <= 0.0.1-2mdk, drakfloppy <= 0.43-10mdk, urpmi <= 3.6-4mdk

%description
The gettext module permits access from perl to the gettext() family of
functions for retrieving message strings from databases constructed to
internationalize software.

It provides gettext(), dgettext(), dcgettext(), textdomain() and
bindtextdomain().

%prep
%setup -q -n %{real_name}-%{version}
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
%{perl_vendorarch}/Locale/*
%{perl_vendorarch}/auto/Locale/*
%{_mandir}/*/*



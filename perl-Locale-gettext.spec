%define	module	gettext
%define modver	1.05

Name:		perl-Locale-gettext
Version:	%{perl_convert_version %{modver}}
Release:	11

Summary:	Message handling functions for Perl
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{module}
Source0:	http://www.cpan.org/modules/by-module/Locale/%{module}-%{modver}.tar.bz2
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
%setup -q -n %{module}-%{modver}
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%{__make}

%check
%{__make} test

%install
%makeinstall_std

%files
%doc README
%{perl_vendorarch}/Locale
%{perl_vendorarch}/auto/Locale
%{_mandir}/*/*

%changelog
* Wed Dec 19 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.50.0-11
- rebuild against new perl
- cleanups

* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 1.50.0-10
+ Revision: 765392
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 1.50.0-9
+ Revision: 763908
- rebuilt for perl-5.14.x

* Fri Jan 20 2012 Oden Eriksson <oeriksson@mandriva.com> 1.50.0-8
+ Revision: 763028
- force it

* Fri Jan 20 2012 Bernhard Rosenkraenzer <bero@bero.eu> 1.50.0-7
+ Revision: 762840
- Build with perl 5.14.x
- Remove some legacy constructs from spec file

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1.50.0-6
+ Revision: 667224
- mass rebuild

* Sun Apr 03 2011 Funda Wang <fwang@mandriva.org> 1.50.0-5
+ Revision: 650030
- rebuild

* Sun Aug 01 2010 Funda Wang <fwang@mandriva.org> 1.50.0-4mdv2011.0
+ Revision: 564523
- rebuild for perl 5.12.1

* Tue Jul 20 2010 Sandro Cazzaniga <kharec@mandriva.org> 1.50.0-3mdv2011.0
+ Revision: 555253
- rebuild

  + Jérôme Quelin <jquelin@mandriva.org>
    - rebuild for 5.12
    - fix package name
    - rebuild using %%perl_convert_version

  + Guillaume Rousse <guillomovitch@mandriva.org>
    - own top-level directory

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 1.05-10mdv2010.0
+ Revision: 426516
- rebuild

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 1.05-9mdv2009.1
+ Revision: 351905
- rebuild

* Mon Sep 29 2008 Thierry Vignaud <tv@mandriva.org> 1.05-8mdv2009.0
+ Revision: 289779
- patch 3: make Locale::Gettext re-exports the LC_* constants coming from POSIX
  instead of those coming from its own XS implementation (#44009)

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 1.05-7mdv2009.0
+ Revision: 223808
- rebuild

* Sun Jan 13 2008 Pixel <pixel@mandriva.com> 1.05-6mdv2008.1
+ Revision: 150906
- rebuild for perl 5.10.0

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Wed Mar 07 2007 Pixel <pixel@mandriva.com> 1.05-5mdv2007.1
+ Revision: 134688
- workaround a segfault (#29248)

* Thu Jan 18 2007 Pixel <pixel@mandriva.com> 1.05-4mdv2007.1
+ Revision: 110360
- when bind_textdomain_codeset to utf8 is done, we know the string returned by
  dgettext (and ngettext...) is utf8. In that case we tell perl it is utf8.
  (it was done for drakxtools, but it really is valid everywhere)
  (!! problems can still occur if bind_textdomain_codeset utf8 is not done!!)
- re-diff patch "add-iconv" and bunzip it

* Wed Aug 16 2006 Olivier Thauvin <nanardon@mandriva.org> 1.05-3mdv2007.0
+ Revision: 56141
- test in %%check
- mkrel
- Import perl-Locale-gettext

* Thu Dec 15 2005 Pixel <pixel@mandriva.com> 1.05-2mdk
- in "add iconv" patch, allow the wanted charset to be undef (meaning standard charset)
  (it was already allowed for the source charset)

* Tue Jun 07 2005 Pascal Terjan <pterjan@mandriva.org> 1.05-1mdk
- New release 1.05

* Tue May 24 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 1.04-1mdk
- 1.04
- cleanup spec, drop patch 0 and 1 (merged), rediff patch 2
- drop obsoletes: perl-gettext

* Fri Nov 12 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 1.01-14mdk
- Rebuild for new perl

* Sat Apr 24 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.01-13mdk
- relink against fixed libintl

* Wed Apr 21 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.01-12mdk
- rebuild for new gettext


%define upstream_name	 MIME-Explode
%define	upstream_version 0.39

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:	4

Summary:	Perl extension for explode MIME messages
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/MIME/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
MIME::Explode is perl module for parsing and decoding single or multipart
MIME messages, and outputting its decoded components to a given directory
ie, this module is designed to allows users to extract the attached files
out of a MIME encoded email messages or mailboxes.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README examples
%{perl_vendorarch}/MIME
%{perl_vendorarch}/auto/MIME
%{_mandir}/man3/*


%changelog
* Wed Jan 25 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.390.0-2
+ Revision: 768358
- svn commit -m mass rebuild of perl extension against perl 5.14.2

* Tue Jun 28 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.390.0-1
+ Revision: 687704
- update to new version 0.39

* Tue Jul 20 2010 Jérôme Quelin <jquelin@mandriva.org> 0.380.0-2mdv2011.0
+ Revision: 556006
- rebuild for perl 5.12

* Wed Jul 29 2009 Jérôme Quelin <jquelin@mandriva.org> 0.380.0-1mdv2010.0
+ Revision: 403861
- rebuild using %%perl_convert_version

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 0.38-5mdv2009.0
+ Revision: 257834
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.38-4mdv2009.0
+ Revision: 245877
- rebuild

* Tue Jan 15 2008 Thierry Vignaud <tv@mandriva.org> 0.38-2mdv2008.1
+ Revision: 152129
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot


* Fri Jun 16 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.38-1mdv2007.0
- New version 0.38

* Sun Jul 10 2005 Oden Eriksson <oeriksson@mandriva.com> 0.37-1mdk
- initial Mandriva package


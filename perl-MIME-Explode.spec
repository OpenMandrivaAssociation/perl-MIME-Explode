%define module	MIME-Explode
%define	name	perl-%{module}
%define	version 0.38
%define	release %mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Perl extension for explode MIME messages
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{module}
Source:		http://www.cpan.org/modules/by-module/MIME/%{module}-%{version}.tar.bz2
BuildRequires:	perl-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
MIME::Explode is perl module for parsing and decoding single or multipart
MIME messages, and outputting its decoded components to a given directory
ie, this module is designed to allows users to extract the attached files
out of a MIME encoded email messages or mailboxes.

%prep
%setup -q -n %{module}-%{version} 

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


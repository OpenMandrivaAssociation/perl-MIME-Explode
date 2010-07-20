%define upstream_name	 MIME-Explode
%define	upstream_version 0.38

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:	Perl extension for explode MIME messages
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
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

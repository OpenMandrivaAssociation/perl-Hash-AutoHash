%define upstream_name    Hash-AutoHash
%define upstream_version 1.17

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    1

Summary:    Object-oriented access to real and tied hashes
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Hash/Hash-AutoHash-%{upstream_version}.tar.gz

BuildRequires: perl(Carp)
BuildRequires: perl(Test::Pod::Content)
BuildRequires: perl(Test::Pod)
BuildRequires: perl(Exporter)
BuildRequires: perl(List::MoreUtils)
BuildRequires: perl(Scalar::Util)
BuildRequires: perl(Test::Deep)
BuildRequires: perl(Test::More)
BuildRequires: perl(Tie::Hash)
BuildRequires: perl(Tie::Hash::MultiValue)
BuildRequires: perl(Tie::ToObject)
BuildRequires: perl(Module::Build::Compat)
BuildArch: noarch

%description
This is yet another module that lets you access or change the elements of a
hash using methods with the same name as the element's key. It follows in
the footsteps of the Hash::AsObject manpage, the Hash::Inflator manpage,
the Data::OpenStruct::Deep manpage, the Object::AutoAccessor manpage, and
probably others. The main difference between this module and its forebears
is that it supports tied hashes, in addition to regular hashes. This allows
a modular division of labor: this class is generic and treats all hashes
the same; any special semantics come from the tied hash.

The class has a 'new' method but also supplies several functions for
constructing new Hash::AutoHash objects. Except in the simplest cases, we
recommend using the constructor functions rather than 'new'.

The constructor functions shown in the SYNOPSIS are all you need for
typical uses. autohash_hash creates a new 'real' (ie, not tied)
Hash::AutoHash object; autohash_tie creates a new tied Hash::AutoHash
object. Once the objects are constructed, the class treats them the same
way.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%{make}

%check
%{make} test

%install
%makeinstall_std

%clean

%files
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/*




%changelog
* Mon Apr 18 2011 Funda Wang <fwang@mandriva.org> 1.120.0-2mdv2011.0
+ Revision: 654995
- rebuild for updated spec-helper

* Tue Mar 02 2010 Jérôme Quelin <jquelin@mandriva.org> 1.120.0-1mdv2011.0
+ Revision: 513475
- update to 1.12

* Thu Feb 25 2010 Jérôme Quelin <jquelin@mandriva.org> 1.110.0-1mdv2010.1
+ Revision: 510970
- update to 1.11

* Tue Nov 17 2009 Jérôme Quelin <jquelin@mandriva.org> 1.100.0-1mdv2010.1
+ Revision: 466797
- import perl-Hash-AutoHash


* Tue Nov 17 2009 cpan2dist 1.10-1mdv
- initial mdv release, generated with cpan2dist


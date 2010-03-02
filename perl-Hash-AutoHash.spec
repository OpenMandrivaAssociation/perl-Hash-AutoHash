%define upstream_name    Hash-AutoHash
%define upstream_version 1.12

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Object-oriented access to real and tied hashes
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Hash/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Carp)
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
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

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
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/*



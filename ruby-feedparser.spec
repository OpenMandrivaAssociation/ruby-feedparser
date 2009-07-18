%define rname feedparser
%define name ruby-%{rname}
%define version 0.6
%define release %mkrel 1

Summary:	RSS and Atom parser for Ruby
Name:		%{name}
Version:	%{version}
Release:	%{release}
URL:		http://home.gna.org/ruby-feedparser/
Source0:	http://download.gna.org/ruby-feedparser/%{name}-%{version}.tar.bz2
License:	Ruby or GPL
Group:		Development/Ruby
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildArch:	noarch
BuildRequires:	ruby-rake graphviz

%description
Ruby-Feedparser is an RSS and Atom parser for Ruby.

Ruby-feedparser is :

    * based on REXML
    * built for robustness : most feeds are not valid
    * fully unit-tested
    * easy to use (it can output text or HTML easily)

%prep
%setup -q
chmod 0644 ChangeLog LICENSE COPYING README

%build
ruby setup.rb config
ruby setup.rb setup
rake rdoc

%check
rake test

%install
rm -rf %buildroot
ruby setup.rb install --prefix=%buildroot

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%{ruby_sitelibdir}/*
%doc ChangeLog LICENSE COPYING README rdoc 



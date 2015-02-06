%define rname feedparser
%define name ruby-%{rname}
%define version 0.7
%define release 3

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




%changelog
* Tue Dec 07 2010 Oden Eriksson <oeriksson@mandriva.com> 0.7-2mdv2011.0
+ Revision: 614740
- the mass rebuild of 2010.1 packages

* Sun Jan 10 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.7-1mdv2010.1
+ Revision: 489196
- update to new version 0.7

* Sat Jul 18 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.6-1mdv2010.0
+ Revision: 397015
- update to new version 0.6

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Nov 12 2007 Pascal Terjan <pterjan@mandriva.org> 0.5-1mdv2008.1
+ Revision: 108157
- update to new version 0.5

* Sun May 20 2007 Pascal Terjan <pterjan@mandriva.org> 0.4-1mdv2008.0
+ Revision: 28868
- 0.4
- enable tests, they work again

* Sat Apr 21 2007 Pascal Terjan <pterjan@mandriva.org> 0.3-2mdv2008.0
+ Revision: 16630
- Use Development/Ruby group


* Mon Jan 01 2007 Pascal Terjan <pterjan@mandriva.org> 0.3-1mdv2007.0
+ Revision: 103026
- move rake test to the check section
- disable tests for now
- 0.3
- use global ruby macros
- fix description
- Import ruby-feedparser

* Wed Dec 28 2005 Pascal Terjan <pterjan@mandriva.org> 0.1-2mdk
- BuildRequires graphviz for the doc

* Mon Nov 28 2005 Pascal Terjan <pterjan@mandriva.org> 0.1-1mdk
- First Mandriva release


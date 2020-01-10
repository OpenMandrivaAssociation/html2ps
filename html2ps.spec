%define prerel b7

Summary:	HTML to PostScript converter
Name:		html2ps
Epoch:		1
Version:	1.0
Release:	0.%{prerel}.1
License:	GPLv2
Group:		Graphics
Url:		http://user.it.uu.se/~jan/html2ps.html
Source0:	http://user.it.uu.se/~jan/%{name}-%{version}%{prerel}.tar.gz
Patch0:		html2ps-1.0b7-conf.patch
Patch1:		html2ps-1.0b7-perl_path.patch
Patch2:		html2ps-1.0b5-open.patch
BuildArch:	noarch

%description
The Perl script html2ps converts HTML to PostScript. It would have more
capabilities if you have some of these packages installed:	ImageMagick,
netpbm-progs, libjpeg-progs, perl-libwww, ghostscript, tetex, tetex-dvips
- see documentation for details.

html2ps can be used as ImageMagick delegate to convert from HTML.

%package -n	xhtml2ps
Summary:	GUI frontend for html2ps, a HTML-to-PostScript converter
Group:		Graphics
Requires:	%{name} = %{EVRD}
Requires:	tk

%description -n	xhtml2ps
xhtml2ps is freely-available GUI frontend for html2ps, a HTML-to-PostScript
converter.

%prep
%setup -qn %{name}-%{version}%{prerel}
%autopatch -p1

%build
sed -i -e '
	s|\@CONFDIR\@|%{_sysconfdir}|;
	s|\@DOCDIR\@|%{_docdir}/%{name}|;
	' html2ps html2ps.1

%install
install -d %{buildroot}%{_bindir}
install -d %{buildroot}%{_sysconfdir}
install -d %{buildroot}%{_mandir}/man1
install -d %{buildroot}%{_mandir}/man5

install -m0755 html2ps %{buildroot}%{_bindir}/html2ps
install -m0755 contrib/xhtml2ps/xhtml2ps %{buildroot}%{_bindir}/xhtml2ps

install -m0644 html2psrc %{buildroot}%{_sysconfdir}/html2psrc
install -m0644 html2ps.1 %{buildroot}%{_mandir}/man1/html2ps.1
install -m0644 html2psrc.5 %{buildroot}%{_mandir}/man5/html2psrc.5

%files
%doc COPYING html2ps.html README sample
%config(noreplace) %{_sysconfdir}/html2psrc
%{_bindir}/html2ps
%{_mandir}/man1/html2ps.1*
%{_mandir}/man5/html2psrc.5*

%files -n xhtml2ps
%doc contrib/xhtml2ps/LICENSE contrib/xhtml2ps/README
%{_bindir}/xhtml2ps


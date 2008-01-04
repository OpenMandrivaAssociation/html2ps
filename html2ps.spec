%define real_version 1.0b5

Summary:	HTML to PostScript converter
Name:		html2ps
Version:	1.0
Release:	%mkrel 0.b5.1
License:	GPL
Group:		Graphics
URL:		http://user.it.uu.se/~jan/html2ps.html
Source:		http://user.it.uu.se/~jan/html2ps-%{real_version}.tar.gz
Patch0:		html2ps-1.0b5-conf.patch
Patch1:		html2ps-1.0b5-perl_path.patch
Patch2:		html2ps-1.0b5-open.patch
BuildArch:	noarch
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
The Perl script html2ps converts HTML to PostScript. It would have more
capabilities if you have some of these packages installed: ImageMagick,
netpbm-progs, libjpeg-progs, perl-libwww, ghostscript, tetex, tetex-dvips
- see documentation for details.

html2ps can be used as ImageMagick delegate to convert from HTML.

%package -n	xhtml2ps
Summary:	GUI frontend for html2ps, a HTML-to-PostScript converter
Group:		Graphics
Requires:	%{name} = %{version}
Requires:	tk

%description -n	xhtml2ps
xhtml2ps is freely-available GUI frontend for html2ps, a HTML-to-PostScript
converter.

%prep

%setup -n %{name}-%{real_version}
%patch0 -p1
%patch1 -p1
%patch2 -p0

%build
perl -pi.orig -e '
        s|\@CONFDIR\@|%{_sysconfdir}|;
        s|\@DOCDIR\@|%{_docdir}/%{name}|;
    ' html2ps html2ps.1

%install
rm -rf %{buildroot}

install -d %{buildroot}%{_bindir}
install -d %{buildroot}%{_sysconfdir}
install -d %{buildroot}%{_mandir}/man1
install -d %{buildroot}%{_mandir}/man5

install -m0755 html2ps %{buildroot}%{_bindir}/html2ps
install -m0755 contrib/xhtml2ps/xhtml2ps %{buildroot}%{_bindir}/xhtml2ps

install -m0644 html2psrc %{buildroot}%{_sysconfdir}/html2psrc
install -m0644 html2ps.1 %{buildroot}%{_mandir}/man1/html2ps.1
install -m0644 html2psrc.5 %{buildroot}%{_mandir}/man5/html2psrc.5

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,0755)
%doc COPYING html2ps.html README sample
%config(noreplace) %{_sysconfdir}/html2psrc
%{_bindir}/html2ps
%{_mandir}/man1/html2ps.1*
%{_mandir}/man5/html2psrc.5*

%files -n xhtml2ps
%defattr(-,root,root,0755)
%doc contrib/xhtml2ps/LICENSE contrib/xhtml2ps/README
%{_bindir}/xhtml2ps

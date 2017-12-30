# revision 33818
# category TLCore
# catalog-ctan /dviware/dvi2tty
# catalog-date 2012-04-09 22:37:34 +0200
# catalog-license gpl
# catalog-version 3.5.1
Name:		texlive-dvi2tty
Version:	6.0.0
Release:	1
Summary:	Produce ASCII from DVI
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/dviware/dvi2tty
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dvi2tty.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dvi2tty.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires:	texlive-dvi2tty.bin

%description
A DVI driver to produce an ASCII representation of the
document. The original version was written in Pascal, and the
present author translated the program to C.

#-----------------------------------------------------------------------
%files
%doc %{_mandir}/man1/disdvi.1*
%doc %{_texmfdistdir}/doc/man/man1/disdvi.man1.pdf
%doc %{_mandir}/man1/dvi2tty.1*
%doc %{_texmfdistdir}/doc/man/man1/dvi2tty.man1.pdf

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_texmfdistdir}/doc/man/man1/*.1 %{buildroot}%{_mandir}/man1

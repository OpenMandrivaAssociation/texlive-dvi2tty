# revision 23089
# category TLCore
# catalog-ctan /dviware/dvi2tty
# catalog-date 2009-11-09 17:50:29 +0100
# catalog-license gpl
# catalog-version 3.5.1
Name:		texlive-dvi2tty
Version:	3.5.1
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
Requires(post):	texlive-kpathsea
Requires:	texlive-dvi2tty.bin
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
A DVI driver to produce an ASCII representation of the
document. The original version was written in Pascal, and the
present author translated the program to C.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_mandir}/man1/dvi2tty.1*
%{_texmfdir}/doc/man/man1/dvi2tty.man1.pdf
%doc %{_mandir}/man1/disdvi.1*
%doc %{_texmfdir}/doc/man/man1/disdvi.man1.pdf
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_texmfdir}/doc/man/man1/*.1 %{buildroot}%{_mandir}/man1
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}

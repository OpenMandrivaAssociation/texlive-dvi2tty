%global tl_name dvi2tty
%global tl_revision 66186

Name:		texlive-%{tl_name}
Epoch:		1
Version:	6.0.0
Release:	%{tl_revision}.1
Summary:	Produce ASCII from DVI
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/dviware/dvi2tty
License:	gpl2
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/dvi2tty.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/dvi2tty.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(dvi2tty.bin)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A DVI driver to produce an ASCII representation of the document. The
original version was written in Pascal, and the present author
translated the program to C.


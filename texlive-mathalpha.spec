Name:		texlive-mathalpha
Version:	61089
Release:	2
Summary:	General package for loading maths alphabets in LaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/mathalpha
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mathalpha.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mathalpha.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Package mathalfa was renamed to mathalpha. For backward
compatibility the old name will continue to be recognized in
LaTeX documents. The package provides means of loading maths
alphabets (such as are normally addressed via macros \mathcal,
\mathbb, \mathfrak and \mathscr), offering various features
normally missing in existing packages for this job.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/mathalpha
%doc %{_texmfdistdir}/doc/latex/mathalpha

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post

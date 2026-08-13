%global tl_name mathalpha
%global tl_revision 77682
%global tl_version 1.145

Name:		texlive-%{tl_name}
Epoch:		1
Version:	%{tl_version}
Release:	%{tl_revision}.1
Summary:	General package for loading maths alphabets in LaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/mathalpha
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mathalpha.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mathalpha.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{version}

%description
Package mathalfa was renamed to mathalpha. For backward compatibility
the old name will continue to be recognized in LaTeX documents. The
package provides means of loading maths alphabets (such as are normally
addressed via macros \mathcal, \mathbb, \mathfrak and \mathscr),
offering various features normally missing in existing packages for this
job.


%install -a
mkdir -p %{buildroot}%{_texmf_updmap_d}
cat > %{buildroot}%{_texmf_updmap_d}/%{tl_name} <<'TL_DROPIN_EOF'
# from mathalpha:
Map mathalpha.map
TL_DROPIN_EOF

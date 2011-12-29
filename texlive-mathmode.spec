# revision 20742
# category Package
# catalog-ctan /info/math/voss/mathmode
# catalog-date 2010-12-14 15:27:20 +0100
# catalog-license lppl
# catalog-version 2.47
Name:		texlive-mathmode
Version:	2.47
Release:	1
Summary:	A comprehensive review of mathematics in (La)TeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/math/voss/mathmode
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mathmode.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mathmode.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg

%description
The review includes: Standard LaTeX mathematics mode; AMSmath;
TeX and mathematics; Other packages; Tuning math typesetting;
Mathematics fonts; Special symbols; Examples; and Lists,
bibliography and index.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/latex/mathmode/Changes
%doc %{_texmfdistdir}/doc/latex/mathmode/Mathmode.bib
%doc %{_texmfdistdir}/doc/latex/mathmode/Mathmode.ist
%doc %{_texmfdistdir}/doc/latex/mathmode/Mathmode.ltx
%doc %{_texmfdistdir}/doc/latex/mathmode/Mathmode.pdf
%doc %{_texmfdistdir}/doc/latex/mathmode/Mathmode.tex
%doc %{_texmfdistdir}/doc/latex/mathmode/README
%doc %{_texmfdistdir}/doc/latex/mathmode/images/EuScript.eps
%doc %{_texmfdistdir}/doc/latex/mathmode/images/EuScript.pdf
%doc %{_texmfdistdir}/doc/latex/mathmode/images/amsalign.eps
%doc %{_texmfdistdir}/doc/latex/mathmode/images/amsalign.pdf
%doc %{_texmfdistdir}/doc/latex/mathmode/images/cm-crop.eps
%doc %{_texmfdistdir}/doc/latex/mathmode/images/cm-crop.pdf
%doc %{_texmfdistdir}/doc/latex/mathmode/images/cmbright-crop.eps
%doc %{_texmfdistdir}/doc/latex/mathmode/images/cmbright-crop.pdf
%doc %{_texmfdistdir}/doc/latex/mathmode/images/colArray.eps
%doc %{_texmfdistdir}/doc/latex/mathmode/images/colArray.pdf
%doc %{_texmfdistdir}/doc/latex/mathmode/images/exscale.eps
%doc %{_texmfdistdir}/doc/latex/mathmode/images/exscale.pdf
%doc %{_texmfdistdir}/doc/latex/mathmode/images/family.eps
%doc %{_texmfdistdir}/doc/latex/mathmode/images/family.pdf
%doc %{_texmfdistdir}/doc/latex/mathmode/images/family0.eps
%doc %{_texmfdistdir}/doc/latex/mathmode/images/family0.pdf
%doc %{_texmfdistdir}/doc/latex/mathmode/images/family1.eps
%doc %{_texmfdistdir}/doc/latex/mathmode/images/family1.pdf
%doc %{_texmfdistdir}/doc/latex/mathmode/images/lm-crop.eps
%doc %{_texmfdistdir}/doc/latex/mathmode/images/lm-crop.pdf
%doc %{_texmfdistdir}/doc/latex/mathmode/images/minionpro-crop.eps
%doc %{_texmfdistdir}/doc/latex/mathmode/images/minionpro-crop.pdf
%doc %{_texmfdistdir}/doc/latex/mathmode/images/node.eps
%doc %{_texmfdistdir}/doc/latex/mathmode/images/node.pdf
%doc %{_texmfdistdir}/doc/latex/mathmode/images/pamath-crop.eps
%doc %{_texmfdistdir}/doc/latex/mathmode/images/pamath-crop.pdf
%doc %{_texmfdistdir}/doc/latex/mathmode/images/pazo-crop.eps
%doc %{_texmfdistdir}/doc/latex/mathmode/images/pazo-crop.pdf
%doc %{_texmfdistdir}/doc/latex/mathmode/images/styles.eps
%doc %{_texmfdistdir}/doc/latex/mathmode/images/styles.pdf
%doc %{_texmfdistdir}/doc/latex/mathmode/images/test-crop.pdf
%doc %{_texmfdistdir}/doc/latex/mathmode/images/test.pdf
%doc %{_texmfdistdir}/doc/latex/mathmode/images/test.tex
%doc %{_texmfdistdir}/doc/latex/mathmode/runLaTeX
%doc %{_texmfdistdir}/doc/latex/mathmode/runPDFLaTeX
%doc %{_texmfdistdir}/doc/latex/mathmode/runVTeX

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}

# revision 23328
# category Package
# catalog-ctan /macros/latex/contrib/exercise
# catalog-date 2011-07-19 17:40:51 +0200
# catalog-license gpl
# catalog-version 1.57
Name:		texlive-exercise
Version:	1.57
Release:	1
Summary:	Typeset exercises, problems, etc. and their answers
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/exercise
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/exercise.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/exercise.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/exercise.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The package helps to typeset exercises or list of exercises
within any document. Exercises, questions and sub-questions are
automatically numbered. It is possible to put answers in the
same document, and display them immediatly, later in the
document or not to print answers at all. The layout of
exercises is fully customisable. It is possible to typeset long
problems, short exercises, questionnaires, etc. Usage of the
babel package is detected, but not fully supported yet (only
English and French are implemented).

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
%{_texmfdistdir}/tex/latex/exercise/exercise.sty
%doc %{_texmfdistdir}/doc/latex/exercise/README
%doc %{_texmfdistdir}/doc/latex/exercise/exercise.pdf
#- source
%doc %{_texmfdistdir}/source/latex/exercise/exercise.dtx
%doc %{_texmfdistdir}/source/latex/exercise/exercise.ins
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}

# revision 26260
# category Package
# catalog-ctan /macros/latex/contrib/exercise
# catalog-date 2012-05-08 15:13:49 +0200
# catalog-license gpl
# catalog-version 1.58
Name:		texlive-exercise
Version:	1.58
Release:	3
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

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/exercise/exercise.sty
%doc %{_texmfdistdir}/doc/latex/exercise/README
%doc %{_texmfdistdir}/doc/latex/exercise/exercise.pdf
#- source
%doc %{_texmfdistdir}/source/latex/exercise/exercise.dtx
%doc %{_texmfdistdir}/source/latex/exercise/exercise.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Mon Jun 11 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.58-1
+ Revision: 804574
- Update to latest release.

* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.57-2
+ Revision: 751680
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.57-1
+ Revision: 718398
- texlive-exercise
- texlive-exercise
- texlive-exercise
- texlive-exercise


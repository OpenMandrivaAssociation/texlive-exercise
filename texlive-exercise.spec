Name:		texlive-exercise
Version:	35417
Release:	2
Summary:	Typeset exercises, problems, etc. and their answers
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/exercise
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/exercise.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/exercise.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/exercise.source.r%{version}.tar.xz
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
%{_texmfdistdir}/tex/latex/exercise
%doc %{_texmfdistdir}/doc/latex/exercise
#- source
%doc %{_texmfdistdir}/source/latex/exercise

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}

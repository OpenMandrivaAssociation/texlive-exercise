%global tl_name exercise
%global tl_revision 76924

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.6
Release:	%{tl_revision}.1
Summary:	Typeset exercises, problems, etc. and their answers
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/exercise
License:	gpl2
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/exercise.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/exercise.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/exercise.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package helps to typeset exercises or list of exercises within any
document. Exercises, questions and sub-questions are automatically
numbered. It is possible to put answers in the same document, and
display them immediately, later in the document or not to print answers
at all. The layout of exercises is fully customisable. It is possible to
typeset long problems, short exercises, questionnaires, etc. Usage of
the babel package is detected, but not fully supported yet (only English
and French are implemented).


Name:		python-rfc3986
Version:	2.0.0
Release:	2
Source0:	https://files.pythonhosted.org/packages/source/r/rfc3986/rfc3986-%{version}.tar.gz
Summary:	Validating URI References per RFC 3986
URL:		https://pypi.org/project/rfc3986/
License:	Apache 2.0
Group:		Development/Python
BuildRequires:	python
BuildSystem:	python
BuildArch:	noarch

%description
Validating URI References per RFC 3986

%files
%{py_sitedir}/rfc3986
%{py_sitedir}/rfc3986-*.*-info

# TODO: finish tests and doc
#
# Conditional build
%bcond_with	tests	# unit tests (need some packages update)
%bcond_with	doc	# Sphinx documentation

%define		module	platformdirs
Summary:	Python module for determining appropriate platform-specific dirs
Summary(pl.UTF-8):	Moduł Pythona do określania odpowiednich katalogów specyficznych dla platformy
Name:		python3-%{module}
Version:	4.3.6
Release:	1
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/platformdirs/
Source0:	https://files.pythonhosted.org/packages/source/p/platformdirs/%{module}-%{version}.tar.gz
# Source0-md5:	9f63e7b2b462ee13ee2bf857f2839926
URL:		https://pypi.org/project/platformdirs/
BuildRequires:	python3-modules >= 1:3.7
BuildRequires:	python3-build
BuildRequires:	python3-installer
%if %{with tests}
BuildRequires:	python3-appdirs = 1.4.4
BuildRequires:	python3-pytest >= 6
BuildRequires:	python3-pytest-cov >= 2.7
BuildRequires:	python3-pytest-mock >= 3.6
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with doc}
BuildRequires:	python3-furo >= 2021.7.5b38
BuildRequires:	python3-proselint >= 0.10.2
BuildRequires:	python3-sphinx-autodoc-typehints >= 1.12
BuildRequires:	sphinx-pdg >= 4
%endif
Requires:	python3-modules >= 1:3.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A small Python module for determining appropriate platform-specific
dirs, e.g. a "user data dir".

%description -l pl.UTF-8
Mały moduł Pythona do określania odpowiednich katalogów specyficznych
dla platformy, np. "katalog danych użytkownika".

%prep
%setup -q -n %{module}-%{version}

%build
%py3_build_pyproject

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
PYTEST_PLUGINS=pytest_cov.plugin,pytest_mock \
%{__python3} -m pytest tests
%endif

%if %{with doc}
sphinx-build -b html -d docs/_build/doctree docs docs/_build/html
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install_pyproject

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.rst
%dir %{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/%{module}/*.py
%{py3_sitescriptdir}/%{module}/__pycache__
%{py3_sitescriptdir}/%{module}/py.typed
%{py3_sitescriptdir}/%{module}-%{version}.dist-info

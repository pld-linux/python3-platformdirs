#
# Conditional build
%bcond_without	tests	# unit tests
%bcond_with	doc	# Sphinx documentation (not in sdist)

%define		module	platformdirs
Summary:	Python module for determining appropriate platform-specific dirs
Summary(pl.UTF-8):	Moduł Pythona do określania odpowiednich katalogów specyficznych dla platformy
Name:		python3-%{module}
Version:	4.14.2
Release:	1
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/platformdirs/
Source0:	https://files.pythonhosted.org/packages/source/p/platformdirs/%{module}-%{version}.tar.gz
# Source0-md5:	07dd523bb5ca12c4525df2cd242336b1
URL:		https://pypi.org/project/platformdirs/
BuildRequires:	python3-Cython >= 3
BuildRequires:	python3-build
BuildRequires:	python3-hatch-fancy-pypi-readme >= 25.1
BuildRequires:	python3-hatch-vcs >= 0.5
BuildRequires:	python3-hatchling >= 1.29
BuildRequires:	python3-installer
BuildRequires:	python3-modules >= 1:3.11
%if %{with tests}
BuildRequires:	python3-appdirs = 1.4.4
#BuildRequires:	python3-covdefaults >= 2.3
#BuildRequires:	python3-diff-cover >= 10.2
BuildRequires:	python3-pytest >= 9.0.2
#BuildRequires:	python3-pytest-cov >= 7
BuildRequires:	python3-pytest-mock >= 3.15.1
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 2.044
%if %{with doc}
BuildRequires:	python3-furo >= 2025.12.19
BuildRequires:	python3-proselint >= 0.14
BuildRequires:	python3-sphinx_autodoc_typehints >= 3.9.2
BuildRequires:	python3-sphinx_copybutton >= 0.5.2
BuildRequires:	python3-sphinx_design >= 0.7
BuildRequires:	python3-sphinx_llm >= 0.4.1
BuildRequires:	python3-sphinx_sitemap >= 2.9
BuildRequires:	python3-sphinxcontrib-mermaid >= 2
BuildRequires:	python3-sphinxcontrib-towncrier >= 0.5.0a0
BuildRequires:	python3-sphinxext-opengraph >= 0.13
BuildRequires:	sphinx-pdg >= 9.1
%endif
Requires:	python3-modules >= 1:3.11
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
# test_import_before_pytest_main deletes PYTEST_DISABLE_PLUGIN_AUTOLOAD,
# thus breaking our manual pytest plugins selection.
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
PYTEST_PLUGINS=platformdirs.pytest_plugin,pytest_mock \
PYTHONPATH=$(pwd)/src \
%{__python3} -m pytest tests -k 'not test_import_before_pytest_main'
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
%doc LICENSE
%dir %{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/%{module}/*.py
%{py3_sitescriptdir}/%{module}/__pycache__
%{py3_sitescriptdir}/%{module}/py.typed
%{py3_sitescriptdir}/%{module}-%{version}.dist-info

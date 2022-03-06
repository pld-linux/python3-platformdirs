%define		module	platformdirs
Summary:	Python module for determining appropriate platform-specific dirs
Summary(pl.UTF-8):	Moduł Pythona do określania odpowiednich katalogów specyficznych dla platformy
Name:		python3-%{module}
Version:	2.4.0
Release:	1
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/platformdirs/
Source0:	https://files.pythonhosted.org/packages/source/p/platformdirs/%{module}-%{version}.tar.gz
# Source0-md5:	4e5b836d19600cc4bf0b789ab1de3b51
URL:		https://pypi.org/project/platformdirs/
BuildRequires:	python3-modules >= 1:3.6
BuildRequires:	python3-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-modules >= 1:3.6
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
%py3_build

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES.rst README.rst
%dir %{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/%{module}/*.py
%{py3_sitescriptdir}/%{module}/__pycache__
%{py3_sitescriptdir}/%{module}/py.typed
%{py3_sitescriptdir}/%{module}-%{version}-py*.egg-info

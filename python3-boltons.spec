#
# Conditional build:
%bcond_without	tests	# unit tests

%define		module	boltons
Summary:	When they're not builtins, they're boltons
Summary(pl.UTF-8):	To, co nie jest wbudowane, jest w boltons
Name:		python3-%{module}
Version:	25.0.0
Release:	1
License:	BSD
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/boltons/
Source0:	https://files.pythonhosted.org/packages/source/b/boltons/%{module}-%{version}.tar.gz
# Source0-md5:	fd7a60168e8cda65b4794f0c72437417
URL:		https://pypi.org/project/boltons/
BuildRequires:	python3-build
BuildRequires:	python3-flit_core >= 3.2
BuildRequires:	python3-installer
BuildRequires:	python3-modules >= 1:3.7
%if %{with tests}
BuildRequires:	python3-pytest
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 2.044
Requires:	python3-modules >= 1:3.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Functionality that should be in the standard library. Like builtins,
but Boltons.

%description -l pl.UTF-8
Funkcjonalność, która powinna być w bibliotece standardowej. Podobnie
jak builtins, ale to są Boltons.

%prep
%setup -q -n %{module}-%{version}

%build
%py3_build_pyproject

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
%{__python3} -m pytest tests
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install_pyproject

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG.md LICENSE README.md
%{py3_sitescriptdir}/boltons
%{py3_sitescriptdir}/boltons-%{version}.dist-info

%define	module	matrix-nio

Name:		python-%{module}
Version:	0.19.0
Release:	1
License:	ISC
Summary:	A Python Matrix client library, designed according to sans I/O principles
Group:		Development/Python
Url:		https://github.com/poljar/matrix-nio
Source:		https://files.pythonhosted.org/packages/source/m/%{module}/%{module}-%{version}.tar.gz
Patch0:		python-matrix-nio-0.19.0-omv-patch-fix-for-require-aiofiles.patch

BuildRequires:	pkgconfig(python3)
BuildRequires:	python3dist(setuptools)
# SECTION test requirements
BuildRequires:	python3dist(aiofiles)
BuildRequires:	python3dist(aiohttp)
BuildRequires:	python3dist(aiohttp-socks)
BuildRequires:	python3dist(future)
BuildRequires:	python-h2
BuildRequires:	python3dist(h11)
BuildRequires:	python3dist(jsonschema)
BuildRequires:	python3dist(logbook)
BuildRequires:	python3dist(pycryptodome)
BuildRequires:	python3dist(unpaddedbase64)
BuildRequires:	fdupes
# e2e
BuildRequires:	python3dist(atomicwrites)
BuildRequires:	python3dist(cachetools)
BuildRequires:	python3dist(peewee)
BuildRequires:	python3dist(python-olm)
BuildRequires:	python3dist(typing)

# e2e
Requires:	python3dist(atomicwrites)
Requires:	python3dist(cachetools)
Requires:	python3dist(peewee)
Requires:	python3dist(python-olm)
Requires:	python3dist(typing)

BuildArch:	noarch

%files
%license LICENSE.md
%doc README.md
%{python_sitelib}/nio/
%{python_sitelib}/matrix_nio-%{version}-py%{pyver}.egg-info/

#----------------------------------------------------------------------------

%description
A Python Matrix client library, designed according to sans I/O principles.

%prep
%autosetup -p1 -n %{module}-%{version}

%build
%py_build

%install
%py_install


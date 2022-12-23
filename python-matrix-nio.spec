Name:		python-matrix-nio
Version:	0.20.1
Release:	1
License:	ISC
Summary:	A Python Matrix client library, designed according to sans I/O principles
Group:		Development/Python
Url:		https://github.com/poljar/matrix-nio
Source0:	https://pypi.io/packages/source/m/matrix-nio/matrix_nio-%{version}.tar.gz
Patch0:		python-matrix-nio-0.20.1-omv-patch-fix-for-require-aiofiles.patch

BuildRequires:	pkgconfig(python)
BuildRequires:	python3dist(pip)
BuildRequires:	python3dist(poetry)
BuildRequires:	python3dist(setuptools)
BuildRequires:	python3dist(wheel)
# SECTION test requirements
BuildRequires:	python3dist(aiofiles)
BuildRequires:	python3dist(aiohttp)
BuildRequires:	python3dist(aiohttp-socks)
BuildRequires:	python3dist(future)
BuildRequires:	python3dist(h2)
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

# e2e
Requires:	python3dist(atomicwrites)
Requires:	python3dist(cachetools)
Requires:	python3dist(peewee)
Requires:	python3dist(python-olm)

BuildArch:	noarch

%files
%license LICENSE.md
%doc README.md
%{python_sitelib}/nio/
%{python_sitelib}/matrix_nio-%{version}*-info/

#----------------------------------------------------------------------------

%description
A Python Matrix client library, designed according to sans I/O principles.

%prep
%autosetup -p1 -n matrix_nio-%{version}

%build
%py_build

%install
%py_install


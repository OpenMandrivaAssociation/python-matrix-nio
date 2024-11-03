Name:		python-matrix-nio
Version:	0.25.2
Release:	1
License:	ISC
Summary:	A Python Matrix client library, designed according to sans I/O principles
Group:		Development/Python
Url:		https://github.com/poljar/matrix-nio
Source0:	https://pypi.io/packages/source/m/matrix-nio/matrix_nio-%{version}.tar.gz
#Patch0:		python-matrix-nio-0.20.1-fix_deps_version.patch

BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(poetry-core)
BuildRequires:	python%{pyver}dist(pytoml)
BuildRequires:	python%{pyver}dist(wheel)
# SECTION test requirements
BuildRequires:	python%{pyver}dist(aiofiles)
BuildRequires:	python%{pyver}dist(aiohttp)
BuildRequires:	python%{pyver}dist(aiohttp-socks)
BuildRequires:	python%{pyver}dist(future)
BuildRequires:	python%{pyver}dist(h2)
BuildRequires:	python%{pyver}dist(h11)
BuildRequires:	python%{pyver}dist(jsonschema)
BuildRequires:	python%{pyver}dist(logbook)
BuildRequires:	python%{pyver}dist(pycryptodome)
BuildRequires:	python%{pyver}dist(unpaddedbase64)
BuildRequires:	fdupes
# e2e
BuildRequires:	python%{pyver}dist(atomicwrites)
BuildRequires:	python%{pyver}dist(cachetools)
BuildRequires:	python%{pyver}dist(peewee)
BuildRequires:	python%{pyver}dist(python-olm)

# e2e
Requires:	python%{pyver}dist(atomicwrites)
Requires:	python%{pyver}dist(cachetools)
Requires:	python%{pyver}dist(peewee)
Requires:	python%{pyver}dist(python-olm)

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


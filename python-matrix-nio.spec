%define oname matrix_nio

Name:		python-matrix-nio
Version:	0.26.0
Release:	1
License:	ISC
Summary:	A Python Matrix client library, designed according to sans I/O principles
Group:		Development/Python
URL:		https://github.com/poljar/matrix-nio
Source0:	https://pypi.io/packages/source/m/matrix-nio/%{oname}-%{version}.tar.gz
#Patch0:		python-matrix-nio-0.20.1-fix_deps_version.patch
BuildSystem:	python
BuildArch:	noarch

BuildRequires:	pkgconfig(python3)
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

%description
A Python Matrix client library, designed according to sans I/O principles.

%prep -a
# Remove bundled egg-info
rm -rf src/%{oname}.egg-info

# Remove version pinning
sed \
    -e 's/"aiohttp-socks.*"/"aiohttp-socks"/' \
    -e 's/"aiofiles.*"/"aiofiles"/' \
    -e 's/"cachetools.*"/"cachetools"/' \
    -e 's/"h11.*"/"h11"/' \
    -e 's/"h2.*"/"h2"/' \
    -e 's/"pycryptodome.*"/"pycryptodomex"/' \
    -e 's/"jsonschema.*"/"jsonschema"/' \
    -i pyproject.toml

%files
%license LICENSE.md
%doc README.md
%{python_sitelib}/nio/
%{python_sitelib}/%{oname}-%{version}.dist-info/

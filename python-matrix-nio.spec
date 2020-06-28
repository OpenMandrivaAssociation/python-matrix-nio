Name:           python-matrix-nio
Version:        0.14.1
Release:        1
License:        ISC
Summary:        A Python Matrix client library, designed according to sans I/O principles
Url:            https://github.com/poljar/matrix-nio
Group:          Development/Languages/Python
Source:         https://files.pythonhosted.org/packages/source/m/matrix-nio/matrix-nio-%{version}.tar.gz

#BuildRequires:  python-rpm-macros
BuildRequires:  python3dist(setuptools)

# SECTION test requirements
BuildRequires:  python3dist(attrs)
BuildRequires:  python3dist(future)
BuildRequires:  python3dist(jsonschema)
BuildRequires:  python3dist(logbook)
BuildRequires:  python3dist(pycryptodome)
BuildRequires:  python3dist(h11)
BuildRequires:  python3dist(h2)
BuildRequires:  python3dist(unpaddedbase64)
BuildRequires:  fdupes

Requires:       python3dist(attrs)
Requires:       python3dist(future)
Requires:       python3dist(jsonschema)
Requires:       python3dist(logbook)
Requires:       python3dist(pycryptodome)
Requires:       python3dist(h11)
Requires:       python-h2
Requires:       python-unpaddedbase64

Recommends:       python3dist(typing)
Recommends:       python3dist(aiohttp)
Recommends:       python3dist(peewee)
Recommends:       python3dist(atomicwrites)

# Not imported to Cooker yet
#Recommends:       python3dist(cachetools)
#Recommends:       python3dist(python-olm)
BuildArch:      noarch

%python_subpackages

%description
A Python Matrix client library, designed according to sans I/O principles.

%prep
%setup -q -n matrix-nio-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%check
%python_exec setup.py test

%files %{python_files}
%doc README.md
%license LICENSE.md
%{python_sitelib}/*
